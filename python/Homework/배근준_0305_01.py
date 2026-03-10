class Sungjuk:
	__titles = "학번", "이름", "국어", "영어", "수학", "총점", "평균", "등급"
	__keys = "sid", "name", "kor", "eng", "mat", "tot", "avg", "grade"
	__rank_grade = dict(zip(tuple("수우미양가"), (90, 80, 70, 60, 0)))
	__sz_ptr = "%-8s", "%-8s", "%-8d", "%-8d", "%-8d", "%-8d", "%-8.2f", "%-8s"
	__loop_ptr = 61

	def __init__(self):
		self._sid = ""
		self._name = ""
		self._kor = 0
		self._eng = 0
		self._mat = 0
		self._tot = 0
		self._avg = 0.0
		self._grade = ""

	def set_sid(self, sid):
		self._sid = sid
	def get_sid(self):
		return self._sid
	sid = property(get_sid, set_sid)
	def set_name(self, name):
		self._name = name
	def get_name(self):
		return self._name
	name = property(get_name, set_name)
	def set_kor(self, kor):
		self._kor = kor
	def get_kor(self):
		return self._kor
	kor = property(get_kor, set_kor)
	def set_eng(self, eng):
		self._eng = eng
	def get_eng(self):
		return self._eng
	eng = property(get_eng, set_eng)
	def set_mat(self, mat):
		self._mat = mat
	def get_mat(self):
		return self._mat
	mat = property(get_mat, set_mat)
	def set_tot(self, tot):
		self._tot = tot
	def get_tot(self):
		return self._tot
	tot = property(get_tot, set_tot)
	def set_avg(self, avg):
		self._avg = avg
	def get_avg(self):
		return self._avg
	avg = property(get_avg, set_avg)
	def set_grade(self, grade):
		self._grade = grade
	def get_grade(self):
		return self._grade
	grade = property(get_grade, set_grade)

	def values(self):
		return self.sid, self.name, self.kor, self.eng, self.mat, self.tot, self.avg, self.grade

	def set(self, key, value):
		if key == "sid":
			self._sid = value
		elif key == "name":
			self._name = value
		elif key == "kor":
			self._kor = value
		elif key == "eng":
			self._eng = value
		elif key == "mat":
			self._mat = value
		elif key == "tot":
			self._tot = value
		elif key == "avg":
			self._avg = value
		elif key == "grade":
			self._grade = value

	def get(self, key):
		if key == "sid":
			return self._sid
		elif key == "name":
			return self._name
		elif key == "kor":
			return self._kor
		elif key == "eng":
			return self._eng
		elif key == "mat":
			return self._mat
		elif key == "tot":
			return self._tot
		elif key == "avg":
			return self._avg
		elif key == "grade":
			return self._grade
		else:
			return None

	def update(self, dct):
		for key, value in dct.items():
			self.set(key, value)

	def input_sungjuk(self, boundary):
		dct = dict(zip(self.__keys[boundary], tuple(map(input, map(lambda x: x + " 입력 => ", self.__titles[boundary])))))
		dct.update(dict(zip(self.__keys[2:5], map(int, map(dct.get, self.__keys[2:5])))))
		self.update(dct)

	def proess_sungjuk(self):
		self._tot = sum(map(self.get, self.__keys[2:5]))
		self._avg = self._tot / 3

		for grade, score in self.__rank_grade.items():
			if self._avg >= score:
				self._grade = grade
				break

	@staticmethod
	def output_line():
		print("=" * Sungjuk.__loop_ptr)

	@staticmethod
	def output_title():
		print(" " * 20 + "*** 성적표 ***")
		Sungjuk.output_line()
		print(*Sungjuk.__titles, sep="     ")
		Sungjuk.output_line()

	def output_sungjuk(self):
		print("".join(self.__sz_ptr) % self.values())

if __name__ == "__main__":
	obj = Sungjuk()
	#obj.input_sungjuk()
	#obj.proess_sungjuk()
	print("\n\t\t\t*** 성적관리 ***")
	print("======================================================")
	print("학번    이름    국어    영어    수학    총점    평균  등급")
	print("======================================================")
	#obj.output_sungjuk()
	print("======================================================")
