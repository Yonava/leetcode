function maxProfit(prices: number[]): number {
    prices.push(-Infinity)
    let difference = 0
    let buyNumber
    for (let i = 0; i < prices.length; i++) {
        if (buyNumber === undefined && prices[i] < prices[i + 1]) {
            buyNumber = prices[i]
            continue
        }
        if (prices[i] > prices[i + 1]) {

            difference += (prices[i] - buyNumber) || 0
            buyNumber = undefined
        }
    }
    return difference

};