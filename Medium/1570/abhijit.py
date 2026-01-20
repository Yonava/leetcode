class SparseVector:
    def __init__(self, nums: List[int]):
        self.weightedIndices = set()
        self.indiceToWeight = {}
        for i,v in enumerate(nums):
            if v != 0:
                self.weightedIndices.add(i)
                self.indiceToWeight[i] = v
        
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        overlappingIndices = self.weightedIndices & vec.weightedIndices
        dotProd = 0
        for k in overlappingIndices:
            dotProd += self.indiceToWeight[k] * vec.indiceToWeight[k]
        return dotProd

        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)