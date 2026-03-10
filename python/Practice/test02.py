# import test01
#
# if __name__ == "___name":
# 	print(test01.hap(100, 200))
#
#
# even = 0
# odd = 0
# i = 1
# n = 100
# # while i <= n:
# while True:
# 	if i % 2 == 0:
# 		even += i
# 	else:
# 		odd += i
# 	i += 1
# 	if i > 100:
# 		break
#
# else:
# 	print("짝수의 합 => %d" % even)
# 	print("홀수의 합 => %d" % odd)

# a = [[10, 20], [30, 40], [50, 60]]
#
# for i in a:
# 	# print(i)
# 	for j in i:
# 		print(j, end=' ')
# 	print()

# a = set("apple")
# print(a)

# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
#
# print(a.difference(b))
# print(a.intersection(b))
# print(a.union(b))

a = {1, 2, 3, 4}
b = a
print(a)
print(b)

a.add(10)
print(a)
print(b)