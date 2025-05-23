# Atividade 
# key 70ff152a767d6fb87937ad1b7ef57db9
# - Consumir a API OpenWeatherMap
# - Criar um app para exibir a temperatura
# 'https://api.openweathermap.org/data/2.5/find?q={cidade}&appid=5796abbde9106b7da4febfae8c44c232&units=metric'



import requests
import json
import os

from dotenv import load_dotenv

load_dotenv()

def temperature(cidade):
    key = str(os.getenv('API_KEY'))
    params = [
        f'q={cidade}',
        f'appid={key}',
        'units=metric'
    ]
    
    formatted_params = "&".join(params)
    
    response = requests.get(f'https://api.openweathermap.org/data/2.5/find?{formatted_params}',
    timeout=30,                        
    )
    
    response_data = response.json()
    print(response_data)
    print(response_data.get('list'))
    
    forecast_list = response_data.get("list", [])
    
    if len(forecast_list) == 0:
        return None
    
    return forecast_list[0]


def main():
    cidade = input("Digite o nome da cidade: ")
    temperatura = temperature(cidade)
    
    if temperatura == None:
        print("Invelizmente não foi possível consultar a temperatura")
        return
    
    # temperatura = temperatura.get("main").get("temp")
    temperatura = temperatura.get('list')
    print(temperatura)

if __name__ == "__main__":
    main()