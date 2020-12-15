# Day 2 part I

The problem boils down to counting the number of occurance of a letter in a string. The real test is how do we parse the input so that we can get the information we need. This is probably easier just to demonstrate with code.
```python
def validate(line):
    # assume we have the following line from the input: "1-3 a: abcde"
    # calling split(' ') on it will split the input into three things: "1-3", "a:", "abcde"
    frequency, letter, password = line.split(' ')

    # now let's clean up the frequency string
    # agian, calling split('-') on it will split frequency into "1", and "3"
    # we will just call map on the resulting list and turn them into integers
    low, high = map(int, frequency.split('-'))

    # letter will always be one character followed by a dash
    letter = letter[0]

    # now we are ready and can simply count the letters
    return low <= password.count(letter) <= high
```

# Day 2 part II
For part II, we need to parse the input the same way. The only difference is how we validate the password. Instead of counting the number of characters, we just need to check the values at the indices. 
```python
def validate(line):
    frequency, letter, password = line.split(' ')
    indices = map(int, frequency.split('-'))
    letter = letter[0]
    
    count = 0
    for idx in indices:
        # index starts at 0 so we need to offset by 1
        if password[idx - 1] == letter:
            count += 1
    return count == 1
```
