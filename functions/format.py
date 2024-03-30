# Responsável por formatar os dados para inserir no banco de dados via Pandas
def formatarEntrada(dados_deslocamento: list) -> dict: 
    return {'Tempo de Deslocamento (min)': [dados_deslocamento[0]], 
            'Meio de Transporte': [dados_deslocamento[1]], 
            'Dia da Semana': [dados_deslocamento[2]], 
            'Intensidade da Chuva': [dados_deslocamento[3]], 
            'Horário de Saída': [dados_deslocamento[4]], 
            'Véspera de Feriado': [dados_deslocamento[5]]
    }

    