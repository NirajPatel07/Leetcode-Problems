
class Solution:
    def reorganizeString(self, s: str) -> str:
        S, count = len(s), Counter(s)  # count = { "a": 5, "b": 2, "c", 2 }
        max_char, max_count = max(count.items(), key=lambda x: x[1])  # get the character with the most entries
		
		# return empty string if arrangement not possible
		# I derived this equation by thinking whether an arrangement would be possible if len(s) is odd and even respectively
        if max_count > (S+1) // 2: return ""  
        
		# max_char = "a" and max_count = 5, we create the following list: [ "a", "a", "a", "a", "a" ]
        res = [max_char for _ in range(max_count)]
        
		# for every other character, we slot them into each string in the list, starting from index 0 to the end, then cycling back to 0
        i = 0
        for k,v in count.items():
            if k == max_char: continue  # we have already added "a" to res so we do not add it again
            for _ in range(v):
                res[i] += k  # string += is optimised in python to be O(1) when adding a character, using a list works as well
                i = i + 1 if i != len(res) - 1 else 0  # move to the next index in res, cycling from the start if the end has been reached
				
		# res = ["ab", "ab", "ac", "ac", "a"]
		# "a" will not be next to another "a" because we are slotting characters in between each "a"
		# same goes for any other chracter because there will be an "a" seperating them 
		
        return ''.join(res)