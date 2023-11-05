"""
https://leetcode.com/problems/find-good-days-to-rob-the-bank/description/
"""

### Solution Delivered to LeetCode###

class Solution(object):
    def check_if_there_is_time_days_before_and_after(self, i_day, time, security):
        print("Se empieza a verificar la primera función:")



        days_that_we_look_after_or_before = time

        remaining_days_before =  i_day
        remaining_days_after = (len(self.listOfDays) - i_day) - 1
        print("Hay [" + str(remaining_days_before) + "] días antes del día [" + str(i_day) + "]")
        print("Hay [" + str(remaining_days_after) + "] días tras el día [" + str(i_day) + "]")

        # Ejemplo:
        # Si existen dos días previos al día 2, es cierto.
        if (remaining_days_before - days_that_we_look_after_or_before) >= 0:
            print("Remaining days before - " + str(time) + " >= 0 -- CORRECT!")
        else:
            print("Remaining days before - " + str(time) + " >= 0 -- FALSE!")

        # Si existen dos días después al día 2, es cierto
        if (remaining_days_after - days_that_we_look_after_or_before) >= 0:
            print("Remaining days after - " + str(time) + " >= 0 -- Correct!")
        else:
            print("Remaining days after - " + str(time) + " >= 0 -- FALSE!")

        if ((remaining_days_before - days_that_we_look_after_or_before) >= 0) and ((remaining_days_after - days_that_we_look_after_or_before) >= 0):
            print("LAS DOS CONDICIONES SON CORRECTAS")
            return True

    def check_if_number_of_guards_time_days_before_are_non_increasing(self, i_day, time, security):
        return True
    def check_if_number_of_guards_time_days_after_are_non_decreasing(self, i_day, time, security):
        return True
    def goodDaysToRobBank(self, security, time):
        self.listOfPotentialDays = []

        # Provisional!!!
        self.listOfDays = []
        for i_day in range(len(security)):
            self.listOfDays.append(i_day)
        print(self.listOfDays)

        # In this loop we will check all the posible days for the robbery
        # That meaning we will go through the three functions below
        for i_day in range(len(security)):


            # This F checks if there exists time days before and after the i day
            first_condition = self.check_if_there_is_time_days_before_and_after(i_day, time, security)

            # This F checks if the number of guards in the time days before have not been increasing
            # (because that would mean there exist other preferable previous days where has been less security)
            second_condition = self.check_if_number_of_guards_time_days_before_are_non_increasing(i_day, time, security)

            # This F checks if the number of guards in the time days after will not decrease
            # (because that would mean there exist other preferable next days where will be less security)
            third_condition = self.check_if_number_of_guards_time_days_after_are_non_decreasing(i_day, time, security)

            if (first_condition and second_condition and third_condition):
                self.listOfPotentialDays.append(i_day)

        # Finally we will return a list that contains all the potential days that satisfy the three functions
        return self.listOfPotentialDays

solution = Solution()
solution.goodDaysToRobBank(security=[5,3,3,3,5,6,2], time=2)
