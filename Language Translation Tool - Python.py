import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES
from PIL import Image, ImageTk

class TranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fancy Translator")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")

        self.translator = Translator()

    
        try:
            self.bg_image = Image.open("background.jpg")  # Ensure this file exists in the correct directory
        except FileNotFoundError:
            messagebox.showerror("File Not Found", "background.jpg not found. Please make sure the file exists.")
            self.root.destroy()
            return

        self.bg_image = self.bg_image.resize((800, 600), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
    
        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    

        # Create a title label
        self.title_label = tk.Label(self.root, text="Fancy Translator", font=("Helvetica", 24, "bold"), bg="#ffffff", fg="#303f9f", relief="solid")
        self.title_label.pack(pady=20)

        # Create frames for input and output
        self.input_frame = tk.Frame(self.root, bg="#ffffff", relief="solid", bd=2)
        self.input_frame.pack(pady=10, padx=20, fill="x")

        self.output_frame = tk.Frame(self.root, bg="#ffffff", relief="solid", bd=2)
        self.output_frame.pack(pady=10, padx=20, fill="x")

        # Source language dropdown
        self.src_lang_label = tk.Label(self.input_frame, text="Source Language:", font=("Helvetica", 14), bg="#ffffff", fg="#303f9f")
        self.src_lang_label.grid(row=0, column=0, padx=10, pady=10)

        self.src_lang = tk.StringVar()
        self.src_lang.set("english")
        self.src_lang_menu = ttk.Combobox(self.input_frame, textvariable=self.src_lang, values=list(LANGUAGES.values()), font=("Helvetica", 12))
        self.src_lang_menu.grid(row=0, column=1, padx=10, pady=10)

        # Target language dropdown
        self.tgt_lang_label = tk.Label(self.input_frame, text="Target Language:", font=("Helvetica", 14), bg="#ffffff", fg="#303f9f")
        self.tgt_lang_label.grid(row=0, column=2, padx=10, pady=10)

        self.tgt_lang = tk.StringVar()
        self.tgt_lang.set("spanish")
        self.tgt_lang_menu = ttk.Combobox(self.input_frame, textvariable=self.tgt_lang, values=list(LANGUAGES.values()), font=("Helvetica", 12))
        self.tgt_lang_menu.grid(row=0, column=3, padx=10, pady=10)

        # Input text area
        self.input_text = tk.Text(self.input_frame, height=10, width=50, font=("Helvetica", 14), bd=2, relief="groove")
        self.input_text.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

        # Translate button with a fancy style
        self.translate_button = tk.Button(self.root, text="Translate", font=("Helvetica", 16, "bold"), bg="#ff7043", fg="#ffffff", command=self.translate_text, relief="raised", bd=5)
        self.translate_button.pack(pady=20)

        # Output text area
        self.output_text = tk.Text(self.output_frame, height=10, width=50, font=("Helvetica", 14), bd=2, relief="groove", state="disabled")
        self.output_text.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

    def translate_text(self):
        src_lang = self.src_lang_menu.get()
        tgt_lang = self.tgt_lang_menu.get()
        text_to_translate = self.input_text.get("1.0", tk.END).strip()

        if not text_to_translate:
            messagebox.showwarning("Input Error", "Please enter text to translate")
            return

        src_lang_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(src_lang.lower())]
        tgt_lang_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(tgt_lang.lower())]

        try:
            translated = self.translator.translate(text_to_translate, src=src_lang_code, dest=tgt_lang_code)
            self.output_text.config(state="normal")
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, translated.text)
            self.output_text.config(state="disabled")
        except Exception as e:
            messagebox.showerror("Translation Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()
