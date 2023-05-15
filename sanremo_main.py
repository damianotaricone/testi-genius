from sanremo import get_links_in_chart_rows
from sanremo import extract_lyrics
from sanremo import extract_song_title

#SAN REMO 2020
url2020 = "https://genius.com/albums/Festival-di-sanremo/Festival-di-sanremo-2020"
link2020 = []
link2020 = get_links_in_chart_rows(url2020)

testi2020 = []
for link in link2020:
    testi2020.append(extract_lyrics(link))

titoli2020 = []
for link in link2020:
    titoli2020.append(extract_song_title(link))


#SAN REMO 2021
url2021 = "https://genius.com/albums/Festival-di-sanremo/Festival-di-sanremo-2021"
link2021 = []
link2021 = get_links_in_chart_rows(url2021)

testi2021 = []
for link in link2021:
    testi2021.append(extract_lyrics(link))

titoli2021 = []
for link in link2021:
    titoli2021.append(extract_song_title(link))


#SAN REMO 2022
url2022 = "https://genius.com/albums/Festival-di-sanremo/Festival-di-sanremo-2022"
link2022 = []
link2022 = get_links_in_chart_rows(url2022)

testi2022 = []
for link in link2022:
    testi2022.append(extract_lyrics(link))

titoli2022 = []
for link in link2022:
    titoli2022.append(extract_song_title(link))


#SAN REMO 2023
url2023 = "https://genius.com/albums/Festival-di-sanremo/Festival-di-sanremo-2023"
link2023 = []
link2023 = get_links_in_chart_rows(url2023)

testi2023 = []
for link in link2023:
    testi2023.append(extract_lyrics(link))

titoli2023 = []
for link in link2023:
    titoli2021.append(extract_song_title(link))


print("ciao")