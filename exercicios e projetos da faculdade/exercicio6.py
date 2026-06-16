import pandas as pd #linha que importa a biblioteca do pandas                                          
#pandas é o uma biblioteca do python feita para trabalhar com dados os organizando é tipo um excel do python 
                                                                                                         
dados = {"titulo": ["O iluminado", "Megamente", "Angry birds"], #o pandas ajuda a organizar os dados quando o codigo é executado
         "genero": ["terror", "comedia", "comedia"],
         "ano":    ["1980",   "2010",    "2016"],
         "nota_de_avaliacao": ["rotten tomatoes 84%", "rotten tomatoes 70%", "rotten tomatoes 44%"] 
}

df = pd.DataFrame(dados)#o comando DataFrame é oq faz a estruturação dos dados e da para usar o pandas para estrurar o melhor 

print(df) 

