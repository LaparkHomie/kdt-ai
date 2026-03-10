# with open('hello.txt', 'w') as file:
# 	for i in range(3):
# 		file.write('Hello, world! {0}\n'.format(i))

# lines = ['안녕하세요.\n', '파이썬\n', '코딩 도장입니다.\n']
# with open('hello.txt', 'w', encoding='utf8') as file:
# 	file.writelines(lines)

# with open('hello.txt', 'r', encoding='utf8') as file:
# 	for i in range(3):
# 		print(file.read())

with open('hello.txt', 'r') as file:
	line = None
	while line != '':
		line = file.readline()
		print(line.strip('\n'))
