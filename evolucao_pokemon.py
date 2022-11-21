import Pokemons
def verificacao_evolucao(pokemon):
    dict_pokemons = Pokemons.pokemons()
    verification = pokemon in dict_pokemons
    if verification == False:
        for key, value in dict_pokemons.items():
            for values in value:
                if pokemon == values:
                    print('pokemon encontrado')
                    key_pokemon = key
       
        result = dict_pokemons[key_pokemon]
        if result[1] == '' and result[0] != '':
            return print(f'Pokemon inicial: {key_pokemon}\nPrimeira evolução: {result[0]}')
        elif result[0] == '' and result[1] == '':
            return print(f'Pokemon inicial: {key_pokemon}\nEste pokemon não possui evoluções')
        elif len(result) > 2:
            return print(f'Pokemon inicial: {key_pokemon}\nEste pokemon possui mais de duas evoluções são elas: {result}')
        else:
            return print(f'Pokemon inicial: {key_pokemon}\nPrimeira evolução: {result[0]}\nSegunda evolução: {result[1]}')
    else:
        result = dict_pokemons[pokemon]
        if result[1] == '' and result[0] != '':
            return print(f'Pokemon inicial: {pokemon}\nPrimeira evolução: {result[0]}')
        elif result[0] == '' and result[1] == '':
            return print(f'Pokemon inicial: {pokemon}\nEste pokemon não possui evoluções')
        elif len(result) > 2:
            return print(f'Pokemon inicial: {pokemon}\nEste pokemon possui mais de duas evoluções são elas: {result}')
        else:
            return print(f'Pokemon inicial: {pokemon}\nPrimeira evolução: {result[0]}\nSegunda evolução: {result[1]}')
