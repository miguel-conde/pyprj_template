import globalsettings
import pandas as pd
import pyarrow.feather as feather
from skimpy import clean_columns
from libTstPyPaths.utils import dataList
import pickle   

# lock_salsas_frias = pd.read_excel(globalsettings.prj_files.raw_salsas_file)
# print(lock_salsas_frias)
# 
## Clean 'salsas' here ...
# salsas = clean_columns(lock_salsas_frias) \
#     .rename(columns = {'ano': 'anho'}) \
#     .astype({'anho': 'int32',
#              'mes_cod': 'int32',
#              'tipo': 'category',
#              'consolidado_ciudades': 'category'})
#     
# salsas['unidades'] = salsas['contenido'] \
#                     .str.extract(r'( [^ ]*$)', expand=False) \
#                     .str.strip() \
#                     .str.replace(r'(\.)', '', regex=True)
# 
# feather.write_feather(salsas, globalsettings.prj_files.clean_salsas_file)

airpass = pd.read_csv(globalsettings.prj_files.raw_airpass_file, sep = ';')
airqual = pd.read_csv(globalsettings.prj_files.raw_airqual_file, sep = ',')
cars    = pd.read_csv(globalsettings.prj_files.raw_cars_file,    sep = ',')
iris    = pd.read_csv(globalsettings.prj_files.raw_iris_file,    sep = ',')
mtcars  = pd.read_csv(globalsettings.prj_files.raw_mtcars_file,  sep = ',')

print(airpass)

all_data = dataList()
# all_data.salsas = salsas
all_data.airpass = airpass
all_data.airqual = airqual
all_data.cars    = cars
all_data.iris    = iris
all_data.mtcars  = mtcars

with open(globalsettings.prj_files.all_data, 'wb') as f:
    pickle.dump(all_data, f)

