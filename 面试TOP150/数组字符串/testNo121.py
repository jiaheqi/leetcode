def maxProfit(prices):
    max_profit = 0
    for left in range(len(prices) - 1):
        for right in range(left+1, len(prices)):
            if prices[right] <= prices[left]:
                continue
            else:
                max_profit = max(max_profit, prices[right] - prices[left])
    return max_profit


if __name__ == '__main__':
    # prices = [7, 1, 5, 3, 6, 4]
    prices = [7,6,4,3,1]
    print(maxProfit(prices))
