from itertools import accumulate, chain, takewhile, repeat


def dichotomy(v_min, v_max, v_actual=None, go_down=True):
	if v_actual is None:
		v_actual = v_max
		go_down = True
	if go_down:
		a, b = (v_min, v_actual)
	else:
		a, b = (v_actual, v_max)
	return a, (a+b) / 2, b


def amortization_table(loan, interest, periodic_payment_amount):
	cashflows = chain([loan], repeat(-periodic_payment_amount))
	return takewhile(lambda amount: amount >= 0, accumulate(cashflows, lambda bal, am: round(bal * (1+interest) + am, 2)))

def reverse_amortization(loan, interest, total_periods):
	print(f"interest: {interest},   (1+interest): {1+interest}")
	first_candidate = round(loan / total_periods, 2)
	# last_candidate = round(((1+interest)**(total_periods + 3)) * first_candidate, 2)
	last_candidate = first_candidate * 3
	# candidates = accumulate(chain([first_candidate], repeat(1+interest)), lambda a, i: round(a * i, 2))
	candidate = None
	go_down = None
	for i in range(20):
		# candidate = next(candidates)
		first_candidate, candidate, last_candidate = (round(x, 2) for x in dichotomy(first_candidate, last_candidate, candidate, go_down))
		print(f"Trial #{i} with candidate {candidate}")
		table = list(amortization_table(loan, interest, candidate))
		periods = len(table)
		if periods > (total_periods + 1):
			go_down = False
		elif periods < total_periods:
			go_down = True
		else:
			return candidate, periods
		# if periods in [total_periods - 1, total_periods, total_periods + 1]:
		# 	return candidate, periods
		print(f"Failing period: {periods}")
	return None, None


def test_table():
	messages = ["Give the loan initial value: ", "Give the intest rate in percentage: ", "Give the amount the customer wishes to pay per period: "]
	loan, interest, periodic = map(lambda s: float(input(s)), messages)
	table = list(amortization_table(loan, interest / 100, periodic))
	print(f"This is the amortization table: {table}")
	periods = len(table)
	total_payments = (periods-1) * periodic + table[-1]
	print(f"Finally the customer will pay: {total_payments} after {periods} periods. This is equivalent to adding a percentage of {round(100*(total_payments - loan) / loan, 2)}% of the inital loan.")

def test_reverse():
	messages = ["Give the loan initial value: ", "Give the intest rate in percentage: ", "Give the total periods you with to pay: "]
	loan, interest, total_periods = map(lambda s: float(input(s)), messages)
	per_period, periods = reverse_amortization(loan, interest / 100, total_periods)
	print(f"total periods proposed is: {periods}. You will pay {per_period} for each period")


if __name__ == "__main__":
	test_table()
	# test_reverse()