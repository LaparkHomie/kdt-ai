def input_num():
	return int(input("첫번째 숫자를 입력하시오 => ")), int(input("첫번째 숫자를 입력하시오 => "))

def min_max_num(num1, num2):
	return min(num1, num2), max(num1, num2)

def proc_gugudan(num1, num2):
	for j in range(num1, num2 + 1):
		print(" ** %d단 **   " % j, end = "")
	print()
	for i in range(1, 10):
		for j in range(num1, num2 + 1):
			print("%d * %d = %2d   " % (j, i, i * j), end = "")
		print()

if __name__ == "__main__":
	num1, num2 = input_num()
	num1, num2 = min_max_num(num1, num2)
	proc_gugudan(num1, num2)
