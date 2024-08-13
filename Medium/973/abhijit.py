class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        for coord in points:
            distance = math.sqrt(coord[0] **2 + coord[1] ** 2)
            result.append((distance, coord))

        result.sort(key=lambda x: x[0])
        return [x[1] for x in result[:k]]