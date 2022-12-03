import requests
from treating_evolution import tratamento_evolution, result_evolution

def pokemon_species(pokemon):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon-species/{pokemon}/')
    result = response.json()
    result_evolution(result, pokemon)
    

if __name__ == "__main__":
    pokemon_species('froakie')
