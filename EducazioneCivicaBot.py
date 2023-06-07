import string
import random
from telegram.ext import Updater, CommandHandler

# Inserisci il tuo token qui
TOKEN = "5782202005:AAHzE6z6aNh1__LODebMzNkl4Usf2M0YQic"

def start(update, context):
    from funzioni import text_start
    text = text_start()
    update.message.reply_text(text)

def password(update, context):
    mod = context.args[0] if context.args else "medio"

    if mod == 'facile':
        lunghezza = '15'
    elif mod == 'medio':
        lunghezza = '25'
    elif mod == 'difficile':
        lunghezza = '35'
    else:
        lunghezza = int(mod)

    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Modalità selezionata: {mod}")

    def p(lunghezza):           # generatore di password in base alla difficoltà
        stringa = string.ascii_lowercase+string.ascii_uppercase+string.punctuation+'1234567890'
        lista = random.sample(stringa,int(lunghezza))
        pw = ''.join([str(elem) for elem in lista])     # da lista --> stringa
        return pw

    pw = p(lunghezza)
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"PASSWORD GENERATA CON SUCCESSO: \n\n{pw}")

def consiglio(update, context):
    from funzioni import frasi
    frasi = frasi()
    frase = random.choice(frasi)

    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Consiglio:")
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"{frase}")

def strength_password(update, context):
    from funzioni import forza_password
    try:
        chiave = context.args[0]
        password = forza_password(chiave)
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"La tua password ha difficoltà ---> {password}/10")
    except:
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Niente inserito!")

chiavi = []
names = []

def save_password(update, context):
    global chiavi, names
    pas = context.args[0]
    name = context.args[1]
    chiavi.append(pas)
    names.append(name)
    context.bot.send_message(chat_id=update.effective_chat.id, text='Password Salvata!')

def list_password(update, context):
    global chiavi, names
    import pyperclip
    try:
        search = context.args[0]
        x = 0
        for nome in names:
            if nome == search:
                pyperclip.copy(chiavi[x])
                context.bot.send_message(chat_id=update.effective_chat.id, text='Password copiata!')
            x += 1
    except:
        context.bot.send_message(chat_id=update.effective_chat.id, text='Scegline una: ')
        x = 0
        for nome in names:
            context.bot.send_message(chat_id=update.effective_chat.id, text=f'- {names[x]}')
            x += 1

def sito(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Eccoti il nostro sito: https://octopus-ssh.github.io/Educazione-Civica-2023/")

def info(update, context):
    text = '''
    BOT VERSION 3.0   
    Di Alessio Perfetto - Augusto Macrì - Cristian Chiarilli   
    ---------------------------------------------------                           
    Questo bot è in grado di gestire tutto il 
    progetto "Sicurezza della rete" 
    semplicemente con pochi comandi 
    messi a disposizione da noi!
    ---------------------------------------------------
    /info
    Questo comando genera le informazioni 
    che stai leggendo ora.
    ---------------------------------------------------
    /password
    Questo comando assegnato come 
    "/password <parametro>" serve a 
    generare una password casuale e 
    di lunghezza in base al parametro 
    assegnato.
    Parametri => "facile","medio","difficile"
    oppure puoi inserire un numero   
    (con medio di default)
    ---------------------------------------------------
    /protezione
    Questo comando viene usato insieme
    ad un parametro:
    "/protezione <password>" in questo
    modo ti restituirà un valore da
    0 su 10 in base alla difficoltà
    della password
    ---------------------------------------------------
    /consiglio
    Questo divertente e utile comando
    ti servirà nel caso abbia bisogno
    di un consiglio casuale su come
    o cosa proteggere nella rete
    ---------------------------------------------------
    /save <password> <nome>
    Questo comando ti permette di
    salvare una password con un
    nome scelto da te nei nostri
    "archivi"
    ---------------------------------------------------
    /list
    Questo è il continuo di "save"
    dato che ti permette di
    visualizzare tutti i nomi delle
    password salvate senza mostrare
    le password stesse!

    Per selezionarne una, basta solo
    fare: "/list <nome>" e verrà
    automaticamente copiata nei
    tuoi appunti
    ---------------------------------------------------
    /sito
    Questo comando mostra il link del sito e
    descrive le informazioni del sito.
    '''
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"{text}")

def main():
    # Crea l'Updater e passa il token
    updater = Updater(TOKEN, use_context=True)

    # Recupera il dispatcher per registrare i comandi
    dp = updater.dispatcher

    # Aggiungi i comandi all'Updater
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("info", info))
    dp.add_handler(CommandHandler("password",password))
    dp.add_handler(CommandHandler("consiglio",consiglio))
    dp.add_handler(CommandHandler("protezione",strength_password))
    dp.add_handler(CommandHandler('save',save_password))
    dp.add_handler(CommandHandler('list',list_password))
    dp.add_handler(CommandHandler('sito',sito))

    # Avvia il bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
