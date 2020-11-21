# Big O Notation Notes

Created: Nov 20, 2020 3:10 PM

- What makes a certain algorithm better than another?
    - Takes less time
    - Takes less space
- Big O is used to formalize counting. Allows us to express the runtime of an algorithm as it grows with the input
- An algorithm is O(f(n)), if the number of operations is less than constant multiples of f(n), as n grows
- Big O is only **concerned with the worst case scenario, *the upper bound***

![Big%20O%20Notation%20Notes%20085a7fa0d35744859a85d36a69aff2d6/Untitled.png](Big%20O%20Notation%20Notes%20085a7fa0d35744859a85d36a69aff2d6/Untitled.png)

- Constant Complexity

![Big%20O%20Notation%20Notes%20085a7fa0d35744859a85d36a69aff2d6/Untitled%201.png](Big%20O%20Notation%20Notes%20085a7fa0d35744859a85d36a69aff2d6/Untitled%201.png)

- Linear Complexity

![Big%20O%20Notation%20Notes%20085a7fa0d35744859a85d36a69aff2d6/Untitled%202.png](Big%20O%20Notation%20Notes%20085a7fa0d35744859a85d36a69aff2d6/Untitled%202.png)

## Big O Simplification

- Ignore Constants
- Ignore smaller terms, the **highest degree term is usually the term Big O cares about**
- Arithmetic operations, assignments, are **constants**
- **Direct array element access (by index) is a constant**

### Space Complexity

- How much additional memory do we consume to run our algorithm?
    - **Only consider the space our algorithm takes, not the space taken up by the input**
- Space Complexity of popular **data structures**
    - Hash Tables/Maps: O(N)
    - Stacks: O(N)
    - Queues: O(N)
    - Strings: O(N)
    - Arrays: O(N)
    - 2D Arrays: O(NM)

### Logarithms

- Some algorithms have a complexity of **O(log(N)) and O(Nlog(N))**
- **What does a logarithm represent?**
    - The number of times you can divide a number by the **log's base**, before you get a value that's less than or equal to 1.
    - **log(N) is better than N**
    - **Nlog(N) is better than N^2**
    - **Nlog(N) is worse than N**
- Examples that involve logs:
    - Binary search [ log(N) ]
    - Merge Sort [ Nlog(N) ]