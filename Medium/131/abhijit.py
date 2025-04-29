class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(s):
            return s == s[::-1]

        def my_partition(s):
            if not s:
                return [[]]  # Base case: an empty string has one partition - the empty list

            result = []

            for i in range(1, len(s) + 1):
                current = s[:i]
                if is_palindrome(current):
                    # Explore the rest
                    rest_partitions = my_partition(s[i:])
                    for partitioning in rest_partitions:
                        result.append([current] + partitioning)

            return result
        return my_partition(s)