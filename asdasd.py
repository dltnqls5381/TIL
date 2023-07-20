# numbers = [1, 2, 3]
# result = map(str, numbers)

# print(result)

# print(list(result))
# result = []
# for number in numbers:
#     result.append(str(number))



# print(result)

def func_name(parm1,parm2):
    return parm1+parm2
print(func_name(1,2))

def add_numbers(x,y):
    result = x+y
    return result

a=2
b=3
s=add_numbers(a,b)
print(s)

def greet(name,age=30):
    print(f'안녕하세요,{name}님! {age}살 이시군요!')

greet(age=30, name="홍길동")
greet("bob")

print('첫', '두' ,'세', end='\t',sep=':')
print('다음 줄')

def func(*S, sep=''):
    print(S, sep)

print("첫",   "두",   "세")




  

    