import heapq
from typing import List

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foodToCuisine = {}     # maps food -> cuisine
        self.foodToRating = {}      # maps food -> rating
        self.cuisineFoodHeap = {}   # maps cuisine -> heap of (-rating, food)

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.foodToCuisine[food] = cuisine
            self.foodToRating[food] = rating

            if cuisine not in self.cuisineFoodHeap:
                self.cuisineFoodHeap[cuisine] = []
            heapq.heappush(self.cuisineFoodHeap[cuisine], (-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.foodToCuisine[food]
        self.foodToRating[food] = newRating
        # Push new rating onto the heap
        heapq.heappush(self.cuisineFoodHeap[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisineFoodHeap[cuisine]
        # Lazy removal: pop until top matches current rating
        while heap:
            rating, food = heap[0]
            if -rating == self.foodToRating[food]:
                return food
            heapq.heappop(heap)  # discard outdated entry

"""
we only ever care about the top rated food. T
when updating the rating, we can change it and add the new value.
The hashmap storing the current rating helps us check if the rating we've found is the current one
if it is not the current one (we reduced or increase the rating previously), we will know by comparing it to the mapping we've found.
this makes the heap self-healing

"""