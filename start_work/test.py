import pandas as pd
import os
import time
print('Привет, название файла **Ограничительный перечень**')
print('напиши путь файла в таком ввиде C:\\Users\\a.vechkanov\\Desktop\\')
a = input('')
pth1 = a

if os.path.exists(pth1):
    df = pd.read_excel(pth1+'Ограничительный перечень.xlsx', sheet_name='Лист1', engine='openpyxl')
           
else:
    print('Увы и ах, но нет файлов')
try:    
    df.drop(labels = [0,1], axis = 0, inplace = True)
    df.drop(labels=['Код продукции','Поставщик','Unnamed: 7','Unnamed: 8','Unnamed: 9','Примечание','№ строки'], axis = 1, inplace=True)
    df = df.reset_index(drop=True)
    df = df.dropna(subset=['Количество'])
    df = df.fillna('unknow')

    for i in df.index:
        if df['Наименование'][i] == 'unknow':
            df['Наименование'][i] = df['Наименование'][i-1]
    print(df)
#df['Наименование']=df['Наименование'].apply(lambda x: 'z' if x=='unknow' else 'y')
#print(df.head())

    df['Количество'] = [float(str(i).replace(",", ".")) for i in df['Количество']]
    df['Количество'] = df['Количество'].astype('float64')

    df_svod = df.pivot_table(index='Наименование', values='Количество', aggfunc='sum')

    df.to_excel("Ограничительный перечень_predproces.xlsx")
    df_svod.to_excel("Ограничительный перечень_svod.xlsx")

    print('Файлы созданы в той же папке что и основной файл')
    os.system("pause")
except:
    print('Скрипт не работает')




