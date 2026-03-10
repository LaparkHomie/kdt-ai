lst = []

inputdct = ("제품코드", "제품명", "수량", "단가", "판매금액")

while True:
	dct = []
	for i in range(0, 4):
		szText = input(inputdct[i] + " 입력 => ")
		if szText == "exit":
			break
		dct.append(szText)
	else:
		dct[2:4] = map(int, dct[2:4])
		dct.append(dct[2] * dct[3])
		lst.append(dct)
		print()
		continue
	break

print("\t" * 3 + "*** 제품관리 ***")
print("=" * 40)
print("    ".join(inputdct))
print("=" * 40)
total = 0
for dct in lst:
	print("%4s       %4s   %4d    %4d    %6d" % tuple(dct))
	total += dct[4]
print("=" * 40)
print("\t" * 3 + "총 판매금액 = %7d" % total)
