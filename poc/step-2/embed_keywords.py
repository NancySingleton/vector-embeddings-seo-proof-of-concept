from utils.csv_helper import read, write
from utils.embedding_helper import embed_text

INPUT_FILE = 'poc/step-2/keywords_input.csv'
OUTPUT_FILE = 'poc/step-2/embedded_keywords.csv'

embedded_keywords = [[row[0], embed_text(row[0])] for row in read(INPUT_FILE)]
write(OUTPUT_FILE, embedded_keywords)
