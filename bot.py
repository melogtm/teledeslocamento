import os
from functions.insert import novoRegistro
from dotenv import load_dotenv
from telebot import TeleBot, types

# Carregando as variáveis de ambiente e armazenando o TOKEN para a classe TeleBot 
load_dotenv() 

TADI_TOKEN = os.getenv('TADI_TOKEN')

bot = TeleBot(TADI_TOKEN) 

"""
Função de tratamento dos dados e registro. Não consegui dividir as 2 em uma - ele exigirá que os dados sejam enviados 2 vezes. 

Provavelmente teria que procurar na documentação se há um outro método de recebimento de dados e chamar outra função.    
"""
def tratarRegistro(message: types.Message) -> None: 
    dataRegistro = message.text.split(' ') # Transforma mensagem em uma lista, melhor de se trabalhar

    # Acho que com os 6 argumentos inicias já basta
    if (len(dataRegistro) < 6): 
        bot.reply_to(message, "Dados insuficientes para realizar esse novo registro. Por favor, tente novamento com o comando /deslocamento.")
    else: 
        bot.reply_to(message, "Tudo bem! Cuidarei do seu registro...")
        
        resultado = novoRegistro(dataRegistro) 

        if (resultado): 
            bot.send_message(message.chat.id, 'Registro realizado *com sucesso!*', parse_mode='Markdown')
        else: 
            bot.send_message(message.chat.id, 'Algo deu *muito errado* :(.', parse_mode='Markdown')

# Checar se o bot está ligado
@bot.message_handler(commands=['check'])
def send_greetings(message: types.Message): 
    bot.reply_to(message, "Sim, estou ativo, pode realizar um registro.") 

# Comando para iniciar o processo de registro
@bot.message_handler(commands=["deslocamento"])
def register_handler(message: types.Message): 
    question = "Tudo bem! Vamos realizar o registro de um novo. Para isso, informe, nesta sequência: \n> *Tempo de Deslocamento em Minutos* \n> *Meio de Transporte - 0: Carro, 1: Metrô-Ônibus, 2: Bicicleta, 3: A pé* \n> *Dia da Semana - 0: Segunda, 1: Terça, 2: Quarta, 3: Quinta, 4: Sexta* \n> *Intensidade da Chuva: 0 - Sem Chuva, 1 - Chuva Fraca, 2 - Chuva Moderada, 3 - Chuva Forte* \n> *Horário de Saída (HH:mm) \n> Véspera de Feriado: 0 - Não, 1 - Sim*"

    sent_dadosDeslocamento = bot.send_message(message.chat.id, question, parse_mode='markdown') 

    bot.register_next_step_handler(sent_dadosDeslocamento, tratarRegistro)

# Comando para receber o banco dados
@bot.message_handler(commands=["receber"]) 
def receber_handler(message: types.Message): 
    with open(os.getcwd() + "/data/deslocamentos.csv", "r", encoding='utf-8') as d: 
        bot.send_document(message.chat.id, d)

# Deixar o Bot em Loop 

bot.infinity_polling() 
