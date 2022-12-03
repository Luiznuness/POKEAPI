import requests
from treating_evolution import result_evolution

def pokemon_species(pokemon):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon-species/{pokemon}/')
    result = response.json()
    result_evolution(result, pokemon)
    geracao_pokemon = result['generation']['name']
    color = result['color']['name']
    print(f'Geração do pokemon solicitado: {geracao_pokemon}\n')
    print(f'Cor do pokemon solicitado: {color}')
if __name__ == "__main__":
    pokemon_species('charmander')
