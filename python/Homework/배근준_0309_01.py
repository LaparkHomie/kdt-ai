from 배근준_0309_02 import Sangpum

sz_title = "입력", "출력", "조회", "수정", "삭제", "종료"
keys = "상품코드", "상품명", "수량", "단가", "판매금액"
ment = 1, 0, 0, 0
types = str, str, int, int, int

lst = []
menu = 0

def get_code_index(szCode):
	for i, val in enumerate(lst):
		if szCode == val.get("상품코드"):
			return i
	return -1

def menu_title():
	print("*** 상품관리 ***")
	for i in range(len(sz_title) - 1):
		print("%d. 상품정보 %s" % (i + 1, sz_title[i]))
	i = len(sz_title) - 1
	print("%d. 프로그램 %s" % (i + 1, sz_title[i]))
	print()

def input_sangpum():
	obj = Sangpum()
	for i in range(4):
		while True:
			try:
				szText = input(keys[i] + " 입력 => ")
				if szText.lower() == "exit":
					print("입력을 취소합니다.\n")
					return

				if i == 0 and get_code_index(szText) >= 0:
					raise Exception("동일한 상품코드가 존재합니다.")

				obj.set(keys[i], Sangpum.OnValidate(szText, types[i]))
			except Exception as e:
				print("입력 오류!!!", e, "\n")
			else:
				break

	obj.DoProcess()
	lst.append(obj)

	print("\n상품 입력 성공!!!\n")

def print_sangpum():
	if len(lst) == 0:
		print("\n출력할 데이터가 없음!!!\n")
		return

	total = 0
	Sangpum.OutputTitle()
	for dct in lst:
		dct.OutputInfo()
		total += dct.get("판매금액")
	Sangpum.OutputLine()
	print("\t" * 3 + "총 판매금액 = %7d" % total)
	print()

def search_sangpum():
	i = 0

	while True:
		try:
			szText = input((sz_title[menu - 1] + "할 ") * ment[i] + keys[i] + " 입력 => ")
			if szText.lower() == "exit":
				print("입력을 취소합니다.\n")
				return

			index = get_code_index(szText)
			if index == -1:
				raise Exception("조회할 상품코드가 존재하지 않습니다.")
		except Exception as e:
			print("입력 오류!!!", e, "\n")
		else:
			break

	Sangpum.OutputTitle()
	lst[index].OutputInfo()
	Sangpum.OutputLine()
	print()

def update_sangpum():
	obj = Sangpum()
	while True:
		for i in range(4):
			while True:
				try:
					szText = input((sz_title[menu - 1] + "할 ") * ment[i] + keys[i] + " 입력 => ")
					if szText.lower() == "exit":
						print("입력을 취소합니다.\n")
						return

					if i == 0:
						index = get_code_index(szText)
						if index == -1:
							raise Exception("조회할 상품코드가 존재하지 않습니다.")

					obj.set(keys[i], Sangpum.OnValidate(szText, types[i]))
				except Exception as e:
					print("입력 오류!!!", e, "\n")
				else:
					break

		obj.DoProcess()
		if lst[index].values() == obj.values():
			print("수정된 상품 정보가 없습니다!!!\n")
		else:
			break

	lst[index] = obj
	print("\n상품 수정 성공!!!\n")

def delete_sangpum():
	i = 0

	while True:
		try:
			szText = input((sz_title[menu - 1] + "할 ") * ment[i] + keys[i] + " 입력 => ")
			if szText.lower() == "exit":
				print("입력을 취소합니다.\n")
				return

			index = get_code_index(szText)
			if index == -1:
				raise Exception("삭제할 상품코드가 존재하지 않습니다.")
		except Exception as e:
			print("입력 오류!!!", e, "\n")
		else:
			break

	del lst[index]

	print("\n상품 삭제 성공!!!\n")

if __name__ == "__main__":
	while True:
		menu_title()
		try:
			menu = int(input("메뉴를 선택하세요 (1~6) => "))
		except Exception as e:
			print("입력 오류!!!", "숫자를 입력하시오.", "\n")
			continue
		if menu == 1:
			input_sangpum()
		elif menu == 2:
			print_sangpum()
		elif menu == 3:
			search_sangpum()
		elif menu == 4:
			update_sangpum()
		elif menu == 5:
			delete_sangpum()
		elif menu == 6:
			print("\n프로그램 종료!!\n")
			break
		else:
			print("입력 오류!!!", "1부터 6 사이의 숫자를 입력하시오.", "\n")
