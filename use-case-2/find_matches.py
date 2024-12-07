from utils.csv_helper import read, write
from utils.embedding_helper import embed_text
from utils.matching_helper import get_best_matches

PREFIX = 'use-case-2/'
REQUIRED_FILE = PREFIX + 'required.csv'
EXISTING_FILE = PREFIX + 'existing.csv'
OUTPUT_FILE = PREFIX + 'best_existing_match_by_required_item.csv'


def get_embeddings_from_csv(filename):
    return [[row[0], embed_text(row[0])] for row in read(filename)]


embeddings_for_required_items = get_embeddings_from_csv(REQUIRED_FILE)
embeddings_for_existing_items = get_embeddings_from_csv(EXISTING_FILE)

best_existing_match_for_each_required_item = [get_best_matches(req, embeddings_for_existing_items, 5) for req in embeddings_for_required_items]
write(OUTPUT_FILE, best_existing_match_for_each_required_item)