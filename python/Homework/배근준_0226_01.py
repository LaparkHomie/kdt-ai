szText = ["학번", "이름", "국어", "영어", "수학"]
szPtr = "%s", "%5s", "%4d", "%8d", "%8d", "%7d", "%8.2f"

lst_rec = []
total = 0
loopptr = 29

while True:
	dct = {}

	for binput in szText:
		szStr = input(binput + " 입력 => ")
		if szStr == "exit":
			break
		dct[binput] = szStr
	else:
		dct[szText[2]] = int(dct[szText[2]])
		dct[szText[3]] = int(dct[szText[3]])
		dct[szText[4]] = int(dct[szText[4]])
		dct["총점"] = dct[szText[2]] + dct[szText[3]] + dct[szText[4]]
		dct["평균"] = dct["총점"] / 3
		total += dct["평균"]

		lst_rec.append(dct)
		print()
		continue
	break

szText.append("총점")
szText.append("평균")

print(" " * 17 + "*** 성적표 ***")
print("=" * loopptr)
print("   ".join(szText))
print("=" * loopptr)
for dct in lst_rec:
	print("".join(szPtr) % tuple(dct.values()))
print("=" * loopptr)
print(" " * 6 + "학생수 : %d" % len(lst_rec) + " " * 6 + "전체 평균 : %.2f" % (total / len(lst_rec)))
