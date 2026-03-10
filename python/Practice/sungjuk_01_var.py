# szText = ("학번", "이름", "국어", "영어", "수학", "총점", "평균")
# sum = 0
# ptrloop = 55
#
# id = input(szText[0] + "입력 => ")
# name = input(szText[1] + "입력 => ")
# kor = int(input(szText[2] + "입력 => "))
# eng = int(input(szText[3] + "입력 => "))
# mat = int(input(szText[4] + "입력 => "))
# tot = kor + eng + mat
# avg = tot / 3
#
# print(" " * 20 + "*** 성적표 ***")
# print("=" * ptrloop)
# for i in range(0, 7):
# 	print(("%s" + " " * 5) % szText[i], end='')
# print("")
# print("=" * ptrloop)
# print("%-8s" * 2 % (id, name), end='')
# print("%-8d" * 4 % (kor, eng, mat, tot), end='')
# print("%-8.2f" % avg)
# print("=" * ptrloop)


# szText = ("학번", "이름", "국어", "영어", "수학", "총점", "평균")
# lst = []
# sum = 0
# ptrloop = 55
#
# for i in range(0, 5):
# 	lst.append(input(szText[i] + " 입력 => "))
# 	if i >= 2:
# 		lst[i] = int(lst[i])
# 		sum += lst[i]
#
# lst.append(sum)
# lst.append(sum / 3)
#
# print(" " * 20 + "*** 성적표 ***")
# print("=" * ptrloop)
# for i in range(0, 7):
# 	print(("%s" + " " * 5) % szText[i], end='')
# print("")
# print("=" * ptrloop)
# print("%-8s" * 2 % tuple(lst[:2]), end='')
# print("%-8d" * 4 % tuple(lst[2:6]), end='')
# print("%-8.2f" % lst[6])
# print("=" * ptrloop)



szText = ("학번", "이름", "국어", "영어", "수학", "총점", "평균")
rankgrade = dict(zip(tuple("수우미양가"), (90, 80, 70, 60, 0)))
dct = {}
ptr = {}
sum = 0
ptrloop = 55

for i in range(0, 5):
	input_data = input(szText[i] + " 입력 => ")
	if i < 2:
		dct[szText[i]], ptr[szText[i]] = input_data, "%-8s"
	else:
		dct[szText[i]], ptr[szText[i]] = int(input_data), "%-8d"
		sum += dct[szText[i]]

dct[szText[5]], ptr[szText[5]] = sum, "%-8d"
dct[szText[6]], ptr[szText[6]] = sum / 3, "%-8.2f"


print(" " * 20 + "*** 성적표 ***")
print("=" * ptrloop)
print(("%s" + " " * 5) * 7 % tuple(dct.keys()))
print("=" * ptrloop)
print("".join(ptr.values()) % tuple(dct.values()))
print("=" * ptrloop)
for grade, score in rankgrade.items():
	if dct["평균"] >= score:
		print("등급: " + grade)
		break
print("=" * ptrloop)
