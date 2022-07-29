from asyncore import read
from operator import index
from numpy import rint
import pandas as pd
import csv
import numpy as np



df = pd.read_csv("planilha.csv", sep=";")
aluno1 = (df['nota1'][0] + df['nota2'][0]) / 2
if (aluno1 >= 7) and (df['faltas'][0] <= 4):
    sitAlu1 = "Aprovado"
else:
    sitAlu1 = "Reprovado"
print(sitAlu1)

aluno2 = (df['nota1'][1] + df['nota2'][1]) / 2
if (aluno2 >= 7) and (df['faltas'][1] <= 4):
    sitAlu2 = "Aprovado"
else:
    sitAlu2 = "Reprovado"
print(sitAlu2)

aluno3 = (df['nota1'][2] + df['nota2'][2]) / 2
if (aluno3 >= 7) and (df['faltas'][2] <= 4):
    sitAlu3 = "Aprovado"
else:
    sitAlu3 = "Reprovado"
print(sitAlu3)

aluno4 = (df['nota1'][3] + df['nota2'][3]) / 2
if (aluno4 >= 7) and (df['faltas'][3] <= 4):
    sitAlu4 = "Aprovado"
else:
    sitAlu4 = "Reprovado"
print(sitAlu4)


df = pd.DataFrame(df)
df.loc[:,'media'] = [aluno1,aluno2,aluno3,aluno4]
df.loc[:,'situação'] = [sitAlu1,sitAlu2,sitAlu3,sitAlu4]
print(df)
print("---------Número maior de faltas-------------")
print(df['faltas'].max())
print("---------Média geral das notas dos aluno-------------")
print(df['media'].mean())
print("---------Maior média dos alunos-------------")
print(df['media'].max())

df.to_csv("alunos_situacao.csv", index = False)

