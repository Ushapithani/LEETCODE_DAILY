class Solution:
    def countStudents(self, students, sandwiches):
        zero = students.count(0)
        one = students.count(1)
        
        for s in sandwiches:
            if s == 0:
                if zero == 0:
                    break
                zero -= 1
            else:
                if one == 0:
                    break
                one -= 1
        
        return zero + one