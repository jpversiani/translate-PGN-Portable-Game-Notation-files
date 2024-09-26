# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 17:32:36 2024

@author: joaop
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 13:28:18 2019
Updated on Wed Sep 25 17:34:21 2024

@author: joaopauloversianiladeia

"""
import pandas as pd
import sys
import time
import re  # biblioteca RegEx
from pathlib import Path
from tkinter import Tk, filedialog
import os

###############################################################################
# Função para carregar arquivos Excel de forma robusta
def carregar_arquivo_excel(filepath):
    """
    Tenta carregar um arquivo Excel, detectando automaticamente o formato (XLS ou XLSX)
    e usando o motor correto para a leitura. Se o arquivo não existir ou estiver corrompido,
    ele será recriado.
    """
    # Se o arquivo não existir ou estiver corrompido, recriá-lo
    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        print(f"Arquivo '{filepath}' não encontrado ou está corrompido. Criando arquivo de exemplo...")
        writer = pd.ExcelWriter(filepath, engine='xlsxwriter')
        exemplo = ['{}', '{}', '{}']
        df_exemplo = pd.DataFrame({'Comentários Traduzidos': exemplo})
        df_exemplo.to_excel(writer, sheet_name='Sheet1', index=False)
        writer.close() # Corrigido: `save()` foi substituído por `close()` by Darcio Alberico
        print(f"Arquivo de exemplo '{filepath}' criado com sucesso.")
    
    # Tentar abrir o arquivo Excel
    try:
        print(f"Tentando abrir o arquivo '{filepath}' com o motor openpyxl...")
        df = pd.read_excel(filepath, usecols=[0], engine='openpyxl')
        print("Arquivo aberto com sucesso usando openpyxl (formato .xlsx).")
        return df

    except Exception as e_openpyxl:
        print(f"Falha ao abrir com openpyxl: {e_openpyxl}")
        print("Tentando recriar o arquivo Excel...")

        # Recriar o arquivo se falhar ao abrir
        writer = pd.ExcelWriter(filepath, engine='xlsxwriter')
        exemplo = ['{}', '{}', '{}']
        df_exemplo = pd.DataFrame({'Comentários Traduzidos': exemplo})
        df_exemplo.to_excel(writer, sheet_name='Sheet1', index=False)
        writer.close() # Corrigido: `save()` foi substituído por `close()` by Darcio Alberico

        # Tentar abrir novamente o arquivo recriado
        try:
            df = pd.read_excel(filepath, usecols=[0], engine='openpyxl')
            print("Arquivo recriado e aberto com sucesso.")
            return df
        except Exception as e:
            print(f"Erro ao tentar recriar o arquivo: {e}")
            sys.exit("Encerrando o programa devido a erros ao abrir o arquivo Excel.")

# Configura a janela do tkinter
root = Tk()
root.withdraw()  # Oculta a janela principal
root.title('Tradutor de arquivos pgns')

# Função para buscar arquivo
def abrir_arquivo():
    root.filename = filedialog.askopenfilename(title="Selecione o arquivo", filetypes=[("Arquivos PGN", "*.pgn")])
    return root.filename

# Exibe o nome do arquivo selecionado
nome_arquivo = abrir_arquivo()

# Verifica se o arquivo foi selecionado corretamente
if not nome_arquivo:
    sys.exit("Nenhum arquivo foi selecionado. O programa será encerrado.")

nome_arquivo_pgn = Path(str(nome_arquivo)).stem + '.pgn'
print(nome_arquivo_pgn)

# Garante que o caminho completo do arquivo esteja correto
if not os.path.exists(nome_arquivo):
    sys.exit(f"Arquivo '{nome_arquivo}' não encontrado. O programa será encerrado.")

t = time.time()

# Arquivo de origem a ser traduzido
try:
    arq_pgn0 = open(nome_arquivo, "r", encoding="utf-8")
except FileNotFoundError as e:
    sys.exit(f"Erro: {e}")

pgn = arq_pgn0.read()
arq_pgn0.close()
pgn0 = pgn
lpgn = len(pgn)
vetor_ab = []
vetor_fc = []
comentarios = []
tmcoment = 0

print('\n########################################################################')
print('Leitura de comentários do arquivo original: \n')

excel_file = 'comentarios_originais.xlsx'
try:
    writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')
except FileNotFoundError:
    writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')

try:
    i = 0
    while i < lpgn:
        # Retirar quebra de linhas
        if pgn[i:i+1] == "\n":
            pgn = pgn[0:i] + ' ' + pgn[i+1:]
        i = i + 1
except Exception as e:
    print(e, file=sys.stderr)
    print('Erro ocorrido na linha:', i)

try:
    lpgn = len(pgn)
    i = 0
    # Lógica de abertura e fechamento dos colchetes de forma alternada
    la = 1
    lf = 0
    while i < lpgn:
        if la == 1:
            # Localizar comentários
            if pgn[i] == '{':
                # Colchete abrindo
                abre = i + 1
                vetor_ab.append(i)
                la = 0
                lf = 1
        if lf == 1:
            if pgn[i] == '}':
                # Colchete fechando
                fecha = i
                vetor_fc.append(i)
                ppgn = pgn[abre:fecha]
                ppgn = ppgn.replace("=", "@")  # Substituição do sinal de "=" para evitar problemas no Excel
                comentarios.append(ppgn)
                tmcoment = tmcoment + (fecha - abre) + 3
                la = 1
                lf = 0
        i = i + 1
    tmcoment = tmcoment + 2
    df = pd.DataFrame({'Comentários Originais': comentarios})
    df.to_excel(writer, sheet_name='Sheet1', index=False)
    writer.close() # Corrigido: `save()` foi substituído por `close()` by Darcio Alberico

except Exception as e:
    print(e, file=sys.stderr)
    print('Erro ocorrido na linha:', i)

if len(vetor_ab) != len(vetor_fc):
    print('**********************************************************************')
    print('Erro: O número de colchetes de abertura "{" é diferente do número colchetes de fechamento "}" no arquivo de origem.')

print('========================================================================')
print('Tamanho do pgn:', lpgn, 'caracteres')
print('Número de colchetes de abertura de comentários originais "{":', len(vetor_ab))
print('Número de colchetes de fechamento de comentários originais "}":', len(vetor_fc))
print('Tamanho dos comentários originais:', tmcoment, 'caracteres')
print('========================================================================')

###########################################################################################################
''' Manual do processo de tradução
    *** 1º - Traduzir o texto do arquivo comentarios_originais.xlsx no tradutor do google: https://translate.google.com.br/ 

    *** 2º - O texto obtido no tradutor deve ser colado no arquivo comentarios_traduzidos.xlsx
    '''
    
print('\n########################################################################')
print('Leitura de comentários traduzidos: \n')

excel_file = 'comentarios_traduzidos.xlsx'

# Usando a função robusta para carregar o arquivo Excel
df2 = carregar_arquivo_excel(excel_file)

# Verifica as colunas do DataFrame
print("Colunas disponíveis no arquivo Excel:", df2.columns)

# Verifica se a coluna 'Comentários Traduzidos' existe, caso contrário, cria-a
if 'Comentários Traduzidos' not in df2.columns:
    print("Coluna 'Comentários Traduzidos' não encontrada. Recriando arquivo com a coluna correta...")
    writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')
    exemplo = ['{}', '{}', '{}']
    df_exemplo = pd.DataFrame({'Comentários Traduzidos': exemplo})
    df_exemplo.to_excel(writer, sheet_name='Sheet1', index=False)
    writer.close() # Corrigido: `save()` foi substituído por `close()` by Darcio Alberico
    df2 = pd.read_excel(excel_file, engine='openpyxl')

# Agora, podemos acessar a coluna 'Comentários Traduzidos'
df3 = df2['Comentários Traduzidos'].values.tolist()
pgn_trad = df3
lpgn2 = len(pgn_trad)

try:
    i = 0
    while i < lpgn2:
        cmts = pgn_trad[i]
        cmts = cmts.replace("@", "=")
        cmts = cmts.replace(" #", "#")
        cmts = cmts.replace(' +', '+')
        cmts = cmts.replace('+ -', '+-')
        cmts = cmts.replace(' =', '=')
        cmts = cmts.replace('= ', '=')
        cmts = cmts.replace("/ ", "/")
        cmts = cmts.replace('{ ', '{')
        cmts = cmts.replace('  }', '}')
        cmts = cmts.replace(' }', '}')
        cmts = cmts.replace('% ', '%')
        cmts = cmts.replace('White', 'brancas')
        cmts = cmts.replace('Black', 'negras')
        cmts = re.sub(r'\[.*(CSL|cal|Cal|%).*\]', '[]', cmts)

        pgn_trad[i] = cmts.encode("latin-1", "ignore").decode("unicode_escape")
        i = i + 1
except Exception as e:
    print(e, file=sys.stderr)
    print('Erro ocorrido na linha:', i)

# Criação do arquivo memória de tradução
excel_file2 = 'memoria_de_traducao.xlsx'

try:
    writer3 = pd.ExcelWriter(excel_file2, engine='xlsxwriter')
except FileNotFoundError:
    writer3 = pd.ExcelWriter(excel_file2, engine='xlsxwriter')

df = pd.DataFrame({'Comentários Originais': comentarios})
df.to_excel(writer3, sheet_name='Sheet1', index=False)

df2 = pd.DataFrame({'Comentários Traduzidos': pgn_trad})
df2.to_excel(writer3, sheet_name='Sheet1', index=False, startcol=1)
writer3.close() # Corrigido: `save()` foi substituído por `close()` by Darcio Alberico

# Criação do pgn traduzido
try:
    lva = len(vetor_ab)
    i = lva - 1
    while i >= 0:
        pti = '{' + pgn_trad[i] + '}'
        pgn0 = str(pgn0[0:vetor_ab[i]]) + str(pti) + str(pgn0[vetor_fc[i] + 1:])
        i = i - 1
except Exception as e:
    print(e, file=sys.stderr)
    print('Erro ocorrido na linha:', i)
    print(pgn_trad[i])

print('########################################################################')
print('Arquivo pgn gerado.')

arq_pgn1 = open(nome_arquivo_pgn[0:-4] + '_traduzido.pgn', 'w', encoding="utf-8")
arq_pgn1.write(pgn0)
arq_pgn1.close()

elapsed = time.time() - t
print('Tempo de execução:', elapsed)
