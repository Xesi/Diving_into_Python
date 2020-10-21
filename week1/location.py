import requests

def get_lacation_info():
    return requests.get("https://freegeoip.app/json/").json()

if __name__ == "__main__":
    print(get_lacation_info()) 