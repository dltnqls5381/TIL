# dust=35

# if dust>150:
#     print("매우나쁨")
# if dust>300:
#     print("위험해요! 나가지 마세요!")
# elif dust > 80:
#     print("나쁨")
# elif dust>30:
#     print("보통")
# else:
#     print("좋음")




# new_list_3 = [i if i%2==1 for i in range(10)]

# print(new_list_3)


# print(list(range(3)))


# k=[]
# for i in range(10):
#     if i% 2 ==1:
#         k.append(i)
#     else: 
#         k.append(str(i))

# print(k)

# numbers = [1, 2, 3, 4, 5]
# ss = []
# for num in numbers: ss.append(num**2)
# print(ss)

# numbers = [1, 2, 3, 4, 5]
# ss = [num**2 for num in numbers]
# print(ss)

# ss = list(i if i%2 ==1 else str(i) for i in range(10))
# print(ss)


# [i for i in range(10) if i%2 ==1 ]

# print([i if i%2 ==1 else str(i) for i in range(10) ])

# numbers = [1, 2, 3, 4, 5]
# k=[]
# for i in numbers:
#     k.append(i**2)
# print(k)



numbers = [1,2,3,4,5]
k=[]
for i in numbers:
    k.append(i**2)
print(k)

numbers = [1,2,3,4,5]
print([i**2 for i in numbers ])

# numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# for i in range(len(numbers)):
#     for j in range(len(numbers)):
#         print(numbers[i][j], end=' ')


# numbers = [1, 2, 3, 4, 5]
# ss = [num**2 for num in numbers]


dust = [1,2]
result = 0
while result < 5 :
      result +=1
      for i in range(2):
           print(dust[i],"a")
    

      print(result,"b")
    