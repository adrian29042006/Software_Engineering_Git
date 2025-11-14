import tkinter as tk  

root = tk.Tk()

root.title("Induktionskochfeld - Temperaturregelung Implementierung")
root.geometry("1000x1000")

label = tk.Label(root, text="Induktionskochfeld Temperaturregelung", font=("Arial", 16))
label.pack(side = "top", pady=10)

# Canvas zum Zeichnen
canvas = tk.Canvas(root, width=300, height=300, bg="black")
canvas.pack(side ="left", pady=20)

canvas.create_oval(50, 50, 100, 100, fill="red", outline="black")


root.mainloop()

