/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function (head) {
  const seen = new Set()
  curr = head
  while (curr !== null) {
    if (seen.has(curr)) return true
    else seen.add(curr)
    curr = curr.next
  }

  return false
};