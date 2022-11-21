import requests
import evolucao_pokemon
def pokemon(name):    
    r = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}/')
    print(r.status_code)
    response = r.json()
    name = response['name']
    id = response['id']
    experiencia = response['base_experience']
    a = response['species']['url']
    print(f'Name: {name[0]}\n')
    status = response["stats"]
    for f in status:
        print(f'{f["stat"]["name"].upper()}')
        print(f'base_stat: {f["base_stat"]}, effort: {f["effort"]}\n')    
    evolucao_pokemon.verificacao_evolucao(name)

if __name__ == "__main__":
    pokemon('zapdos')

