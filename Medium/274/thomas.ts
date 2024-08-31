function hIndex(citations: number[]): number {
    let highest = 0
    const sorted = citations.sort((a, b) => a - b)
    for (let i = 0; i < sorted.length; i++) {
        highest = Math.max(Math.min(sorted.length - i, sorted[i]), highest)
    }
    return highest
}