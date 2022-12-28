class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        #Brute Force: For each day, check days afterwards for first day that has greater temp. Do this for each day.

        #More efficient algo: For each day, we can ask ourselves... is current day temp. the first larger temp.
        #than the current temperatures that we did not find such case for? If so, we could update all of the 
        #temperatures seen up till now and set their first next larger temp to be current day's temp!

        #We can easily keep track of days that we did not find larger temperatures coming after it at any given moment
        #in a stack data structure!

        ans = [0] * len(temps)
        #end of array will serve as top side of stack!
        #stack will have array of tuples, tuple: (day, temp)
        stack = []
        for i,temp in enumerate(temps):
            #if stack is empty: implies current day's temperature won't be warmer temperature day of previous days
            #seen up till now, if any!
            if(not stack):
                stack.append((i,temp))
                continue
            #otherwise, we will keep popping 
            while stack and stack[-1][1] < temp:
                prevDay, prevTemp = stack.pop()
                #update for prevDay in answer array the # days wait to reach warmer temp. day(diff btw day i(warmer))
                #compared to that of previous day!
                ans[prevDay] = i - prevDay
            #before moving to next day, push current day's info to stack!
            stack.append((i, temp))
        #any entries in ans array not overwritten won't have warmer temperature! -> remain as default entry value of 0!
        return ans