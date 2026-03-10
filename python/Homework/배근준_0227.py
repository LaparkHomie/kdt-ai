prime = []

num1 = int(input("첫번째 숫자를 입력하세요 => "))
num2 = int(input("두번째 숫자를 입력하세요 => "))

if num1 > num2:
	num1, num2 = num2, num1

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

i = max(i + 1, num1)
if i % 2 == 0:
	i += 1

for i in range(i, num2 + 1, 2):
	for j in prime:
		if i % j == 0 or j * j > i:
			break
	if i % j or j * j > i:
		prime.append(i)

idx = 0
while True:
	if idx >= len(prime) or prime[idx] >= num1:
		break
	idx += 1

for i in range(idx, len(prime)):
	print("%5d" % prime[i], end=" ")
	if (i - idx + 1) % 10 == 0:
		print()

if len(prime) and (i - idx + 1) % 10:
	print()
print("총소수의 갯수 = %d" % (len(prime) - idx))
