from datetime import date

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        y1, m1, d1 = map(int, date1.split("-"))
        y2, m2, d2 = map(int, date2.split("-"))

        day1 = date(y1, m1, d1)
        day2 = date(y2, m2, d2)

        return abs((day1 - day2).days)