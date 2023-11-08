"""
https://leetcode.com/problems/find-good-days-to-rob-the-bank/description/
"""

### Solution Implemented (still inefficient) ###
import time
from icecream import ic
start_time = time.time()

class Solution(object):
    def manage_exceptions(self, time, security, available_days):
        # If time is equal to zero:
        if time == 0:
            potential_days = list(range(available_days))
            return potential_days

        # If the array just have a given number:
        elif len(set(security)) == 1:
            potential_days = []
            for i in range(time, available_days - time):
                potential_days.append(i)
            return potential_days


    def check_second_and_third_condition(self, i_day, time, security):
        # Se toman en cuenta todos los valores de time desde time hasta 1.
        for time in range(time, 0, -1):
            # Second condition
            if security[i_day - time] < security[i_day - (time - 1)]:
                return
            # Third condition
            if security[i_day + time] < security[i_day + (time - 1)]:
                return
        return True

    def goodDaysToRobBank(self, security, time):
        potential_days = []
        available_days = len(security)

        # Se manejan las excepciones [PROVISIONAL]
        if self.manage_exceptions(time, security, available_days) != None:
            print("El problema se ha resuelto siendo tratado como una excepción")
            return self.manage_exceptions(time, security, available_days)

        # For the rest of situations:
        else:
            # First condition
            for i_day in range(time, available_days - time):
                if self.check_second_and_third_condition(i_day, time, security):
                    potential_days.append(i_day)

        print("Lista de días potenciales " + str(potential_days))
        return potential_days

solution = Solution()
solution.goodDaysToRobBank(security=[5,3,3,3,5,6,2], time=2)

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Tiempo de ejecución: {elapsed_time} segundos")