/**
 * @param {number[]} height
 * @return {number}
 */
const trap = function (height) {
  const leftMax = Array(height.length).fill(0)
  const rightMax = Array(height.length).fill(0)

  leftMax[0] = height.at(0)
  rightMax[rightMax.length - 1] = height.at(-1)

  for (let i = 1; i < height.length; i++) {
    leftMax[i] = Math.max(leftMax[i - 1], height[i])
  }
  for (let i = height.length - 2; i >= 0; i--) {
    rightMax[i] = Math.max(rightMax[i + 1], height[i])
  }

  let res = 0
  for (let i = 0; i < height.length; i++) {
    const waterWeCanContain = Math.min(leftMax[i], rightMax[i])
    const finalWater = waterWeCanContain - height[i]
    res += (finalWater > 0 ? finalWater : 0)
  }

  return res
};