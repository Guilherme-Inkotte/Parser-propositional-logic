# O programa que você desenvolverá irá receber como entrada um arquivo de texto (.txt) contendo várias strings. A primeira linha do arquivo indica quantas strings estão no arquivo de texto de entrada. As linhas subsequentes contém uma string por linha. A seguir está um exemplo das linhas que podem existir em um arquivo de testes para o programa que você irá desenvolver: 
#   3 
#   abbaba 
#   abababb 
#   bbabbaaab 
# Neste  exemplo  temos  3  strings  de  entrada.  O  número  de  strings em  cada  arquivo será representado  por  um  número  inteiro  positivo.  A  resposta  do  seu  programa  deverá conter  uma, e somente uma linha de saída para cada string. Estas linhas conterão a string de entrada e o resultado  da validação conforme o formato indicado a seguir: 
#   abbaba: não pertence.  

def belongsToLanguage(x):
  return x in ['a', 'b'];

def readNumberOfStrings(line):
  print(type(int(line.strip())));
  return line.strip();

def finiteStateMachine(fileName):
  with open(fileName, 'r') as f:
    print('Lendo o arquivo ' + fileName + ':');
    lines = f.readlines();
    readNumberOfStrings(lines[0]);
    f.close();

finiteStateMachine('strings1.txt');