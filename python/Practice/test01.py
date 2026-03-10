# a = [1, 2, 3, 4]
# a.append(5)
# print(a)
# a.append([6, 7])
# print(a)
#
# b = [4, 1, 3, 2]
# print(b)
# b.sort()
# print(b)
# b.reverse()
# print(b)

# a = [1, 2, 3]
# a.insert(1, 4)
# print(a)
# a.remove(1)
# print(a)
# print(a.pop())
# print(a)
# a = [1, 2, 2, 2, 3, 3, 4]
# print(a.count(2))
# a.extend([5, 6, 7])
# print(a)

# a = [10, 10.5, 'Python']
# print(a)
# print(a[0])
# print(a[-1])
# print(a[-2])
# print(a[2][0])
# a[2] = 'java'
# print(a)
# a[2][0] = 'J'
# print(a)

# a = [1, 2, 3, 4, 5]
# print(a)
# b = a[:2]
# c = a[2:]
# print(c)
# d = a[-1:]
# print(d)
# e = a[-3:]
# print(e)

# t1 = ()
# print(type(t1))
# t2 = (10,)
# print(type(t2))
# print(t2)
# t3 = (1, 2, 3)
# print(t3)
# t4 = 1, 2, 3
# print(t4)
# x, y, z = t4
# print(x, y, z)
# t5 = (1, 10.5, 'Python')
# print(t5)
# print(t5[2])
# print(t5[2][0:2])
# t5[2] = 'Java'

# a = (1, 2, 3, [4, 5])
# a[3][0] = 10
# a[3] = 100

# dct = {}
# dct['id'] = 'hong'
# dct['pw'] = '1234'
# print(dct)
# dct['email'] = 'hong@gmail.com'
# print(dct)
# dct['id'] = 'lee'
# print(dct)
# del dct['email']
# print(dct)

# dct = {}
# dct['id'] = 'hong'
# dct['pw'] = '1234'
# dct['email'] = 'hong@gmail.com'
#
# print(dct)
# print(dct.keys())
# print(dct.values())
# print(dct.items())
# res = dct.get('id') # dct['id']
# print(res)

# grade = float(input("총 평점을 입력해 주세요: "))
#
# if grade >= 4.3:
# 	print("당신은 장학금 수여 대상자 입니다.")
# 	print("축하합니다.")
#
# print("공부 열심히 하세요.")

# data = int(input("숫자를 입력하시오: "))
#
# if data % 2 == 0:
# 	print("입력된 값은 짝수입니다.")
# 	if (data % 4) == 0:
# 		print("입력된 값은 4의 배수입니다.")
# 	else:
# 		print("입력된 값은 4의 배수가 아닙니다.")
# else:
# 		print("입력된 값은 홀수입니다.")
# 		if (data % 3) == 0:
# 			print("입력된 값은 3의 배수입니다.")
# 		else:
# 				print("입력된 값은 3의 배수가 아닙니다.")
#
# print("The End..")

# score = int(input("총점을 입력해 주세요: "))
#
# if score >= 90:
# 	print("수")
# elif 80 <= score < 90:
# 	print("우")
# elif 70 <= score < 80:
# 	print("미")
# elif 60 <= score < 70:
# 	print("양")
# else:
# 	print("가")
#
# print("The End..")

# even, odd = 0, 0
# for item in range(1, 101):
# 	if item % 2 == 0:
# 		even += item
# 	else:
# 		odd += item
#
# print("1부터 100까지 짝수의 합은", even, "입니다")
# print("1부터 100까지 홀수의 합은", odd, "입니다")

# message = "Hello!"
# messages = ["Hello World", "강릉원주대학교 정보기술공학과"]
# numbers = (1, 2, 3)
# polygon = {"triangle":2, "rectangle":1, "line":0}
# color = {"red", "green", "blue"} # set
#
# for item in message:
# 	print(item)
# print("1.---------------")
# for item in messages:
# 	print(item)
# print("2.---------------")
# for item in numbers:
# 	print(item)
# print("3.---------------")
# for item in polygon:
# 	print(item)
# print("4.---------------")
# for item in color:
# 	print(item)
# print("5.---------------")

# total = 0
# for item in range(1, 101, 1):
# 	total = total + item
# else:
# 	print("1부터 10까지 합은", total, "입니다.")

# a = [1, 2, 3, 4]
# result = [num * 3 for num in a if num % 2 == 0]
# print(result)

#import random
# from random import randint
#
# i = 0
# while i != 3:
# 	i = randint(1, 6)
# 	print(i)

def hap(a, b):
	return a + b

if __name__ == "__main__":
	x = 10
	y = 20
	print(hap(x, y))
