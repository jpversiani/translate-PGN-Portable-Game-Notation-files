# Code to help translate PGN files (Portable Game Notation)

Portable Game Notation (PGN) is a standard plain text format for recording chess games (both the moves and related data), which can be read by humans and is also supported by most chess software.

# Código para auxílio na tradução de arquivos PGN (Portable Game Notation).

Portable Game Notation (PGN) é um formato de texto simples padrão para gravar jogos de xadrez (tanto os movimentos quanto os dados relacionados), que pode ser lido por humanos e também é suportado pela maioria dos softwares de xadrez.

## Links:

https://en.wikipedia.org/wiki/Portable_Game_Notation

http://www.saremba.de/chessgml/standards/pgn/pgn-complete.htm

https://youtu.be/Xwqh2yn-kVo

## Manual in English

1 - Install python, sublime and excel and pandas libraries.

To install python, sublime follow this step by step: https://www.wikiajuda.com.br/Como_Instalar_e_Configurar_o_Python_no_Windows_Com_o_Sublime_Text

python sites and sublime:
https://www.python.org
https://www.sublimetext.com/

2 - After to install the libraries go to the start menu and type cmd. Open the command prompt and enter the following commands (one at a time.):

pip install pandas

pip install xlrd

pip install XlsxWriter

pip install openpyxl

pip install PySimpleGUI

pip install pathlib


3 - Open the editor_comment17.py file in sublime and leave the pgn you want to edit/translate in the same folder as the editor_comment17.py file.
After running the first time, check if the excel files were saved: original_comments.xlsx and translated_comments.xlsx. Then go to googletraduror and choose the option to translate document and choose the original_comments.xlsx file, after the translator finishes the translation, copy and paste in the other translated_comments.xlsx file and delete the 2 cell where "original_comments" is written.

4- Go back to the sublime editor and run the second time.

5- After the execution, the translated pgn file will be saved: pgn_traduzado.pgn

6- Open the file using Notepad(Text block and save normally.)

7- After pasting the translated comments, don't forget to save the file before running the code again.

8- Open in chessbase and check if everything is ok.


## Manual em Português 

1 - Instale o python, sublime e bibliotecas do excel e pandas.

Para instalar o python, sublime siga o esse passo a passo: https://www.wikiajuda.com.br/Como_Instalar_e_Configurar_o_Python_no_Windows_Com_o_Sublime_Text

sites do python e sublime:
https://www.python.org
https://www.sublimetext.com/

2 - Depois pra instalar as bibliotecas vá no menu iniciar e digite cmd. Abra o prompt de comando e digite os seguintes comandos (um de cada vez.):

pip install pandas

pip install xlrd

pip install XlsxWriter

pip install openpyxl

pip install PySimpleGUI

pip install pathlib

3 - Abra o arquivo editor_coment17.py no sublime e deixe o pgn que deseja editar/traduzir na mesma pasta que estiver o arquivo editor_coment17.py.
Depois de executar a primeira vez, observe se foram salvos os arquivos excel: comentarios_originais.xlsx e comentarios_traduzidos.xlsx. Então vá no googletraduror e escolha a opção de traduzir documento e escolha o arquivo de comentarios_originais.xlsx, após o tradutor finalizar a tradução, copie e cole no outro arquivo comentarios_traduzidos.xlsx e exclua a 2 célula onde estiver escrito "comentarios_originais". 

4- Volte no editor sublime e execute a segunda vez.

5- Após a execução vai ser salvo o arquivo pgn traduzido: pgn_traduzido.pgn 

6- Abra o arquivo usando o Notepad(Bloco de texto e salve normalmente.)

7- Após colar os comentários traduzidos não se esqueça de salvar o arquivo antes de executar novamente o código.

8- Abra no chessbase e verifique se está tudo ok.
