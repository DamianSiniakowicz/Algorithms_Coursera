#stocks = list, first item = return, second item = risk
#riskBudget = knapsack max weight
#return max return possible

def optimalStockBasket(stocks, riskBudget):
	
	keep = []
	for index in range(len(stocks)):
		if stocks[index][0] > 0:
			keep.append(index)
	Stocks = [stocks[stock] for stock in range(len(stocks)) if stock in keep]
	print Stocks

	portfolios = {} # (number_stocks,total_risk) : total_return

	for number_stocks in range(len(Stocks)+1):
		for risk in range(0,riskBudget+1):
			if number_stocks == 0:
				portfolios[(number_stocks,risk)] = 0
			elif Stocks[number_stocks-1][1] > risk:
				portfolios[(number_stocks,risk)] = portfolios[(number_stocks-1,risk)]
			else:
				risk_acquired = Stocks[number_stocks-1][1]
				return_acquired = Stocks[number_stocks-1][0]
				portfolios[(number_stocks,risk)] = max(portfolios[(number_stocks-1,risk)], portfolios[(number_stocks-1,risk-risk_acquired)]+return_acquired)

	return portfolios[(len(Stocks),riskBudget)]  
