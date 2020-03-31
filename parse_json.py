import re
import json, csv

def toCSV(name_list):
    with open('table_recipe.csv', 'w', encoding='utf-8', newline='') as file :
        csvfile = csv.writer(file)
        for row in name_list:
            csvfile.writerow(row)

food = []
ingredients = []
recipess = []

with open('recipe.json', 'r', encoding='utf-8-sig') as recipe :
    json_data = json.load(recipe)
    for data in json_data:
        # table_FOOD
        food.append([
            data['name'], 
            data['img'], 
            data['summary'], 
            data['info']['info2'],
            data['info']['info3']
        ])

        # table_INGREDIENT
        for ingres in data['ingre']:
            ingredients.append([
                ingres['ingre_name'],
                ingres['ingre_unit']
            ])

        # food_id 매기기
        c = 0
        for rcp in data['recipe']:
            c = c + 1
            recipess.append([
                data['name'],
                c,
                rcp['txt'],
                rcp['img']
            ])
        
#toCSV(recipess)