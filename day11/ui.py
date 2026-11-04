import tkinter as tk

root = tk.Tk();
root.title("My first python UI-Application")
root.geometry("400x200")

def button__click():
    text_element.config(text="Button clicked! Nothing happened.")

text_element = tk.Label(root, text="Click the button and look what will happen.", font=("Arial", 14))
text_element.pack(pady=20)

button = tk.Button(root, text="Click me!", command=button__click)
button.pack(pady=10)

root.mainloop()