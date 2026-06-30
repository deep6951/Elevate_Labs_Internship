import requests

API_KEY = "a8953ef1336cffdc627d3562cfae43a811ea0227eebecb33a9db5bdd5ba0db68159695103e6aaaaa"

def check_ip(ip):

    url = "https://api.abuseipdb.com/api/v2/check"

    headers = {
        "Key": API_KEY,
        "Accept": "application/json"
    }

    params = {
        "ipAddress": ip,
        "maxAgeInDays": 90
    }

    response = requests.get(
        url,
        headers=headers,
        params=params
    )

    return response.json()