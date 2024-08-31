function candy(ratings: number[]): number {
    const answer = new Array(ratings.length).fill(1)
    for (let i = 0; i < ratings.length - 1; i++) {
        if (ratings[i] < ratings[i + 1]) answer[i + 1] = answer[i] + 1
    }

    for (let i = ratings.length - 2; i >= 0; i--) {
        if (ratings[i] > ratings[i + 1]) answer[i] = Math.max(answer[i], answer[i + 1] + 1)
    }

    return answer.reduce((acc, curr) => acc + curr, 0)
}