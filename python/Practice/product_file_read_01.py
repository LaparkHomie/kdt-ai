import os

keys = ("code", "name", "count", "price", "value")

if os.path.exists('product_data.txt'):
	fp = open("product_data.txt", "r", encoding="utf-8")
	lst = []
	for line in fp:
		rec = line.strip("\n").split(",")
		dct = dict(zip(keys, rec))
		dct["count"] = int(dct["count"])
		dct["price"] = int(dct["price"])
		dct["value"] = int(dct["value"])
		lst.append(dct)

	fp.close()

	inputdct = ("제품코드", "제품명", "수량", "단가", "판매금액")
	total = 0
	print("\t" * 3 + "*** 제품관리 ***")
	print("=" * 40)
	print("    ".join(inputdct))
	print("=" * 40)
	for dct in lst:
		print("%4s       %4s   %4d    %4d    %6d" % tuple(dct.values()))
		total += dct["value"]
	print("=" * 40)
	print("\t" * 3 + "총 판매금액 = %7d" % total)

else:
	print("파일이 존재하지 않습니다")
