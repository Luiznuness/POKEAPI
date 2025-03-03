import requests

def evolution(url):
    # REQUEST API EVOLUTION POKEMON
    response = requests.get(url).json()
    start = response['chain']
    # POKEMON INICIAL
    first_evolution = start['species']['name']
    
    # PRIMEIRA EVOLUÇÃO
    if len(start['evolves_to']) == 0:
        meio_evolution = ''
    elif len(start['evolves_to']) > 1:
        meio_evolution = []
        total = len(start['evolves_to'])
        for vezes in range(0, total):
            inicio = start['evolves_to'][vezes]['species']['name'] 
            meio_evolution.append(inicio)
            return f"{first_evolution},{meio_evolution}"
    elif len(start['evolves_to']) == 1:
        meio_evolution = start['evolves_to'][0]['species']['name']

    # SEGUNDA EVOLUÇÃO
    if len(start['evolves_to']) == 0:
        evolution_finish = ''

    elif len(start['evolves_to'][0]['evolves_to']) == 2:
        evolution_finish = []
        for vezes in range(0, 2):
            inicio = start['evolves_to'][0]['evolves_to'][vezes]['species']['name']
            evolution_finish.append(inicio)
        evolution_finish = ', '.join(evolution_finish)
        return f"{first_evolution},{meio_evolution},{evolution_finish}"

    elif len(start['evolves_to'][0]['evolves_to']) == 1:
        evolution_finish = start['evolves_to'][0]['evolves_to'][0]['species']['name']
    
    else:
        evolution_finish = ''
    return f"{first_evolution},{meio_evolution},{evolution_finish}"
