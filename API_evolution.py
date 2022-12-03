import requests

def evolution(url):
    r = requests.get(url)
    response = r.json()
    começo = response['chain']
    # POKEMON INICIAL
    first_evolution = começo['species']['name']
    
    # PRIMEIRA EVOLUÇÃO
    if len(começo['evolves_to']) == 0:
        meio_evolution = ''
    elif len(começo['evolves_to']) > 1:
        meio_evolution = []
        total = len(começo['evolves_to'])
        for vezes in range(0, total):
            inicio = começo['evolves_to'][vezes]['species']['name'] 
            meio_evolution.append(inicio)
        #meio_evolution = ','.join(meio_evolution)
        return f"{first_evolution},{meio_evolution}"
    elif len(começo['evolves_to']) == 1:
        meio_evolution = começo['evolves_to'][0]['species']['name']

    # SEGUNDA EVOLUÇÃO
    if len(começo['evolves_to']) == 0:
        evolution_finish = ''

    elif len(começo['evolves_to'][0]['evolves_to']) == 2:
        evolution_finish = []
        for vezes in range(0, 2):
            inicio = começo['evolves_to'][0]['evolves_to'][vezes]['species']['name']
            evolution_finish.append(inicio)
        evolution_finish = ', '.join(evolution_finish)
        return f"{first_evolution},{meio_evolution},{evolution_finish}"

    elif len(começo['evolves_to'][0]['evolves_to']) == 1:
        evolution_finish = começo['evolves_to'][0]['evolves_to'][0]['species']['name']
    
    else:
        evolution_finish = ''
    return f"{first_evolution},{meio_evolution},{evolution_finish}"
