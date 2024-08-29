function jump(nums: number[]): number {
    let goal = nums.length - 1
    let steps = 0
    while (goal !== 0) {
        for (let i = 0; i < goal; i++) {
            if (nums[i] + i >= goal) {
                steps++
                goal = i
                break
            }
        }
    }

    return steps
}