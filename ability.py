def ability(name):
    import requests,json
    abilities=[]
    req = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(name))
    pokedata = json.loads(req.text)
    for ability in pokedata['abilities']:
        abilities.append(ability['ability']['name'])
    return abilities
