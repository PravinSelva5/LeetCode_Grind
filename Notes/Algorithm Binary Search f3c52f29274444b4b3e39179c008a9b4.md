# Algorithm: Binary Search

Created: Nov 21, 2020 1:00 PM

- A search techique to find elements in a collection **THAT IS SORTED.**
- Steps:
    - Initialize 2 pointers, **start** at beginning of array, **end** at the end of the array
    - find the element at the **middle of the 2 pointers**
    - If
        - element at the middle is **bigger than our goal, set end pointer to middle**
    - Else if
        - element at the **middle is smaller than our goal, set start pointer to middle + 1**