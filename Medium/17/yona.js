/**
 * @param {string} digits
 * @return {string[]}
 */

const phoneMap = {
  '2': 'abc',
  '3': 'def',
  '4': 'ghi',
  '5': 'jkl',
  '6': 'mno',
  '7': 'pqrs',
  '8': 'tuv',
  '9': 'wxyz'
}

var letterCombinations = function (digits) {
  if (!digits) return []
  const combos = []
  const backtrack = (index, currCombo) => {
    if (index === digits.length) {
      combos.push(currCombo)
      return
    }

    const letters = phoneMap[digits[index]]
    if (letters) {
      for (const letter of letters) {
        backtrack(index + 1, currCombo + letter)
      }
    }
  }
  backtrack(0, "")
  return combos
};