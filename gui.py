import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import *
from text_to_speech import tts
import shutil
import os


class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1000x600")
        self.root.title("Text to Speech")

        top_padding = Frame(self.root, height=150)
        top_padding.pack()

        self.title = tk.Label(self.root, font=("Arial", 24, "bold"))
        self.title.pack(pady=10)

        self.subtitle = Label(self.root, font=("Arial", 14))
        self.subtitle.pack(pady=5)

        self.text = Text(self.root, height=10)
        self.text.pack(pady=15)

        self.button = Button(self.root, font=("Arial", 12))
        self.button.pack(pady=20)

        self.re_generate_button = None

        self.create_widgets()

    def create_widgets(self):
        if self.re_generate_button is not None:
            self.re_generate_button.pack_forget()
            self.text.delete("1.0", "end-1c")

        # Main H1 title
        self.title.config(text="Convert Text to Speech Instantly")

        # Subtitle
        self.subtitle.config(text="Turn written words into lifelike speech with ease.")

        self.button.config(command=self.convert, text="Generate Speech")

    def convert(self):
        content = self.text.get("1.0", "end-1c")
        if tts(content):
            self.re_configure()
        else:
            messagebox.showinfo("Error", "Speech conversion failed. Try again.")

    def re_configure(self):
        self.title.config(text="Your Speech is Ready!")
        self.subtitle.config(text="Download your Speech below")
        self.button.config(command=self.download_audio, text="Download Speech")
        messagebox.showinfo("Success", "Your speech is ready. Download it!")

        self.re_generate_button = Button(self.root, command=self.create_widgets, text="Generate Another",
                                         font=("Arial", 12))
        self.re_generate_button.pack()

    def download_audio(self):
        self.button.config(state="disabled")

        mp3_filename = "output.mp3"

        # Check if the file exists
        if os.path.exists(mp3_filename):
            # Prompt the user to choose a location to save the MP3 file
            destination_path = filedialog.asksaveasfilename(defaultextension=".mp3",
                                                            filetypes=[("MP3 files", "*.mp3"), ("All files", "*.*")])

            if destination_path:
                # Copy the MP3 file to the chosen location
                shutil.copy(mp3_filename, destination_path)
                print("File saved")
                messagebox.showinfo("File saved", "File successfully saved to destination")

            else:
                messagebox.showinfo("Error", "No destination selected.")
        else:
            messagebox.showinfo("Not Found", f"File {mp3_filename} not found.")


app = GUI()
app.root.mainloop()