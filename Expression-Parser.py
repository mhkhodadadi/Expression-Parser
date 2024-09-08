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

def calExp(numList, opList):
    for n in numList:
        if n[0] == '-':
            n = n[1:]
        if not n.replace('.','',1).isdigit():
            return 'Err...'
    a = float(numList[0])
    result = a
    b = 0
    op = ''
    for i in range(len(numList)-1):
        b = float(numList[i+1])
        if i<len(numList) - 1:
            op = opList[i]
        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        if op == '*':
            result = a * b
        elif op == '/':
            result = a / b
        a = result
    return result

def calculate(str):
    list1 = getNums(str,['+','-'])
    opList1 = getOps(str,['+','-'])
    i = 0
    for item in list1:
        if '*' in item or '/' in item:
            list2 = getNums(item,['*','/'])
            opList2 = getOps(item,['*','/'])
            newItem = calExp(list2, opList2)
            list1[i] = "% s" % newItem
        i += 1
    return calExp(list1, opList1)

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

while True:
    str = input('Cal>')
    if str.find('_') != -1:
        print('Err...')
        continue
    if str.lower() == 'exit' or str.lower() == 'e':
        break
    str = preCal(str)
    print(calculate(str))
## 