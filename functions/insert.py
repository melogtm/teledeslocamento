from functions.format import formatarEntrada
import pandas as pd
from os import getcwd 

# Inserir novo registro de deslocamento ao banco de dados 
def novoRegistro(dados: list) -> bool:
    nova_entrada = pd.DataFrame(formatarEntrada(dados))

    try:
        nova_entrada.to_csv(getcwd() + '/data/deslocamentos.csv', mode='a', header=False, index=False)
        
        return True
    except Exception as e:
        print(e) 
        return False 
    

    
