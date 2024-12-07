import annoy

VECTOR_LENGTH = 1536


def build_index(embeddings):
    index = annoy.AnnoyIndex(VECTOR_LENGTH, 'dot')

    for idx, embedding in enumerate(embeddings):
        index.add_item(idx, embedding[1])

    index.build(10)
    return index


def get_best_match(embedding, potential_matches):
    matches = get_best_matches(embedding, potential_matches, 1)
    return [matches[0], matches[1][0]]


def get_best_matches(embedding, potential_matches, number):
    item_name = embedding[0]
    item_vector = embedding[1]

    index_of_potential_matches = build_index(potential_matches)

    indexes_of_best_matches = index_of_potential_matches.get_nns_by_vector(item_vector, number)
    best_match_names = [potential_matches[idx][0] for idx in indexes_of_best_matches]

    return [item_name, best_match_names]