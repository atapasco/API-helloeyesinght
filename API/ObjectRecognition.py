import requests
import json
API_TOKEN = "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"
API_URL = "https://api-inference.huggingface.co/models/google/vit-base-patch16-224"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.request("POST", API_URL, headers=headers, data=data)
    objeto = json.loads(response.content.decode("utf-8"))
    objeto = objeto[0]['label']
    print(objeto)
    objeto = {"objeto": str(objeto)}
    return objeto

#output = query("tasa.jpg")
#print(output)