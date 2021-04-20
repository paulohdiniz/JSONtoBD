from faker import Faker 
  
# To create a json file
import json        

from random import randint     
  
fake = Faker() 
def input_data(x): 
    for i in range(0, x): 
        geral = {}
        geral['model'] = "livros.Livro"
        geral['pk'] = i + 1
        geral['fields'] = {}
        geral['fields']['id'] = i + 1
        geral['fields']['titulo'] = fake.word() 
        geral['fields']['nota_media']= randint(1, 100)/10
        geral['fields']['num_paginas']= randint(1, 1000)
        geral['fields']['data_publicacao']= fake.date()
        geral['fields']['total_de_notas']= randint(1, 100)
        geral['fields']['autor_id']= randint(1, 30) 
        geral['fields']['editora_id']= randint(1, 30) 
        geral['fields']['genero_id']= randint(1, 30)
        geral['fields']['capa']= fake.image_url()
        with open('LivrosForLoadData.json', 'a') as fp: 
            if (i == 0):
                fp.write("[")
            json.dump(geral, fp)
            if (i != x-1):
                fp.write(',')
            else:
                fp.write(']')
def main(): 
    number = 100
    input_data(number) 
main() 