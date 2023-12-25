# def odz(x, y):
#     return 1 <= x <= 8 and 1 <= y <= 8
# def rook(lad_x, lad_y, other_x, other_y):
#     return lad_x == other_x or lad_y == other_y
#
# def king(king_x, king_y, target_x, target_y):
#     return abs(king_x - target_x) <= 1 and abs(king_y - target_y) <= 1
#
# def queen(queen_x, queen_y, target_x, target_y):
#     return queen_x == target_x or queen_y == target_y or abs(queen_x - target_x) == abs(queen_y - target_y)
#
# def horse(knight_x, knight_y, target_x, target_y):
#     return (abs(knight_x - target_x) == 2 and abs(knight_y - target_y) == 1) or (abs(knight_x - target_x) == 1 and abs(knight_y - target_y) == 2)
# class Error(Exception):
#     def __init__(self, figure):
#         self.figure = figure
#         super().__init__(f"Неверное название фигуры: {figure}. Введите 'rook', 'king', 'queen' или 'knight'.")
# figures = ['rook', 'king', 'queen', 'knight']
#
#
# try:
#     f = input()
#     c1_x=int(input())
#     c1_y=int(input())
#     c2_x=int(input())
#     c2_y=int(input())
#     if f.lower() not in figures:
#         raise Error(f)
#     if not (odz(c1_x, c1_y) and odz(c2_x, c2_y)):
#         raise ValueError("Неверные координаты шахматной доски.")
#     if f=="rook":
#         if rook(c1_x, c1_y, c2_y, c2_y):
#             print("YES")
#         else:
#             print("NO")
#     elif f=="king":
#         if king(c1_x, c1_y, c2_y, c2_y):
#             print("YES")
#         else:
#             print("NO")
#     elif f=="queen":
#         if queen(c1_x, c1_y, c2_x, c2_y):
#             print("YES")
#         else:
#             print("NO")
#     elif f=="horse":
#         if horse(c1_x, c1_y, c2_x, c2_y):
#             print("YES")
#         else:
#             print("NO")
#
# except ValueError as e:
#     print(f"Ошибка: {e}")
# except Error as e:
#     print(f"Ошибка: {e}")
# except Exception as e:
#     print(f"Произошла ошибка: {e}")




def f(number):
    return 2+number
try:
    n=int(input())
    g=f(n)
except ValueError:
    print('Ожидаемый тип данных — число!')
else:
    print(g)




# try:
#     m=[1, 2, 3, 4, 5]
#     i=int(input("индекс: "))
#     e = m[i]
#     print(f"Элемент с индексом {i}: {e}")
# except IndexError:
#     print("Ошибка: Индекс выходит за границы массива.")
# except ValueError:
#     print("Ошибка: Введите целочисленный индекс.")


