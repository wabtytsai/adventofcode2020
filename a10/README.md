# Day 10 part I

The goal is to use every adapter and find the number of different jumps in jolts. Since adapters can only connect to a source with lower ratings, we essentially just need to look at the list of adapters, when sorted, what is the jump in jolts between each element. 

```python
def count_jumps(adapters):
    jumps = [0, 0, 0, 0]

    # we start at the charging outlet, which as 0 jolts
    last = 0
    adapters.sort()
    for adapter in adapters:
        # count the difference in jolts
        jumps[adapter - last] += 1
        last = adapter
    return jumps

# jumps[1] * jumps[3] gives the answer
```

# Day 10 part II

For part II things start to get interesting (read: tricky). At a quick glance, we seemed to be asked to find all the valid permutations of how the list of adapters can be arranged. With some quick math, we can see this quickly turns exponetial, and brute force probably would be too slow. In fact, the question told you that it self:

> there must be more than a trillion valid ways to arrange them! Surely, there must be an efficient way to count the arrangements.

Thus we need to make some observations. Assuming the list of adapters is sorted
- the number of valid arrangements is dependent on the number of ways we can arrange the adapters to get to the last element. 
  - This is because we always have to use the last element, and connect it to the device's built-in adapter (always +3).
- The number of valid arrangements up to the last element is dependent on (# of ways to arrange up to [last element - 1]) + (# of ways to arrange up to[last element - 2]) + (# of ways to arrange up to [last element - 3]), if they exist.
  - Since adapters can jump 1, 2, or 3 jolts, we can reach the last element via 3 these different ways
- Similarly, for any other element, the number of valid arrangements up to the element is dependent on the # of ways to arrange up to [element - 1], [element - 2], [element - 3], if they exist.
- Lastly, the number of ways to arrange only the first adapter is just 1, since we have to connect it to the charging outlet (0). 

We see that to get the final answer, we need to build up information for the previous elements, and use them to compute the answer for the next element. Using point (3), we can derive our algorithm:

```python
def count_arrangements(adapters):
    adapters.sort()
    arrangements = [0] * (adapters[-1] + 1)
    # arrangments[i] will give us number of arrangments up to adapter i

    # there is always exactly 1 way to get to 0
    arrangements[0] = 1

    for adapter in adapters:
        # lookback to the previous 3 arrangments
        # using max to not go below 0
        previous = arrangements[max(adapter - 3, 0): adapter]
        arrangements[adapter] = sum(previous)

    return arrangements[-1]
```