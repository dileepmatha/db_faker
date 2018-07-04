import psycopg2
from faker import Faker
from psycopg2.extensions import AsIs
import random
import json
import sys
fake = Faker()
db_name = sys.argv[1]
table_name = sys.argv[2]
n =  int(sys.argv[3])
conn = psycopg2.connect(host='localhost', user='postgres', password='password', dbname=db_name, port = 5432)
cursor = conn.cursor()
# cursor.execute("""CREATE TABLE actdb (text_field VARCHAR(255) NOT NULL,extra TEXT NOT NULL, explain jsonb NOT NULL, points integer NOT NULL, question_type VARCHAR(70) NOT NULL, display_type VARCHAR(70) NOT NULL,time_alloated INTEGER NOT NULL, options jsonb NOT NULL, answers jsonb NOT NULL)""")
for i in range(n):
	text_field = fake.sentence()
	extra = fake.paragraph(nb_sentences=15, ext_word_list=None)
	points = random.randint(1,51)
	if i%2 is 0:
		question_type = 'Multiple Choice'
	else:
		question_type = 'Multiple Answer'
	if i%2 is 0:
		display_type = 'Postion1'
	else:
		display_type = 'Postion2'
	time_alloated = random.randint(1,151)
	explain = {}
	explain['explanation'] = fake.sentence()
	explain = json.dumps(explain)
	arr = []
	options = {}
	arr.append(fake.word())
	arr.append(fake.word())
	arr.append(fake.word())
	arr.append(fake.word())
	options['options'] = arr
	options = json.dumps(options)
	arr.clear()
	answers = {}
	arr.append(fake.word())
	arr.append(fake.word())
	answers['answers'] = arr
	answers = json.dumps(answers)
	arr.clear()
	cursor.execute("INSERT INTO %s VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s);", (AsIs(table_name), text_field, extra,explain, points, question_type, display_type, time_alloated, options, answers,))
conn.commit()
conn.close()