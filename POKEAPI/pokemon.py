import requests
from POKEAPI.treating_evolution import result_evolution

def pokemon_species(pokemon):
    # REQUEST API POKEMON
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon-species/{pokemon}/').json()
    # Função que procura as evoluções do pokemon solicitado
    result_evolution(response, pokemon)
    geracao_pokemon = response['generation']['name']
    color = response['color']['name']
    print(f'\nGeração do pokemon solicitado: {geracao_pokemon}')
    print(f'\nCor do pokemon solicitado: {color}\n')