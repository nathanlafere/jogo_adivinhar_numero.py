import random

def game():
    secret_number = random.randint(1,100)
    tentativa = float(input('Tente um número :').replace(',','.'))
    while True:
        if tentativa - int(tentativa) != 0: 
            print(f'O valor da sua tentativa foi {int(tentativa)}, valores após a vírgula serão ignorados.')
        if int(tentativa) == secret_number:
            print('~=~'*80)
            print('~=~'*14,'Parabéns você acertou o número XD.','~=~'*14)
            print('~=~'*80)
            return
        elif int(tentativa) > secret_number:
            print('~=~'*80)
            tentativa = float(input('Muito alto, tente um número menor :').replace(',','.'))
        else:
            print('~=~'*80)
            tentativa = float(input('Muito baixo, tente um número maior :').replace(',','.'))

while True:
    first_Q = input('Deseja jogar (S/N): ').upper()
    if first_Q[0] == 'S':
        game()
    if first_Q[0] == 'N':
        break
    else:
        first_Q = input('Por favor digite apenas S ou N: ').upper()
        if first_Q[0] == 'S':
            game()
        if first_Q[0] == 'N':
            break