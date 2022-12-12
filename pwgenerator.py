'''
Password Generator made to generate random passwords of desired length and with
selectable set of characters
'''

import tkinter as tk
import generator

class App(tk.Tk):
    '''Tkinter app for generating random passwords'''
    MAX_PWSIZE = 256

    def __init__(self):
        super().__init__()

        # Settings basic window parameters
        self.title("Password Generator")
        self.resizable(False, False)
        self.frame = tk.Frame(self)

        # Making variables for checkboxes and inputfields
        self.len_var = tk.StringVar()
        self.char_var = tk.StringVar()
        self.info_var = tk.StringVar()
        self.lc_checkbox_var = tk.IntVar()
        self.uc_checkbox_var = tk.IntVar()
        self.n_checkbox_var = tk.IntVar()
        self.sc_checkbox_var = tk.IntVar()
        self.c_checkbox_var = tk.IntVar()
        self.show_hide_var = tk.IntVar()
        self.create_widgets()

    def create_widgets(self):
        '''Creates widgets'''

        paddingx = (10, 0)
        paddingy = (10, 10)
        self.frame.grid()

        # Labels
        label = tk.Label(self.frame, text="Password Generator")
        len_label = tk.Label(self.frame, text="Password length (max 256)")
        self.info_label = tk.Label(self.frame, text="", textvariable=self.info_var)
        self.pw_text = tk.Entry(self.frame, width=128, justify="center")
        self.pw_text.config(state="readonly")

        # Checkboxes
        lc_checkbox = tk.Checkbutton(self.frame, text="Lowercase letters",
            variable=self.lc_checkbox_var)
        uc_checkbox = tk.Checkbutton(self.frame, text="Uppercase letters",
            variable=self.uc_checkbox_var)
        n_checkbox = tk.Checkbutton(self.frame, text="Numbers",
            variable=self.n_checkbox_var)
        self.sc_checkbox = tk.Checkbutton(
            self.frame,
            text="Special characters (\" !\"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~\")",
            variable=self.sc_checkbox_var,
            command=self.update_checkbox)
        self.c_checkbox = tk.Checkbutton(
            self.frame,
            text="Custom set of special characters",
            variable=self.c_checkbox_var,
            command=self.update_inputfield)
        self.show_hide_check = tk.Checkbutton(self.frame, text="Hide password",
            variable=self.show_hide_var,
            command=self.update_pw)

        # Buttons
        start_button = tk.Button(self.frame, text="Generate randomly",
            command=self.generate_randomly, height=2, width=51)
        start2_button = tk.Button(self.frame, text="Generate randomly by mouse",
            command=self.generate_randomly_mouse, height=2, width=51)
        copy_button = tk.Button(self.frame, text="Copy password to clipboard",
            command=self.copy_to_clipboard, height=2, width=50)

        # Input fields
        l_vcmd = (self.register(self.validate_length), "%S", "%d")
        len_inputfield = tk.Entry(self.frame, textvariable=self.len_var,
            validate="key", validatecommand=l_vcmd)

        c_vcmd = (self.register(self.validate_characters), "%S", "%d")
        self.char_inputfield = tk.Entry(self.frame, textvariable=self.char_var,
                validate="key", validatecommand=c_vcmd)

        # Showing them on screen
        label.grid(column=0, row=0, columnspan=2, pady=paddingy)
        len_label.grid(column=0, row=6, pady=paddingy, padx=paddingx, sticky="e")
        self.info_label.grid(column=0, row=7, sticky="n", columnspan=2)
        self.pw_text.grid(column=0, row=9, columnspan=2, pady=(20, 10), padx=(20, 20))

        lc_checkbox.grid(column=0, row=1, padx=paddingx, sticky="w")
        uc_checkbox.grid(column=0, row=2, padx=paddingx, sticky="w")
        n_checkbox.grid(column=0, row=3, padx=paddingx, sticky="w")
        self.sc_checkbox.grid(column=0, row=4, padx=paddingx, sticky="w")
        self.c_checkbox.grid(column=0, row=5, padx=paddingx, sticky="w")
        self.show_hide_check.grid(column=0, row=10, padx=paddingx, sticky="w")

        start_button.grid(column=0, row=8, pady=paddingy, sticky="n")
        start2_button.grid(column=1, row=8, pady=paddingy, sticky="n")
        copy_button.grid(column=0, row=10, pady=(2, 20), columnspan=2, sticky="n")

        len_inputfield.grid(column=1, row=6, pady=(5, 5), sticky="w")

    def update_pw(self):
        if self.show_hide_var.get():
            self.show_hide_check.configure(text="Show password")
            self.pw_text.configure(show='*')
        else:
            self.show_hide_check.configure(text="Hide password")
            self.pw_text.configure(show='')

    def update_inputfield(self):
        '''Updating the characters inputfield based on checkbox state'''
        if not self.c_checkbox_var.get():
            # If checkbox is off we delete the inputfield
            self.char_inputfield.delete(0, len(self.char_inputfield.get()))
            self.char_inputfield.grid_forget()
        else:
            # If checkbox is checked we make the inputfield and disable the
            # checkbox that indicates use of all special characters
            self.char_inputfield.grid(column=0, row=6, padx=(35, 0), sticky="w")
            self.sc_checkbox.deselect()

    def update_checkbox(self):
        '''Updating when special characters checkbox is being checked'''
        if self.sc_checkbox_var.get():
            # If checkbox is on we delete the inputfield and deselect the checkbox
            # for custom selected characters
            self.char_inputfield.delete(0, len(self.char_inputfield.get()))
            self.char_inputfield.grid_forget()
            self.c_checkbox.deselect()

    def validate_length(self, value, action):
        '''Checks if the entered number is integer'''
        # If "0" is passed from %d percent substitution that means
        # deletion is being made (see Tk entry page)
        if action == "0":
            return True

        length_val = self.len_var.get()
        try:
            # Checks if user entered valid integer
            int(value)

            # For style purpose; so user doesn't enter 0s before actual desired
            # password length
            if length_val == "" and value == "0":
                self.bell()
                return False

            # Checks if user is trying to enter password longer than specified
            if int(self.len_var.get() + value) <= self.MAX_PWSIZE:
                return True
            else:
                self.bell()
                return False
        except:
            # In case invalid integer is entered
            self.bell()
            return False

    def validate_characters(self, value, action):
        '''Checks if the entered set of special characters is good'''
        # If "0" is passed from %d percent substitution that means
        # deletion is being made (see Tk entry page)
        if action == str(0):
            return True

        if value in generator.SPECIAL_CHARACTERS and value not in self.char_inputfield.get():
            return True
        else:
            self.bell()
            return False

    def validate_run(self):
        '''
        Used to check if at least one option for characters is selected
        and that desired length of password is valid and not 0
        '''
        # Getting the value of length inputfield
        length = self.len_var.get()
        # Making a array of checkbox values
        checks = []
        checks.append(self.lc_checkbox_var.get())
        checks.append(self.uc_checkbox_var.get())
        checks.append(self.n_checkbox_var.get())

        # Used to determine special characters that are going to be used
        chars = ""

        # Adding special characters
        if self.sc_checkbox_var.get():
            chars = generator.SPECIAL_CHARACTERS
        else:
            chars = self.char_inputfield.get()

        rtrn_val = {
            "valid" : False,
            "length" : length,
            "checks" : checks,
            "chars" : chars
        }
        if length != "" and (1 in checks or chars != ""):
            rtrn_val["valid"] = True

        return rtrn_val

    def generate_randomly(self):
        '''Used by generate randomly button'''
        validate = self.validate_run()
        if validate["valid"]:
            # Generating password
            password = generator.create_password(int(validate["length"]),
                                                validate["checks"], validate["chars"])
            # Changing the value of password
            self.pw_text.config(state="normal")
            self.pw_text.delete(0, len(self.pw_text.get()))
            self.pw_text.insert(0, password)
            self.pw_text.config(state="readonly")
        else:
            self.bell()

    def generate_randomly_mouse(self):
        '''Used by generate randomly by mouse button'''
        validate = self.validate_run()
        if validate["valid"]:
            # Generating password
            self.info_var.set("Keep moving mouse to create random password")
            # Making a function to call after first waiting for info label to show
            def make_pw():
                password = ""
                for i in range(int(validate["length"])):
                    password += generator.create_password_mouse(validate["checks"],
                                                                validate["chars"])
                # Changing the value of password
                self.pw_text.config(state="normal")
                self.pw_text.delete(0, len(self.pw_text.get()))
                self.pw_text.insert(0, password)
                self.pw_text.config(state="readonly")
                self.info_var.set("")
            self.info_label.after(100, make_pw)
        else:
            self.bell()

    def copy_to_clipboard(self):
        password = self.pw_text.get()
        self.clipboard_clear()
        self.clipboard_append(password)

if __name__ == "__main__":
    app = App()
    app.mainloop()
