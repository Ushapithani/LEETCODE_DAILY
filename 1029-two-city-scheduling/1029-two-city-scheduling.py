class Solution:
    def twoCitySchedCost(self, costs):
        total_cost = 0
        refunds = []

        for a, b in costs:
            total_cost += a
            refunds.append(b - a)

        refunds.sort()

        n = len(costs) // 2

        for i in range(n):
            total_cost += refunds[i]

        return total_cost