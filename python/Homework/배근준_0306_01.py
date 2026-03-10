from 배근준_0306_02 import Sungjuk
import sys
import os

sz_title = "입력", "출력", "조회", "수정", "삭제", "종료"

lst = []

def menu_title():
	print("*** 성적관리 ***")
	for i in range(len(sz_title) - 1):
		print("%d. 성적정보 %s" % (i + 1, sz_title[i]))
	i = len(sz_title) - 1
	print("%d. 프로그램 %s" % (i + 1, sz_title[i]))
	print()

def input_sungjuk():
	obj = Sungjuk()
	while True:
		try:
			obj.input_sungjuk(slice(0, 5)) # 중복 데이터 들어오는지 확인
		except Exception as e:
			print()
		else:
			break

	obj.proess_sungjuk()
	lst.append(obj)

	print("\n성적 입력 성공!!!\n")

def print_sungjuk():
	if len(lst) == 0:
		print("\n출력할 데이터가 없음!!!\n")
		return

	Sungjuk.output_title()
	tot_avg = 0
	for obj in lst:
		obj.output_sungjuk()
		tot_avg += obj.avg
	Sungjuk.output_line()
	print("학생수: %d, 전체 평균: %.2f" % (len(lst), tot_avg / len(lst)))

def search_sungjuk():
	while True:
		try:
			sid = Sungjuk.input_sid("조회")
		except Exception as e:
			print()
		else:
			break

	for obj in lst:
		if obj.sid == sid:
			Sungjuk.output_title()
			obj.output_sungjuk()
			Sungjuk.output_line()

			break
	else:
		print("\n조회할 데이터가 없음!!!\n")

def update_sungjuk():
	while True:
		try:
			sid = Sungjuk.input_sid("수정")
		except Exception as e:
			print()
		else:
			break

	for obj in lst:
		if obj.sid == sid:
			while True:
				try:
					obj.input_sungjuk(slice(2, 5))
				except Exception as e:
					print()
				else:
					obj.proess_sungjuk()

					print("\n성적 수정 성공!!!\n")
					break
			break
	else:
		print("\n수정할 데이터가 없음!!!\n")

def delete_sungjuk():
	while True:
		try:
			sid = Sungjuk.input_sid("삭제")
		except Exception as e:
			print()
		else:
			break

	for obj in lst:
		if obj.sid == sid:
			lst.remove(obj)

			print("\n성적 삭제 성공!!!\n")

			break
	else:
		print("\n삭제할 데이터가 없음!!!\n")

if __name__ == "__main__":
	while True:
		menu_title()
		try:
			menu = int(input("메뉴를 선택하세요 (1~6) => "))
		except Exception as e:
			print("입력 오류!!!(숫자를 입력하세요)")
			continue
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
