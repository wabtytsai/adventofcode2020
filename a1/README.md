# Day 1 part I

Given a list of numbers, the goal is to find 2 numbers that sum to 2020. 

## Brute Force approach
Since the input size is fairly small (200 numbers), a brute force approach of trying every single pair of numbers to see if they sum to 2020 would work.

```python
def two_sum(numbers):
    for x in range(len(numbers)):
        for y in range(x + 1, len(numbers)):
            if numbers[x] + numbers[y] == 2020:
                return x * y
```

## Using a Set
We can make a key observation that if
> x + y = 2020
then
> y = 2020 - x
Since both `x` and `y` have to come from `numbers`, we can simply check if `2020 - x` is also in `numbers`. Using a set or dictionary in python would let us do lookups in constant time, with the tradeoff of using more space. 

```python
def two_sum(numbers):
    numbers_set = set(numbers)
    for x in range(len(numbers)):
        if 2020 - numbers[x] in numbers_set:
            return numbers[x] * (2020 - numbers[x])
```

## Using Two Pointers
If space is a concern, we can approach this problem with a different method by sacrificing a bit of speed. We first sort the list, then have 2 pointers, `start` and `end`, that points to the start and end of the list, respectively. We obtain a sum by adding the two numbers at the pointers. Since the expenses only have positive numbers, and the list is sorted, increasing `start` will also increase the sum. Similarily, decreasing `end` will also decrease the sum. Thus, we can obtain an algorithm where we increase `start` as long as the sum is smaller than 2020, and decrease `end` as long as the sum is bigger than 2020, until we have sum equal to 2020.

```python
def two_sum(numbers):
    sorted_numbers = sorted(numbers)
    end = len(sorted_numbers) - 1
    for start in range(len(sorted_numbers)):
        while sorted_numbers[start] + sorted_numbers[end] > 2020:
            end -= 1
        if end <= start:
            break
        if sorted_numbers[start] + sorted_numbers[end] == 2020:
            return sorted_numbers[start] * sorted_numbers[end]
    return -1
```

# Day 1 part II

We have a similar problem to part I, except we now have to find 3 numbers that sum to 2020. We again can use similar approaches that we have for part I. 

## Brute Force approach
Again, since the input size is fairly small (200 numbers), a brute force approach of trying every single triplet of numbers to see if they sum to 2020 would work.

```python
def three_sum(numbers):
    for x in range(len(numbers)):
        for y in range(x + 1, len(numbers)):
            for z in range(y + 1, len(numbers)):
                if numbers[x] + numbers[y] + numbers[z] == 2020:
                    return numbers[x] * numbers[y] * numbers[z]
```

## Using a Set
Using the similar observation as above, we can rearrange
> x + y + z = 2020
to get
> x + y = 2020 - z
Thus we can reduce the problem to a two-sum problem with variable target sum.

```python
def three_sum(numbers):
    numbers_set = set(numbers)
    for z in range(len(numbers)):
        new_sum = 2020 - numbers[z]
        for x in range(z + 1, len(numbers)):
            if new_sum - numbers[x] in numbers_set:
                return numbers[x] * numbers[z] * (new_sum - numbers[x] )
```

## Using Two Pointers
Similar to using a set, we can reduce the problem to a two-sum problem with a variable target sum, and use the two pointers approach to solve it.

```python
def three_sum(numbers):
    sorted_numbers = sorted(numbers)
    for z in range(len(sorted_numbers)):
        new_sum = 2020 - sorted_numbers[z]
        end = len(sorted_numbers) - 1
        for start in range(z + 1, len(sorted_numbers)):
            while sorted_numbers[start] + sorted_numbers[end] > new_sum:
                end -= 1
            if end <= start:
                break
            if sorted_numbers[start] + sorted_numbers[end] == new_sum:
                return sorted_numbers[start] * sorted_numbers[end] * sorted_numbers[z]
    return -1
```

Note, in the two-sum case, two pointers is slightly slower than using a set, since we have to sort it first, making the sorting the bottleneck. In three-sum, the crux of the either algorithms is O(n^2), thus they both O(n^2) for time, but the set uses linear space while two pointers uses constant space. 