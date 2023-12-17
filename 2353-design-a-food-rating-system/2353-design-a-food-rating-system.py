class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.N = len(foods)
        ticket = {}
        h = {k: [] for k in set(cuisines)}
        fToC = {}

        for i in range(self.N):
            heapq.heappush(h[cuisines[i]], (-ratings[i], foods[i], 0))
            ticket[foods[i]]=0
            fToC[foods[i]] = cuisines[i]
        
        self.h = h
        self.ticket=ticket
        self.cnt=1
        self.fToC=fToC

    def changeRating(self, food: str, newRating: int) -> None:
        self.ticket[food]=self.cnt  #<- memorize newest rating update 
        heapq.heappush(self.h[self.fToC[food]], (-newRating, food, self.cnt))

        self.cnt += 1
        

    def highestRated(self, cuisine: str) -> str:
        while self.h[cuisine][0][2] < self.ticket[self.h[cuisine][0][1]]:
            # current best rating is outdated so remove it
            heapq.heappop(self.h[cuisine])
        return self.h[cuisine][0][1]