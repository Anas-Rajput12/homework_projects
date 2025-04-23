import hashlib

def hash_password(password):
    """
    Hashes a password using SHA256 and returns the hexadecimal digest.
    """
    return hashlib.sha256(password.encode()).hexdigest()


def login(email, password_to_check, stored_logins):
    """
    Returns True if the hashed password_to_check matches the stored hash for the email.
    """
    # Get the hashed password from stored_logins using the email
    if email not in stored_logins:
        return False
    
    # Hash the password_to_check
    hashed_password = hash_password(password_to_check)
    
    # Compare it with the stored hashed password
    return stored_logins[email] == hashed_password


# Example usage
def main():
    # Example database of emails and hashed passwords
    stored_logins = {
        'ali@example.com': hash_password('password123'),
        'ahmed@example.com': hash_password('qwerty456'),
    }

    # Test cases
    print(login('ali@example.com', 'password123', stored_logins))  # True
    print(login('ahmed@example.com', 'wrongpassword', stored_logins))  # False
    print(login('hassan@example.com', 'any', stored_logins))        # False

if __name__ == '__main__':
    main()
