from sortedcontainers import SortedList
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foods = {}
        self.ratings = defaultdict(SortedList)
        
        for i in range(len(foods)):
            self.foods[foods[i]] = (cuisines[i],ratings[i])
            self.ratings[cuisines[i]].add((ratings[i],foods[i]))

    def changeRating(self, food: str, newRating: int) -> None:
        c,r = self.foods[food]
        self.foods[food] = (c,newRating)
        self.ratings[c].discard((r,food))
        self.ratings[c].add((newRating,food))
        
    def highestRated(self, cuisine: str) -> str:
        rating = self.ratings[cuisine][-1][0] 
        topRated = set()
        i = len(self.ratings[cuisine])-1
        while( i >=0 and self.ratings[cuisine][i][0] == rating):
            topRated.add(self.ratings[cuisine][i][1])
            i -= 1
        return min(topRated)

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)