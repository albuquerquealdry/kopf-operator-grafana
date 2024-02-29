import requests

def create_ds(url, headers, name, server, uid, team, labels, directory):
    dashboard_payload = {
      "dashboard": {
        "id": None,
        "uid": None,
        "title": f"{team}/{name}",
        "tags": [ labels ],
        "timezone": "browser",
        "schemaVersion": 16,
        "refresh": "25s"
        },
        "folderUid": directory,
        "message": "Made changes to xyz",
        "overwrite": False
}
    response = requests.post(url, headers=headers, json=dashboard_payload)
    if response.status_code == 200:
        print("Dashboard criado com sucesso!")
    else:
        print(f"Falha ao criar o dashboard. Status code: {response.status_code}")
        print(response.text)
