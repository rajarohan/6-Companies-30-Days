class Solution:
    def shoppingOffers(self, price: list[int], special: list[list[int]], needs: list[int]) -> int:
        valid_specials = []
        for offer in special:
            if sum(offer[i] * price[i] for i in range(len(price))) > offer[-1]:
                valid_specials.append(offer)
        memo = {}
        def dfs(needs):
            needs_tuple = tuple(needs)
            if needs_tuple in memo:
                return memo[needs_tuple]
            min_cost = sum(need * p for need, p in zip(needs, price))
            for offer in valid_specials:
                new_needs = []
                for i in range(len(needs)):
                    if needs[i] < offer[i]:
                        break
                    new_needs.append(needs[i] - offer[i])
                else:
                    min_cost = min(min_cost, offer[-1] + dfs(new_needs))
            memo[needs_tuple] = min_cost
            return min_cost
        return dfs(needs)
