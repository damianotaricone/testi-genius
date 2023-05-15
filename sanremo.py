import requests
from bs4 import BeautifulSoup
import csv
import re

def get_links_in_chart_rows(url):
    # scarica la pagina web
    response = requests.get(url)
    html = response.content

    # crea un oggetto BeautifulSoup per analizzare l'HTML
    soup = BeautifulSoup(html, 'html.parser')

    # trova tutti gli elementi con la classe 'chart_row chart_row--light_border chart_row--full_bleed_left chart_row--align_baseline chart_row--no_hover'
    chart_rows = soup.find_all('div', {'class': 'chart_row chart_row--light_border chart_row--full_bleed_left chart_row--align_baseline chart_row--no_hover'})

    # estrai tutti i link all'interno degli elementi trovati
    links = []
    for row in chart_rows:
        link = row.find('a')
        if link is not None:
            links.append(link.get('href'))

    return links


def extract_lyrics(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    elements = soup.find_all(class_='Lyrics__Container-sc-1ynbvzw-5')

    lyrics = ''
    for element in elements:
        # Estrai il testo dagli elementi "div"
        for content in element.contents:
            if content.name == 'br':
                lyrics += '\n'
            elif content.name == 'i' or content.name == 'b' or content.name == 'a':
                lyrics += content.get_text()
            else:
                if callable(getattr(content, 'strip', None)):
                    lyrics += content.strip()

    # Rimuovi i tag HTML
    clean_lyrics = re.compile('<.*?>')
    lyrics = re.sub(clean_lyrics, '', lyrics)

    return lyrics


def extract_song_title(url):
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    span = soup.find('span', class_='SongHeaderdesktop__HiddenMask-sc-1effuo1-11 iMpFIj')
    if span is not None:
        title = span.text.strip()
        return title
    else:
        return None


 
def extract_lyrics_with_title(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    elements = soup.find_all(class_='Lyrics__Container-sc-1ynbvzw-5')

    lyrics = ''
    for element in elements:
        # Estrai il testo dagli elementi "div"
        for content in element.contents:
            if content.name == 'br':
                lyrics += ' '
            elif content.name == 'i' or content.name == 'b' or content.name == 'a':
                lyrics += content.get_text()
            else:
                if callable(getattr(content, 'strip', None)):
                    lyrics += content.strip()
 
    # Rimuovi i tag HTML
    clean_lyrics = re.compile('<.*?>')
    lyrics = re.sub(clean_lyrics, '', lyrics)

    # Rimuovi il testo tra parentesi quadre []
    lyrics = re.sub(r'\[.*?\]', '', lyrics)
    
     # Rimuovi "n2005"
    lyrics = lyrics.replace('\u2005', '')

    return lyrics.strip()

testo = extract_lyrics_with_title("https://genius.com/Ghali-cara-italia-lyrics")
print(testo)