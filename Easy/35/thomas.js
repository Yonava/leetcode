function searchInsert(nums, target) {
    if (nums.length === 0) return 0
    let left = 0
    let right = nums.length - 1
    let mid
    while (right >= left) {
        mid = left + Math.floor((right - left) / 2)
        if (nums[mid] == target) return mid; 
        if (nums[mid] > target) right = mid - 1
        else left = mid + 1;
    }
    if (nums[mid] >= target) return mid
    return mid + 1
}