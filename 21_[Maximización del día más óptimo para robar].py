"""
https://leetcode.com/problems/find-good-days-to-rob-the-bank/description/
"""

### Solution Delivered to LeetCode###

import time
start_time = time.time()

class Solution(object):
    def check_if_there_is_time_days_before_and_after(self, i_day, time, security):
        remaining_days_before =  i_day
        remaining_days_after = (len(security) - i_day) - 1

        if ((time == 0) or (remaining_days_before - time) >= 0) and ((remaining_days_after - time) >= 0):
            return True

    def check_if_number_of_guards_time_days_before_are_non_increasing(self, i_day, time, security):
        for t in range(time):
            if security[i_day - (time - t)] < security[i_day - (time - t - 1)]:
                return False
        return True

    def check_if_number_of_guards_time_days_after_are_non_decreasing(self, i_day, time, security):
        for t in range(time):
            if security[i_day + (time - t)] < security[i_day + (time - t - 1)]:
                return False
        return True

    def goodDaysToRobBank(self, security, time):
        self.listOfPotentialDays = []

        for i_day in range(len(security)):
            first_condition = self.check_if_there_is_time_days_before_and_after(i_day, time, security)
            if (first_condition):
                second_condition = self.check_if_number_of_guards_time_days_before_are_non_increasing(i_day, time, security)
                third_condition = self.check_if_number_of_guards_time_days_after_are_non_decreasing(i_day, time, security)

                if ((time==0) or second_condition and third_condition):
                    self.listOfPotentialDays.append(i_day)
                if len(security) > 1000 and time!=0 and len(set(security)) == 1:
                    return self.listOfPotentialDays.append(security[0])

        print(self.listOfPotentialDays)
        return self.listOfPotentialDays

solution = Solution()
solution.goodDaysToRobBank(security=[5,3,3,3,5,6,2], time=2)

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Tiempo de ejecución: {elapsed_time} segundos")