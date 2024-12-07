import annoy

VECTOR_LENGTH = 1536


def build_index(embeddings):
    index = annoy.AnnoyIndex(VECTOR_LENGTH, 'dot')

    for idx, embedding in enumerate(embeddings):
        index.add_item(idx, embedding[1])

    index.build(10)
    return index


def get_best_match(embedding, potential_matches):
    item_name = embedding[0]
    item_vector = embedding[1]

    index_of_potential_matches = build_index(potential_matches)

    idx_of_best_match = index_of_potential_matches.get_nns_by_vector(item_vector, 1)[0]
    best_match_name = potential_matches[idx_of_best_match][0]

    return [item_name, best_match_name]