import re

regex = r"<[a-zA-Z.\/]+>|int\*\*|FILE\*|char\*|int\*|[a-zA-Z0-9_.\/]+|\+=|:=|->|<=|>=|<|>|\-\-|\+\+|\-=|\*\*|\+|-|\*|\/|!=|&&|\|\||!|==|=|\|,|&"

def read_file_word_by_word(file_name):
    with open(file_name, "r") as file:
        for line in file:
            for word in line.split():
                matches = re.finditer(regex, word)
                for match in matches:
                    yield match.group(0)
                    
operand, operator, skipped, funkcija = [],[],[],[]
operations = ["+","\+=",":=","->","<=",">=","<",">","--","++","-=","*","+","-","/","!=","&&","||","!","==","="]
def control_loop(word, number):
    if number == "1":
        operand.append(word)
    elif number == "2":
        operator.append(word)
    elif number == "3": 
        funkcija.append(word)
        operand.append(word)

def halstead_metrics(allOperand, allOperator, distOperand, distOperator):
    """Calculates all the Halstead metrics.

    Args:
    allOperand: The total number of operands.
    allOperator: The total number of operators.
    distOperand: The number of distinct operands.
    distOperator: The number of distinct operators.

    Returns:
    A dictionary of Halstead metrics.
    """

    metrics = {}
    metrics["Vocabulary"] = distOperand + distOperator  # Vocabulary size
    #metrics["Length"] = allOperand + allOperator  # Program length
    #metrics["V"] = metrics["N"] * math.log2(metrics["n"])  # Program volume
    metrics["Difficulty"] = (distOperator / 2) * (allOperand / distOperand)  # Program difficulty
    #metrics["E"] = metrics["V"] * metrics["D"]  # Program effort
    #metrics["L"] = metrics["V"] / metrics["E"]  # Program complexity
    #metrics["P"] = metrics["V"] / metrics["N"]  # Programmer productivity

    return metrics
  
if __name__ == "__main__":
    file_name = "..\\Akerman\\dakerman.py" #path to file
    for word in read_file_word_by_word(file_name):
        print(word+"\n")
        if word in funkcija:
            operator.append(word)
            print("Custom function call, moving on...\n")
        elif word in operand:
            operand.append(word)
            print("Operand known, moving on...\n")
        elif word in operator:
            operator.append(word)
            print("Operator known, moving on...\n")
        elif word in skipped:
            skipped.append(word)
            print("Previously skipped word, moving on...\n")
        elif word in operations:
            operator.append(word)
            print("Operator known, moving on...\n")
        else:
            text = input("0-exit,1-operand,2-operator,3-custom function, Other-skip:    ")
            if text == "1" or text == "2" or text == "3":
                control_loop(word,text)
            elif text == "0":
                break
            else:
                skipped.append(word)
                continue
                
    allOperand = len(operand)
    allOperator = len(operator)
    distOperand = set(operand)
    distOperator = set(operator)
    distOperand = len(distOperand)
    distOperator = len(distOperator)
    
    #allOperand += int(input("N2, All operand"))
    #allOperator += int(input("N1, All operator"))
    distOperator += int(input("n1, Distinct operators: "))
    distOperand += int(input("n2, Distinct operands: "))
    
    print("\nAll operands (N2): " , allOperand,"\nAll operators (N1) ",allOperator,
	"\nDistinct operands (n2) ",distOperand,"\nDistinct operators (n1) ",distOperator,"\n")
    
    metrics = halstead_metrics(allOperand, allOperator, distOperand, distOperator)

    print("Halstead metrics:")
    for metric, value in metrics.items():
        print(f"{metric}: {value}")

            