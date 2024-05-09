import requests

def check_ip(ip_a, api_key):
    url = f"https://otx.alienvault.com/api/v1/indicators/IPv4/{ip_a}/general"
    heads = {"X-OTX-API-KEY": api_key}

    try:
        response = requests.get(url, heads=heads)
        response.raise_for_status()
        data = response.json()
        
        if 'pulse_info' in data:
            return True, data['pulse_info']['count']
        else:
            return False, 0
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return False, 0


api_key = 'a64e2e0462f526d9f440a94be83fbe67c6f1723331b897a0f5768ce21308fcbb'
ip_a = input("Enter the IP address to check: ")

is_mal, count = check_ip(ip_a, api_key)

if is_mal:
    print(f"The IP address {ip_a} is malicious, found in {count} threat reports.")
else:
    print(f"The IP address {ip_a} is not malicious.")