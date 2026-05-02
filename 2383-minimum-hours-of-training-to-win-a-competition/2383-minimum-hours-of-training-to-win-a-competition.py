class Solution:
    def minNumberOfHours(self, energy, experience, energyArr, expArr):
        hours = 0
        
        for i in range(len(energyArr)):
            if energy <= energyArr[i]:
                need = energyArr[i] + 1 - energy
                hours += need
                energy += need
            
            if experience <= expArr[i]:
                need = expArr[i] + 1 - experience
                hours += need
                experience += need
            
            energy -= energyArr[i]
            experience += expArr[i]
        
        return hours