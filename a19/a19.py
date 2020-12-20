fin = open('a19.in')
lines = fin.read()
fin.close()

rules_raw, messages = lines.split("\n\n")
rules_raw = rules_raw.split('\n')
messages = messages.split('\n')

rules = dict()
double = dict()
for rule in rules_raw:
    token, children = rule.split(': ')
    token = int(token.strip())
    if children[0] == '"':
        rules[token] = children[1]
        double[token] = children[1]
    else:
        rules[token] = []
        double[token] = []
        children = children.split(" | ")
        for child in children:
            rules[token].append(list(map(int, child.split(" "))))
            double[token].append(list(map(int, child.split(" "))))

def parse(string, tokens):
##    print(string, tokens)
    if len(tokens) > len(string):
        return False
    elif len(tokens) == 0 or len(string) == 0:
        return len(tokens) == len(string) == 0
    
    token = tokens.pop(0)
    if isinstance(token, str):
        if string[0] == token:
            return parse(string[1:], tokens.copy())
    else:
        for rule in rules[token]:
            if parse(string, list(rule) + tokens.copy()):
                return True
    return False

def find_valid():
    count = 0
    for message in messages:
        if parse(message, list(rules[0][0])):
            count += 1
    return count

print(find_valid())
            
####    for i in range(len(tokens)):
####        if tokens[i] in 'ab':
####            continue
####        else:
####            done = False
####            rules = tree[tokens[i]]
####            for rule in rules:
####                yield tokens[:i] + rule + tokens[i + 1:], False
####            break
####    if done:
####        yield tokens, True
####
####queue = [['0']]
####valid = set()
####while len(queue) > 0:
####    tokens = queue.pop(0)
####    if len(queue) % 20000 == 0:
####        print(len(queue))
####    for parsed, done in one_step(tokens):
####        if done:
####            valid.add("".join(parsed))
####        else:
####            queue.append(parsed)
####
####count = 0
####for message in messages:
####    if message.strip() in valid:
####        count += 1
####print(count)
##
##
####language = dict()
####checked = dict()
####
####for rule in rules:
####    token, children = rule.split(':')
####    token = token.strip()
####    
####    children = children.strip().strip('"').split("|")
####    if len(children) == 1:
####        print(children)
####    for child in children:
####        child = child.strip()
####        if child not in language:
####            language[child] = []
####        language[child].append(token)
####        
####
####def parse(tokens):
####    global language, checked
######    print(tokens)
####    key = "".join(tokens)
####    if key in checked:
####        return checked[key]
####    if tokens == ['0']:
####        return True
####    
####    copy = tokens[:]
####    for width in range(1, 3):
####        for i in range(len(copy) - width + 1):
####            token = " ".join(copy[i: i + width])
######            print(token)
####            if token not in language: continue
####            for replace in language[token]:
####                if parse(copy[:i] + [replace] + copy[i + width:]):
####                    checked[key] = True
####                    return True
####    checked[key] = False
####    return False
####
####        
####count = 0
####for i in range(len(messages)):
####    print(i)
####    tokens = []
####    for token in list(messages[i]):
####        tokens.append(language[token][0])
####    if parse(tokens):
####        count += 1
####        
####print("count", count)
