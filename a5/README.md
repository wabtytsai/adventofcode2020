# Day 5 part I

For part I, one could jump right in by writing a few if/else statements to manually calculate the seat id, and that would be perfectly fine. However, there is a quicker way to solve this problem, and if it isn't clear at first glance, we can make some observations to help us out.

1) We first notice that there are 128 rows on the plan, and 8 seats per row, which gives us 1024 ids total. That's 2^10!
2) Each letter in the boarding pass has us take either the lower or upper half, which is kind of like binary search!
3) Last (technically first), the question told us the airline uses **binary space partitioning**!

It might not be obvious, but the boarding passes are actually just the binary representation of the corresponding ids in disguised. We simply need to replace all the "B"s and "R"s with 1s, and "F"s and "L"s with 0s.

```python
def seatToID(seat):
    number = ""
    for i in seat:
        if i in "BR":
            number += "1"
        else:
            number += "0"
    return int(number, 2)

# using a set for part II
ids = set()
for seat in seats:
    ids.add(seatToID(seat))
# max(ids) gives the answer
```

# Day 5 part II

Assuming we already have the `ids` from part I, we just need to see, from the smallest id to the largest id, which one is missing. For the sake of completeness:

```python
def find_my_seat(ids):
    for i in range(min(ids), max(ids)):
        if i not in ids:
            return i
```