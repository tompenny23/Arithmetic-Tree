###tompenny23
###Calculates arithmetic tree
import sys
def calculator(pos_of_root):
    total = "First"
    if operators[pos_of_root] == "+" or operators[pos_of_root] == "*":
        for i in children[str(pos_of_root)]:
            if operators[i] != "+" and operators[i] != "*":
                if operators[pos_of_root] == "+":  
                    if total == "First":
                        total = int(operators[i])
                    else:
                        total += int(operators[i])
                elif operators[pos_of_root] == "*":
                    if total == "First":
                        total = int(operators[i])
                    else:
                        total *= int(operators[i])
            else:
                if operators[pos_of_root] == "+":  
                    if total == "First":
                        total = calculator(i)
                    else:
                        total += calculator(i) 
                elif operators[pos_of_root] == "*":
                    if total == "First":
                        total = calculator(i)
                    else:
                        total *= calculator(i) 
    if total == "First":
        total = operators[pos_of_root]
    return total   

input_lines = []
for line in sys.stdin:
    element_list = line.rstrip().split(sep = ",")
    input_lines.append(element_list)
count = 0
while count < len(input_lines):
    pred = input_lines[count]
    global operators
    operators = input_lines[count + 1]
    length = len(pred)
    pos_of_root = pred.index("-1")
    global children
    children = {}
    for i in range(length):
        try:
            children[pred[i]].append(i)
        except:
            children[pred[i]] = [i]
    print(calculator(pos_of_root))
    count += 2

       

            
        
        
            
            
        
