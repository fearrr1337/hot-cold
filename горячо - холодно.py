import random

botNumber = random.randint(1,20)
playerNumber = int(input('Введите свое число от 1 до 20: '))

while botNumber != playerNumber:
    if botNumber - playerNumber <= 2:
        print('Горячо')
    elif botNumber - playerNumber < 2 <= 4:
        print('Тепло')
    else:
        print('Холодно')
    playerNumber = int(input('Введите свое число от 1 до 20: '))
print(f"ты угадал, моё число: {botNumber}")