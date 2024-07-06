# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer
# from tkinter import *
# Explicit imports to satisfy Flake8

from pathlib import Path
import subprocess
from tkinter import Tk, Canvas, Button, PhotoImage


def relative_to_assets(path: str) -> Path:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/start_page")
    return ASSETS_PATH / Path(path)


class StartPage:
    def __init__(self):
        self.window = Tk()
        self.window.title("Start Page - North Sussex Judo")
        self.window.iconbitmap("./assets/icon.ico")
        self.window.geometry("500x500")
        self.window.configure(bg="#F8F8F8")

        self.canvas = Canvas(
            self.window,
            bg="#F8F8F8",
            height=500,
            width=500,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        # Load and place background image
        image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(250.0, 250.0, image=image_image_1)

        # Load and place title line
        image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(250.0, 258.0, image=image_image_2)

        # Load and place start button
        button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.start_button_clicked,
            relief="flat"
        )
        self.button_1.place(x=96.0, y=284.0, width=311.0, height=50.0)

        # Load and place upper title ("North Sussex")
        image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
        self.image_3 = self.canvas.create_image(250.0, 141.0, image=image_image_3)

        # Load and place lower title ("Judo")
        image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
        self.image_4 = self.canvas.create_image(249.0, 207.0, image=image_image_4)

        self.window.resizable(False, False)
        self.window.mainloop()

    def start_button_clicked(self):
        self.window.destroy()
        subprocess.run(["python", "calc_page.py"])

