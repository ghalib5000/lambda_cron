import requests
def version():
    api = "https://api.github.com/repos/Ryujinx/release-channel-master/releases/latest"
    response_API = requests.get(api)
    return {"the current version of ryujinx is": response_API.json()["tag_name"]}