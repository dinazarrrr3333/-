import random
count = 0
for number in range(10):
    player = int(input("""выберите ход
    1 камень
    2 ножницы
    3 бумага
    твой ответ?   """))
    
    if player ==1:
        print("вы выбрал камень  ")
    elif player ==2:
        print("вы выбрали ножнецы  ")
    elif player ==3:
        print("вы выбрали бумагу  ")
    else:
        print("я вас не понял")
    comp = random.randint(1,3)
    if comp ==1:
        print("он выбрал камень  ")
    elif comp == 2:
        print("он выбрал ножницы  ")
    else:
        print("он выбрал бумагу  ")
    if player == comp:
        print("ничья")
    elif player == 1 and comp == 3 or player == 3 and comp == 2 or player == 2 and comp == 1:
        print("вы прoиграли")
    else:
        print( "вы выиграли")
        count += 1
    if count == 3:
        print("игра окончена!")
        break

