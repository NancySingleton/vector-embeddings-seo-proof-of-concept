import ast
import csv
import annoy


def read_embeddings_file(filename):
    with open(filename) as page_embeddings_file:
        reader = csv.reader(page_embeddings_file, delimiter='|')
        return [row for row in reader]


def get_page_embeddings():
    return read_embeddings_file('step-3/step_1_output.csv')


def get_keyword_embeddings():
    return read_embeddings_file('step-3/step_2_output.csv')


def get_vector(embedding):
    return ast.literal_eval(embedding[1])


def get_new_index():
    vector_length = 1536
    return annoy.AnnoyIndex(vector_length, 'dot')


def build_embeddings_index(embeddings):
    index = get_new_index()
    for idx, embedding in enumerate(embeddings):
        index.add_item(idx, get_vector(embedding))
    index.build(10)
    return index


def get_pages_index():
    return build_embeddings_index(page_embeddings)


def get_match_for_embedding(embedding, potential_matches):
    name = embedding[0]
    match_index = page_index.get_nns_by_vector(get_vector(embedding), 1)[0]
    match_name = potential_matches[match_index][0]
    return [name, match_name]


def get_match_for_keyword(keyword_embedding):
    return get_match_for_embedding(keyword_embedding, page_embeddings)


def write_csv(filename, matches):
    with open(filename, 'w') as output_file:
        writer = csv.writer(output_file, delimiter='|', quoting=csv.QUOTE_NONE)
        for x in matches:
            writer.writerow(x)


def write_keyword_matches_csv(matches):
    write_csv('step-3/best_page_match_by_keyword.csv', matches)


page_embeddings = get_page_embeddings()
page_index = get_pages_index()

keyword_matches = [get_match_for_keyword(keyword_embedding) for keyword_embedding in get_keyword_embeddings()]
write_keyword_matches_csv(keyword_matches)