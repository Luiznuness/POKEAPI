import requests
from API_evolution import evolution

def todas_evolucoes(lista):
    while True:
            evolucao_pokemon = str(input('Deseja saber todas as evoluções? ')).upper()[0]
            if evolucao_pokemon == 'S':
                if lista[-1] == '':
                    del lista[-1]
                    print('Este pokemon só possui uma evolução')
                    print(f'{lista[-1]}')
                break
            elif evolucao_pokemon == 'N':
                break
            else:
                print('Desculpa, não entendi tente novamente')

def tratamento_evolution(lista, pokemon):
    pokemon_select = pokemon
    lista_pokemon = lista
    if lista_pokemon[1] == '' and lista_pokemon[2] == '':
        return 'Pokemon não possui evoluções'
    elif len(lista_pokemon) > 4:
        print('Este pokemon é um pokemon inicial e tem muitas evoluções')
        result = todas_evolucoes(lista_pokemon)
        return result
    elif len(lista_pokemon) == 3:
        indici = lista_pokemon.index(pokemon)
        if indici == 0:
            print('Este é um pokemon inicial')
            result = todas_evolucoes(lista_pokemon)
            return result
        elif indici == 1:
            print(f'Pokemon evoluido de {lista_pokemon[0]}')
            result = todas_evolucoes(lista_pokemon)
            return result
        else:
            result = todas_evolucoes(lista_pokemon)
            return result
    elif len(lista_pokemon) == 4:
        print('Este pokemon tem dois ultimas evoluções ou seja dependendo do clima ele evolui para um pokemon')
        while True:
            evolucao_pokemon = str(input('Deseja saber todas as evoluções? ')).upper()[0]
            if evolucao_pokemon == 'S':
                return f'{lista_pokemon[1]}, ({lista_pokemon[2]} - {lista_pokemon[3]})'
            elif evolucao_pokemon == 'N':
                break
            else:
                print('Desculpa, não entendi tente novamente')
    

def alguma_coisa(pokemon):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon-species/{pokemon}/')
    result = response.json()
    evolucao = result['evolution_chain']['url']
    teste_result = evolution(evolucao)
    teste_result = ''.join(teste_result)
    lista_evolution = teste_result.split(',')
    result_tratamento = tratamento_evolution(lista_evolution, pokemon)
    if result_tratamento != None:
        print(result_tratamento)

if __name__ == "__main__":
    alguma_coisa('froakie')
