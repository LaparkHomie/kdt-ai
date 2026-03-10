# code = input("제품코드 입력 => ")
# name = input("제품명 입력 => ")
# count = int(input("수량 입력 => "))
# price = int(input("단가 입력 => "))
# value = count * price
#
# print("")
# print("제품코드   제품명    수량    단가    판매금액")
# print("==============================================")
# print("%4s    %4s  %4d     %4d   %6d" % (code, name, count, price, value))
# print("==============================================")
#
#

# code = input("제품코드 입력 => ")
# name = input("제품명 입력 => ")
# count = int(input("수량 입력 => "))
# price = int(input("단가 입력 => "))
# value = count * price
#
# product = [code, name, count, price, value]
#
# print("")
# print("제품코드   제품명    수량    단가    판매금액")
# print("==============================================")
# print("%4s    %4s  %4d     %4d   %6d" % tuple(product))
# print("==============================================")


szText = ("제품코드", "제품명", "수량", "단가")
dct = {}
for i in range(0, 4):
	dct[szText[i]] = input("제품코드 입력 => ")
	if i >= 2:
		dct[szText[i]] = int(dct[szText[i]])

dct["판매금액"] = dct["수량"] * dct["단가"]

print()
print("제품코드   제품명    수량    단가    판매금액")
print("==============================================")
print("%4s    %4s  %4d     %4d   %6d" % tuple(dct.values()))
print("==============================================")
