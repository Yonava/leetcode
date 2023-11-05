/**
 * @param {string[]} strs
 * @return {string[][]}
 */
const groupAnagrams = (strs) => {
  const bucket = [];
  const indexMap = new Map();
  for (const str of strs) {
    const sortedStr = str.split('').sort().join('');
    const index = indexMap.get(sortedStr);
    if (typeof index === 'number') {
      bucket[index].push(str);
    } else {
      bucket.push([str]);
      indexMap.set(sortedStr, bucket.length - 1);
    }
  }

  return bucket;
};