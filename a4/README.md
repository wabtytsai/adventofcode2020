# Day 4 part I

String parsing! The first part of the problem involves parsing the input and see if all but the `cid` field are present. For each passport, we can use a dictionary to keep track of the fields that exist, and loop through each passport. Again, this is one of those things where it's easier to demonstrate with code.

```python
def validate(passports):
    # passports are separated by two newlines
    passports = passports.split("\n\n")
    total = 0
    for passport in passports:
        valid = {
            'byr': 0,
            'iyr': 0,
            'eyr': 0,
            'hgt': 0,
            'hcl': 0,
            'ecl': 0,
            'pid': 0,
        }
        
        items = []
        # passport items could span multiple lines
        for line in passport.split("\n"):
            # items are separated by spaces
            items += line.split(" ")
        
        for item in items:
            # each item is of the format "<field>:<value>"
            field, value = item.split(":")
            # don't care about cid
            if field == 'cid': continue
            valid[field] = 1
        
        # need all 7 fields present to be valid
        if sum(valid.values()) == 7:
            total += 1
    return total
```

# Day 4 part II

Part II of the question is not harder, but just a bit tedious. We have done most of the heavy lifting with part I already, as we have parsed the input and separated the items into fields and values. Now, instead of unconditionally set the `valid` dictionary to `1` for all fields, we need to validate each type of field value. I won't go into all of them, but here are some examples:
```python
# assume all inputes are strings

def validate_byr(value):
    return 1920 <= int(value) <= 2002

def validate_hgt(value):
    height = int(value[:-2])
    unit = value[-2:]
    if unit == 'cm':
        return 150 <= height <= 193
    elif unit == 'in':
        return 59 <= height <= 76
    return False

#### in the middle of validate in part I ####
        field, value = item.split(":")
            if field == 'byr': 
                valid[field] = validate_byr(value)
#### and so on ####
```
And so on. Of course this is assuming we are not getting totally invalid inputs like "byr:awef", which would cause our validator to throw by attempting to cast a string into an integer, but we can worry about that when we need to. 
