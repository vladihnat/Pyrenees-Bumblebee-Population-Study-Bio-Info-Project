import pandas as pd

# Lire un fichier CSV compressé en Gzip
data_1863_1949 = pd.read_csv("Q_65_1863-1949_RR-T-Vent.csv.gz",sep=';')
data_1950_2023 = pd.read_csv("Q_65_previous-1950-2023_RR-T-Vent.csv.gz",sep=';')

data_1950_2023['AAAAMMJJ'] = pd.to_datetime(data_1950_2023['AAAAMMJJ'], format='%Y%m%d')


# Filtrer les entrées où l'année est <= 2006 pour être en accord avec l'article des bourdons 
data_1950_2006 = data_1950_2023[data_1950_2023['AAAAMMJJ'].dt.year <= 2006]

# Compter le nombre d'entrées correspondantes
nombre_entrees = data_1950_2006.shape[0]

print(f"Nombre d'entrées entre 1950 et 2006 : {nombre_entrees}")
print(data_1950_2023.shape)
