function canJump(nums: number[]): boolean {
    let index = 0
    for (const number of nums) {
        if (index < 0) return false
        if (number > index) index = number
        index -= 1
    }
    return true
}