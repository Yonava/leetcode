function lengthOfLastWord(s: string): number {
    const words = s.split(' ').filter(word => word.length > 0)
    return words[words.length - 1].length
}