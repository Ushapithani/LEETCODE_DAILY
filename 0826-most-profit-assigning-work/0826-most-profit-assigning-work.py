class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        workers = sorted(worker)

        total = 0
        best = 0
        j = 0

        for ability in workers:
            while j < len(jobs) and jobs[j][0] <= ability:
                best = max(best, jobs[j][1])
                j += 1
            total += best

        return total
        