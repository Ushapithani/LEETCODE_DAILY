class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        
        has_lower = has_upper = has_digit = has_special = False
        special = "!@#$%^&*()-+"
        
        for i in range(len(password)):
            if i > 0 and password[i] == password[i-1]:
                return False
            
            if password[i].islower():
                has_lower = True
            elif password[i].isupper():
                has_upper = True
            elif password[i].isdigit():
                has_digit = True
            elif password[i] in special:
                has_special = True
        
        return has_lower and has_upper and has_digit and has_special