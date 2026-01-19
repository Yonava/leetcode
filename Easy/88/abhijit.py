class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        mem = [0] * (m + n)
        
        n1, n2 = 0, 0
        curr_pos = 0
        while curr_pos < len(mem):

            if n1 < m and n2 < n:
                if nums1[n1] < nums2[n2]:
                    mem[curr_pos] = nums1[n1]
                    n1 += 1
                else:
                    mem[curr_pos] = nums2[n2]
                    n2 +=1
            elif n1 < m:
                # m is greater
                mem[curr_pos] = nums1[n1]
                n1 += 1
            else:
                mem[curr_pos] = nums2[n2]
                n2 += 1
            
            curr_pos += 1

        for i in range(m+n):
            nums1[i] = mem[i]
        
# to do this without any additional memory. we can start from the end of the array
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        a, b, write_index = m-1, n-1, m + n - 1

        while b >= 0:
            if a >= 0 and nums1[a] > nums2[b]:
                nums1[write_index] = nums1[a]
                a -= 1
            else:
                nums1[write_index] = nums2[b]
                b -= 1

            write_index -= 1

# we can stop after we are done with nums2 because 
# we are writing into nums2 and the remainder are already in sorted order