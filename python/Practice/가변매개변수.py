def add(a, *b):
	hap = a
	for val in b:
		hap += val
	return hap

print(add(10, 20, 30)) # 함수 호출문
print(add(10, 20, 30, 40)) # 함수 호출문
