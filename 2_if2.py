"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""
string_1 = ''
string_2 = ''

def main(string_1, string_2):
      if not type(string_1) == type(string_2) != type(str):
            return 0
      elif string_2 == string_1:
            return 1
      elif len(string_1) > len(string_2):
            return 2
      elif string_2 == 'learn':
            return 3
      else:
            print('Я без понятия чего ты хочешь')
    
if __name__ == "__main__":
    main(string_1, string_2)

print(main('asd', 1)) # Долже вернуться 0
print(main('asd', 'asd')) # Долже вернуться 1
print(main('asdasd', 'asd')) # Долже вернуться 2
print(main('asd', 'learn')) # Долже вернуться 3