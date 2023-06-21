import tkinter as tk
import customtkinter as ctk
from assets.info import *
from PIL import Image

#window
window = ctk.CTk() #inherits from tk
window.title("Ryu Encryption")
window.iconbitmap("assets/logo.ico")
window.minsize(475, 300)
window.maxsize(475, 300)
ctk.set_appearance_mode("dark")

COLOR_DEFAULT = "Red"
COLOR_DEFAULT_HOVER ="Coral"

#sidebar
frame_sidebar = ctk.CTkFrame(window, fg_color="Coral")
frame_sidebar.pack(side=tk.LEFT)
frame_sidebar.pack_propagate(False)
frame_sidebar.configure(width=75, height=300)

#mainframe
frame_main = ctk.CTkFrame(window, fg_color="transparent")
frame_main.pack(side=tk.LEFT)
frame_main.pack_propagate(False)
frame_main.configure(width=400, height=300)

# Destroy all widgets within the frame
def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def tool():
	#clear frame
	clear_frame(frame_main)

	#widgets
	entry_upload = ctk.CTkEntry(frame_main,
		placeholder_text="Input Plaintext",
		width=300)
	entry_upload.pack()

	entry_key = ctk.CTkEntry(frame_main,
		placeholder_text="Input Key",
		width=300)
	entry_key.pack()


	#Encryption & Decryption Frame
	frame_encdec = ctk.CTkFrame(frame_main, fg_color="transparent")
	frame_encdec.pack(padx=10, pady=10)

	radio_var_encdec = tk.IntVar(value=0)
	radiobutton_encdec_1 = ctk.CTkRadioButton(frame_encdec,
		text="Encrypt",
		hover_color=COLOR_DEFAULT_HOVER,
		fg_color=COLOR_DEFAULT,
		variable= radio_var_encdec,
		value=1)

	radiobutton_encdec_2 = ctk.CTkRadioButton(frame_encdec,
		text="Decrypt",
		hover_color=COLOR_DEFAULT_HOVER,
		fg_color=COLOR_DEFAULT,
		variable= radio_var_encdec,
		value=2)
  
	radiobutton_encdec_1.pack()
	radiobutton_encdec_2.pack()

	#Level Frame
	frame_level = ctk.CTkFrame(frame_main, fg_color="transparent")
	frame_level.pack(padx=10, pady=10)

	radio_var_level = tk.IntVar(value=0)
	radiobutton_level_1 = ctk.CTkRadioButton(frame_level,
		text="Level 1",
		hover_color=COLOR_DEFAULT_HOVER,
		fg_color=COLOR_DEFAULT,
		variable= radio_var_level,
		value=1)
	radiobutton_level_2 = ctk.CTkRadioButton(frame_level,
		text="Level 2",
		hover_color=COLOR_DEFAULT_HOVER,
		fg_color=COLOR_DEFAULT,
		variable= radio_var_level,
		value=2)
	radiobutton_level_3 = ctk.CTkRadioButton(frame_level,
		text="Level 3",
		hover_color=COLOR_DEFAULT_HOVER,
		fg_color=COLOR_DEFAULT,
		variable= radio_var_level,
		value=3)

	radiobutton_level_1.pack()
	radiobutton_level_2.pack()
	radiobutton_level_3.pack()

	button_perform = ctk.CTkButton(frame_main,
		text="Perform",
		hover_color=COLOR_DEFAULT,
		fg_color=COLOR_DEFAULT_HOVER)
	button_perform.pack(pady=5)


	entry_download = ctk.CTkEntry(frame_main,
		placeholder_text="Output Ciphertext",
		width=300)
	entry_download.pack()

def info():
	#clear frame
	clear_frame(frame_main)

	infobox = ctk.CTkTextbox(frame_main, width=400, height=300, wrap="word")
	infobox.insert("0.0", INFO)  # insert at line 0 character 0
	infobox.configure(state="disabled")  # configure textbox to be read-only
	infobox.pack()
	

image_info = ctk.CTkImage(
	light_image = Image.open("assets/button_info.png"),
	dark_image = Image.open("assets/button_info.png"))
image_tool = ctk.CTkImage(
	light_image = Image.open("assets/button_tool.png"),
	dark_image = Image.open("assets/button_tool.png"))

button_info = ctk.CTkButton(frame_sidebar, text=None, command=lambda:info(), image=image_info, fg_color="transparent", height=150)
button_tool = ctk.CTkButton(frame_sidebar, text=None, command=lambda:tool(), image=image_tool, fg_color="transparent", height=150)
button_info.pack()
button_tool.pack()

#run
tool()
window.mainloop()