class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        window = defaultdict(int)
        max_fruits = 1
        
        l = 0
        for i ,fruit in enumerate(fruits):
            window[fruit] += 1
            while len(window)>= 3:
                window[fruits[l]] -= 1
                if window[fruits[l]] == 0:
                    del window[fruits[l]]
                l +=1
            max_fruits = max(max_fruits,i-l+1)
                
        return max_fruits