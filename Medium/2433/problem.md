# Find The Original Array of Prefix Xor

[Find The Original Array of Prefix Xor](https://leetcode.com/problems/find-the-original-array-of-prefix-xor)

You are given an integer array pref of size n. Find and return the array arr of size n that satisfies:

pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i].
Note that ^ denotes the bitwise-xor operation.

It can be proven that the answer is unique.

**Example:**

```text
Input: pref = [5,2,0,3,1]
Output: [5,7,2,3,2]
Explanation: From the array [5,7,2,3,2] we have the following:
- pref[0] = 5.
- pref[1] = 5 ^ 7 = 2.
- pref[2] = 5 ^ 7 ^ 2 = 0.
- pref[3] = 5 ^ 7 ^ 2 ^ 3 = 3.
- pref[4] = 5 ^ 7 ^ 2 ^ 3 ^ 2 = 1.
```