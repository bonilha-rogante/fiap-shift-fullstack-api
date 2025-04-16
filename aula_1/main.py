import requests
import json

def list_users():
    try:
        response = requests.get(
            "https://jsonplaceholder.typicode.com/users",
            timeout=30,
        )
        
        if response.status_code != 200:
            raise RuntimeError(f"Status code não esperado: {response.status_code}")

        response_data = response.json()

        # print(f"Status Code:  {response.status_code}")
        # print(f"Content: {response.content}")
        # print(f"Content (text): {response.text}")
        # print(response_data)
        # print(response_data[0].get("username"))
        return response_data
    except Exception as exception:
        print(f"Ooops! Deu erro: {str(exception)}")
        return []

def main():
    users = list_users()
    
    print("Lista de usuários")
    
    for user in users:
        print(f' - {user.get('name')} ({user.get('email')})')
        # print(json.dumps(users, indent=2))

if __name__ == "__main__":
    main()