/**
 * @param {number} n
 * @param {number[]} left
 * @param {number[]} right
 * @return {number}
 */
const getLastMoment = function(n, left, right) {
    // max range is n
    // min is 1
    let newRight = []
    for (pos of right) {
        newRight.push(n-pos)
    }

    const maxLeft = Math.max.apply(Math, left)
    const maxRight = Math.max.apply(Math, newRight)
    return Math.max(maxLeft, maxRight)
};