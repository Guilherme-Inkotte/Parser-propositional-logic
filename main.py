# O programa que você desenvolverá irá receber como entrada um arquivo de texto (.txt) contendo várias strings. A primeira linha do arquivo indica quantas strings estão no arquivo de texto de entrada. As linhas subsequentes contém uma string por linha. A seguir está um exemplo das linhas que podem existir em um arquivo de testes para o programa que você irá desenvolver:
#   3
#   abbaba
#   abababb
#   bbabbaaab
# Neste  exemplo  temos  3  strings  de  entrada.  O  número  de  strings em  cada  arquivo será representado  por  um  número  inteiro  positivo.  A  resposta  do  seu  programa  deverá conter  uma, e somente uma linha de saída para cada string. Estas linhas conterão a string de entrada e o resultado  da validação conforme o formato indicado a seguir:
#   abbaba: não pertence.


def belongsToLanguage(x):
    return x in ['a', 'b']

def readNumberOfStrings(line):
    return int(line.strip())

def initialState(string, length):
    if 1 >= length:
      print(string + ': não pertence.');
    elif(not(belongsToLanguage(string[0]))):
      print(string + ': não pertence.');
    elif string[0] == 'a':
      firstState(string, 1, length);
    elif string[0] == 'b':
      thirdState(string, 1, length);

def firstState(string, charIndex, length):
    if charIndex + 1 == length:
      print(string + ': não pertence.');
    elif(not(belongsToLanguage(string[charIndex]))):
      print(string + ': não pertence.');
    elif string[charIndex] == 'a':
      fourthState(string);
    elif string[charIndex] == 'b':
      secondState(string, charIndex + 1, length);

def secondState(string, charIndex, length):
    if charIndex + 1 == length:
      print(string + ': não pertence.');
    elif(not(belongsToLanguage(string[charIndex]))):
      print(string + ': não pertence.');
    elif string[charIndex] == 'a':
      fourthState(string);
    elif string[charIndex] == 'b':
      thirdState(string, charIndex + 1, length);

def thirdState(string, charIndex, length):
    if charIndex + 1 == length:
      print(string + ': pertence.');
    elif(not(belongsToLanguage(string[charIndex]))):
      print(string + ': não pertence.');
    elif string[charIndex] == 'a':
      firstState(string, charIndex + 1, length);
    elif string[charIndex] == 'b':
      thirdState(string, charIndex + 1, length);

def fourthState(string):
    print(string + ': não pertence.');

def finiteStateMachine(fileName):
    with open(fileName, 'r') as f:
        print('Lendo o arquivo ' + fileName + ':');
        lines = f.readlines();
        numberOfStrings = readNumberOfStrings(lines[0]);
        for i in range(1, numberOfStrings + 1):
            print(i);
            strippedLine = lines[i].strip();
            lineLenght = len(lines[i]);
            initialState(strippedLine, lineLenght);
        f.close()

finiteStateMachine('strings1.txt')
