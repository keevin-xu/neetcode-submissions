class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        amount_map = dict()

        def help(amount):
            if amount == 0:

                amount_map[0] = 0

                return 0
            mini = float('inf')
            for x in coins:
                if x <= amount:
                    curr = (amount_map[amount - x] if (amount - x) in amount_map else help(amount - x))
                    if curr < mini:
                        mini = curr
            amount_map[amount] = 1 + mini
            return 1 + mini
        out = help(amount)
        if out < float('inf'):
            return out
        return -1