# Expression-Parser

## Features
* Support for operators (+, -, *, /)
* Support for multiple parentheses
* No special library is needed

### 1. Main function, basic controls, identifying parentheses and calling operational routines
```javascript
def preCal(str):
    while True:
        i = str.rfind('(')
        if i == -1:
            break
        j = str.find(')',i)
        s1 = str[i:j+1]
        n = calculate(s1[1:len(s1)-1])
        str = f"{str[:i]}{n}{str[j+1:]}"
        str = str.replace('-+','-').replace('+-','-').replace('--','+')
    return str
```
### 2. Number recognition function
```javascript
def getNums(str, op):
    str = str.replace('*-','*_').replace('/-','/_')
    str = str.replace('-+','-').replace('+-','-').replace('--','+')
    minFirst = False
    if str[0] == '-':
        str = str[1:]
        minFirst = True
    str = str[1:] if str[0] == '+' or str[0] == '*' or str[0] == '/' else str
    str = str.replace(op[0],',').replace(op[1],',')
    if minFirst == True:
        str = '-'+str
    str = str.replace('_','-')
    return str.split(',')
```    
### 3. Operator recognition function
```javascript
def getOps(str, op):
    str = str.replace('-*','*').replace('*-','*').replace('-/','/').replace('/-','/')
    str = str.replace('-+','-').replace('+-','-').replace('--','+')
    if str[0] == '-':
        str = str[1:]
    str = str[1:] if str[0] == '+' or str[0] == '*' or str[0] == '/' else str
    list = []
    for c in str:
        if c == op[0] or c == op[1]:
            list.append(c)
    return list
```    
