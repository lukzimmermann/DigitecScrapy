import requests

def get_public_ip():
    try:
        response = requests.get('https://httpbin.org/ip')
        if response.status_code == 200:
            print(response.json())
            return response.json().get('origin')
        else:
            return "Failed to retrieve public IP"
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage: 109.202.196.59
public_ip = get_public_ip()
print("Your public IP address is:", public_ip)