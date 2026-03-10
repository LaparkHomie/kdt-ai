import csv
import os

DATA_PATH = "sungjuk_data.csv"
sz_title = "입력", "출력", "조회", "수정", "삭제", "종료"
keys = "학번", "이름", "국어", "영어", "수학", "총점", "평균", "등급"
rank_grade = dict(zip(tuple("수우미양가"), (90, 80, 70, 60, 0)))
sz_ptr = "%-8s", "%-8s", "%-8d", "%-8d", "%-8d", "%-8d", "%-8.2f", "%-8s"
loop_ptr = 61

def menu_title():
	print("*** 성적관리 ***")
	for i in range(len(sz_title) - 1):
		print("%d. 성적정보 %s" % (i + 1, sz_title[i]))
	print("%d. 프로그램 %s" % (6, sz_title[5]))
	print()

def input_sungjuk():
	first_file = True
	if os.path.exists(DATA_PATH):
		first_file = False

	dct = {}
	dct = dict(zip(keys[5], tuple(map(input, map(lambda x: x + " 입력 => ", keys[5])))))
	for i in range(0, 5):
		dct[keys[i]] = input(keys[i] + " 입력 => ")

	dct.update(dict(zip(keys[2:5], map(int, map(dct.get, keys[2:5]))))) # 국영수
	dct["총점"] = sum(map(dct.get, keys[2:5]))                           # 총점
	dct["평균"] = dct["총점"] / 3                                         # 평균
	for grade, score in rank_grade.items():
		if dct["평균"] >= score:
			dct["등급"] = grade       # 등급
			break

	fp = open(DATA_PATH, "a", encoding="utf-8", newline='')
	wr = csv.DictWriter(fp, fieldnames=keys)

	if first_file:
		wr.writeheader()
	wr.writerow(dct)

	fp.close()

def print_sungjuk():
	if os.path.exists(DATA_PATH):
		fp = open(DATA_PATH, "r", encoding="utf-8", newline='')
		lines = list(csv.DictReader(fp))
		fp.close()

		count = len(lines)
		total = 0

		print(" " * 20 + "*** 성적표 ***")
		print("=" * loop_ptr)
		print(*keys, sep="     ")
		print("=" * loop_ptr)
		for dct in lines:
			dct.update(dict(zip(keys[2:6], map(int, map(dct.get, keys[2:6])))))
			dct["평균"] = float(dct["평균"])
			print("".join(sz_ptr) % tuple(dct.values()))
			total += dct["평균"]
		print("=" * loop_ptr)
		print("학생수: %d, 전체 평균: %.2f" % (count, total / count))
	print()

def search_sungjuk():
	if os.path.exists(DATA_PATH):
		code = input("조회할 학번을 입력 => ")

		fp = open(DATA_PATH, "r", encoding="utf-8", newline='')
		lines = list(csv.DictReader(fp))
		fp.close()

		print(" " * 20 + "*** 성적표 ***")
		print("=" * loop_ptr)
		print(*keys, sep="     ")
		print("=" * loop_ptr)
		for dct in lines:
			if dct["학번"] == code:
				dct.update(dict(zip(keys[2:6], map(int, map(dct.get, keys[2:6])))))
				dct["평균"] = float(dct["평균"])
				print("".join(sz_ptr) % tuple(dct.values()))
				break
		print("=" * loop_ptr)
	print()

def update_sungjuk():
	if os.path.exists(DATA_PATH):
		code = input("수정할 학번을 입력 => ")

		fp = open(DATA_PATH, "r", encoding="utf-8", newline='')
		lines = list(csv.DictReader(fp))
		fp.close()

		for dct in lines:
			if dct["학번"] == code:
				for i in range(2, 5):
					dct[keys[i]] = int(input(keys[i] + " 입력 => "))

				dct["총점"] = sum(map(dct.get, keys[2:5])) # 총점
				dct["평균"] = dct["총점"] / 3               # 평균
				for grade, score in rank_grade.items():
					if dct["평균"] >= score:
						dct["등급"] = grade
						break

				fp = open(DATA_PATH, "w", encoding="utf-8", newline='')
				wr = csv.DictWriter(fp, fieldnames=keys)
				wr.writeheader()
				wr.writerows(lines)
				fp.close()
				break
		else:
			print("수정할 학번이 없음")
	print()

def delete_sungjuk():
	if os.path.exists(DATA_PATH):
		code = input("삭제할 학번을 입력 => ")

		fp = open(DATA_PATH, "r", encoding="utf-8", newline='')
		lines = list(csv.DictReader(fp))
		fp.close()

		for dct in lines:
			if dct["학번"] == code:
				lines.remove(dct)

				fp = open(DATA_PATH, "w", encoding="utf-8", newline='')
				wr = csv.DictWriter(fp, fieldnames=keys)
				wr.writeheader()
				wr.writerows(lines)
				fp.close()
				break
		else:
			print("삭제할 학번이 없음")
	print()

if __name__ == "__main__":
	while True:
		menu_title()
		menu = int(input("메뉴를 선택하세요(1~6) => "))
		if menu == 1:
			input_sungjuk()
		elif menu == 2:
			print_sungjuk()
		elif menu == 3:
			search_sungjuk()
		elif menu == 4:
			update_sungjuk()
		elif menu == 5:
			delete_sungjuk()
		elif menu == 6:
			print("\n프로그램 종료!!\n")
			break
		else:
			print("\n메뉴를 다시 입력하세요!!\n")
