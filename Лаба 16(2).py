import tkinter as tk

root = tk.Tk()
root.title("Анімація машини")
canvas_width = 800
canvas_height = 250
root.geometry(f"{canvas_width}x{canvas_height}")

canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="lightblue")
canvas.pack()

car_body = canvas.create_rectangle(0, 140, 120, 180, fill="red", outline="black")
car_top = canvas.create_rectangle(20, 110, 90, 140, fill="red", outline="black")
window = canvas.create_rectangle(30, 115, 80, 135, fill="skyblue", outline="white")
wheel1 = canvas.create_oval(15, 175, 35, 195, fill="black")
wheel2 = canvas.create_oval(85, 175, 105, 195, fill="black")

car_parts = [car_body, car_top, window, wheel1, wheel2]

def move_car():
    x1, y1, x2, y2 = canvas.coords(car_body)
    if x2 < canvas_width:
        for part in car_parts:
            canvas.move(part, 5, 0)
        root.after(30, move_car)

move_car()

root.mainloop()