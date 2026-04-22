from datetime import datetime

class Solution:
    def dayOfYear(self, d: str) -> int:
        return datetime.strptime(d, "%Y-%m-%d").timetuple().tm_yday