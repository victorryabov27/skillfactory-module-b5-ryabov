# Приветствие
def greet():
    print("                 ""\n"
          "Приветствуем  вас""\n"
          "     в  игре     ""\n"
          "крестики - нолики""\n"
          "                 ""\n"
          "формат ввода: x y""\n"
          "x - номер  строки""\n"
          "y - номер столбца""\n")


greet()


# Игровое поле
field = [[" "] * 3 for i in range(3)]


def show():
    print("   0  1  2")
    for i in range(3):
        print(i, end="")
        for j in range(3):
            print("  "f"{field[i][j]}", end="")
        print()
    print()


# Запрос координат
def ask():
    while True:
        cords = input("Ваш ход: ").split()
        if len(cords) != 2:
            print("Введите 2 координаты!")
            continue
        x, y = cords
        if not x.isdigit() or not y.isdigit():
            print("Координаты должны быть цифрами!")
            continue
        x, y = int(x), int(y)
        if x < 0 or x > 2 or y < 0 or y > 2:
            print("Такой клетки не существует!")
            continue
        if field[x][y] != " ":
            print("Эта клетка уже занята!")
            continue
        return x, y


# Проверка выигрышных комбинаций
def check_win():
    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(field[i][j])
        if symbols == ["X", "X", "X"]:
            print("Выиграл крестик!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл нолик!")
            return True
    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(field[j][i])
        if symbols == ["X", "X", "X"]:
            print("Выиграл крестик!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл нолик!")
            return True
    symbols = []
    for i in range(3):
        symbols.append(field[i][i])
    if symbols == ["X", "X", "X"]:
        print("Выиграл крестик!")
        return True
    if symbols == ["0", "0", "0"]:
        print("Выиграл нолик!")
        return True
    symbols = []
    for i in range(3):
        symbols.append(field[i][2 - i])
    if symbols == ["X", "X", "X"]:
        print("Выиграл крестик!")
        return True
    if symbols == ["0", "0", "0"]:
        print("Выиграл нолик!")
        return True
    return False


# Вывод игры
num = 0
while True:
    num += 1
    if num % 2 == 1:
        print("  Ходит крестик")
    else:
        print("  Ходит нолик")
    x, y = ask()
    if num % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"
    show()
    if check_win():
        break
    if num == 9:
        print("Ничья!")
        break
