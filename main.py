import sqlite3
import random

db_file_name = 'movies.db'


def create_db():
    with sqlite3.connect(db_file_name) as conn:
        with open('movies.sql', 'rt') as file:
            schema = file.read()
            conn.executescript(schema)


def find_movie(movie_type, genre, start_year, end_year):
    sql = f'''
        SELECT * FROM movies
        WHERE type = '{movie_type}' AND (genre LIKE '%{genre}%') AND (year >= '{start_year}' AND year <= '{end_year}');
        
    '''
    with sqlite3.connect(db_file_name) as conn:
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        if rows:
            row = random.choice(rows)
            id, name, genre, year, movie_type = row
            print(name)
        else:
            print('Ничего не найдено')


movie_type = input('Введите тип')
genre = input('Введите жанр')
year = input('Введите год')
start_year = year[:-1] + '0'
end_year = year[:-1] + '9'
find_movie(movie_type, genre, start_year, end_year)