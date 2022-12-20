import tkinter
import customtkinter

customtkinter.set_appearance_mode('system')
customtkinter.set_default_color_theme('dark-blue')

root = customtkinter.CTk()
root.geometry('400x240')

def buttonFunction():
    print("pressed")

button = customtkinter.CTkButton(master = root, text = 'CTKButton', command = buttonFunction)
button.place(relx = 0.5, rely = 0.5, anchor = customtkinter.CENTER)

root.mainloop()