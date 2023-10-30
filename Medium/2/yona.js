/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
const addTwoNumbers = (l1, l2) => {
  let [curr1, curr2] = [l1, l2]
  let remainder = 0
  let tail = null
  let head = null
  while (curr1 !== null || curr2 !== null) {
    const val1 = curr1?.val ?? 0
    const val2 = curr2?.val ?? 0
    const newVal = val1 + val2 + remainder
    remainder = Math.floor(newVal / 10)
    const node = { val: newVal % 10, next: null }
    if (tail !== null) tail.next = node
    tail = node
    if (head === null) head = tail
    curr1 = curr1?.next ?? null
    curr2 = curr2?.next ?? null
  }

  if (remainder) {
    const node = { val: remainder, next: null }
    tail.next = node
  }

  return head
};