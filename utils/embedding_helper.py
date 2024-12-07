import requests

OPENAI_API_KEY = "<YOUR_API_KEY>"


def embed_text(keyword):
    url = 'https://api.openai.com/v1/embeddings'
    auth_header = {'Authorization': 'Bearer ' + OPENAI_API_KEY}
    request_body = {
        'model': 'text-embedding-3-small',
        'input': keyword,
        'encoding_format': 'float'
    }
    r = requests.post(url, headers=auth_header, json=request_body)
    return r.json()['data'][0]['embedding']
