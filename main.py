from number_day import GuessNumber
import os
import time

a = GuessNumber()
c = a.num_day
n = a.num_sort
t = a.attempts

linha = ('-'+'#'*40+'-')

while True:

    print("""
-###############- Adivinhe o numero! -###############-

            Escola um dos numeros abaixo

                 {} | {} | {} | {}
                 {} | {} | {} | {}

-####################################################-
        """.format(n[0], n[1], n[2], n[3], n[4], n[5], n[6], n[7]))

    h = int(input(": "))
    print(linha)

    os.system('cls')
    
    b = a.result_input(h)

    if b == 0:
        print(f'O resultado é menor que {h}, escolha outro numero: \n')
        t += 1
    elif b == 1:
        print(f'O resultado é maior que {h}, escolha outro numero: \n')
        t += 1
    elif b == 3:
        print(f"""
-#####################################-
    Parabens o você acertou {h} !!!

        Total de {t} tentativas:
-#####################################-
        """)
        break
    time.sleep(2)