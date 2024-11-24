import ast
import csv
import annoy


def get_page_embeddings():
    with open('step-3/step_1_output.csv') as page_embeddings_file:
        reader = csv.reader(page_embeddings_file, delimiter='|')
        return [row for row in reader]


def get_keyword_embeddings():
    with open('step-3/step_2_output.csv') as keyword_embeddings_file:
        reader = csv.reader(keyword_embeddings_file, delimiter='|')
        return [row for row in reader]


def get_vector(embedding):
    return ast.literal_eval(embedding[1])


def get_index():
    vector_length = 1536
    return annoy.AnnoyIndex(vector_length, 'euclidean')


def get_pages_index(page_embeddings):
    index = get_index()
    for idx, page_embedding in enumerate(page_embeddings):
        index.add_item(idx, get_vector(page_embedding))
    index.build(10)
    return index


def get_match_for_keyword(keyword_embedding):
    keyword = keyword_embedding[0]
    nearest_neighbour_idx = index.get_nns_by_vector(get_vector(keyword_embedding), 1)[0]
    nearest_neighbour = page_embeddings[nearest_neighbour_idx][0]
    return [keyword, nearest_neighbour]


def write_matches_csv(matches):
    with open('step-3/matches.csv', 'w') as output_file:
        writer = csv.writer(output_file, delimiter='|', quoting=csv.QUOTE_NONE)
        for x in matches:
            writer.writerow(x)


page_embeddings = get_page_embeddings()
index = get_pages_index(page_embeddings)

matches = [get_match_for_keyword(keyword_embedding) for keyword_embedding in get_keyword_embeddings()]
write_matches_csv(matches)
