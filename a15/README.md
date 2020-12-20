# Day 15

Day 15's both parts are the same problem, but just different parameters. The question itself is not too hard to understand, and it gave us the algorithm already. We just need to keep track of the history of numbers we visited, and look back to see what the next number should be.

```python
def van_eck(start, n):
    sequence = start[:]
    for turn in range(len(start), n):
        current = 0
        for i in range(len(sequence) - 2, -1, -1):
            if sequence[i] == sequence[turn - 1]:
                current = turn - 1 - i
                break
        sequence.append(current)
    return sequence[-1]
```

This, however, doesn't quite work for part II, as the input is too large for this to run quickly. Since we are looking back the sequence list, we are potentially running O(n^2) time, and 30 million squared is a lot, so we need to find a way to improve this. 

One trick we can observe is that, we actually don't care about all the previous number, and we only need the **last** occurance of each number. Thus instead of keeping a list of all the numbers, we can instead keep a dictionary, where the value is the highest turn the key appears in.

```python
def van_eck(start, n):
    history = {}
    for idx, value in enumerate(start):
        history[value] = idx

    previous = start[-1]
    for turn in range(len(start), n):
        # need to check if previous value has been seen before or not
        if previous not in history:
            current = 0
        else:
            # history[previous] stores the last position it appeared in
            current = turn - 1 - history[previous]
        # we have found the value for the next turn, let's update the last seen position for the previous value
        history[previous] = turn - 1
        previous = current
    return previous
```

This now runs in linear time, but a natual question is: how much space does this use? I [don't know](https://www.youtube.com/watch?v=etMJxB-igrc). 