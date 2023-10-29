/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
const twoSum = (nums, target) => {
  const map = new Map();
  for (const num in nums) {
    const comp = target - nums[num];
    const compIndex = map.get(comp);
    if (compIndex) return [compIndex, num];
    map.set(nums[num], num);
  }
};