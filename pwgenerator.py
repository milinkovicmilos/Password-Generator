'''
Password Generator made to generate random passwords of desired length and with
selectable set of characters
'''

import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Password Generator")
        self.resizable(True, True)
        self.frame = tk.Frame(self)

        self.len_var = tk.StringVar()
        self.char_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        '''Creates widgets'''

        paddingx = (10, 50)
        paddingy = (20, 20)
        self.frame.grid()

        # Labels
        label = tk.Label(self.frame, text="Password Generator")
        len_label = tk.Label(self.frame, text="Password length")

        # Checkboxes
        lc_checkbox = tk.Checkbutton(self.frame, text="Lowercase letters")
        uc_checkbox = tk.Checkbutton(self.frame, text="Uppercase letters")
        n_checkbox = tk.Checkbutton(self.frame, text="Numbers")
        sc_checkbox = tk.Checkbutton(self.frame, text="Special characters (\" !\"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~\")")
        c_checkbox = tk.Checkbutton(self.frame, text="Custom set of special characters")

        # Buttons
        start_button = tk.Button(self.frame, text="Generate randomly", padx=20)
        test_button = tk.Button(self.frame, text="Generate randomly by mouse", padx=20)

        # Input field

        len_inputfield = tk.Entry(self.frame, textvariable=self.len_var)
        char_inputfield = tk.Entry(self.frame, textvariable=self.char_var)

        # Showing them on screen
        label.grid(column=0, row=0, columnspan=2, pady=paddingy)
        len_label.grid(column=0, row=8, padx=paddingx, sticky="e")

        lc_checkbox.grid(column=0, row=1, sticky="w")
        uc_checkbox.grid(column=0, row=2, sticky="w")
        n_checkbox.grid(column=0, row=3, sticky="w")
        sc_checkbox.grid(column=0, row=4, sticky="w")
        c_checkbox.grid(column=0, row=5, sticky="w")

        start_button.grid(column=0, row=7, padx=paddingx, pady=paddingy, sticky="w")
        test_button.grid(column=1, row=7, padx=(0,20), pady=paddingy, sticky="e")

        len_inputfield.grid(column=1, row=8, pady=paddingy, sticky="w")
        char_inputfield.grid(column=1, row=6)

if __name__ == "__main__":
    app = App()
    app.mainloop()
