# Transpile python into Casio Basic

# Part 1: Lexical Analyzer
import re, sys

def nuVar(name):
    if name in correspVars:
        return usedVars[correspVars.index(name)]
    else:
        x = 65
        while chr(x) in usedVars:
            x += 1
            if x == 91:
                print("No more Variables!")
        var = chr(x)
    usedVars.append(var)
    correspVars.append(name)
    return var

def evalu(string):
    splitted = string.split(" ")
    for y in range(len(splitted)):
        if splitted[y] in correspVars:
            splitted[y] = usedVars[correspVars.index(splitted[y])]
        for repl in [["==", "="], ["%", "Rmdr"], ["**", "^"]]:
            if splitted[y] == repl[0]:
                splitted[y] = repl[1]
    if splitted[0][:6] == "input(":
        splitted[0] = splitted[0][6:-1] + "?"
    return " ".join(splitted)




def convert(string):
    global lastIndent, dotodo, todo, defining

    tabs = ((len(string) - len(string.lstrip(' ')))/4)
    diff = lastIndent - tabs

    for x in range(len(todo)):
        if todo[x][1] > tabs:
            print(todo[x][0])
            todo.pop(x)

    if defining:
        if tabs == 0:
            defining = False
        else:
            functions[-1][1].append(string)
            return

    string = (string.lstrip(' ')).lstrip('\t')

    #Comments:
    if string[0] == "#":
        return "'" + string[1:-1]
    #Covering Elses, before all the other stuff
    if string == "else:\n":
        #if todo[-1] == "IfEnd\nIfEnd":
            #print("Else")
            #return
        return "Else"
    #Covering elifs
    m = re.search('(?<=elif).*', string)
    if m:
        todo.pop()
        todo.append(["IfEnd\nIfEnd", tabs])
        return "Else\nIf" + evalu(m.group(0)[:-1]) + "\nThen"



    for repl in ["+", "==", "-", "/", "%", "**"]:
        string = string.replace(repl, " %s " %(repl))
    if tabs > lastIndent:
        lastIndent = tabs
    if tabs < lastIndent:
        print(lastIndent-tabs-1)
        for x in range(int(lastIndent-tabs-1)):
            print(todo[-1])
            todo.pop()
    lastIndent = tabs
    if string == "\n":
        return ""
    if string[:2] == "\t":
        string = string[2:]


    # Covers assignments
    m = re.search('(?<==).*', string)
    name = re.search('.*?[( = ),( = )]', string)
    if m and m.group(0)[0] != "=":
        value = m.group(0)
        if value[0] == " ":
            value = value[1:]
            name = name.group(0).replace(" ", "")
        return("%s -> %s" %(evalu(value), nuVar(name)))


    #Covers printing
    m = re.search('(?<=print\().*', string)
    if m:
        return evalu(m.group(0)[:-1])+"_"

    #Converts if statements
    m = re.search('(?<=if) .*', string)
    if m:
        todo.append(["IfEnd", tabs])
        return "If" + evalu(m.group(0)[:-1]) + "\nThen"

    #Converts For loops:
    m = re.search('(?<=for ).*', string)
    if m:
        broken = re.findall(r"[\w']+", string)
        if len(broken)>5:
            start = broken[4]
            end = int(broken[5]) - 1
        else:
            start = 0
            if broken[-1].isdigit():
                end = int(broken[-1]) - 1
            else:
                end = evalu(broken[-1])
        todo.append(['Next', tabs])
        return "For " + str(start) + " -> " + nuVar(broken[1]) + " to " + str(end)

    # Converts While loops:
    m = re.search('(?<=while).*', string)
    if m:
        todo.append(['WhileEnd', tabs])
        return "While" + evalu(m.group(0)[:-1])

    #Converts functions, as new external programs
    m = re.search('(?<=def ).*(?<=\().*\):', string)
    if m:
        functions.append([m.group(0)[:-3], []])
        defining = True
        return
    #Converts function-calls
    m = re.search('.*(?<=())', string)
    if m:
        return "Prog " + m.group(0)[:-2].upper()

    return ("Couldn't convert [%s]" %(string[:-1]))

usedVars, correspVars, lastIndent, dotodo, todo, functions, defining = [], [], 0, False, [], [], False
def main():
    if len(sys.argv) < 2:
        print("\nUsage:\n\tpython[2.7+] transpiler.py [path/to/code.py]\n\nA program to transpile Python into the Casio Basic on fx-9860 AU PLUS calculators. Not tested on any other caclulator. See https://github.com/noahingham/Python----CasioBasic-Transpiler for more information. By Noah Ingham - August 2013.")
        return
    with open(sys.argv[1], "r") as f:
        string = f.readlines()
    print("\n" + sys.argv[1][:-3].upper() + "\n"+"-"*80)
    for x in range(len(string)):
        res = convert(string[x])
        if res:
            print(res)
    for x in reversed(todo):
        print(x[0])
    # print("\n\n")
    print("-"*80)

    # Treating functions as seperate, callable functions
    for x in functions:
        print("\n\n" + x[0].upper() + "\n" + "-"*80)
        for x in x[1]:
            res = convert(x)
            if res:
                print(res)
        for x in range(len(todo)-1, -1, -1):
            print(todo[x][0])
            todo.pop(x)
        global lastIndent, dotodo
        lastIndent, dotodo = 0, False
        print("-"*80)

    # print(usedVars)
    # print(correspVars)

if __name__ == "__main__":
    main()
