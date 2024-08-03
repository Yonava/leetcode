function fullJustify(words: string[], maxWidth: number): string[] {
  const spaceEachLine = (wordsToSpace: string[], lastLineFlag: boolean = false) => {
    const numWords = wordsToSpace.length
    const lengthOfWords = wordsToSpace.join('').length

    const extraSpaces = maxWidth - lengthOfWords
    const spacesPerWordGap = Math.floor(extraSpaces / (numWords - 1))
    const spacesPerWordAboveZero = spacesPerWordGap > 0 ? spacesPerWordGap : 1


    let greedySpaces = extraSpaces - spacesPerWordAboveZero * (numWords - 1)
    if (numWords === 1) greedySpaces = extraSpaces

    const spacedLine: string[] = []
    if (!lastLineFlag) for (let i = 0; i < wordsToSpace.length; i++) {
      spacedLine.push(wordsToSpace[i])
      if (i !== wordsToSpace.length - 1) {
        spacedLine.push(' '.repeat(spacesPerWordAboveZero))
      }
      if (greedySpaces > 0) {
        spacedLine.push(' ')
        greedySpaces -= 1
        if (numWords === 1) spacedLine.push(' '.repeat(greedySpaces))
      }
    }

    else {
      for (let i = 0; i < wordsToSpace.length; i++) {
        spacedLine.push(wordsToSpace[i])
        if (i !== wordsToSpace.length - 1) spacedLine.push(' ')
      }

      const extraSpacesAboveZero = (extraSpaces - numWords) < 0 ? -1 : (extraSpaces - numWords)

      spacedLine.push(' '.repeat(extraSpacesAboveZero + 1))
    }
    return spacedLine.flat().join('')
  }

  let startingIndexOfLine = 0
  let currentWordLength = 0
  let numWords = 0
  const output: string[] = []

  for (let i = 0; i < words.length; i++) {
    if ((currentWordLength + numWords + words[i].length) > maxWidth) {
      output.push(spaceEachLine(words.slice(startingIndexOfLine, i)))
      numWords = 0
      currentWordLength = 0
      startingIndexOfLine = i
    }
    if (i === words.length - 1) output.push(spaceEachLine(words.slice(startingIndexOfLine, words.length), true))

    currentWordLength += words[i].length
    numWords++
  }
  return output
};