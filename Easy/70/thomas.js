/**
 * @param {number} n
 * @return {number}
 */

let memo = {}
var climbStairs = function(n) {
    if (n <= 3) {
        return n
    }
    else if (memo[n]) {
        return memo[n]
    }
    
    memo[n] = (climbStairs(n-2) + climbStairs(n-1))
    console.log(memo)
    return memo[n]
};