"""
https://leetcode.com/problems/find-good-days-to-rob-the-bank/description/
"""

### Solution Delivered to LeetCode###

import time
start_time = time.time()

class Solution(object):
    def check_first_condition(self, i_day, time, security):
        remaining_days_before =  i_day
        remaining_days_after = (len(security) - i_day) - 1

        if ((remaining_days_before - time >= 0) and (remaining_days_after - time >= 0)):
            return True

    def check_second_and_third_condition(self, i_day, time, security):
        for t in range(time):
            # Second condition
            if security[i_day - (time - t)] < security[i_day - (time - t - 1)]:
                return
            # Third condition
            if security[i_day + (time - t)] < security[i_day + (time - t - 1)]:
                return
        return True

    def goodDaysToRobBank(self, security, time):
        potential_days = []

        # If time is equal to zero:
        if time == 0:
            for i_day in range(len(security)):
                potential_days.append(i_day)

        # If the array just have a given number:
        elif len(set(security)) == 1:
            for i_day in range(len(security)):
                if self.check_first_condition(i_day, time, security):
                    potential_days.append(i_day)

        # For the rest of situations:
        else:
            for i_day in range(len(security)):
                first_condition = self.check_first_condition(i_day, time, security)

                if first_condition:
                    if self.check_second_and_third_condition(i_day, time, security):
                        potential_days.append(i_day)

        print(potential_days)
        return potential_days

solution = Solution()
solution.goodDaysToRobBank(security=[5,3,3,3,5,6,2], time=2)

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Tiempo de ejecución: {elapsed_time} segundos")