from itertools import accumulate, chain, takewhile, repeat


def amortization_table(loan, interest, periodic_payment_amount):
	cashflows = chain([loan], repeat(-periodic_payment_amount))
	return takewhile(lambda amount: amount >= 0, accumulate(cashflows, lambda bal, am: round(bal * (1+interest) + am, 2)))


if __name__ == "__main__":
	messages = ["Give the loan initial value: ", "Give the intest rate in percentage: ", "Give the amount the customer wishes to pay per period: "]
	loan, interest, periodic = map(lambda s: float(input(s)), messages)
	table = list(amortization_table(loan, interest / 100, periodic))
	print(f"This is the amortization table: {table}")
	periods = len(table)
	total_payments = (periods-1) * periodic + table[-1]
	print(f"Finally the customer will pay: {total_payments} after {periods} periods. This is equivalent to adding a percentage of {round(100*(total_payments - loan) / loan, 2)}% of the inital loan.")