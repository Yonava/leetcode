class Solution:
    def heapify(self,arr, N, i):
        largest = i  # Initialize largest as root
        l = 2 * i + 1     # left = 2*i + 1
        r = 2 * i + 2     # right = 2*i + 2

        # See if left child of root exists and is
        # greater than root
        if l < N and arr[largest] < arr[l]:
            largest = l

        # See if right child of root exists and is
        # greater than root
        if r < N and arr[largest] < arr[r]:
            largest = r

        # Change root, if needed
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # swap

            # Heapify the root.
            self.heapify(arr, N, largest)

    # The main function to sort an array of given size


    def heapSort(self,arr):
        N = len(arr)

        # Build a maxheap.
        for i in range(N//2 - 1, -1, -1):
            self.heapify(arr, N, i)

        # One by one extract elements
        for i in range(N-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # swap
            self.heapify(arr, i, 0)

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.heapSort(nums)
    