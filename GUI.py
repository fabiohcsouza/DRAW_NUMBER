import tkinter as tk
from tkinter import StringVar, ttk
from number_day import GuessNumber



class Button(tk.Frame):
    def __init__(self, container, bg='#1f1f1f') -> None:
        super().__init__(container)
        self.a = GuessNumber()

        self.configure(bg='#1f1f1f')
        self.grid(row=0, column=0, padx=5, pady=5)
        
        self.create_label()
        self.create_button()



    def create_label(self):
        self.label_0 = ttk.Label(self, text=f'Pontuação: {self.a.punctuation}', font=("Helvetica", 11, 'bold'), justify='center', foreground='#ffffff', background='#1f1f1f')
        self.label_0.grid(row=0, column=0, columnspan=1, pady=5, sticky=tk.SE) 

        self.label_1 = ttk.Label(self, text=f'Tentativas: {self.a.attempts}', font=("Helvetica", 11, 'bold'), justify='center', foreground='#ffffff', background='#1f1f1f')
        self.label_1.grid(row=0, column=2, columnspan=3, pady=5, sticky=tk.SE)


    def create_button(self):
        n = self.a.num_sort
        ttk.Style().configure("TButton", padding='5 25', relief="flat", bg="#ffffff", fg='#000000')

        self.buton_0 = ttk.Button(self, text=n[0], command=lambda: self.num_result(int(n[0])))
        self.buton_0.grid(row=1, column=0, padx=5, pady=5, sticky=tk.NSEW)

        self.buton_1 = ttk.Button(self, text=n[1], command=lambda: self.num_result(int(n[1])))
        self.buton_1.grid(row=1, column=1, padx=5, pady=5, sticky=tk.NSEW)

        self.buton_2 = ttk.Button(self, text=n[2], command=lambda: self.num_result(int(n[2])))
        self.buton_2.grid(row=1, column=2, padx=5, pady=5, sticky=tk.NSEW)

        self.buton_3 = ttk.Button(self, text=n[3], command=lambda: self.num_result(int(n[3])))
        self.buton_3.grid(row=1, column=3, padx=5, pady=5, sticky=tk.NSEW)

        self.buton_4 = ttk.Button(self, text=n[4], command=lambda: self.num_result(int(n[4])))
        self.buton_4.grid(row=2, column=0, padx=5, pady=5, sticky=tk.NSEW)

        self.buton_5 = ttk.Button(self, text=n[5], command=lambda: self.num_result(int(n[5])))
        self.buton_5.grid(row=2, column=1, padx=5, pady=5, sticky=tk.NSEW)

        self.buton_6 = ttk.Button(self, text=n[6], command=lambda: self.num_result(int(n[6])))
        self.buton_6.grid(row=2, column=2, padx=5, pady=5, sticky=tk.NSEW)

        self.buton_7 = ttk.Button(self, text=n[7], command=lambda: self.num_result(int(n[7])))
        self.buton_7.grid(row=2, column=3, padx=5, pady=5, sticky=tk.NSEW)  


    def num_result(self, num: int):
        b = self.a.result_input(num)
        t = self.a.attempts
        p = self.a.punctuation

        if b == 0:
            print(f'O resultado é menor que {num}, escolha outro numero: \n')
            t += 1
            self.update1()
        elif b == 1:
            print(f'O resultado é maior que {num}, escolha outro numero: \n')
            t += 1
            self.update1()
 
        elif b == 3:
            print(f'Parabens {num} \n')
            p += 1
            self.update2()
            self.a.main()
            self.create_button()
            self.update4()

    def update1(self):
        self.label_1['text'] = f'Pontuação: {self.a.attempts}'
        print(self.a.attempts)


    def update2(self):
        self.label_0['text'] = f'Tentativas: {self.a.punctuation}'
        print(self.a.punctuation)

    def update4(self):
        n = self.a.num_sort

        self.buton_0['text'] = text=n[0]
        self.buton_0['command']=lambda: self.num_result(int(n[0]))

        self.buton_1['text'] = text=n[1]
        self.buton_1['command']=lambda: self.num_result(int(n[1]))

        self.buton_2['text'] = text=n[2]
        self.buton_2['command']=lambda: self.num_result(int(n[2]))

        self.buton_3['text'] = text=n[3]
        self.buton_3['command']=lambda: self.num_result(int(n[3]))

        self.buton_4['text'] = text=n[4]
        self.buton_4['command']=lambda: self.num_result(int(n[4]))

        self.buton_5['text'] = text=n[5]
        self.buton_5['command']=lambda: self.num_result(int(n[5]))

        self.buton_6['text'] = text=n[6]
        self.buton_6['command']=lambda: self.num_result(int(n[6]))

        self.buton_7['text'] = text=n[7]
        self.buton_7['command']=lambda: self.num_result(int(n[7]))


        
class MyLabel(tk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.create_label()
        self.create_widgets()
        self.configure(background='#ffffff')
        self.grid(row=0, column=0, padx=5, pady=5)
    
    def create_label(self):
        self.label_0 = ttk.Label(self, text='Adivinhe o numero!', font=("Helvetica", 18), justify='center', background='#ffffff')
        self.label_0.grid(row=0, column=0) 

        self.label_1 = ttk.Label(self, background='#1f1f1f')
        self.label_1.grid(row=1, column=0)

    def create_widgets(self):
        b = Button(self.label_1)


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Window, configure, label
        self.title("Adivinhe o numero!!!")
        self.geometry('395x240')
        self.configure(background='#1f1f1f')

        self.create_widgets()
    
    def create_widgets(self):
        l = MyLabel(self)


if __name__ == "__main__":
    app = App()
    app.mainloop()