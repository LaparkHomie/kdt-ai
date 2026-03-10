import random

print("금요일마다 찾아오는 행운의 시간!")
print("금주의 로또번호는......")
print()
print(*sorted(random.sample(range(1, 46), 6)), sep=", ")
print()
print("축하합니다~ 당첨자께서는 가까운 은행 지점에 방문하셔서 상금을 수령하시기 바랍니다.")
