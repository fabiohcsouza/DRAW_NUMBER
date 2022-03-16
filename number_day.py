"""
Esse algoritmo deve sortear um numero e o usuario deve advinhar esse numero.

    1. Sortear uma sequencia de 8 numero e armazenar em uma var=list.
    2. Sortear 1 numero da var=list e armazenar var=num_day.
    3. Mostar na tela as 8 opções da var=list e solicitar input ao usuario.
    4. comparar input com var=num_day e salvar as tentavas caso o usuario erre.
    5. caso o input == var=num_day input true. 

"""

import random

class GuessNumber():
    def __init__(self) -> None:
        super().__init__()
        self.num_sort = []
        self.num_day = 0
        self.attempts = 0
        self.punctuation = 0
        self.main()


    def sort_number(self, num: list):
        """Draw the num: list."""
        out = random.choice(num)
        return out
    

    def list_num(self, qtdx: int, qtdy: int):
        """Generate a list of num: x, y."""
        return list(range(qtdx, qtdy))

    def result_input(self, num: int):
        """Compare if the number num: int == num.day."""
        c = self.num_day

        if num > c:
            self.attempts += 1
            return 0
        elif num < c:
            self.attempts += 1
            return 1
        elif num == c:
            self.attempts += 1
            self.punctuation += 1
            self.num_sort.clear()
            return 3

    def main(self):
        # Range number to draw
        list_num = self.list_num(1, 100)
        for num in range(8):
            a = self.sort_number(list_num)
            # Validates if the number is not repeated and add to the list: num_sort
            if a is not self.num_sort:
                self.num_sort.append(a)
            pass
        # Draw and set the number of the day
        self.num_day = self.sort_number(self.num_sort)
        
