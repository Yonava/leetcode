/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var backspaceCompare = function (s, t) {
    let s1 = []
    let s2 = []

    for (letter of s.split('')) {
        if (letter === '#') s1.pop()
        else s1.push(letter)
    }

    for (letter of t.split('')) {
        if (letter === '#') s2.pop()
        else s2.push(letter)
    }

    return s1.join('') === s2.join('')
};