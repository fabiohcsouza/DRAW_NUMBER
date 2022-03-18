import tkinter as tk
from tkinter import StringVar, ttk
from number_day import GuessNumber


class MyFrame(tk.Frame):
    def __init__(self, container, bg='#1f1f1f') -> None:
        super().__init__(container)
        # Variables function number day
        self.a = GuessNumber()
        self.text_var_punctuation = StringVar()
        self.text_var_attempts = StringVar()
        self.text_var_messager = StringVar()

        # Configure Frame 
        self.configure(bg='#1f1f1f')
        self.grid(row=0, column=0, padx=5, pady=5)

        self.main()


    def create_label_title(self):
        # Create Label
        ttk.Label(self, text='Adivinhe o numero!', font=("Helvetica", 18), justify='center', 
                    background='#ffffff').grid(row=0, column=0, columnspan=4) 


    def create_label_punctuation(self):
        # Create Label
        ttk.Label(self, textvariable=self.text_var_punctuation, font=("Helvetica", 11, 'bold'), justify='center', 
                    foreground='#ffffff', background='#1f1f1f').grid(row=1, column=0, columnspan=1, pady=5, sticky=tk.SE) 


    def create_label_attempts(self):
        # Create Label
        ttk.Label(self, textvariable=self.text_var_attempts, font=("Helvetica", 11, 'bold'), justify='center', 
                    foreground='#ffffff', background='#1f1f1f').grid(row=1, column=2, columnspan=3, pady=5, sticky=tk.SE)
    

    def create_label_messager(self):
        # Create Label
        ttk.Label(self, textvariable=self.text_var_messager, font=("Helvetica", 11, 'bold'), justify='center', 
                    foreground='#ffffff', background='#1f1f1f').grid(row=4, column=0, columnspan=4)

    
    def create_button(self):
        # Create Button
        n = self.a.num_sort
        ttk.Style().configure("TButton", padding='5 25', relief="flat")

        ttk.Button(self, text=n[0], command=lambda: self.num_result(int(n[0]))).grid(row=2, column=0, padx=5, pady=5, sticky=tk.NSEW)  
        ttk.Button(self, text=n[1], command=lambda: self.num_result(int(n[1]))).grid(row=2, column=1, padx=5, pady=5, sticky=tk.NSEW)  
        ttk.Button(self, text=n[2], command=lambda: self.num_result(int(n[2]))).grid(row=2, column=2, padx=5, pady=5, sticky=tk.NSEW)  
        ttk.Button(self, text=n[3], command=lambda: self.num_result(int(n[3]))).grid(row=2, column=3, padx=5, pady=5, sticky=tk.NSEW)  
        ttk.Button(self, text=n[4], command=lambda: self.num_result(int(n[4]))).grid(row=3, column=0, padx=5, pady=5, sticky=tk.NSEW)  
        ttk.Button(self, text=n[5], command=lambda: self.num_result(int(n[5]))).grid(row=3, column=1, padx=5, pady=5, sticky=tk.NSEW)  
        ttk.Button(self, text=n[6], command=lambda: self.num_result(int(n[6]))).grid(row=3, column=2, padx=5, pady=5, sticky=tk.NSEW)  
        ttk.Button(self, text=n[7], command=lambda: self.num_result(int(n[7]))).grid(row=3, column=3, padx=5, pady=5, sticky=tk.NSEW)  


    def num_result(self, num: int):
        # Variables number day
        b = self.a.result_input(num)
        t = self.a.attempts
        p = self.a.punctuation

        # Validade response button
        if b == 0:
            t += 1
            # Set str var, call function
            self.text_var_messager.set(f'O resultado é menor que {num}, escolha outro numero.')
            self.text_var_attempts.set(f'Tentativas: {self.a.attempts}')
            self.create_label_messager()
            self.create_label_attempts()

        # Validade response button
        elif b == 1:
            t += 1
            # Set str var, call function
            self.text_var_messager.set(f'O resultado é maior que {num}, escolha outro numero.')
            self.text_var_attempts.set(f'Tentativas: {self.a.attempts}')
            self.create_label_messager()
            self.create_label_attempts()

        # Validade response button
        elif b == 3:
            p += 1
            # Set str var, call function
            self.text_var_messager.set(f'Parabens você acertou {num} !!!')
            self.text_var_punctuation.set(f'Pontuação: {self.a.punctuation}')
            self.create_label_messager()
            self.create_label_punctuation()
            self.a.main()
            self.create_button()

    def main(self):
        # Set str var
        self.text_var_punctuation.set(f'Pontuação: {self.a.punctuation}')
        self.text_var_attempts.set(f'Tentativas: {self.a.attempts}')

        # Call modules
        self.create_label_title()
        self.create_label_attempts()
        self.create_label_punctuation()
        self.create_label_messager()
        self.create_button()

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Window, configure, label
        self.title("Adivinhe o numero!!!")
        self.geometry('390x260')
        self.configure(background='#1f1f1f')

        self.create_widgets()
    
    def create_widgets(self):
        a = MyFrame(self)


if __name__ == "__main__":
    app = App()
    app.mainloop()