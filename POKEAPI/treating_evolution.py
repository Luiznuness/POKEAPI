from POKEAPI.API_evolution import evolution

def todas_evolucoes(lista):
    del lista[0]
    while True:
        evolucao_pokemon = str(input('\nDeseja saber todas as evoluções? ')).upper()[0]
        print('\n')
        if evolucao_pokemon == 'S':
            if lista[-1] == '':
                del lista[-1]
                print('Este pokemon só possui uma evolução')
                print(f'{lista[-1]}')
                break
            else:
                for pokemon in lista:
                    print(pokemon)
                break
        elif evolucao_pokemon == 'N':
            break
        else:
            print('Desculpa, não entendi tente novamente')


def tratamento_evolution(lista, pokemon):
    lista_pokemon = lista
    if lista_pokemon[1] == '' and lista_pokemon[2] == '':
        return 'Pokemon não possui evoluções'
    elif len(lista_pokemon) > 4:
        print('Este pokemon é um pokemon inicial e tem muitas evoluções')
        todas_evolucoes(lista_pokemon)
        return
    elif len(lista_pokemon) == 3:
        indici = lista_pokemon.index(pokemon)
        if indici == 0:
            print('Este é um pokemon inicial')
            todas_evolucoes(lista_pokemon)
            return
        elif indici == 1:
            print(f'Pokemon evoluido de {lista_pokemon[0]}')
            todas_evolucoes(lista_pokemon)
            return
        else:
            todas_evolucoes(lista_pokemon)
            return
    elif len(lista_pokemon) == 4:
        print('Este pokemon tem dois tipos de evoluções ou seja dependendo do clima ele evolui para um pokemon')
        while True:
            evolucao_pokemon = str(input('Deseja saber todas as evoluções? ')).upper()[0]
            if evolucao_pokemon == 'S':
                print(f'{lista_pokemon[1]}, ({lista_pokemon[2]} - {lista_pokemon[3]})')
            elif evolucao_pokemon == 'N':
                break
            else:
                print('Desculpa, não entendi tente novamente')

def result_evolution(result, pokemon):
    # Encontra a URL para fazer o request para achar as evoluções
    evolucao = result['evolution_chain']['url']
    # Função para encontrar as evoluções do pokemon
    result_evolution = evolution(evolucao) # Retorna as evoluções do pokemon
    lista_evolution = result_evolution.split(',')
    tratamento_evolution(lista_evolution, pokemon)