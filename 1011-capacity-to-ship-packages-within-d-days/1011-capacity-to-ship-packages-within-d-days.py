class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        
        def feasible(capacity):
            days_needed, current_load = 1, 0
            for weight in weights:
                if current_load + weight > capacity:
                    days_needed += 1
                    current_load = 0
                current_load += weight
            return days_needed <= days
        
        while left < right:
            mid_capacity = (left + right) // 2
            if feasible(mid_capacity):
                right = mid_capacity
            else:
                left = mid_capacity + 1
        
        return left