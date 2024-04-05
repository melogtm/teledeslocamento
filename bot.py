import os 
import logging
from os.path import join, dirname 
from dotenv import load_dotenv
from telegram.constants import ParseMode
from telegram.ext import ApplicationBuilder, Updater, CommandHandler, MessageHandler, filters, ContextTypes
from functions.insert import novoRegistro

# Carregar variáveis de ambiente
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
TOKEN = os.environ.get("TADI_TOKEN") 

# Configurando o Logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Primeira Interação com o Bot
async def start(update: Updater, context: ContextTypes.DEFAULT_TYPE): 
    nome = update.message.from_user.first_name
    await update.message.reply_text(f"Olá, eu sou o Xantadi! Como posso te ajudar, {nome}?")

# Ajuda
async def help(update: Updater, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Para realizar um novo registro, informe, nesta sequência: \n> *Tempo de Deslocamento em Minutos* \n> *Meio de Transporte - 0: Carro, 1: Metrô-Ônibus, 2: Bicicleta, 3: A pé* \n> *Dia da Semana - 0: Segunda, 1: Terça, 2: Quarta, 3: Quinta, 4: Sexta* \n> *Intensidade da Chuva: 0 - Sem Chuva, 1 - Chuva Fraca, 2 - Chuva Moderada, 3 - Chuva Forte* \n> *Horário de Saída (HH:mm)* \n> *Véspera de Feriado*: 0 - Não, 1 - Sim", parse_mode=ParseMode.MARKDOWN)

# Registro
async def registro(update: Updater, context: ContextTypes.DEFAULT_TYPE): 
    dados_informados = context.args
    
    if (len(dados_informados) < 6): 
        await update.message.reply_text("Dados insuficientes para realizar esse novo registro. Por favor, tente novamento com o comando /registro.")
        return 
    
    resultado = novoRegistro(dados_informados)

    if resultado:
        await update.message.reply_text("Registro realizado *com sucesso!*", parse_mode=ParseMode.MARKDOWN)
        return
    
    await update.message.reply_text("Algo de errado não está certo. Tente novamente *checando os valores*", parse_mode=ParseMode.MARKDOWN)


# Comando para receber o banco dados
async def receber(update: Updater, context: ContextTypes.DEFAULT_TYPE): 
    
    path_to_document = join(dirname(__file__), 'data/deslocamentos.csv')

    with open(path_to_document, mode='r', encoding='utf-8') as d:   
        await update.message.reply_document(d, quote=True) 

# Comando não existe
async def unknown(update: Updater, context: ContextTypes.DEFAULT_TYPE): 
    await update.message.reply_text("Esse comando não existe.") 


if __name__ == "__main__": 
    bot = ApplicationBuilder().token(TOKEN).build()

    # Adicionar comandos
    bot.add_handler(CommandHandler("start", start))
    bot.add_handler(CommandHandler("help", help))
    bot.add_handler(CommandHandler("registro", registro))
    bot.add_handler(CommandHandler("receber", receber))
    
    # Resposta caso o usuário envie um comando não esperado
    bot.add_handler(MessageHandler(filters.COMMAND, unknown))

    bot.run_polling()