from tkinter import *
from tkinter import messagebox, scrolledtext
import os
import time

BG_COLOR = "#333333"
HL_COLOR = "ORANGE"
TEXT_COLOR = "white"

class MainUi():
    def __init__(self):
        # window
        self.window = Tk()
        self.window.title("Asset Publisher")
        self.window.config(padx=10, pady=10, bg=BG_COLOR)
        self.window.resizable(False, False)

        # title
        self.title = Label(text="Asset Publisher :", font=("Arial", 20, "bold"), height=2, bg=BG_COLOR, fg=TEXT_COLOR)
        self.title.grid(row=0, column=0, columnspan=3)

        # user names
        self.asset_label = Label(text="Asset Name :", height=2, bg=BG_COLOR, fg=TEXT_COLOR)
        self.asset_entry = Entry(width=40)
        self.asset_label.grid(row=1, column=0)
        self.asset_entry.grid(row=1, column=1, columnspan=2)
        
        self.descr_label = Label(text="Description :", height=2, bg=BG_COLOR, fg=TEXT_COLOR)
        self.descr_entry = Entry(width=40)
        self.descr_label.grid(row=2, column=0)
        self.descr_entry.grid(row=2, column=1, columnspan=2)

        # settings
        self.settings_label = Label(text="Settings :", font=("Arial", 15, "bold"), bg=BG_COLOR, fg=TEXT_COLOR)
        self.settings_label.grid(row=3, column=0, columnspan=3, pady=10)

        # checkboxes
        self.geo_cbox_label = Label(text="Geometry", bg=BG_COLOR, fg=TEXT_COLOR).grid(row=4, column=0)
        self.geo_cbox_label = Label(text="Textures", bg=BG_COLOR, fg=TEXT_COLOR).grid(row=4, column=1)
        self.geo_cbox_label = Label(text="Shader", bg=BG_COLOR, fg=TEXT_COLOR).grid(row=4, column=2)
        self.geo_cbox = IntVar()
        Checkbutton(variable=self.geo_cbox, bg=BG_COLOR, activebackground=BG_COLOR).grid(row=5, column=0)
        self.tex_cbox = IntVar()
        Checkbutton(variable=self.tex_cbox, bg=BG_COLOR, activebackground=BG_COLOR).grid(row=5, column=1)
        self.shader_cbox = IntVar()
        Checkbutton(variable=self.shader_cbox, bg=BG_COLOR, activebackground=BG_COLOR).grid(row=5, column=2)

        # output window
        self.output = scrolledtext.ScrolledText(width=40, height=8)
        self.output.insert(END, "Ready to publish...")
        self.output.config(state="disabled")
        self.output.grid(row=7, columnspan=3, padx=10, pady=20, sticky="nsew")

        # buttons
        self.create_btn = Button(text="Create", width=10, bg=BG_COLOR, fg=TEXT_COLOR, activebackground=HL_COLOR, command=self.publish)
        self.create_btn.grid(row=8, column=1, padx=0, pady=5)
        self.cancel_btn = Button(text="Cancel", width=10, bg=BG_COLOR, fg=TEXT_COLOR, activebackground=HL_COLOR, command=self.close)
        self.cancel_btn.grid(row=8, column=2, padx=0, pady=5)

        self.window.mainloop()

    def close(self):
        self.window.destroy()

    def publish(self):
        # simulate publishing
        if self.asset_entry.get() != "" and self.descr_entry.get() != "":
            if self.geo_cbox.get() == 1 or self.tex_cbox.get() == 1 or self.shader_cbox.get() == 1:
                self.output.config(state="normal")
                self.output.delete("1.0", END)

                self.output.insert(END, "Starting publish...")
                self.output.insert(END, f"\nAsset name : {self.asset_entry.get()}")
                self.output.insert(END, f"\nDescription : {self.descr_entry.get()}")
                self.output.insert(END, f"\nUser : {os.getlogin()}")
                self.output.update()

                if self.geo_cbox.get() == 1:
                    self.output.insert(END, "\nPublishing geo...")
                    self.output.update()
                    time.sleep(1.5)
                    self.output.insert(END, "\nGeometry published!")
                    self.output.update()
                    self.output.yview_moveto(1)
                    

                if self.tex_cbox.get() == 1:
                    time.sleep(0.5)
                    self.output.insert(END, "\nPublishing textures...")
                    self.output.update()
                    time.sleep(2)
                    self.output.insert(END, "\nTextures published!")
                    self.output.update()
                    self.output.yview_moveto(1)

                if self.shader_cbox.get() == 1:
                    time.sleep(0.5)
                    self.output.insert(END, "\nPublishing shaders...")
                    self.output.update()
                    time.sleep(1)
                    self.output.insert(END, "\nShader published!")
                    self.output.update()
                    self.output.yview_moveto(1)

                self.output.insert(END, "\nPublish was successfull!")
                self.output.yview_moveto(1)
                self.output.config(state="disabled")
            else:
                messagebox.showwarning("Warning", "Please, select at least one element to publish.")
        else:
            messagebox.showwarning("Warning", "Please name your asset and add description.")


if __name__ == "__main__":
    ui = MainUi()
