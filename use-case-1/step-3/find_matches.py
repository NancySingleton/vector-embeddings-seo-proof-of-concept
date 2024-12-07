import ast
from utils.csv_helper import read, write
from utils.matching_helper import get_best_match

PREFIX = 'use-case-1/step-3/'
PAGE_EMBEDDINGS_FILE = PREFIX + 'step_1_output.csv'
KEYWORDS_EMBEDDINGS_FILE = PREFIX + 'step_2_output.csv'
PAGE_MATCH_BY_KEYWORD_FILE = PREFIX + 'best_page_match_by_keyword.csv'
KEYWORD_MATCH_BY_PAGE_FILE = PREFIX + 'best_keyword_match_by_page.csv'


def read_embeddings(filename):
    return [[e[0], ast.literal_eval(e[1])] for e in read(filename)]


page_embeddings = read_embeddings(PAGE_EMBEDDINGS_FILE)
keyword_embeddings = read_embeddings(KEYWORDS_EMBEDDINGS_FILE)

page_matches_by_keyword = [get_best_match(keyword_embedding, page_embeddings) for keyword_embedding in keyword_embeddings]
write(PAGE_MATCH_BY_KEYWORD_FILE, page_matches_by_keyword)

keyword_matches_by_page = [get_best_match(page_embedding, keyword_embeddings) for page_embedding in page_embeddings]
write(KEYWORD_MATCH_BY_PAGE_FILE, keyword_matches_by_page)