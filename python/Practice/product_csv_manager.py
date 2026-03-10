import csv
import os

keys = "code", "name", "count", "price", "value"
szInput = "제품코드", "제품명", "수량", "단가", "판매금액"
szPtr = "%4s", "  %4s", "%4d", " %4d", "%6d"
title = "입력", "출력", "조회", "수정", "삭제", "종료"

def menu_title():
	print("*** 제품관리 ***")
	for i in range(len(title)):
		print("%d. 제품정보 %s" % (i + 1, title[i]))
	print()

def input_data():
	file_first = True
	if os.path.exists("product_data.csv"):
		file_first = False
	fp = open("product_data.csv", "at", encoding="utf-8", newline='')
	wr = csv.DictWriter(fp, fieldnames=keys)

	rec = []
	for i in range(0, 4):
		rec.append(input(szInput[i] + " 입력 => "))
	rec[2:4] = map(int, rec[2:4])
	rec.append(rec[2] * rec[3])
	dct = dict(zip(keys, rec))

	if file_first:
		wr.writeheader()
	wr.writerow(dct)

	fp.close()

def print_data():
	if os.path.exists("product_data.csv"):
		fp = open("product_data.csv", "r", encoding="utf-8", newline='')
		lines = csv.DictReader(fp)

		lst = []
		for dct in lines:
			dct["count"] = int(dct["count"])
			dct["price"] = int(dct["price"])
			dct["value"] = int(dct["value"])
			lst.append(dct)
		print("\t" * 3 + "*** 제품관리 ***")
		print("=" * 40)
		print("    ".join(szInput))
		print("=" * 40)
		total = 0
		for dct in lst:
			print("   ".join(szPtr) % tuple(dct.values()))
			total += dct["value"]
		print("=" * 40)
		print("\t" * 3 + "총 판매금액 = %7d" % total)

def search_data():
	# 제품코드를 입력받아 해당 제품 정보를 출력한다.
	if os.path.exists("product_data.csv"):
		product_code = input("조회할 제품코드를 입력 => ")

		fp = open("product_data.csv", "r", encoding="utf-8", newline='')
		lines = csv.DictReader(fp)
		# lst = list(csv.DictReader(fp))

		for dct in lines:
			if dct["code"] == product_code:
				dct["count"] = int(dct["count"])
				dct["price"] = int(dct["price"])
				dct["value"] = int(dct["value"])

				print("\t" * 3 + "*** 제품관리 ***")
				print("=" * 40)
				print("    ".join(szInput))
				print("=" * 40)
				print("   ".join(szPtr) % tuple(dct.values()))
				print("=" * 40)
				break
		else:
			print("조회할 제품 코드가 없음")

def update_data():
	# 제품코드를 입력받아 일치하는 데이터를 찾아서 수량과 단가를 입력받아 금액을 수정 후 파일 전체를 재저장
	if os.path.exists("product_data.csv"):
		product_code = input("수정할 제품코드를 입력 => ")
		fp = open("product_data.csv", "r", encoding="utf-8", newline='')
		lst = list(csv.DictReader(fp))
		fp.close()

		for dct in lst:
			if dct["code"] == product_code:
				for i in range(2, 4):
					dct[keys[i]] = int(input(szInput[i] + " 입력 -> "))
				dct["value"] = dct["count"] * dct["price"]
				break
		else:
			print("수정할 제품 정보가 없음")
			return
		fp = open("product_data.csv", "w", encoding="utf-8", newline='')
		wr = csv.DictWriter(fp, fieldnames=keys)
		wr.writeheader()
		wr.writerows(lst)
		fp.close()

def delete_data():
	if os.path.exists("product_data.csv"):
		product_code = input("삭제할 제품코드를 입력 => ")
		fp = open("product_data.csv", "r", encoding="utf-8", newline='')
		lst = list(csv.DictReader(fp))
		fp.close()

		for dct in lst:
			if dct["code"] == product_code:
				lst.remove(dct)
				break
		else:
			print("삭제할 제품 정보가 없음")
			return
		fp = open("product_data.csv", "w", encoding="utf-8", newline='')
		wr = csv.DictWriter(fp, fieldnames=keys)
		wr.writeheader()
		wr.writerows(lst)
		fp.close()

if __name__ == "__main__":
	while True:
		menu_title()
		menu = int(input("메뉴를 선택하세요(1~6) => "))
		if menu == 1:
			input_data()
		elif menu == 2:
			print_data()
		elif menu == 3:
			search_data()
		elif menu == 4:
			update_data()
		elif menu == 5:
			delete_data()
		elif menu == 6:
			print("\n프로그램 종료!!\n")
			break
		else:
			print("\n메뉴를 다시 입력하세요!!\n")

		print()
