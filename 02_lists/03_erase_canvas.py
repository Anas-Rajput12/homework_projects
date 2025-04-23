import tkinter as tk

CELL_SIZE = 40
ROWS = 10
COLS = 10

class EraserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Canvas Eraser")

        self.canvas = tk.Canvas(root, width=COLS * CELL_SIZE, height=ROWS * CELL_SIZE, bg="white")
        self.canvas.pack()

        self.cells = []
        self.create_grid()

        # Create eraser rectangle
        self.eraser = self.canvas.create_rectangle(0, 0, CELL_SIZE, CELL_SIZE, outline="black", fill="gray")

        # Bind mouse motion to move eraser
        self.canvas.bind("<B1-Motion>", self.move_eraser)

    def create_grid(self):
        for row in range(ROWS):
            row_cells = []
            for col in range(COLS):
                x1 = col * CELL_SIZE
                y1 = row * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE
                cell = self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="white")
                row_cells.append(cell)
            self.cells.append(row_cells)

    def move_eraser(self, event):
        # Center the eraser on the mouse
        x1 = event.x - CELL_SIZE // 2
        y1 = event.y - CELL_SIZE // 2
        x2 = event.x + CELL_SIZE // 2
        y2 = event.y + CELL_SIZE // 2

        self.canvas.coords(self.eraser, x1, y1, x2, y2)

        # Check for collision and erase
        overlapping = self.canvas.find_overlapping(x1, y1, x2, y2)
        for item in overlapping:
            if item != self.eraser:
                self.canvas.itemconfig(item, fill="white")

# Run the app
root = tk.Tk()
app = EraserApp(root)
root.mainloop()
