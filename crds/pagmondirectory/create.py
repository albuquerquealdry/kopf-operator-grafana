import kopf
import requests

def create_fn(uid, directory, url, headers,  **kwargs):
    data = {
        'title': f'{directory}',
        'uid': f'{uid}'
    }
    response = requests.post(url, headers=headers, json=data)
    return {
        "status_code": response.status_code
    }