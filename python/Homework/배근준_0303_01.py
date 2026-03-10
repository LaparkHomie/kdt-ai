prime = []
start_idx = 0
end_idx = 0

def input_num():
	return int(input("첫번째 숫자를 입력하세요 => ")), int(input("두번째 숫자를 입력하세요 => "))

def min_max_num(num1, num2):
	return min(num1, num2), max(num1, num2)

def proc_print_prime(num1, num2):
	global start_idx
	global end_idx

	if num2 > 1:
		prime.append(2)
	elif num1 < 2:
		num1 = 2

	for i in range(3, int((num2 - 1) ** 0.5 + 1), 2):
		for j in prime:
			if i % j == 0 or j * j > i:
				break
		if i % j or j * j > i:
			prime.append(i)

	for i in range(max(i + 1, num1) // 2 * 2 + 1, num2 + 1, 2):
		for j in prime:
			if i % j == 0 or j * j > i:
				break
		if i % j or j * j > i:
			prime.append(i)

	end_idx = len(prime)

	while True:
		if start_idx >= end_idx or prime[start_idx] >= num1:
			break
		start_idx += 1

	for i in range(start_idx, end_idx):
		print("%5d" % prime[i], end=" ")
		if (i - start_idx + 1) % 10 == 0:
			print()

	if end_idx and (i - start_idx + 1) % 10:
		print()



def print_total_prime():
	print("총소수의 갯수 = %d" % (end_idx - start_idx))

if __name__ == "__main__":
	num1, num2 = input_num()
	num1, num2 = min_max_num(num1, num2)
	proc_print_prime(num1, num2)
	print_total_prime()
