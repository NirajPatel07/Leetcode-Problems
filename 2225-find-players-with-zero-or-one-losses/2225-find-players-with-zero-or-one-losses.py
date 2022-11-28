from collections import Counter


class Solution:
    def findWinners(self, matches: list[list[int]]):
        cnt = Counter()

        for winner, loser in matches:
            cnt[winner] += 0
            cnt[loser] += 1

        always_winner, only_one_loss = [], []

        for player, losses in cnt.items():
            if losses == 0:
                always_winner.append(player)
            elif losses == 1:
                only_one_loss.append(player)

        return sorted(always_winner), sorted(only_one_loss)