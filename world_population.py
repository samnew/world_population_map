import json
from country_codes import get_country_code
from pygal.maps.world import World
from pygal.style import RotateStyle as RS
from pygal.style import LightStyle as LS

filename = 'population.json'
with open(filename) as f:
    pop_data = json.load(f)

cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2015':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        #print(country_name + ": " + str(population))
        code = get_country_code(country_name)
        if code:
            #print(code + ": " + str(population))
            cc_populations[code] = population
        # else:
        #     print('ERROR - ' + country_name)
cc_pops_1, cc_pops_2, cc_pops_3 = {},{},{}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop
#print(len(cc_pops_1), len(cc_pops_2),len(cc_pops_3))


wm_style = RS('#336699', base_style=LS)
#wm_style = LightStyle
wm = World(style=wm_style)
wm.title ="World Population in 2015, by Country"
#wm.add('2015',cc_populations)
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn',cc_pops_2)
wm.add('>1bn',cc_pops_3)

wm.render_to_file('world_population.svg')