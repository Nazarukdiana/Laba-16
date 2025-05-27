import tkinter as tk
from tkinter import PhotoImage
import pygame

# Ініціалізація Pygame для відтворення звуку
pygame.mixer.init()

# Функція для відтворення звуку
def play_sound(word):
    pygame.mixer.music.load(f"{word}.m4a")
    pygame.mixer.music.play()

# Головне вікно
root = tk.Tk()
root.title("Вивчаємо англійську мову")
root.geometry("600x300")  # Збільшено ширину для 3 картинок

# Canvas для малювання
canvas = tk.Canvas(root, width=600, height=250)
canvas.pack()

# Завантаження зображення 1 — Apple
apple_img = PhotoImage(file="apple.png")
canvas.create_image(100, 125, image=apple_img)
apple_button = tk.Button(root, text="Apple", command=lambda: play_sound("apple"))
apple_button.place(x=70, y=260)

# Завантаження зображення 2 — Dog
dog_img = PhotoImage(file="dog.png")
canvas.create_image(300, 125, image=dog_img)
dog_button = tk.Button(root, text="Dog", command=lambda: play_sound("dog"))
dog_button.place(x=270, y=260)

# Завантаження зображення 3 — Cat
cat_img = PhotoImage(file="cat.png")
canvas.create_image(500, 125, image=cat_img)
cat_button = tk.Button(root, text="Cat", command=lambda: play_sound("cat"))
cat_button.place(x=470, y=260)

# Запуск головного циклу
root.mainloop()