#!/usr/bin/python3
import sys
import requests

def get_github_user_id(username, token):
    url = "https://api.github.com/user"
    headers = {"Authorization": f"token {token}"}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json().get('id')
    else:
        return None

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    user_id = get_github_user_id(username, token)
    print(user_id)
