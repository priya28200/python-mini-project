import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class PhotoManipulationApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Photo Manipulation")

        self.image_label = tk.Label(master)
        self.image_label.pack()

        self.load_button = tk.Button(master, text="Load Image", command=self.load_image)
        self.load_button.pack()

        self.rotate_button = tk.Button(master, text="Rotate", command=self.rotate_image)
        self.rotate_button.pack()

        self.resize_button = tk.Button(master, text="Resize", command=self.resize_image)
        self.resize_button.pack()

        self.save_button = tk.Button(master, text="Save Image", command=self.save_image)
        self.save_button.pack()

        self.image = None

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
        if file_path:
            self.image = Image.open(file_path)
            self.display_image()

    def display_image(self):
        if self.image:
            self.photo = ImageTk.PhotoImage(self.image)
            self.image_label.config(image=self.photo)
            self.image_label.image = self.photo
        else:
            messagebox.showerror("Error", "No image loaded.")

    def rotate_image(self):
        if self.image:
            self.image = self.image.rotate(90)
            self.display_image()
        else:
            messagebox.showerror("Error", "No image loaded.")

    def resize_image(self):
        if self.image:
            width = int(self.image.width / 2)
            height = int(self.image.height / 2)
            self.image = self.image.resize((width, height))
            self.display_image()
        else:
            messagebox.showerror("Error", "No image loaded.")

    def save_image(self):
        if self.image:
            file_path = filedialog.asksaveasfilename(defaultextension=".png")
            if file_path:
                self.image.save(file_path)
                messagebox.showinfo("Success", "Image saved successfully.")
        else:
            messagebox.showerror("Error", "No image loaded.")

def main():
    root = tk.Tk()
    app = PhotoManipulationApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
