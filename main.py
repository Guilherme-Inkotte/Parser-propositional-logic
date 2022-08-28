# Author: Guilherme Henrique Schneider Inkotte

# Para  obter  os  pontos  relativos  a  este  trabalho, você  deverá  fazer  um  programa,  usando  a linguagem de programação que desejar, que seja capaz de validar expressões de lógica propisicional escritas em latex e definir se são expressões gramaticalmente corretas. Você validará apenas a forma da expressão (sintaxe).
# A entrada será fornecida por um arquivo de textos que será carregado em linha de comando, com a seguinte formatação:
# 1. Na primeira linha deste arquivo existe um número inteiro que informa quantas expressões lógicas estão no arquivo.
# 2. Cada uma das linhas seguintes contém uma expressão lógica que deve ser validada.
# A saída do seu programa será no terminal padrão do sistema e constituirá de uma linha de saída para cada expressão lógica de entrada contendo ou a palavra valida ou a palavra inválida e nada mais.
# Gramática:
# Formula=Constante|Proposicao|FormulaUnaria|FormulaBinaria.
# Constante="T"|"F".
# Proposicao=[a−z0−9]+
# FormulaUnaria=AbreParen OperadorUnario Formula FechaParen
# FormulaBinaria=AbreParen OperatorBinario Formula Formula FechaParen
# AbreParen="("
# FechaParen=")"
# OperatorUnario="¬"
# OperatorBinario="∨"|"∧"|"→"|"↔"
# Cada  expressão  lógica  avaliada  pode  ter  qualquer  combinação  das  operações  de  negação, conjunção, disjunção, implicação e bi-implicação sem limites na combiação de preposições e operações.
# Os valores lógicos True e False estão representados na gramática e, como tal, podem ser usados em qualquer expressão de entrada.

import re

propositionRegex = re.compile(r'^[a-z0-9]+$')


def constant(str):
    return str in ['T', 'F']


def proposition(str):
    return propositionRegex.search(str)


def openParentheses(str):
    return str == '('


def closeParentheses(str):
    return str == ')'


def unaryOperator(str):
    return str == '¬'


def binaryOperator(str):
    return str in ['∨', '∧', '→', '↔']


def unaryFormula(str):
    splitStr = str.split()
    if (len(splitStr) < 4): return False
    if (not openParentheses(splitStr[0]) or not unaryOperator(splitStr[1])
            or not closeParentheses(splitStr[len(splitStr) - 1])):
        return False
    splitStr.pop()
    splitStr.pop(0)
    splitStr.pop(0)
    return formula(' '.join(splitStr))


def binaryFormula(str):
    splitStr = str.split()
    if len(splitStr) < 5: return False
    if (not openParentheses(splitStr[0]) or not binaryOperator(splitStr[1])
            or not closeParentheses(splitStr[len(splitStr) - 1])):
        return False
    splitStr.pop()
    splitStr.pop(0)
    splitStr.pop(0)
    if (formula(splitStr[0])):
        splitStr.pop(0)
        return formula(' '.join(splitStr))
    if (formula(splitStr[len(splitStr) - 1])):
        splitStr.pop()
        return formula(' '.join(splitStr))
    doubleFormulaString = ' '.join(splitStr)
    parenthesesStackCount = 0
    endOfFirstFormulaIndex = -1
    for charIndex in range(len(doubleFormulaString)):
        if doubleFormulaString[charIndex] == "(":
            parenthesesStackCount += 1
        if doubleFormulaString[charIndex] == ")":
            parenthesesStackCount -= 1
            if parenthesesStackCount < 0:
                return False
            if parenthesesStackCount == 0:
                endOfFirstFormulaIndex = charIndex
                break
    if parenthesesStackCount != 0: return False
    return formula(doubleFormulaString[:endOfFirstFormulaIndex+1]) and formula(doubleFormulaString[endOfFirstFormulaIndex+2:])


def formula(str):
    return (constant(str) or proposition(str) or unaryFormula(str)
            or binaryFormula(str))


def readNumberOfStrings(line):
    return int(line.strip())


def parser(fileName):
    with open(fileName, 'r') as f:
        print('Lendo o arquivo ' + fileName + ':')
        lines = f.readlines()
        numberOfStrings = readNumberOfStrings(lines[0])
        for i in range(1, numberOfStrings + 1):
            strippedLine = lines[i].strip()
            if (formula(strippedLine)):
                print(strippedLine + ': válida')
            else:
                print(strippedLine + ': inválida')
        print()
        f.close()


parser('strings1.txt')
# Para testar com novos arquivos, é necessário chamar a função finiteStateMachine com
# o nome do arquivo no parâmetro.
