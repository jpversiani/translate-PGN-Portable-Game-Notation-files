# Code to help translate PGN files (Portable Game Notation)

**Portable Game Notation (PGN)** is a standard plain text format for recording chess games (both the moves and related data), which can be read by humans and is also supported by most chess software.

# Código para auxílio na tradução de arquivos PGN (Portable Game Notation)

**Portable Game Notation (PGN)** é um formato de texto simples padrão para gravar jogos de xadrez (tanto os movimentos quanto os dados relacionados), que pode ser lido por humanos e também é suportado pela maioria dos softwares de xadrez.

## Links:

- https://en.wikipedia.org/wiki/Portable_Game_Notation
- http://www.saremba.de/chessgml/standards/pgn/pgn-complete.htm
- https://youtu.be/Xwqh2yn-kVo

---

## Manual in English

### 1 - Install Python, Sublime Text and the necessary libraries (Pandas and Excel-related libraries).

To install Python and Sublime Text, follow this step by step:  
https://www.wikiajuda.com.br/Como_Instalar_e_Configurar_o_Python_no_Windows_Com_o_Sublime_Text

### Python and Sublime Text websites:
- https://www.python.org
- https://www.sublimetext.com/

### 2 - Install the required libraries:
Go to the start menu and type `cmd`. Open a command prompt (CMD) and run the following commands one by one:

```bash
pip install pandas
pip install xlrd
pip install XlsxWriter
pip install openpyxl
pip install tkinter
pip install pathlib
```

### 3. Open the `editor_coment.py` file in Sublime Text and ensure the PGN file you want to edit/translate is in the same folder as the script.

### 4. Run the script for the first time:
After running it, check if the Excel files `comentarios_originais.xlsx` and `comentarios_traduzidos.xlsx` have been generated.

### 5. Translate the comments using Google Translator:
- Open Google Translator and choose the option to translate a document.
- Select the `comentarios_originais.xlsx` file and translate it.
- Copy and paste the translated content into the `comentarios_traduzidos.xlsx` file.
- Delete the second cell where "comentarios_originais" is written.

### 6. Run the script again:
This time, it will generate the translated PGN file: `pgn_traduzido.pgn`.

### 7. Open the translated PGN file in Notepad (or any text editor) and save it normally.

### 8. Open the translated PGN file in ChessBase or another chess software to verify everything is correct.

---

## Manual em Português 

### 1. Instale o Python, Sublime Text e as bibliotecas necessárias (Pandas e bibliotecas relacionadas ao Excel).
Para instalar o Python e Sublime Text, siga este passo a passo:  
[Como Instalar e Configurar o Python no Windows com o Sublime Text](https://www.wikiajuda.com.br/Como_Instalar_e_Configurar_o_Python_no_Windows_Com_o_Sublime_Text)

### Sites do Python e Sublime Text:
- https://www.python.org
- https://www.sublimetext.com/

### 2. Instale as bibliotecas necessárias:
Abra o prompt de comando (CMD) e execute os seguintes comandos, um de cada vez:

```bash
pip install pandas
pip install xlrd
pip install XlsxWriter
pip install openpyxl
pip install tkinter
pip install pathlib
```


### 3. Abra o arquivo `editor_coment.py` no Sublime Text e certifique-se de que o arquivo PGN que deseja editar/traduzir está na mesma pasta que o script.

### 4. Execute o script pela primeira vez:
Verifique se os arquivos Excel `comentarios_originais.xlsx` e `comentarios_traduzidos.xlsx` foram gerados.

### 5. Traduza os comentários usando o Google Tradutor:
- Acesse o Google Tradutor e escolha a opção de traduzir documento.
- Selecione o arquivo `comentarios_originais.xlsx` e traduza-o.
- Copie e cole o conteúdo traduzido no arquivo `comentarios_traduzidos.xlsx`.
- Exclua a célula onde está escrito "comentarios_originais".

### 6. Execute o script novamente:
Dessa vez, ele vai gerar o arquivo PGN traduzido: `pgn_traduzido.pgn`.

### 7. Abra o arquivo PGN traduzido no Bloco de Notas (ou qualquer editor de texto) e salve-o normalmente.

### 8. Abra o arquivo PGN traduzido no ChessBase ou outro software de xadrez para verificar se tudo está correto.

---

## Updates:
- The interface was updated to use **Tkinter** instead of **PySimpleGUI** for selecting files.
- Improved error handling for Excel files using the `openpyxl`, `xlrd`, and `xlsxwriter` libraries.
- The code automatically checks for and regenerates necessary Excel files (`comentarios_originais.xlsx` and `comentarios_traduzidos.xlsx`) if they are missing or corrupted.

Make sure to keep these libraries updated using `pip` commands as shown in step 2.

## Atualizações:
- A interface foi atualizada para usar **Tkinter** em vez de **PySimpleGUI** para a seleção de arquivos.
- Melhoria no tratamento de erros para arquivos Excel utilizando as bibliotecas `openpyxl`, `xlrd` e `xlsxwriter`.
- O código verifica automaticamente e recria os arquivos Excel necessários (`comentarios_originais.xlsx` e `comentarios_traduzidos.xlsx`) se eles estiverem ausentes ou corrompidos.

Certifique-se de manter essas bibliotecas atualizadas utilizando os comandos `pip` mostrados no passo 2.

## Melhorias Futuras:
- Implementar a opção de conectar a modelos de linguagem de código aberto para automatizar a tradução dos comentários nos arquivos PGN, eliminando a necessidade de usar o Google Tradutor manualmente.
- Melhorar a interface gráfica para tornar o processo de seleção de arquivos e geração de PGNs traduzidos ainda mais intuitivo.

## Agradecimentos:
Gostaria de expressar meus sinceros agradecimentos aos colegas do grupo de WhatsApp **Xadrez em Português** pelo apoio e contribuições ao projeto:

- Darcio Alberico
- Edson Fiuza
- Guilhermo (desde Peru)
- Carlos André
- Nilson Félix

Seu apoio e sugestões foram essenciais para o desenvolvimento desta ferramenta. Muito obrigado a todos!
