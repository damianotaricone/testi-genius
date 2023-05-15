import csv
import sanremo_main
import sqlite3

with open('sanremo2020.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Titolo', 'Testo', 'Anno'])
    for i in range(len(sanremo_main.titoli2020)):
        titolo = sanremo_main.titoli2020[i]
        testo = sanremo_main.testi2020[i]
        anno = 2020
        writer.writerow([titolo, testo, anno])


# Apri il file CSV
with open('sanremo2020.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    # Connettiti al database
    conn = sqlite3.connect('sanremo.db')
    c = conn.cursor()
    # Crea la tabella 'canzoni' se non esiste già
    c.execute('''CREATE TABLE IF NOT EXISTS canzoni
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  titolo TEXT,
                  testo TEXT,
                  anno TEXT)''')
    # Leggi ogni riga del file CSV e inseriscila nella tabella 'canzoni'
    for row in reader:
        titolo = row['Titolo']
        testo = row['Testo']
        anno = '2020' # imposta l'anno fisso a 2020
        c.execute("INSERT INTO canzoni (titolo, testo, anno) VALUES (?, ?, ?)", (titolo, testo, anno))
    # Salva le modifiche e chiudi la connessione al database
    conn.commit()
    conn.close()


# Connessione al database
conn = sqlite3.connect('sanremo.db')

# Caricamento dei dati della tabella in un DataFrame
df = pd.read_sql_query("SELECT * from canzoni", conn)

# Chiusura della connessione
conn.close()

# Visualizzazione del DataFrame
print(df)






