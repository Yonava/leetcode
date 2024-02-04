/**
 * @param {number[]} height
 * @return {number}
 */

const maxArea = function (height) {
  let [left, right] = [0, height.length - 1]
  let res = Math.min(height[left], height[right]) * (right - left)

  while (left <= right) {
    if (height[left] > height[right]) right--
    else if (height[right] > height[left]) left++
    else {
      left++
      right--
    }

    const newCap = Math.min(height[left], height[right]) * (right - left)
    if (newCap > res) res = newCap
  }

  return res
};