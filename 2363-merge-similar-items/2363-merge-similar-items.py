class Solution:
    def mergeSimilarItems(self, items1, items2):
        weights = {}

        for value, weight in items1:
            weights[value] = weights.get(value, 0) + weight

        for value, weight in items2:
            weights[value] = weights.get(value, 0) + weight

        answer = []

        for value in sorted(weights):
            answer.append([value, weights[value]])

        return answer