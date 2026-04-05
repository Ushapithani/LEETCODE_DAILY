import datetime

class Solution:
    def dayOfTheWeek(self, day, month, year):
        return datetime.date(year, month, day).strftime("%A")