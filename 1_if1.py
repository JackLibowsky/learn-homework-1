"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""
age = int(input('Введите ваш взраст: '))

def main():
    if age < 7:
        print('ходит в детский сад')
    elif age < 18:
        print('ходит в школу')
    elif age <= 24:
        print('учится в ВУЗе')
    else:
        print('Работает')

if __name__ == "__main__":
    main()