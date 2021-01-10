import PySimpleGUI as sg
import requests, json

sg.theme('DarkAmber')

# Define the window's contents
layout = [[sg.Text("What's the name of the pokemon?")],
          [sg.Input(key='-INPUT-')],
          [sg.Button('Ok'), sg.Button('Quit')]]

# Create the window
window = sg.Window('Pokedex', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        window.close()
        break
    elif event == 'Ok':        
        try:
            pokename = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(values['-INPUT-']))
            pokedata = json.loads(pokename.text)
    
            poketype = pokedata['types'][0]['type']['name']

            sg.Print('{} type'.format(poketype))
    
            req = requests.get(pokedata['types'][0]['type']['url'])
            damage_data = json.loads(req.text)
            double_damage = damage_data['damage_relations']['double_damage_from']
            sg.Print('{} takes double damage from these types of pokemon'.format(values['-INPUT-']),text_color='white')
            for damage in double_damage:
                sg.Print(damage['name'])
        
            for elements in double_damage:
                url = elements['url']
                req = requests.get(url)
                double_damage_data = json.loads(req.text)
                sg.Print('{} takes double damage from these {} pokemon'.format(values['-INPUT-'], elements['name']),text_color='white')
                for i in range(5):
                    sg.Print(double_damage_data['pokemon'][i]['pokemon']['name'])
            
            sg.Print("{}'s abilities".format(values['-INPUT-']),text_color='white')
            for ability in pokedata['abilities']:
                sg.Print(ability['ability']['name'])
        except Exception as exc:
            sg.Print('{} does not exist. Try again'.format(values['-INPUT-']))
                 
