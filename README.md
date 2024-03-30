# TeleDeslocamento

TeleDeslocamento é apenas um bot escrito para registrar algumas informações acerca do meu deslocamento até a universidade. 

Trata-se de um exercício da matéria Análise de Dados e Informações. 

## Informações 
O projeto foi pensando em ser usado apenas por mim, logo não há uma preocupação enorme em tratar os diversos errors e possíveis entradas pelo usuário.

Mesmo assim para instalar, basta criar um arquivo `.env` e [adicionar o token do seu bot](https://core.telegram.org/bots) como `TADI_TOKEN`.

```bash
# Instalar dependências
pip install -r requirements.txt

# Iniciar o bot
python3 bot.py
```

## Por que um bot de Telegram em vez do terminal?

Por conta da vontade em me familiarizar com a API do Telegram para Bots, e talvez implementa-lá em futuros projetos.

## License

[MIT](https://choosealicense.com/licenses/mit/)