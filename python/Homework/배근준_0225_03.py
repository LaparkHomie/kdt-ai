num1 = int(input("첫번째 숫자를 입력하시오 => "))
num2 = int(input("두번째 숫자를 입력하시오 => "))

if num1 > num2:
	num1, num2 = num2, num1

for j in range(num1, num2 + 1):
	print(" ** %d단 **   " % j, end = "")
print("")
for i in range(1, 10):
	for j in range(num1, num2 + 1):
		print("%d * %d = %2d   " % (j, i, i * j), end = "")
	print("")
