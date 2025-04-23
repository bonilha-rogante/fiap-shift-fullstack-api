import requests
import json
import os

from dotenv import load_dotenv

load_dotenv()

def get_cep(cep: str):
    try:
        response = requests.get(f'https://viacep.com.br/ws/{cep}/json/', 
                    timeout=30,
            )
        
        if response.status_code != 200:
            raise RuntimeError(f"Status code não esperado: {response.status_code}")
        
        response_data = response.json()
        return response_data
    except Exception as e:
        print(f'Error: {e}')
        return []


def get_temp(city: str):
    key = str(os.getenv('API_KEY'))
    params = [
        f'q={city}',
        f'appid={key}',
        'units=metric'
    ]
        
    formatted_params = '&'.join(params)
        
    response = requests.get(f'https://api.openweathermap.org/data/2.5/find?{formatted_params}',
        timeout=30,
        )
    
    if response.status_code != 200:
        raise RuntimeError(f'Status code não esperado: {response.status_code}')
    
    response_data = response.json()
    
    forecast_list = response_data.get('list', [])
    
    if len(forecast_list) == 0:
        return None
    
    return forecast_list[0]
    

def main():
    cep = input(f'Digite seu CEP sem hífen "-": ')
    localidade = get_cep(cep)
    localidade = localidade.get('localidade')
    
    temperature = get_temp(localidade)
    temperature = temperature.get('main').get('temp')
    # print(temperature)
    
    print(f'A temperatura na Cidade: {localidade}, é de {temperature}')

if __name__ == '__main__':
    main()