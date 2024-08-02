function isPalindrome(s: string): boolean {
    const array = s.split(' ').join('').replaceAll(/[^a-zA-Z0-9]/g, '').toLowerCase()
    return array === array.split('').reverse().join('')
}