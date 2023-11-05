"""
https://leetcode.com/problems/find-the-winner-of-an-array-game/?envType=daily-question&envId=2023-11-05
"""

### Solution Delivered to LeetCode###

class Solution():
    def __init__(self):
        self.last_winner = None
        self.elements_frequency = {}
        self.final_result = None

    def search_for_potential_winners(self, k):
        self.elements_frequency[self.winner] += 1

        if self.elements_frequency[self.winner] >= k:
            self.final_result = self.winner

    def manage_list_movements(self, arr):
        first_element = arr[0]
        second_element = arr[1]

        if first_element > second_element:
            arr.pop(1)
            arr.append(second_element)
            self.winner = first_element
        else:
            arr.pop(0)
            arr.append(first_element)
            self.winner = second_element

    def getWinner(self, arr, k):
        maxNumber = max(arr)

        while self.final_result == None:
            self.manage_list_movements(arr)

            if self.winner == maxNumber:
                self.final_result = self.winner

            if self.winner == self.last_winner:
                self.search_for_potential_winners(k)
            else:
                self.elements_frequency = {self.winner: 1}
                if k==1:
                    self.search_for_potential_winners(k)
                self.last_winner = self.winner

        return self.final_result

solution = Solution()
solution.getWinner(arr=[2,1,3,5,4,6,7], k=2)