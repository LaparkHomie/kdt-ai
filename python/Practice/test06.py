# class Person:
# 	def greeting(self):
# 		print('안녕하세요.')
#
# class Student(Person):
# 	def study(self):
# 		print('공부하기')
#
# james = Student()
# james.greeting()
# james.study()
import abc
# class Person:
# 	def greeting(self):
# 		print('안녕하세요.')
#
# class PersonList:
# 	def __init__(self):
# 		self.person_list = []
#
# 	def append_person(self, person):
# 		self.person_list.append(person)
#
# if __name__ == '__main__':
# 	person = Person()
# 	person.greeting()
# 	pl = PersonList()
# 	pl.append_person(person)
# 	print(pl.person_list)
# 	pl.person_list[0].greeting()

# class Person:
# 	def __init__(self):
# 		print('Person __init__')
# 		self.hello = '안녕하세요.'
#
# class Student(Person):
# 	def __init__(self):
# 		super().__init__()
# 		print('Student __init__')
# 		self.school = '파이썬 코딩 도장'
#
# james = Student()
# print(james.school)
# print(james.hello) # 기반 클래스의 속성을 출력하려고 하면 에러가 발생함

# class Person:
# 	def __init__(self):
# 		print('Person __init__')
# 		self.hello = '안녕하세요.'
#
# class Student(Person):
# 	pass
#
# james = Student()
# print(james.hello)

# class Person:
# 	def greeting(self):
# 		print('안녕하세요.')
#
# class Student(Person):
# 	def greeting(self):
# 		print('안녕하세요. 저는 파이썬 코딩 도장 학생입니다.')
#
# # james = Student()
# # james.greeting()
#
# lst = []
# person1 = Student()
# person2 = Person()
#
# lst.append(person1)
# lst.append(person2)
#
# for d in lst:
# 	d.greeting()

# class Person:
# 	def __init__(self):
# 		print("Person Class")
# 	def greeting(self):
# 		print('안녕하세요.1')
#
# class University:
# 	def __init__(self):
# 		print("Univerisity Class")
# 	def manager_credit(self):
# 		print('학점 관리')
# 	def greeting(self):
# 		print('안녕하세요2')
#
# class Undergraduate(Person, University):
# 	def study(self):
# 		print('공부하기')
#
# james = Undergraduate()
# james.greeting()
# james.manager_credit()
# james.study()

# class A:
# 	def greeting(self):
# 		print('안녕하세요. A입니다.')
#
# class B(A):
# 	def greeting(self):
# 		print('안녕하세요. B입니다.')
#
# class C(A):
# 	def greeting(self):
# 		print('안녕하세요. C입니다.')
#
# class D(B, C):
# 	pass
#
# myclass = D()
# myclass.greeting()

# from abc import *
# class StudentBase(metaclass=ABCMeta):
# 	@abc.abstractmethod
# 	def study(self):
# 		pass
#
# 	@abc.abstractmethod
# 	def go_to_school(self):
# 		pass
#
# class Student(StudentBase):
# 	def study(self):
# 		print('공부하기')
#
# 	def go_to_school(self):
# 		print('학교가기')
#
# class Children(Student):
# 	def study(self):
# 		print('재미나게 놀기')
#
# 	def go_to_school(self):
# 		print('유치원가기')
#
# 	def sleep(self):
# 		print("낮잠 자기")
#
# james = Student()
# james.study()
# james.go_to_school()
# print("-" * 20)
# jack = Children()
# jack.study()
# jack.go_to_school()
# jack.sleep()
#
# print("-" * 20)
#
# lst = []
# lst.append(jack)
# lst.append(james)
#
# for data in lst:
# 	data.study()
# 	data.go_to_school()
# 	print('#' * 20)

# def ten_div(x):
# 	return 10 / x
#
# try:
# 	x = int(input('나눌 숫자를 입력하세요: '))
# 	y = 10 / x
# 	print(y)
# except ZeroDivisionError as e:
# 	print('예외가 발생했습니다.', e)
# except Exception as e:
# 	print('예외가 발생했습니다.', e)

# y = [10, 20, 30]
#
# try:
# 	index, x  = map(int, input('인덱스와 나눌 숫자를 입력하세요: ').split())
# 	print(y[index] / x)
# except ZeroDivisionError:
# 	print('숫자를 0으로 나눌 수 없습니다.')
# except IndexError:
# 	print('잘못된 인덱스입니다.')
# except:
# 	print("나머지 예외 처리")

# y = [10, 20, 30]
#
# try:
# 	index, x  = map(int, input('인덱스와 나눌 숫자를 입력하세요: ').split())
# 	print(y[index] / x)
# except ZeroDivisionError as e:
# 	print('숫자를 0으로 나눌 수 없습니다.', e)
# except IndexError as e:
# 	print('잘못된 인덱스입니다.', e)
# except Exception as e:
# 	print("Exception 예외입니다.", e.args[0])

# try:
# 	x = int(input('나눌 숫자를 입력하세요: '))
# 	y = 10 / x
# except ZeroDivisionError:
# 	print('숫자를 0으로 나눌 수 없습니다.')
# except:
# 	print("모든 예외 처리")
# else:
# 	print(y)
# finally:
# 	print('코드 실행이 끝났습니다.')

# try:
# 	x = int(input('3의 배수를 입력하세요: '))
# 	if x % 3 != 0:
# 		raise Exception('3의 배수가 아닙니다.')
# 	print(x)
# except Exception as e:
# 	print('예외가 발생했습니다.', e)


# def three_multiple():
# 	try:
# 		x = int(input('3의 배수를 입력하세요: '))
# 		if x % 3 != 0:
# 			raise Exception('3의 배수가 아닙니다.')
# 		print(x)
# 	except Exception as e:
# 		print('three_multiple 함수에서 예외가 발생했습니다.', e)
# 		raise
#
# try:
# 	three_multiple()
# except Exception as e:
# 	print('예외가 발생했습니다', e)

# class NotThreeMultipleError(Exception):
# 	def __init__(self):
# 		super().__init__('3의 배수가 아닙니다.')
#
# def three_multiple():
# 	try:
# 		x = int(input('3의 배수를 입력하세요: '))
# 		if x % 3 != 0:
# 			raise NotThreeMultipleError
# 		print(x)
# 	except Exception as e:
# 		print('예외가 발생했습니다.', e)
#
# three_multiple()

class AgeException(Exception):
	def __init__(self, msg1, msg2):
		self._message1 = msg1
		self._message2 = msg2

def input_age():
	age = int(input("나이를 입력해 주세요: "))

	if age < 0:
		raise AgeException("나이는 음수가 될수 없습니다.", "")
	elif age > 150:
		raise AgeException("150세이상 살수 있을까요?", "흠")
	else:
		return age

if __name__ == '__main__':
	try:
		age = input_age()
	except AgeException as e:
		print(e.args)
	else:
		print("나이는 %d세입니다." % age)
