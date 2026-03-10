szText = ["학번", "이름", "국어", "영어", "수학"]
szPtr = "%s", "%5s", "%4d", "%8d", "%8d", "%7d", "%8.2f"

lst_rec = []
total = 0
loopptr = 29

while True:
	lst = []

	for binput in szText:
		szStr = input(binput + " 입력 => ")
		if szStr == "exit":
			break
		lst.append(szStr)
	else:
		lst[2:5] = map(int, lst[2:5])           #2~4: 국영수
		lst.append(lst[2] + lst[3] + lst[4])    # 5: 총점
		lst.append(lst[5] / 3)                  # 6: 평균
		total += lst[6]

		lst_rec.append(lst)
		print()
		continue
	break

szText.append("총점")
szText.append("평균")

print(" " * 17 + "*** 성적표 ***")
print("=" * loopptr)
print("   ".join(szText))
print("=" * loopptr)
for lst in lst_rec:
	print("".join(szPtr) % tuple(lst))
print("=" * loopptr)
print(" " * 6 + "학생수 : %d" % len(lst_rec) + " " * 6 + "전체 평균 : %.2f" % (total / len(lst_rec)))
