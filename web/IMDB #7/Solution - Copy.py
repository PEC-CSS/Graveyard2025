from bs4 import BeautifulSoup
import pandas as pd
import os
import json
from difflib import get_close_matches
import re

html_file = r"C:\Users\Naman Vasudev\Desktop\Web Scrapping Tutorial\IMDB TOP 250 (2).html"   ## ADD YOUR FILE PATH, OTHERWISE IT WILL SHOW ERROR
json_file = r"C:\Users\Naman Vasudev\Desktop\Web Scrapping Tutorial\IMDB TOP 250.json"
# ADD YOUR FILE PATH, otherise error will be shown

with open(html_file, 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

with open(json_file, 'r', encoding='utf-8') as file:
    json_data = json.load(file)
movie_containers = soup.find_all('li', class_='ipc-metadata-list-summary-item')
data = []
json_genres = {}
for item in json_data['props']['pageProps']['pageData']['chartTitles']['edges']:
    title = item['node']['titleText']['text'].strip().lower()
    genres = [genre['genre']['text'].strip().lower() for genre in item['node']['titleGenres']['genres']]
    json_genres[title] = genres

for movie in movie_containers:
    
    title_tag = movie.find('h3', class_='ipc-title__text')
    title = title_tag.text.strip() if title_tag else 'N/A'
    title = re.sub(r'^\d+\.\s*', '', title)
    title_lower = title.lower()
    
    
    year_tag = movie.find('span', class_='sc-d5ea4b9d-7 URyjV dli-title-metadata-item')
    year = year_tag.text.strip() if year_tag else 'N/A'
    
    
    director_tag = movie.find('span', string='Director')
    director = director_tag.find_next('a').text.strip() if director_tag else 'N/A'
    
    
    actors = []
    actors_tag = movie.find('span', string='Stars')
    if actors_tag:
        actor_links = actors_tag.find_all_next('a', class_='ipc-link')[:3]
        actors = [actor.text.strip() for actor in actor_links]
    

    rating_tag = movie.find('span', class_='ipc-rating-star')
    rating_text = rating_tag.text.strip() if rating_tag else '0.0'
    rating_match = re.search(r'\d+\.\d+', rating_text)
    rating = float(rating_match.group()) if rating_match else 0.0
    
    
    matched_title = get_close_matches(title_lower, json_genres.keys(), n=1, cutoff=0.7)
    genre_list = json_genres.get(matched_title[0], ['Controversy (Search Web)']) if matched_title else ['Controversy (Search Web)']
    
    data.append([title, year, director, ', '.join(actors), rating, genre_list])


save_dir = r"C:\Users\Naman Vasudev\Desktop\Web Scrapping Tutorial"
os.makedirs(save_dir, exist_ok=True)
excel_filename = os.path.join(save_dir, 'imdb_top250.xlsx')

df = pd.DataFrame(data, columns=['Title', 'Year', 'Director', 'Stars', 'Rating', 'Genre'])
df.to_excel(excel_filename, index=False)

print("Top 250 IMDb movies are created as an Excel file.")


filter_type = input("Choose filter type (Actor, Director, or Genre (Case, Spaces, Spelling Sensitive)): ").strip().lower()
filter_value = input(f"Enter {filter_type} name: ").strip().lower()


valid_filter_types = {
    "actor": "Stars",
    "director": "Director",
    "genre": "Genre"
}

if filter_type not in valid_filter_types:
    print("Invalid filter type! Please choose Actor, Director, or Genre.")
    exit()

column_name = valid_filter_types[filter_type]

if filter_type == "genre":
    filtered_df = df[df[column_name].apply(lambda genres: any(filter_value in g.lower() for g in genres))]
else:
    filtered_df = df[df[column_name].str.lower().str.contains(filter_value)]

M = min(int(input("Enter the number of top movies to display (M): ")), len(filtered_df))

filtered_df = filtered_df.sort_values(by='Rating', ascending=False).head(M)
print(filtered_df[['Title', 'Rating']].to_string(index=False))