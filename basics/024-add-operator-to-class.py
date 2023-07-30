

class Expense:
	def __init__(self, name, cost):
		self.name = name
		self.cost = cost

	def __add__(self, other):
		return self.cost + other.cost


food = Expense('food', 200)
travel = Expense('travel', 30)

total = food + travel
print(f'total: {total}')