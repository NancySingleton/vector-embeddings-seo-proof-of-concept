from utils.csv_helper import read, write
from utils.matching_helper import get_best_match

PAGE_EMBEDDINGS_FILE = 'poc/step-3/step_1_output.csv'
KEYWORDS_EMBEDDINGS_FILE = 'poc/step-3/step_2_output.csv'
PAGE_MATCH_BY_KEYWORD_FILE = 'poc/step-3/best_page_match_by_keyword.csv'
KEYWORD_MATCH_BY_PAGE_FILE = 'poc/step-3/best_keyword_match_by_page.csv'

page_embeddings = read(PAGE_EMBEDDINGS_FILE)
keyword_embeddings = read(KEYWORDS_EMBEDDINGS_FILE)

page_matches_by_keyword = [get_best_match(keyword_embedding, page_embeddings) for keyword_embedding in keyword_embeddings]
write(PAGE_MATCH_BY_KEYWORD_FILE, page_matches_by_keyword)

keyword_matches_by_page = [get_best_match(page_embedding, keyword_embeddings) for page_embedding in page_embeddings]
write(KEYWORD_MATCH_BY_PAGE_FILE, keyword_matches_by_page)