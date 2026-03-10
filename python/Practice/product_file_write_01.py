lst = []
total = 0

keys = ("code", "name", "count", "price", "value")
inputdct = ("제품코드", "제품명", "수량", "단가", "판매금액")

fp = open("product_data.txt", "w", encoding="utf-8")
while True:
	rec = []
	for i in range(0, 4):
		szText = input(inputdct[i] + " 입력 => ")
		if szText == "exit":
			break
		rec.append(szText)
	else:
		dct = dict(zip(keys, rec))
		dct["count"] = int(dct["count"])
		dct["price"] = int(dct["price"])
		dct["value"] = dct["count"] * dct["price"]
		lst.append(dct)

		fp.write(",".join(map(str, dct.values())) + "\n")

		print()
		continue
	break

fp.close()
print("\t" * 3 + "*** 제품관리 ***")
print("=" * 40)
print("    ".join(inputdct))
print("=" * 40)
total = 0
for dct in lst:
	print("%4s       %4s   %4d    %4d    %6d" % tuple(dct.values()))
	total += dct["value"]
print("=" * 40)
print("\t" * 3 + "총 판매금액 = %7d" % total)
