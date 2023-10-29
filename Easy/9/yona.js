/**
 * @param {number} x
 * @return {boolean}
 */
const isPalindrome = (x) => {
  return x.toString().split('').reverse().join('') === x.toString()
};