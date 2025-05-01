import streamlit as st
import hashlib
import json
import os
import time
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import base64

# Constants
DATA_FILE = "secure_data.json"
MASTER_PASSWORD = "admin123"  # Demo purpose only, can be improved
LOCKOUT_TIME = 60  # seconds after 3 failed attempts
SALT = b'some_salt_'  # Normally, a random salt per user is better

# Load or initialize storage
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        stored_data = json.load(f)
else:
    stored_data = {}  # Format: {username: {entry_id: {encrypted_text, hashed_passkey}}}

# Session State variables
if 'failed_attempts' not in st.session_state:
    st.session_state.failed_attempts = 0
if 'lockout_until' not in st.session_state:
    st.session_state.lockout_until = None
if 'authorized' not in st.session_state:
    st.session_state.authorized = True

# Key generation for Fernet
def generate_fernet_key(passkey):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=SALT,
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(passkey.encode()))

# Function to encrypt data
def encrypt_data(text, passkey):
    cipher = Fernet(generate_fernet_key(passkey))
    return cipher.encrypt(text.encode()).decode()

# Function to decrypt data
def decrypt_data(encrypted_text, passkey):
    try:
        cipher = Fernet(generate_fernet_key(passkey))
        return cipher.decrypt(encrypted_text.encode()).decode()
    except:
        return None

# Save data to JSON
def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump(stored_data, f, indent=4)

# UI Title
st.title("🛡️ Secure Data Encryption System")

# Lockout Management
if st.session_state.lockout_until:
    if time.time() < st.session_state.lockout_until:
        st.error(f"🚫 Locked out due to multiple failed attempts. Try again after {int(st.session_state.lockout_until - time.time())} seconds.")
        st.stop()
    else:
        st.session_state.failed_attempts = 0
        st.session_state.lockout_until = None

# Navigation
menu = ["Home", "Store Data", "Retrieve Data", "Login"]
choice = st.sidebar.selectbox("Navigation", menu)

if choice == "Home":
    st.subheader("🏡 Welcome!")
    st.write("🔐 This system allows **secure storage and retrieval** of your data using **passkeys**.")

elif choice == "Store Data":
    st.subheader("📥 Store Your Data")
    username = st.text_input("Enter Username:")
    user_data = st.text_area("Enter Data to Store:")
    passkey = st.text_input("Enter Passkey:", type="password")

    if st.button("Encrypt & Save"):
        if username and user_data and passkey:
            encrypted_text = encrypt_data(user_data, passkey)
            hashed_passkey = hashlib.pbkdf2_hmac('sha256', passkey.encode(), SALT, 100000).hex()

            if username not in stored_data:
                stored_data[username] = {}

            stored_data[username][encrypted_text] = {"encrypted_text": encrypted_text, "passkey": hashed_passkey}
            save_data()
            st.success("✅ Data encrypted and stored successfully!")
        else:
            st.error("⚠️ All fields are required!")

elif choice == "Retrieve Data":
    st.subheader("🔎 Retrieve Your Data")
    username = st.text_input("Enter Username:")
    encrypted_text = st.text_area("Paste Your Encrypted Data:")
    passkey = st.text_input("Enter Your Passkey:", type="password")

    if st.button("Decrypt"):
        if username and encrypted_text and passkey:
            if username not in stored_data or encrypted_text not in stored_data[username]:
                st.error("❌ No such data found.")
            else:
                stored_entry = stored_data[username][encrypted_text]
                expected_hash = stored_entry["passkey"]
                entered_hash = hashlib.pbkdf2_hmac('sha256', passkey.encode(), SALT, 100000).hex()

                if entered_hash == expected_hash:
                    decrypted_text = decrypt_data(encrypted_text, passkey)
                    if decrypted_text:
                        st.session_state.failed_attempts = 0
                        st.success(f"✅ Decrypted Text: {decrypted_text}")
                    else:
                        st.error("❌ Decryption failed!")
                else:
                    st.session_state.failed_attempts += 1
                    attempts_left = 3 - st.session_state.failed_attempts
                    if attempts_left > 0:
                        st.error(f"❌ Incorrect Passkey! Attempts left: {attempts_left}")
                    else:
                        st.error("❌ Too many failed attempts! Redirecting to Login...")
                        st.session_state.lockout_until = time.time() + LOCKOUT_TIME
                        st.session_state.authorized = False
                        st.experimental_rerun()
        else:
            st.error("⚠️ All fields are required!")

elif choice == "Login":
    st.subheader("🔐 Admin Login Required")
    login_pass = st.text_input("Enter Master Password:", type="password")
    if st.button("Login"):
        if login_pass == MASTER_PASSWORD:
            st.session_state.failed_attempts = 0
            st.session_state.lockout_until = None
            st.session_state.authorized = True
            st.success("✅ Reauthorized Successfully!")
            st.experimental_rerun()
        else:
            st.error("❌ Incorrect Master Password.")

