import csv
import requests

OPENAI_API_KEY = "<YOUR_API_KEY>"


def get_keywords():
    with open('step-2/keywords_input.csv') as keywords_file:
        reader = csv.reader(keywords_file)
        return [row[0] for row in reader]


def embed_keyword(keyword):
    url = 'https://api.openai.com/v1/embeddings'
    auth_header = {'Authorization': 'Bearer ' + OPENAI_API_KEY}
    request_body = {
        'model': 'text-embedding-3-small',
        'input': keyword,
        'encoding_format': 'float'
    }
    r = requests.post(url, headers=auth_header, json=request_body)
    return r.json()['data'][0]['embedding']


def write_embedded_keywords_csv(keywords):
    with open('step-2/embedded_keywords.csv', 'w') as output_file:
        writer = csv.writer(output_file, delimiter='|', quoting=csv.QUOTE_NONE)
        for x in keywords:
            writer.writerow(x)


embedded_keywords = [[keyword, embed_keyword(keyword)] for keyword in get_keywords()]
write_embedded_keywords_csv(embedded_keywords)
