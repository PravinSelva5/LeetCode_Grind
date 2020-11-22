'''
The i-th  person has weight people[i] and each boat can carry a maximum weight of limit.

Each boat carries at most 2 people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.  (It is guaranteed each person can be carried by a boat.)

        - sort the array
        - attempt to add the heaviest and lightest person in the same boat
            - Use two pointers. One pointing at the beginning of the array (left ptr) and another pointing at the end of the array (right ptr)
        - Loop as long as the beginning pointer is bigger than or equal to the end pointer
            - If weights of people at the left and right ptrs are lower than the limit, MOVE left ptr to the RIGHT, MOVE right ptr to the LEFT, and increment no. of boats needed
            - If weights of people at LEFT and RIGHT pointers are bigger than the limit, move RIGHT pointer TO THE LEFT, and INCREMENT NUMBER OF BOATS NEEDED. Add the heaviest in a boat by himself
            - If pointers are equal, increment the number of boats by 1 (solo passenger)
            
            Time Complexity - O(N log(N))
            Space Complexity - O(N)
            
            Submission Results
            11/21/2020 20:57	Accepted	548 ms	21.1 MB	python3
'''
from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        # Sort the weights
        people.sort()
        
        # Initialize pointers
        left_pointer = 0
        right_pointer = len(people) - 1
        min_number_of_boats = 0
        
        while (left_pointer <= right_pointer):
            
            # If pointers are pointing at the same weight
            if left_pointer == right_pointer:
                min_number_of_boats += 1
                break
            
            # Check if heaviest and lightest person can be carried by the boat
            if people[left_pointer] + people[right_pointer] <= limit:
                right_pointer -= 1
                left_pointer += 1
                min_number_of_boats += 1
                
            # If both people can't be added, let the heaviest person go on the boat alone
            elif people[left_pointer] + people[right_pointer] > limit:
                right_pointer -= 1
                min_number_of_boats += 1
        
        return min_number_of_boats

S = solution