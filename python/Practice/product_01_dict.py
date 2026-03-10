lst = []

inputdct = dict(zip(("code", "name", "count", "price"), ("제품코드", "제품명", "수량", "단가")))

while True:
	dct = {}
	for K, V in inputdct.items():
		dct[K] = input(V + " 입력 => ")
		if dct[K] == "exit":
			break
	else:
		dct["count"] = int(dct["count"])
		dct["price"] = int(dct["price"])
		dct["value"] = dct["count"] * dct["price"]
		lst.append(dct)
		print()
		continue
	break

inputdct["total"] = "판매금액"

print("\t" * 3 + "*** 제품관리 ***")
print("=" * 40)
print("    ".join(inputdct.values()))
print("=" * 40)
total = 0
for dct in lst:
	print("%4s       %4s   %4d    %4d    %6d" % tuple(dct.values()))
	total += dct["value"]
print("=" * 40)
print("\t" * 3 + "총 판매금액 = %7d" % total)
