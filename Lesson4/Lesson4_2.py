def diction(*args):
    new_dict=dict()
    for i in args:
        new_dict.update(i)
    return new_dict


a={ "Ford" : ["Mustang", "Scorpio"],
    "Opel" : ["Vectra", "Corsa"],
    "Kia"  : ["Cerato", "Ceed"],
    "Huyndai": ["Sonata", "Elantra"]}
b={ "Bmw": "i320","Mercedes":"Vito","Renault":"Megan"}
c={ "Peugeot":"208", "Tesla":"X", "MG":"i5"}

print(diction(a,b,c))

