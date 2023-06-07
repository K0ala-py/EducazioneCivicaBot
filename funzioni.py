from password_strength import PasswordStats

def frasi():
    frasi = ["Utilizzare una password complessa e unica per ogni account.",
    "Tenere il software del computer e dei dispositivi mobile sempre aggiornato.",
    "Utilizzare un software di sicurezza per proteggere il computer da malware e virus.",
    "Non cliccare su link sospetti o aprire allegati di posta elettronica da mittenti sconosciuti.",
    "Utilizzare una connessione internet sicura, ad esempio una connessione VPN.",
    "Non utilizzare reti Wi-Fi pubbliche non protette.",
    "Utilizzare la crittografia per proteggere i dati sensibili.",
    "Fare il backup dei dati importanti.",
    "Utilizzare un firewall per proteggere il computer dalle intrusioni esterne.",
    "Non condividere informazioni personali con siti web o servizi sconosciuti.",
    "Utilizzare la verifica in due passaggi per gli account importanti.",
    "Utilizzare un software di gestione delle password per generare e memorizzare password sicure.",
    "Non utilizzare la stessa password per più account.",
    "Utilizzare un software di controllo genitori per proteggere i bambini dai contenuti pericolosi in rete.",
    "Utilizzare un software di controllo delle applicazioni per limitare l'accesso ai dati del computer.",
    "Utilizzare un software di sicurezza mobile per proteggere i dispositivi mobile dalle minacce.",
    "Utilizzare un software di pulizia del sistema per rimuovere i file temporanei e i cookie dal computer.",
    "Utilizzare un software di crittografia dei dati per proteggere i dati sensibili sui dispositivi mobile.",
    "Utilizzare un software di sicurezza per la posta elettronica per proteggere la posta elettronica dalle minacce.",
    "Utilizzare un software di sicurezza per il browser per proteggere il browser dalle minacce.",
    "Utilizzare un software di sicurezza per il cloud per proteggere i dati nel cloud.",
    "Utilizzare un software di sicurezza per la rete domestica per proteggere la rete domestica dalle minacce.",
    "Utilizzare un software di sicurezza per i dispositivi IoT per proteggere i dispositivi IoT dalle minacce.",
    "Utilizzare un software di sicurezza per i dispositivi di archiviazione esterni per proteggere i dati sui dispositivi di archiviazione esterni."]
    return frasi

def text_start():
    text = '''Ciao, Benvenuto in questo Bot!
    \nQuesto bot è in grado di fornire funzioni e siti creati da noi!
    \nEcco i comandi disponibili:\n-------------------------------------------
    /info --> ottieni tutte le info sul Bot!
    /password <parametro> --> Genera una
    password in base al parametro 
    (facile,medio,difficile)
    /protezione <password> --> ti da la 
    possibilità di verificare la 
    difficoltà di una password inserita
    /consiglio --> genera un consiglio casuale 
    sulla rete!
    /save <password> <nome> --> salva una
    password con il relativo nome
    /list --> mostra il nome di
    tutte le password salvate
    /sito --> link del sito
    '''
    return text

def forza_password(passoword):
    stats = PasswordStats(passoword)
    parola = str(round(stats.strength()*10,1))
    return parola
