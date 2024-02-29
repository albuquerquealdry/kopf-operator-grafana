import kopf
import requests

def delete_fn(url,uid, headers, **kwargs):
    url = f'{url}/{uid}'
    response = requests.delete(url, headers=headers)
    return {
        "status_code": response.status_code
    }