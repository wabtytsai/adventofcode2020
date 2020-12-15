# Day 14 part I

Basically we are given a set of masks, group of (memory address, value) pairs for each mask, and we need to write the values to the memory address after override the values in binary with the mask. Since we need to line up the position of the binary value with the sart of the mask (which is on the right), we can use a small trick of padding the beginning of the binary value with 0s. Then we can just simply loop through value one character at a time, and override the character with the mask value if needed.
```python
def apply_mask(mask, value):
    value = "0" * (len(mask) - len(value)) + value
    result = ""
    for i in range(len(mask)):
        result += value[i] if mask[i] == 'X' else mask[i]
    return result
```
To keep track of the values we are storing, we can use a dictionary with the key being the memory address. With this, we can loop through the input, update mask as needed, and call `apply_mask` on the values before storing it at the dictionary. 

# Day 14 part II

For part II, a few things changed.
1) We are applying the mask to the address instead of the value now
2) The mask is applied differently now
3) We need to find all the possible values of the floating address

For (1), it's fairly easy to handle: we just need to pass the address to our mask function instead of the value. For (2), we just need to tweak how we assign the value according to the new rule. Let's rename our function too to distinguish between the new decoder and part I. 
```python
def decode_address(mask, address):
    address = "0" * (len(mask) - len(address)) + address
    result = ""
    for i in range(len(mask)):
        if mask[i] == 'X':
            result += 'X'
        elif mask[i] == '1':
            result += '1'
        else:
            result += address[i]
    return result
```
`decode_address` will return a floating address, which we then need to find all the possible values it could take on. To help us find all the possible combination of vlaues, we can use a helper function that splits the first X in the address into two addresses, one with a 0 and the other with a 1, and recursively calls itself with the two new addresses, until we are rid of all Xs. 
```python
def find_addresses(address):
    idx = address.find('X')
    if idx == -1:
        return [int(address, 2)]
    else:
        pre = address[:idx]
        suf = address[idx + 1:]
        return find_addresses(pre + '0' + suf) + find_addresses(pre + '1' + suf)
```
Now we again just need to loop through all the input, update mask as needed, call `decode_address` to get the floating address, call `find_addresses` to find all the possible addresses, and finally update each address with the value from the input. 
