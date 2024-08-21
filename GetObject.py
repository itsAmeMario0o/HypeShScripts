# Auth per https://developer.cisco.com/docs/cisco-defense-orchestrator/getting-started/#api-user-prerequisites
import json
import requests

def get_token_from_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
        return data.get('token')  # Assuming the token is under the 'token' key

def make_request(jwt_token):
    base_url = "https://edge.us.cdo.cisco.com/"
    endpoint = "api/v1/object"
    url = f"{base_url}{endpoint}"

    headers = {"Authorization": f"Bearer {jwt_token}"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        print(json.dumps(data, indent=4))
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

# Replace 'token.json' with the actual path to your JSON file
token_file = 'token1.json'
jwt_token = get_token_from_json(token_file)
make_request(jwt_token)