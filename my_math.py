# class Animal:
#     def __init__(self, name):
#        self.name = name

#     def walk(self):
#         print('걷는다!')

#     def eat(self):
#         print(f'{self.name}!먹는다!')

# dog = Animal('dog')
# dog.walk()

# lunch = ['짜장면', '짬뽕', '탕수육']

# for idx, num in enumerate (lunch):
#     print(idx, num)
#     # 아래는 출력 예시입니다.
#     # 0 짜장면
#     # 1 짬뽕
# #     # 2 탕수육

# documents = ['java', 'python', 's5g4', 's5g2', 'spring', 'django', 'extra']
# python_class = [documents[i+1] for i in range(0, 9, 2)]

# print(python_class)


numbers = [4,6,10,-8,5]
for i in range(len(numbers)):
    numbers[i] = numbers[i]*2

print(numbers)