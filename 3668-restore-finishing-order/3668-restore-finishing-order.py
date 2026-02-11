class Solution:
    def recoverOrder(self, order, friends):
        result = []
        friend_set = set(friends)   # quick lookup
        for participant in order:
            if participant in friend_set:
                result.append(participant)
        return result