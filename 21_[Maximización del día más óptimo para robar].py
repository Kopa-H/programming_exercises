"""
https://leetcode.com/problems/find-good-days-to-rob-the-bank/description/
"""

### Solution Delivered to LeetCode###
import time
start_time = time.time()

class Solution(object):
    def check_first_condition(self, i_day, time, available_days):
        remaining_days_before = i_day
        remaining_days_after = (available_days - i_day) - 1

        if ((remaining_days_before - time >= 0) and (remaining_days_after - time >= 0)):
            return True

    def manage_exeptions(self, time, security, available_days):
        # If time is equal to zero:
        if time == 0:
            potential_days = list(range(available_days))
            return potential_days

        # If the array just have a given number:
        elif len(set(security)) == 1:
            for i_day in range(available_days):
                if self.check_first_condition(i_day, time, available_days):
                    potential_days.append(i_day)
                    return potential_days

    def search_good_days_to_rob(self, security, time):
        potential_days = []
        available_days = len(security)

        # Se manejan las excepciones [PROVISIONAL]
        potential_days_exception = self.manage_exeptions(time, security, available_days)
        if potential_days_exception != None:
            print("El problema se ha resuelto siendo tratado como una excepción")
            print(potential_days_exception)
            return potential_days_exception

        # Se crea un array de ceros con la misma longitud que available_days:
        acumulative_security = [0] * available_days
        # Se asigna el primer valor de acumulative_security como el primer valor de security:
        acumulative_security[0] = security[0]

        # Para acabar de llenar el array con la suma progresiva de los números contenidos: -Ej. [1,2,3,4] --> [1,3,6,10]-
        for i in range(1, available_days):
            acumulative_security[i] = acumulative_security[i - 1] + security[i]
        print("Acumulative Security: " + str(acumulative_security))

        # Se empieza el bucle a partir de 2 y se termina en 5
        # (es decir, se calcula únicamente aquello verificado por la primera condición)
        for i in range(time, available_days - time):
            # Se prepara la segunda condición
            left_sum = acumulative_security[i] - acumulative_security[i - time]
            # Se prepara la tercera condición
            right_sum = acumulative_security[i + time] - acumulative_security[i]

            if left_sum >= 0 and right_sum >= 0:
                potential_days.append(i - time)

        print(potential_days)
        return potential_days

solution = Solution()
solution.search_good_days_to_rob(security=[5,3,3,3,5,6,2], time=2)

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Tiempo de ejecución: {elapsed_time} segundos")

### First Solution Implemented (inefficient) ###
"""
import time
start_time = time.time()

class Solution(object):
    def check_first_condition(self, i_day, time, available_days):
        remaining_days_before =  i_day
        remaining_days_after = (available_days - i_day) - 1

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

    def search_good_days_to_rob(self, security, time):
        potential_days = []
        available_days = len(security)

        # If time is equal to zero:
        if time == 0:
            potential_days = list(range(available_days))

        # If the array just have a given number:
        elif len(set(security)) == 1:
            for i_day in range(available_days):
                if self.check_first_condition(i_day, time, available_days):
                    potential_days.append(i_day)

        # For the rest of situations:
        else:
            for i_day in range(available_days):
                if self.check_first_condition(i_day, time, available_days):
                    if self.check_second_and_third_condition(i_day, time, security):
                        potential_days.append(i_day)

        print("Lista de días potenciales " + str(potential_days))
        return potential_days

solution = Solution()
solution.search_good_days_to_rob(security=["x"], time="y")

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Tiempo de ejecución: {elapsed_time} segundos") = [24.3"]
"""