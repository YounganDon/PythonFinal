
import tkinter as tk
from tkinter import messagebox
import cv2
from PIL import Image, ImageTk

class LiveFeedPage:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Live Feed")
        self.root.configure(bg="black")

        tk.Label(self.root, text="Welcome to seenIXO", font=("Helvetica", 16), bg="black", fg="red").pack(pady=21)
        self.camera_button = tk.Button(self.root, text="Access Camera", command=self.access_camera, bg="black", fg="red")
        self.camera_button.pack(pady=10)

        self.cap = None
        self.photo = None

        self.root.mainloop()

    def access_camera(self):
        self.cap = cv2.VideoCapture(0)  # Open the default camera (change the argument if using an external camera)

        if not self.cap.isOpened():
            messagebox.showerror("Error", "Unable to access the camera.")
            return

        self.camera_button.config(state=tk.DISABLED)
        self.show_camera_feed()

    def show_camera_feed(self):
        ret, frame = self.cap.read()

        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(frame)
            self.photo = ImageTk.PhotoImage(image=image)

            if hasattr(self, "canvas"):
                self.canvas.config(image=self.photo)
            else:
                self.canvas = tk.Label(self.root, image=self.photo)
                self.canvas.pack(pady=10)

            self.root.after(10, self.show_camera_feed)
        else:
            self.release_camera()

    def release_camera(self):
        if self.cap is not None:
            self.cap.release()
        self.camera_button.config(state=tk.NORMAL)
        if hasattr(self, "canvas"):
            self.canvas.pack_forget()

if __name__ == "__main__":
    root = tk.Tk()
    LoginPage(root)
    root.mainloop()
