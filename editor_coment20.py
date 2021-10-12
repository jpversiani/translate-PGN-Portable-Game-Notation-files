# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 13:28:18 2019

@author: joaopauloversiani
"""
import pandas as pd
import sys
import time
import re # biblioteca RegEx
from pathlib import Path
###############################################################################
# Digite os seguinte comandos para instalar os módulos: PySimpleGui e pathlib: 
# pip install PySimpleGUI
# pip install pathlib

from pathlib import Path
import PySimpleGUI as sg
###############################################################################

sg.theme('Dark Blue 3')  # please make your creations colorful

layout = [  [sg.Text('Nome do Arquivo')],
            [sg.Input(), sg.FileBrowse()], 
            [sg.OK(), sg.Cancel()]] 

window = sg.Window('Tradutor de arquivos pgns', layout)

event, values = window.Read()
window.close()
nome_arquivo_pgn = Path(str(values[0])).stem+'.pgn'
#nome_arquivo_pgn = Path(root.filename).stem+'.pgn'
print(nome_arquivo_pgn)

#print ('filename')
#print (filename)


t = time.time()

# Arquivo de origem a ser traduzido
arq_pgn0 = open(nome_arquivo_pgn, "r", encoding="utf-8")
#arq_pgn0 = open(nome_arquivo_pgn, "r", errors = "ignore")


pgn = arq_pgn0.read()
arq_pgn0.close
pgn0 = pgn
lpgn = len(pgn)
vetor_ab = []
vetor_fc = []
comentarios = []
tmcoment = 0

print('\n########################################################################')
print('Leitura de comentarios do arquivo original: \n')

excel_file = 'comentarios_originais.xlsx'
try:
    #pandas_simple = pd.read_excel(excel_file)
    writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')
except FileNotFoundError:
           
    writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')

try:
  i = 0
  while i < lpgn:
      # retirar quebra de linhas
    if pgn[i:i+1] == "\n":
          pgn = pgn[0:i] + ' ' + pgn[i+1:]
    i = i + 1
   
except Exception as e:
    print(e, file=sys.stderr)
    print('erro ocorrido na linha:', i)

try:
  lpgn = len(pgn) 
  i = 0    
  # logica de abertura e fechamento dos colchetes de forma alternada
  la = 1 
  lf = 0
  while i < lpgn:

     if la == 1:
              # localizar comentários
        if pgn[i] == '{':
              #colchete abrindo
              abre = i+1
              vetor_ab.append(i)
              la = 0
              lf = 1
     if lf == 1:         
        if pgn[i] == '}':
              #colchete fechando
              fecha = i
              vetor_fc.append(i)           
              ppgn = pgn[abre:fecha]
              ppgn = ppgn.replace("=","@") #substituicao do sinal de "=", pois o excel entende esse sinal como início de uma fórmula.
              comentarios.append(ppgn)
              tmcoment = tmcoment + (fecha-abre)+3
              la = 1
              lf = 0
     i = i + 1  
  tmcoment = tmcoment + 2
  df = pd.DataFrame({'Comentários Originais': comentarios})
  #df = pd.DataFrame(comentarios)
  df.to_excel(writer, sheet_name='Sheet1',index=False)
  writer.save()
  # = df['Comentários Originais'].values.tolist()

except Exception as e:
    print(e, file=sys.stderr)
    print('erro ocorrido na linha:')
    print('linha:', i)

if len(vetor_ab) != len(vetor_fc):
    print('**********************************************************************') 
    print('Erro: O número de colchetes de abertura "{" é diferente do número colchetes de fechamento "}" no arquivo de origem.')  
   
print('========================================================================') 
print('tamanho do pgn:',lpgn, 'caracteres')     
print('número de colchetes de abertura de comentários originais"{":',len(vetor_ab))
print('número de colchetes de fechamento de comentários originais"}":',len(vetor_fc))
print('tamanho dos comentários originais:',tmcoment, 'caracteres')
print('========================================================================')  

###########################################################################################################
''' Manual do processo de tradução
    *** 1º - Traduzir o texto do arquivo coments_original.xlsx no tradutor do google: https://translate.google.com.br/ 

    *** 2º - O texto obtido no tradutor deve ser colado no arquivo coments_traduzido.xlsx
    '''
    
print('\n########################################################################')
print('Leitura de comentarios do arquivo original: \n')


excel_file = 'comentarios_traduzidos.xlsx'

try:
    df2 = pd.read_excel(excel_file,usecols=[0])
    #writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')
except FileNotFoundError:
           
    writer2 = pd.ExcelWriter(excel_file, engine='xlsxwriter')
    comts = ['{}','{}','{}']
    df2 = pd.DataFrame({'Comentários Traduzidos': comts})
    df2.to_excel(writer2, sheet_name='Sheet1',index=False)
    writer2.save()
  
df3 = df2['Comentários Traduzidos'].values.tolist()
pgn_trad = df3    
lpgn2 = len(pgn_trad)

try:
    i = 0
    while i < lpgn2:
        j = 0
        #print(i)
        cmts = pgn_trad[i]

        cmts = cmts.replace("@","=")
        cmts = cmts.replace(" #","#")  
        cmts = cmts.replace(' +','+')
        cmts = cmts.replace('+ -','+-')  
        cmts = cmts.replace(' =','=') 
        cmts = cmts.replace('= ','=') 
        cmts = cmts.replace("/ ","/") 
        cmts = cmts.replace('{ ','{')
        cmts = cmts.replace('  }','}')
        cmts = cmts.replace(' }','}')
        cmts = cmts.replace('% ','%')
        cmts = cmts.replace('White','brancas')
        cmts = cmts.replace('Black','negras')
        cmts = re.sub(r'\[.*(CSL|cal|Cal|%).*\]', '[]', cmts)

        #cmts = cmts.replace('"',"'")
                           
        pgn_trad[i] = cmts.encode("latin-1","ignore").decode("unicode_escape")
         
        i = i + 1
        '''
        lecm = len(cmts)
        while j < lecm:
           if j == 0 and cmts[j] != "{":
              cmts = "{" + cmts[j:]
              pgn_trad[i] = cmts.encode("latin-1","ignore").decode("unicode_escape")
              print(cmts)
           if j == (len(cmts)-1) and cmts[j] != "}":
              #print('teste')
              cmts = cmts[0:len(cmts)] + "}"
              pgn_trad[i] = cmts .encode("latin-1","ignore").decode("unicode_escape")
              print(cmts)
           j = j + 1
        i = i + 1
        '''
except Exception as e:
    print(e, file=sys.stderr)
    print('erro ocorrido na linha:', i)

#criaçao do arquivo memoria de traducao

excel_file2 = 'memoria_de_traducao.xlsx'

try:
    #pandas_simple = pd.read_excel(excel_file)
    writer3 = pd.ExcelWriter(excel_file2, engine='xlsxwriter')
except FileNotFoundError:
           
    writer3 = pd.ExcelWriter(excel_file2, engine='xlsxwriter')    
    
df = pd.DataFrame({'Comentários Originais': comentarios})
#df = pd.DataFrame(comentarios)
df.to_excel(writer3, sheet_name='Sheet1',index=False)

df2 = pd.DataFrame({'Comentários Traduzidos': pgn_trad})
df2.to_excel(writer3, sheet_name='Sheet1',index=False,startcol=1) 
writer3.save()    
    

# criação do pgn traduzido
try:
  lva = len(vetor_ab)

  i = lva-1
  dif = 0 
  while i >= 0:  
    pti = '{'+pgn_trad[i]+'}'
    #pti = pti.encode("utf8")
    #print(pti)        
    pgn0 = str(pgn0[0:vetor_ab[i]]) + str(pti) + str(pgn0[vetor_fc[i]+1:])   
    i = i - 1    

except Exception as e:
    print(e, file=sys.stderr)
    print('erro ocorrido na linha:', i)
    print(pgn_trad[i])
print('########################################################################')
print('Arquivo pgn gerado.')  

#pgn0 = pgn0.encode("utf-8")
#print(pgn0)

#arq_pgn1 = open (nome_arquivo_pgn[0:-4] +'_traduzido.pgn', 'w',encoding="latin-1")
arq_pgn1 = open (nome_arquivo_pgn[0:-4] +'_traduzido.pgn', 'w',encoding="utf-8") 
#arq_pgn1 = open ('pgn_traduzido-dv.pgn', 'w',encoding="cp1252")  
#arq_pgn1 = open ('pgn_traduzido-rt2.pgn', 'w',encoding="utf-8") 
#arq_pgn1 = open ('pgn_traduzidoV12.pgn', 'w') 

#article = re.sub(r'\[.*(CSL|cal|Cal|%).*\]', '[]', pgn0)

arq_pgn1.write(pgn0) 
arq_pgn1.close()

elapsed = time.time() - t
print('tempo de execução:', elapsed)