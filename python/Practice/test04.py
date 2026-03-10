# def add_sub(a, b):
# 	return a + b, a - b
#
# # print(add_sub(10, 20))
# x, y = add_sub(10, 20)
# print(x, y)
#
# def mul(a, b):
# 	c = a * b
# 	return c
#
# def add(a, b):
# 	c = a + b
# 	print(c)
# 	d = mul(a, b)
# 	print(d)
#
# x = 10
# y = 20
# add(x, y)


# def circle_area(r):
# 	result = 3.14 * (r ** 2)
# 	return result
#
# if __name__ == '__main__':
# 	radius = 3
# 	area = circle_area(radius)
# 	print("반지름: %d, 면적: %.2f" % (radius, area))
# 	print(r)

# pi = 3.141592653589793238462643383279502884197169399375105820
#
# def circle_area_with_pi(r):
# 	pi = 3.14
# 	result = pi * (r ** 2)
# 	return result
#
# def circle_area_without_pi(r):
# 	result = pi * (r ** 2)
# 	return result
#
# def sum_areas():
# 	results = [circle_area_with_pi(3), circle_area_without_pi(3)]
# 	return sum(results)
#
# if __name__ == '__main__':
# 	print("PI:", pi)
# 	print("반지름:", 3, "면적:", circle_area_with_pi(3))
# 	print("반지름:", 3, "면적:", circle_area_without_pi(3))
# 	print(sum_areas())

# pi = 3.14
# def circle_area(r):
# 	global pi
# 	pi = pi + 0.0015
# 	result = pi * (r ** 2)
# 	return result
#
# if __name__ == "__main__":
# 	print("PI:", pi)
# 	print("반지름:", 3, "면적:", circle_area(3))
# 	print("PI:", pi)

def factorial(n):
	res = 1
	for i in range(1, n + 1):
		res *= i
	return res
