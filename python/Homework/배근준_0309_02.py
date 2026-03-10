class Sangpum:
	__m_keys = "상품코드", "상품명", "수량", "단가", "판매금액"
	__m_loop_ptr = 45
	__m_sz_ptr = "%4s   ", "%4s", "%4d", "%4d", "%4d"

	def __init__(self):
		self.__m_code = ""
		self.__m_name = ""
		self.__m_count = 0
		self.__m_unitprice = 0
		self.__m_price = ""

	def values(self):
		return self.__m_code, self.__m_name, self.__m_count, self.__m_unitprice, self.__m_price

	def get(self, value):
		for i, key in enumerate(self.values()):
			if value == self.__m_keys[i]:
				return key

	def set(self, key, value):
		if key == self.__m_keys[0]:
			self.__m_code = value
		elif key == self.__m_keys[1]:
			self.__m_name = value
		elif key == self.__m_keys[2]:
			self.__m_count = value
		elif key == self.__m_keys[3]:
			self.__m_unitprice = value
		elif key == self.__m_keys[4]:
			self.__m_price = value

	@staticmethod
	def OnValidate(szText, type):
		if type == str:
			if szText.strip() == "":
				raise Exception("입력란을 비워놓지 마시오.")
			return szText

		elif type == int:
			try:
				val = int(szText)
				if val < 1:
					raise Exception("1 이상의 값을 입력하시오.")
			except ValueError:
				raise Exception("숫자를 입력하시오.")

			return val

	def DoProcess(self):
		self.__m_price = self.__m_count * self.__m_unitprice

	@staticmethod
	def OutputLine():
		print("=" * Sangpum.__m_loop_ptr)

	@staticmethod
	def OutputTitle():
		print("\t" * 3 + "*** 상품관리 ***")
		Sangpum.OutputLine()
		print(*Sangpum.__m_keys, sep="     ")
		Sangpum.OutputLine()

	def OutputInfo(self):
		print("    ".join(self.__m_sz_ptr) % self.values())
