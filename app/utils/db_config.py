import psycopg2

con = psycopg2.connect(
   database="starwars", user='postgres', password='namungoona', host='127.0.0.1', port= '5432')