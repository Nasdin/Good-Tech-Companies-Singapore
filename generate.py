def make_table_headers(headers):
    header_titles = "| " + " | ".join(headers) + " |"
    word_lengths = [len(header) for header in headers]
    word_lengths[3] = 30  # Special case for index 3 because this belongs to image, which we want to widen
    table_structure = "|" + "|".join("-" * word_length for word_length in word_lengths) + '|'

    return header_titles + '\n' + table_structure
