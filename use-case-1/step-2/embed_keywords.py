from utils.csv_helper import read, write
from utils.embedding_helper import embed_text

PREFIX = 'use-case-1/step-2/'
INPUT_FILE = PREFIX + 'keywords_input.csv'
OUTPUT_FILE = PREFIX + 'use-case-1/step-2/embedded_keywords.csv'

embedded_keywords = [[row[0], embed_text(row[0])] for row in read(INPUT_FILE)]
write(OUTPUT_FILE, embedded_keywords)
