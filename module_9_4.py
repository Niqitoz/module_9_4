import random

first = 'Мама мыла раму'
second = 'Рамена мало было'

a = list(map(lambda x,y: x==y, first, second))

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        file = open(file_name, 'w', encoding='utf8')
        for data in data_set:
            file.write(str(data))
        file.close()
    return write_everything

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return random.choice(self.words)

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
first_ball = MysticBall('Да', 'Нет', 'Наверное', 'Странно')
print(first_ball())
print(first_ball())
print(first_ball())