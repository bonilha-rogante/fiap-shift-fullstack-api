import requests
import json

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
    try:
        params = [
            f'q={city}',
            'appid=5796abbde9106b7da4febfae8c44c232',
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
    
    except Exception as e:
        print(f'Error: {e}')

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