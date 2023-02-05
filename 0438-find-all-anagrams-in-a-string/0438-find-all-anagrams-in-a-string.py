class Solution:
    def findAnagrams(self, source_string: str, target_string: str) -> List[int]:
        result = []

        # store count of each character in target_string
        target_counter = Counter(target_string)
        # store count of each character in the first window of source_string
        source_window_counter = Counter(source_string[:len(target_string)])

        for i in range(len(source_string) - len(target_string)):
            # check if current window is an anagram of target_string
            if target_counter == source_window_counter:
                result.append(i)

            # decrease count of left edge character
            source_window_counter[source_string[i]] -= 1

            # remove character if count reaches 0
            if source_window_counter[source_string[i]] == 0:
                del source_window_counter[source_string[i]]

            # increase count of right edge character
            source_window_counter[source_string[i + len(target_string)]] += 1

        # check if last window is an anagram of target_string
        if target_counter == source_window_counter:
            result.append(len(source_string) - len(target_string))
            
        return result