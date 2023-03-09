# Other

```python
!pip install nbconvert
import nbconvert
```

    Defaulting to user installation because normal site-packages is not writeable
    Requirement already satisfied: nbconvert in /usr/local/lib/python3.7/dist-packages (6.5.3)
    Requirement already satisfied: jupyterlab-pygments in /usr/local/lib/python3.7/dist-packages (from nbconvert) (0.2.2)
    Requirement already satisfied: traitlets>=5.0 in /usr/local/lib/python3.7/dist-packages (from nbconvert) (5.3.0)
    Requirement already satisfied: entrypoints>=0.2.2 in /usr/lib/python3/dist-packages (from nbconvert) (0.3)
    Requirement already satisfied: mistune<2,>=0.8.1 in /usr/local/lib/python3.7/dist-packages (from nbconvert) (0.8.4)
    Requirement already satisfied: nbclient>=0.5.0 in /usr/local/lib/python3.7/dist-packages (from nbconvert) (0.5.13)
    Requirement already satisfied: jupyter-core>=4.7 in /usr/local/lib/python3.7/dist-packages (from nbconvert) (4.11.1)
    Requirement already satisfied: defusedxml in /usr/local/lib/python3.7/dist-packages (from nbconvert) (0.7.1)
    Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.7/dist-packages (from nbconvert) (2.1.1)
    Requirement already satisfied: nbformat>=5.1 in /usr/local/lib/python3.7/dist-packages (from nbconvert) (5.4.0)
    Requirement already satisfied: tinycss2 in /usr/local/lib/python3.7/dist-packages (from nbconvert) (1.1.1)
    Requirement already satisfied: bleach in /usr/local/lib/python3.7/dist-packages (from nbconvert) (1.5.0)
    Requirement already satisfied: pandocfilters>=1.4.1 in /usr/local/lib/python3.7/dist-packages (from nbconvert) (1.5.0)
    Requirement already satisfied: pygments>=2.4.1 in /usr/local/lib/python3.7/dist-packages (from nbconvert) (2.13.0)
    Requirement already satisfied: packaging in /usr/local/lib/python3.7/dist-packages (from nbconvert) (21.3)
    Requirement already satisfied: lxml in /usr/local/lib/python3.7/dist-packages (from nbconvert) (4.9.1)
    Requirement already satisfied: jinja2>=3.0 in /usr/local/lib/python3.7/dist-packages (from nbconvert) (3.1.2)
    Requirement already satisfied: beautifulsoup4 in /usr/local/lib/python3.7/dist-packages (from nbconvert) (4.7.1)
    Requirement already satisfied: nest-asyncio in /usr/local/lib/python3.7/dist-packages (from nbclient>=0.5.0->nbconvert) (1.5.5)
    Requirement already satisfied: jupyter-client>=6.1.5 in /usr/local/lib/python3.7/dist-packages (from nbclient>=0.5.0->nbconvert) (7.3.4)
    Requirement already satisfied: jsonschema>=2.6 in /usr/local/lib/python3.7/dist-packages (from nbformat>=5.1->nbconvert) (4.14.0)
    Requirement already satisfied: fastjsonschema in /usr/local/lib/python3.7/dist-packages (from nbformat>=5.1->nbconvert) (2.16.1)
    Requirement already satisfied: soupsieve>=1.2 in /usr/local/lib/python3.7/dist-packages (from beautifulsoup4->nbconvert) (2.3.2.post1)
    Requirement already satisfied: html5lib!=0.9999,!=0.99999,<0.99999999,>=0.999 in /usr/local/lib/python3.7/dist-packages (from bleach->nbconvert) (0.9999999)
    Requirement already satisfied: six in /usr/lib/python3/dist-packages (from bleach->nbconvert) (1.12.0)
    Requirement already satisfied: pyparsing!=3.0.5,>=2.0.2 in /usr/local/lib/python3.7/dist-packages (from packaging->nbconvert) (3.0.9)
    Requirement already satisfied: webencodings>=0.4 in /usr/local/lib/python3.7/dist-packages (from tinycss2->nbconvert) (0.5.1)
    Requirement already satisfied: importlib-resources>=1.4.0 in /usr/local/lib/python3.7/dist-packages (from jsonschema>=2.6->nbformat>=5.1->nbconvert) (5.9.0)
    Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in /usr/local/lib/python3.7/dist-packages (from jsonschema>=2.6->nbformat>=5.1->nbconvert) (0.18.1)
    Requirement already satisfied: typing-extensions in /usr/local/lib/python3.7/dist-packages (from jsonschema>=2.6->nbformat>=5.1->nbconvert) (4.3.0)
    Requirement already satisfied: pkgutil-resolve-name>=1.3.10 in /usr/local/lib/python3.7/dist-packages (from jsonschema>=2.6->nbformat>=5.1->nbconvert) (1.3.10)
    Requirement already satisfied: importlib-metadata in /usr/local/lib/python3.7/dist-packages (from jsonschema>=2.6->nbformat>=5.1->nbconvert) (4.12.0)
    Requirement already satisfied: attrs>=17.4.0 in /usr/local/lib/python3.7/dist-packages (from jsonschema>=2.6->nbformat>=5.1->nbconvert) (19.1.0)
    Requirement already satisfied: tornado>=6.0 in /usr/local/lib/python3.7/dist-packages (from jupyter-client>=6.1.5->nbclient>=0.5.0->nbconvert) (6.2)
    Requirement already satisfied: pyzmq>=23.0 in /usr/local/lib/python3.7/dist-packages (from jupyter-client>=6.1.5->nbclient>=0.5.0->nbconvert) (23.2.1)
    Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.7/dist-packages (from jupyter-client>=6.1.5->nbclient>=0.5.0->nbconvert) (2.8.2)
    Requirement already satisfied: zipp>=3.1.0 in /usr/local/lib/python3.7/dist-packages (from importlib-resources>=1.4.0->jsonschema>=2.6->nbformat>=5.1->nbconvert) (3.8.1)
    --- Logging error ---
    Traceback (most recent call last):
      File "/usr/local/lib/python3.7/dist-packages/pip/_internal/utils/logging.py", line 177, in emit
        self.console.print(renderable, overflow="ignore", crop=False, style=style)
      File "/usr/local/lib/python3.7/dist-packages/pip/_vendor/rich/console.py", line 1673, in print
        extend(render(renderable, render_options))
      File "/usr/local/lib/python3.7/dist-packages/pip/_vendor/rich/console.py", line 1305, in render
        for render_output in iter_render:
      File "/usr/local/lib/python3.7/dist-packages/pip/_internal/utils/logging.py", line 134, in __rich_console__
        for line in lines:
      File "/usr/local/lib/python3.7/dist-packages/pip/_vendor/rich/segment.py", line 249, in split_lines
        for segment in segments:
      File "/usr/local/lib/python3.7/dist-packages/pip/_vendor/rich/console.py", line 1283, in render
        renderable = rich_cast(renderable)
      File "/usr/local/lib/python3.7/dist-packages/pip/_vendor/rich/protocol.py", line 36, in rich_cast
        renderable = cast_method()
      File "/usr/local/lib/python3.7/dist-packages/pip/_internal/self_outdated_check.py", line 130, in __rich__
        pip_cmd = get_best_invocation_for_this_pip()
      File "/usr/local/lib/python3.7/dist-packages/pip/_internal/utils/entrypoints.py", line 60, in get_best_invocation_for_this_pip
        os.path.join(binary_prefix, exe_name),
      File "/usr/lib/python3.7/genericpath.py", line 97, in samefile
        s2 = os.stat(f2)
    FileNotFoundError: [Errno 2] No such file or directory: '/usr/bin/pip'
    Call stack:
      File "/usr/local/bin/pip", line 8, in <module>
        sys.exit(main())
      File "/usr/local/lib/python3.7/dist-packages/pip/_internal/cli/main.py", line 70, in main
        return command.main(cmd_args)
      File "/usr/local/lib/python3.7/dist-packages/pip/_internal/cli/base_command.py", line 101, in main
        return self._main(args)
      File "/usr/local/lib/python3.7/dist-packages/pip/_internal/cli/base_command.py", line 223, in _main
        self.handle_pip_version_check(options)
      File "/usr/local/lib/python3.7/dist-packages/pip/_internal/cli/req_command.py", line 190, in handle_pip_version_check
        pip_self_version_check(session, options)
      File "/usr/local/lib/python3.7/dist-packages/pip/_internal/self_outdated_check.py", line 236, in pip_self_version_check
        logger.warning("[present-rich] %s", upgrade_prompt)
      File "/usr/lib/python3.7/logging/__init__.py", line 1395, in warning
        self._log(WARNING, msg, args, **kwargs)
      File "/usr/lib/python3.7/logging/__init__.py", line 1519, in _log
        self.handle(record)
      File "/usr/lib/python3.7/logging/__init__.py", line 1529, in handle
        self.callHandlers(record)
      File "/usr/lib/python3.7/logging/__init__.py", line 1591, in callHandlers
        hdlr.handle(record)
      File "/usr/lib/python3.7/logging/__init__.py", line 905, in handle
        self.emit(record)
      File "/usr/local/lib/python3.7/dist-packages/pip/_internal/utils/logging.py", line 179, in emit
        self.handleError(record)
    Message: '[present-rich] %s'
    Arguments: (UpgradePrompt(old='22.2.2', new='23.0.1'),)


https://gitlab.sima-land.ru/dev-dep/analytics/reports/-/issues/1336

# Введение

**ТЗ**


    Провести аб-тест кнопки "В корзину" с ценой, карточка товара и экран отзывов
    В задаче: dev-dep/mobile/react#4447 (closed) и связанной dev-dep/mobile/react#4449 (closed) реализовали новый вид кнопки , по результатам исследования https://docs.google.com/document/d/1XhoLvTt2k4FRPB6IWWpnckoXxdni9zCFx7To30t37Fs/edit?usp=sharing

    где мы выводим цену товара + количество на кнопке "В корзину"

    Гипотеза: если стоимость товара, и его количество будет всегда на виду, то увеличится конверсия в покладку товаров в корзину

    Необходимо провести а/б и убедиться что конверсия не ухудшилась

    Посчитать:

    отказы клиентов, после добавления товара в корзину товар стали меньше удалять
    покладку товаров в корзину в карточке товара и на экране отзывов
    конверсию в спасибо за заказ
    (карточка товара) если возможно, то как изменилась покладка из положения экрана ниже строки с элементом "Сравнить" (т.е стали ли чаще добавлять товар в корзину не возвращаясь к началу экрана где мы сейчас выводим стоимость)
    (экран отзывов) уменьшились ли выходы с экрана отзывов в карточку товара для покладки товара в корзину, или стали чаще добавлять с экрана отзывов

    сегмент С

    116.0.0

    ois 2023-01-23

    android 2023-01-29

![image.png](attachment:0086f819-d3ea-4d59-9779-e135dc6f5dd6.png)

**страница отзывов** 

![image.png](attachment:58be4aa9-4dcf-40f1-bfad-c939055a01a0.png)

БЫЛО
![image.png](attachment:3a8f3b2c-879e-4bcc-9820-82c6fe2f9f0a.png)
СТАЛО
![image.png](attachment:dae6d036-fada-43f0-aca5-ed23e25f7a3b.png)

Краткое описание используемых id
event_type_id = 1 -- Просмотр страницы

event_type_id = 17 -- Просмотр карточки

event_type_id = 2 -- Добавление в корзину

event_type_id = 7 -- Удаление из корзины

event_type_id = 3 -- Добавление в избранное

event_type_id = 6 -- Сделан заказ 

and source_id = 2 -- мобильная версия  

select *               -- тип страницы карточка (frodo.event.page_type_id)
from frodo.page_type
where id = 521872670 

select *               -- тип страницы отзыв (frodo.event.page_type_id)
from frodo.page_type
where id = 1769007887 

select *               -- тип страницы корзина (frodo.event.page_type_id)
from frodo.page_type
where id = 195266743


Запрос для отслеживания евентов тестового юзера моб приложения 
select source_id, created_at, event_type_id, url_path, sid, category, page_type_id, app_major, app_minor, app_patch
from event
where user_id = 1154803
    and created_date = today()
    and created_at >= '2023-03-03 10:00:00'
# Загружаю библиотеки  и подготавливаю коннекты с бд

## Коннект с базой кликхауса


```python
import os
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from infi.clickhouse_orm.database import Database
import requests
import time

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import numpy as np

import pandas as pd
import numpy as np
from scipy import stats as st

import warnings
warnings.filterwarnings(action='ignore')

from matplotlib import pyplot as plt
import seaborn as sns
%matplotlib inline
```


```python
db_name = os.environ.get('CLICKHOUSE_DATABASE')
db = Database(
    db_name=db_name, 
    db_url=os.environ.get('CLICKHOUSE_URL'),
    username=os.environ.get('CLICKHOUSE_USER'),
    password=os.environ.get('CLICKHOUSE_PASSWORD'),
    readonly=True
)
```


```python
import pandas as pd
import numpy as np

from matplotlib import pyplot as plt
import seaborn as sns

import plotly
import plotly.graph_objs as go
import plotly.express as px
import plotly.figure_factory as ff
from plotly.subplots import make_subplots

from io import BytesIO
import requests

import os

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, silhouette_score
from sklearn.ensemble import RandomForestClassifier
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import KMeans

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

import itertools
```


```python
def get_connect():
    return Database(
        db_name=os.environ.get('CLICKHOUSE_DATABASE'),
        db_url=os.environ.get('CLICKHOUSE_URL'),
        username=os.environ.get('CLICKHOUSE_USER'),
        password=os.environ.get('CLICKHOUSE_PASSWORD'),
        readonly=True)
```


```python
def eye_load(q):
    DB = get_connect()
    return pd.DataFrame.from_records([s.to_dict() for s in DB.select(q)])
```


```python
query = """
    select *
    from frodo.event
    limit 10
"""
```


```python
test = eye_load(query)
```


```python
test.head(1)
```

## Коннект с базой site


```python
pip install psycopg2-binary
```


```python
from sqlalchemy import create_engine
import sqlalchemy
import pandas as pd
```


```python
db_config = {'user': 'lebedev', # имя пользователя
'pwd': 'fRs4Tg5Slk0Dbr3', # пароль
'host': 'david.sima-land.ru',
'port': 6432, # порт подключения
'db': 'redash_ro'} # название базы данных
connection_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_config['user'],
db_config['pwd'],
db_config['host'],
db_config['port'],
db_config['db'])
# сохраняем коннектор
engine = create_engine(connection_string, connect_args={'sslmode':'require'})
```


```python
query = '''
        SELECT * 
        FROM web.item
           '''
pd.io.sql.read_sql(query, con = engine).head()
```

# <div class="alert alert-success"> <b>Конверсия отказы клиентов после добавления в корзину сегментов А и С</div>

## **выполнено в редаше**

```
import pandas as pd

# 1 запрос
query1 =  execute_query('frodo',   
                                """
                              select test_segment, sid, uniq(uid) as users
                                from frodo.event
                                    where created_date >= '2023-01-29'
                                        and source_id = 2
                                        and page_type_id = 195266743 
                                        and event_type_id = 7
                                        and test_segment in ('A', 'B')
                                        and toInt32OrZero(app_major) >= 116
                                group by test_segment, sid
                    """)
                    
# 2 запрос
query2=  execute_query('paxi_prod',   
                                """
                              select sid, min_qty
                                from web.item
                                where min_qty > 1
                    """)
                    
query1_df = pd.DataFrame()
query2_df = pd.DataFrame()

# query1_df


if len(query1['rows']) > 0:
    query1_df = query1_df.append(query1['rows'])
if len(query2['rows']) > 0:
    query2_df = query2_df.append(query2['rows'])
    
query1_df=query1_df.merge(query2_df, on=['sid'], how = 'left')


def min_qty_category(min_qty):
    if min_qty > 1:
        return 'Группа'
    else:
        return 'Одиночный'
        
query1_df['min_qty_category'] = query1_df['min_qty'].apply(min_qty_category)


print(
    query1_df.pivot_table(index=['test_segment', 'min_qty_category'], values='users', aggfunc='sum')
    )
```

## Итог

Итог

![image.png](attachment:c5e89a98-934e-46b7-b08b-a1ff857e203a.png)

отказы клиентов с групповыми товарами

![image.png](attachment:ff429296-64ac-4c3d-ab5d-018514d2f237.png)

отказы клиентов с одиночными товарами

![image.png](attachment:6fda67cf-7ebb-46fc-a06a-84ce65b919bf.png)

🤔 \
<span style="color:blue"> 
Гипотеза - 'отказы клиентов, после добавления товара в корзину товар стали меньше удалять'.\
Разница конверсий добавление в корзину / отказ в групповых товарах и одиночных товарах в сегментах A и C отсутсвует. </span>

# <div class="alert alert-success"> <b>Посчитаем среднии конверсии отзывы/покладка групп А и С с обрезанием выбросов</div>

## Запрос


```python
query_1 = """
--    select quantileExact(cr_A_116), quantileExact(cr_C_116), quantileExact(cr_A_117), quantileExact(cr_C_117), quantileExact(cr_A_118), quantileExact(cr_C_118), quantileExact(cr_A), quantileExact(cr_C)  
--    from(
        select created_date, cr_A_116, cr_C_116, cr_A_117, cr_C_117, cr_A_118, cr_C_118, cr_A, cr_C
        from 
            (select created_date,

                uniqIf(uid, test_segment='A' and event_type_id = 2 and toInt32OrZero(app_major) = 116) as add_cart_A_116, 
                uniqIf(uid, test_segment='A' and event_type_id = 1 and toInt32OrZero(app_major) = 116) as view_cart_A_116, 
                add_cart_A_116/view_cart_A_116*100 as cr_A_116,

                uniqIf(uid, test_segment='C' and event_type_id = 2 and toInt32OrZero(app_major) = 116) as add_cart_C_116, 
                uniqIf(uid, test_segment='C' and event_type_id = 1 and toInt32OrZero(app_major) = 116) as view_cart_C_116, 
                add_cart_C_116/view_cart_C_116*100 as cr_C_116,

                uniqIf(uid, test_segment='A' and event_type_id = 2 and toInt32OrZero(app_major) = 117) as add_cart_A_117, 
                uniqIf(uid, test_segment='A' and event_type_id = 1 and toInt32OrZero(app_major) = 117) as view_cart_A_117, 
                add_cart_A_117/view_cart_A_117*100 as cr_A_117,

                uniqIf(uid, test_segment='C' and event_type_id = 2 and toInt32OrZero(app_major) = 117) as add_cart_C_117, 
                uniqIf(uid, test_segment='C' and event_type_id = 1 and toInt32OrZero(app_major) = 117) as view_cart_C_117, 
                add_cart_C_117/view_cart_C_117*100 as cr_C_117, 

                uniqIf(uid, test_segment='A' and event_type_id = 2 and toInt32OrZero(app_major) = 118) as add_cart_A_118, 
                uniqIf(uid, test_segment='A' and event_type_id = 1 and toInt32OrZero(app_major) = 118) as view_cart_A_118, 
                add_cart_A_118/view_cart_A_118*100 as cr_A_118,

                uniqIf(uid, test_segment='C' and event_type_id = 2 and toInt32OrZero(app_major) = 118) as add_cart_C_118, 
                uniqIf(uid, test_segment='C' and event_type_id = 1 and toInt32OrZero(app_major) = 118) as view_cart_C_118, 
                add_cart_C_118/view_cart_C_118*100 as cr_C_118,
                
                uniqIf(uid, test_segment='A' and event_type_id = 2) as add_cart_A, 
                uniqIf(uid, test_segment='A' and event_type_id = 1) as view_cart_A, 
                add_cart_A/view_cart_A*100 as cr_A,
                
                uniqIf(uid, test_segment='C' and event_type_id = 2) as add_cart_C, 
                uniqIf(uid, test_segment='C' and event_type_id = 1) as view_cart_C, 
                add_cart_C/view_cart_C*100 as cr_C

            from frodo.event
            where created_date>='2023-01-29' 
                and test_segment IN ('A', 'C')
                and source_id = 2
                and page_type_id=1769007887
                and event_type_id IN (1, 2)
            group by created_date
            order by created_date asc)
--                )
"""
```


```python
cr = eye_load(query_1)
```


```python
cr.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>cr_A</th>
      <th>cr_A_116</th>
      <th>cr_A_117</th>
      <th>cr_A_118</th>
      <th>cr_C</th>
      <th>cr_C_116</th>
      <th>cr_C_117</th>
      <th>cr_C_118</th>
      <th>created_date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>7.398932</td>
      <td>7.398932</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>9.725490</td>
      <td>9.725490</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2023-01-29</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5.958674</td>
      <td>5.958674</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>8.654327</td>
      <td>8.654327</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2023-01-30</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6.556684</td>
      <td>6.556684</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>9.786325</td>
      <td>9.790509</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>2023-01-31</td>
    </tr>
    <tr>
      <th>3</th>
      <td>6.742902</td>
      <td>6.742902</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>9.116926</td>
      <td>9.116926</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2023-02-01</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5.886709</td>
      <td>5.886709</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>9.031262</td>
      <td>9.031262</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2023-02-02</td>
    </tr>
  </tbody>
</table>
</div>




```python
cr.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>cr_A</th>
      <th>cr_A_116</th>
      <th>cr_A_117</th>
      <th>cr_A_118</th>
      <th>cr_C</th>
      <th>cr_C_116</th>
      <th>cr_C_117</th>
      <th>cr_C_118</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>40.000000</td>
      <td>40.000000</td>
      <td>32.000000</td>
      <td>19.000000</td>
      <td>40.000000</td>
      <td>40.000000</td>
      <td>33.000000</td>
      <td>19.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>6.754235</td>
      <td>5.636028</td>
      <td>7.145856</td>
      <td>6.273117</td>
      <td>9.517848</td>
      <td>9.176917</td>
      <td>8.837805</td>
      <td>14.611952</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.571112</td>
      <td>1.771550</td>
      <td>3.894885</td>
      <td>2.117866</td>
      <td>0.690540</td>
      <td>2.109915</td>
      <td>2.783797</td>
      <td>20.795202</td>
    </tr>
    <tr>
      <th>min</th>
      <td>5.160142</td>
      <td>1.204819</td>
      <td>1.234568</td>
      <td>0.000000</td>
      <td>7.865169</td>
      <td>4.895105</td>
      <td>0.000000</td>
      <td>5.940594</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>6.495732</td>
      <td>4.260870</td>
      <td>5.709159</td>
      <td>5.438842</td>
      <td>9.000948</td>
      <td>8.579349</td>
      <td>8.957590</td>
      <td>8.833585</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>6.789123</td>
      <td>6.284801</td>
      <td>6.745541</td>
      <td>6.666667</td>
      <td>9.612139</td>
      <td>9.164828</td>
      <td>9.685230</td>
      <td>9.819639</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>7.146365</td>
      <td>6.747824</td>
      <td>7.595254</td>
      <td>7.250605</td>
      <td>10.159858</td>
      <td>10.264846</td>
      <td>10.049628</td>
      <td>10.680094</td>
    </tr>
    <tr>
      <th>max</th>
      <td>8.027606</td>
      <td>8.910891</td>
      <td>25.000000</td>
      <td>9.826590</td>
      <td>10.685413</td>
      <td>14.193548</td>
      <td>11.643836</td>
      <td>100.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
def mean_qua(table, column):
    '''
    Среднее по квантилям.
    Принимает таблицу и название столбца.
    Обрезаем стобец по 02 и 08 квантилю.
    '''
    qua_02 = table[column].quantile([.2,.8])[0.2]
    qua_08 = table[column].quantile([.2,.8])[0.8]    
    return round(table[(table.loc[:, column] > table.loc[:, column].quantile([.2,.8])[0.2]) & (table.loc[:, column] < table.loc[:, column].quantile([.2,.8])[0.8])][column].mean(), 2) 

```

## Итог


```python
fig, axs = plt.subplots(nrows= 2, ncols= 1, figsize=(6.4, 7))

sns.boxplot(
        data = cr,
        x = 'cr_A',
        ax = axs[0]
        )

sns.boxplot(
        data = cr,
        x = 'cr_C',
        ax = axs[1]
        )

# ax[0].set_title('Manual DateFormatter', loc='left', y=0.85, x=0.02,
#              fontsize='medium')

fig. suptitle('отзывы/покладка групп А и С с обрезанием выбросов')

plt.show()
```


    
![png](output_43_0.png)
    



```python
print('Среднее значение конверсий cr_A_116 - ', mean_qua(cr, 'cr_A_116'))
print('Среднее значение конверсий cr_С_116 - ', mean_qua(cr, 'cr_C_116'))
print('Разница конверсий С - А ', mean_qua(cr, 'cr_C_116')-mean_qua(cr, 'cr_A_116'))
```

    Среднее значение конверсий cr_A_116 -  6.15
    Среднее значение конверсий cr_С_116 -  9.15
    Разница конверсий С - А  3.0



```python
print('Среднее значение конверсий cr_A_117 - ', mean_qua(cr, 'cr_A_117'))
print('Среднее значение конверсий cr_С_117 - ', mean_qua(cr, 'cr_C_117'))
print('Разница конверсий С - А ', mean_qua(cr, 'cr_C_117')-mean_qua(cr, 'cr_A_117'))
```

    Среднее значение конверсий cr_A_117 -  6.67
    Среднее значение конверсий cr_С_117 -  9.68
    Разница конверсий С - А  3.01



```python
print('Среднее значение конверсий cr_A_118 - ', mean_qua(cr, 'cr_A_118'))
print('Среднее значение конверсий cr_С_118 - ', mean_qua(cr, 'cr_C_118'))
print('Разница конверсий С - А ', mean_qua(cr, 'cr_C_118')-mean_qua(cr, 'cr_A_118'))
```

    Среднее значение конверсий cr_A_118 -  6.56
    Среднее значение конверсий cr_С_118 -  10.05
    Разница конверсий С - А  3.490000000000001



```python
print('Среднее значение конверсий cr_A - ', mean_qua(cr, 'cr_A'))
print('Среднее значение конверсий cr_С - ', mean_qua(cr, 'cr_C'))
print('Разница конверсий С - А ', mean_qua(cr, 'cr_C')-mean_qua(cr, 'cr_A'))
```

    Среднее значение конверсий cr_A -  6.74
    Среднее значение конверсий cr_С -  9.11
    Разница конверсий С - А  2.369999999999999


## Проверка ttest

Стьюдентный критерий для парных выборок используется для сравнения средних значений двух выборок, когда каждое наблюдение в одной выборке может быть сопоставлено с наблюдением в другой выборке.


```python
query_2 = """
            select created_date,

            uniqIf(uid, test_segment='A' and event_type_id = 2 and toInt32OrZero(app_major) = 116) as add_cart_A_116, 
            uniqIf(uid, test_segment='A' and event_type_id = 1 and toInt32OrZero(app_major) = 116) as view_cart_A_116, 
            add_cart_A_116/view_cart_A_116*100 as cr_A_116,
            
            uniqIf(uid, test_segment='C' and event_type_id = 2 and toInt32OrZero(app_major) = 116) as add_cart_C_116, 
            uniqIf(uid, test_segment='C' and event_type_id = 1 and toInt32OrZero(app_major) = 116) as view_cart_C_116, 
            add_cart_C_116/view_cart_C_116*100 as cr_C_116,
            
            uniqIf(uid, test_segment='A' and event_type_id = 2 and toInt32OrZero(app_major) = 117) as add_cart_A_117, 
            uniqIf(uid, test_segment='A' and event_type_id = 1 and toInt32OrZero(app_major) = 117) as view_cart_A_117, 
            add_cart_A_117/view_cart_A_117*100 as cr_A_117,
            
            uniqIf(uid, test_segment='C' and event_type_id = 2 and toInt32OrZero(app_major) = 117) as add_cart_C_117, 
            uniqIf(uid, test_segment='C' and event_type_id = 1 and toInt32OrZero(app_major) = 117) as view_cart_C_117, 
            add_cart_C_117/view_cart_C_117*100 as cr_C_117, 
            
            uniqIf(uid, test_segment='A' and event_type_id = 2 and toInt32OrZero(app_major) = 118) as add_cart_A_118, 
            uniqIf(uid, test_segment='A' and event_type_id = 1 and toInt32OrZero(app_major) = 118) as view_cart_A_118, 
            add_cart_A_118/view_cart_A_118*100 as cr_A_118,
            
            uniqIf(uid, test_segment='C' and event_type_id = 2 and toInt32OrZero(app_major) = 118) as add_cart_C_118, 
            uniqIf(uid, test_segment='C' and event_type_id = 1 and toInt32OrZero(app_major) = 118) as view_cart_C_118, 
            add_cart_C_118/view_cart_C_118*100 as cr_C_118 

            from frodo.event
            where created_date>='2023-01-29' 
                and test_segment IN ('A', 'C')
                and source_id = 2
                and page_type_id=1769007887
                and event_type_id IN (1, 2)
            group by created_date
            order by created_date asc             
"""
```


```python
uniq_uid = eye_load(query_2)
```


```python
uniq_uid.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>add_cart_A_116</th>
      <th>add_cart_A_117</th>
      <th>add_cart_A_118</th>
      <th>add_cart_C_116</th>
      <th>add_cart_C_117</th>
      <th>add_cart_C_118</th>
      <th>cr_A_116</th>
      <th>cr_A_117</th>
      <th>cr_A_118</th>
      <th>cr_C_116</th>
      <th>cr_C_117</th>
      <th>cr_C_118</th>
      <th>created_date</th>
      <th>view_cart_A_116</th>
      <th>view_cart_A_117</th>
      <th>view_cart_A_118</th>
      <th>view_cart_C_116</th>
      <th>view_cart_C_117</th>
      <th>view_cart_C_118</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>35</th>
      <td>9</td>
      <td>9</td>
      <td>163</td>
      <td>6</td>
      <td>14</td>
      <td>245</td>
      <td>8.910891</td>
      <td>6.040268</td>
      <td>7.096212</td>
      <td>6.000000</td>
      <td>8.588957</td>
      <td>10.647545</td>
      <td>2023-03-05</td>
      <td>101</td>
      <td>149</td>
      <td>2297</td>
      <td>100</td>
      <td>163</td>
      <td>2301</td>
    </tr>
    <tr>
      <th>36</th>
      <td>1</td>
      <td>3</td>
      <td>154</td>
      <td>5</td>
      <td>6</td>
      <td>236</td>
      <td>1.204819</td>
      <td>2.542373</td>
      <td>7.236842</td>
      <td>5.208333</td>
      <td>4.580153</td>
      <td>10.966543</td>
      <td>2023-03-06</td>
      <td>83</td>
      <td>118</td>
      <td>2128</td>
      <td>96</td>
      <td>131</td>
      <td>2152</td>
    </tr>
    <tr>
      <th>37</th>
      <td>3</td>
      <td>1</td>
      <td>119</td>
      <td>6</td>
      <td>11</td>
      <td>148</td>
      <td>3.846154</td>
      <td>1.234568</td>
      <td>6.655481</td>
      <td>8.823529</td>
      <td>11.340206</td>
      <td>8.305275</td>
      <td>2023-03-07</td>
      <td>78</td>
      <td>81</td>
      <td>1788</td>
      <td>68</td>
      <td>97</td>
      <td>1782</td>
    </tr>
    <tr>
      <th>38</th>
      <td>4</td>
      <td>8</td>
      <td>117</td>
      <td>8</td>
      <td>7</td>
      <td>160</td>
      <td>5.405405</td>
      <td>9.523810</td>
      <td>6.763006</td>
      <td>12.698413</td>
      <td>8.139535</td>
      <td>8.888889</td>
      <td>2023-03-08</td>
      <td>74</td>
      <td>84</td>
      <td>1730</td>
      <td>63</td>
      <td>86</td>
      <td>1800</td>
    </tr>
    <tr>
      <th>39</th>
      <td>1</td>
      <td>1</td>
      <td>28</td>
      <td>3</td>
      <td>2</td>
      <td>38</td>
      <td>4.000000</td>
      <td>6.250000</td>
      <td>5.353728</td>
      <td>12.500000</td>
      <td>9.523810</td>
      <td>7.676768</td>
      <td>2023-03-09</td>
      <td>25</td>
      <td>16</td>
      <td>523</td>
      <td>24</td>
      <td>21</td>
      <td>495</td>
    </tr>
  </tbody>
</table>
</div>




```python
alpha = 0.05
```


```python
sns.distplot(uniq_uid['cr_A_116']);
sns.distplot(uniq_uid['cr_C_116']);
```


    
![png](output_54_0.png)
    


$\begin{equation*}
 \begin{cases}
   H_0 :\text{Средние конверсии равны}\\
   H_1 :\text{Средние конверсии отличаются}
 \end{cases}
\end{equation*}$


```python
results = st.ttest_ind(uniq_uid['cr_A_116'], uniq_uid['cr_C_116'], equal_var=False)
print('p-значение: ', results.pvalue)

if (results.pvalue < alpha):
    print("Отвергаем нулевую гипотезу")
else:
    print("Не получилось отвергнуть нулевую гипотезу")
```

    p-значение:  6.384585674262265e-12
    Отвергаем нулевую гипотезу


$\begin{equation*}
 \begin{cases}
   H_0 :\text{Средняя конверсии в группе А и группе С ровна}\\
   H_1 :\text{Средняя коверсия в группе С больше средней конверсии группы А}
 \end{cases}
\end{equation*}$


```python
results = st.ttest_rel(uniq_uid['cr_C_116'], uniq_uid['cr_A_116'])

# тест односторонний: p-value будет в два раза меньше
print('p-значение: ', results.pvalue / 2)

# тест односторонний влево:
# отвергаем гипотезу только если выборочное среднее значимо меньше предполагаемого значения
if (results.pvalue / 2 < alpha) and (uniq_uid['cr_C_116'].mean() > uniq_uid['cr_A_116'].mean()):
    print("Отвергаем нулевую гипотезу")
else:
    print("Не получилось отвергнуть нулевую гипотезу")
```

    p-значение:  6.297699369312241e-11
    Отвергаем нулевую гипотезу


## Итог

🤔 \
<span style="color:blue"> 
Разница конверсий статистически значима, **конверсия в сегменте С выше чем в сегменте А** и составляет:\
       * версия моб. приложения = 116    - 3%\
       * версия моб. приложения = 117    - 3.01%\
       * версия моб. приложения = 118    - 3.5%\
       * версия моб. приложения >= 116    - 2.37%</span>

## <div class="alert alert-info"> <b>Проведем аб тест старым способом</div>

### Импортируем библиотеки


```python
from common.components_container import components_container
```

### Запросы


```python
ab_test = components_container.ab_test

# Параметры теста
ab_test.set_period((36, 0))
ab_test.set_a_segment('A')
ab_test.set_b_segment('C')
ab_test.set_metric_field('created_date')
ab_test.set_amount_field('cnt')

shows_query = """
        select created_date, test_segment, uniq(uid) as cnt
        from frodo.event
        where created_date>='2023-01-29' 
            and test_segment IN ('A', 'C')
            and source_id = 2
            and page_type_id=1769007887
            and event_type_id = 1
            and toInt32OrZero(app_major) >= 116
        group by created_date, test_segment
        order by created_date asc
"""
ab_test.set_shows_query(shows_query)

adds_query = """
        select created_date, test_segment, uniq(uid) as cnt
        from frodo.event
        where created_date>='2023-01-29' 
            and test_segment IN ('A', 'C')
            and source_id = 2
            and page_type_id=1769007887
            and event_type_id = 2
            and toInt32OrZero(app_major) >= 116
        group by created_date, test_segment
        order by created_date asc
"""
ab_test.set_targets_query(adds_query)
```

### Итог


```python
ab_test.make_report()
```


<h5>Среднее значение конверсии сегмента A: 6.75%</h5>



<h5>Среднее значение конверсии сегмента C: 9.53%</h5>



<h5>Среднее значение прироста конверсии: 2.77%</h5>



<h5>Тест значимости: Student. На уровне значимости 0.1 ЗНАЧИМО</h5>



<h5>Тест значимости: Student. На уровне значимости 0.05 ЗНАЧИМО</h5>



<h5>Тест значимости: Student. На уровне значимости 0.01 ЗНАЧИМО</h5>


# <div class="alert alert-success"> <b>Посчитаем среднии конверсии карточка/покладка групп А и С с обрезанием выбросов</div>

## Запрос


```python
query_1 = """
--    select quantileExact(cr_A_116), quantileExact(cr_C_116), quantileExact(cr_A_117), quantileExact(cr_C_117), quantileExact(cr_A_118), quantileExact(cr_C_118), quantileExact(cr_A), quantileExact(cr_C)  
--    from(
        select created_date, cr_A_116, cr_C_116, cr_A_117, cr_C_117, cr_A_118, cr_C_118, cr_A, cr_C
        from 
            (select created_date,

                uniqIf(uid, test_segment='A' and event_type_id = 2 and toInt32OrZero(app_major) = 116) as add_cart_A_116, 
                uniqIf(uid, test_segment='A' and event_type_id = 1 and toInt32OrZero(app_major) = 116) as view_cart_A_116, 
                add_cart_A_116/view_cart_A_116*100 as cr_A_116,

                uniqIf(uid, test_segment='C' and event_type_id = 2 and toInt32OrZero(app_major) = 116) as add_cart_C_116, 
                uniqIf(uid, test_segment='C' and event_type_id = 1 and toInt32OrZero(app_major) = 116) as view_cart_C_116, 
                add_cart_C_116/view_cart_C_116*100 as cr_C_116,

                uniqIf(uid, test_segment='A' and event_type_id = 2 and toInt32OrZero(app_major) = 117) as add_cart_A_117, 
                uniqIf(uid, test_segment='A' and event_type_id = 1 and toInt32OrZero(app_major) = 117) as view_cart_A_117, 
                add_cart_A_117/view_cart_A_117*100 as cr_A_117,

                uniqIf(uid, test_segment='C' and event_type_id = 2 and toInt32OrZero(app_major) = 117) as add_cart_C_117, 
                uniqIf(uid, test_segment='C' and event_type_id = 1 and toInt32OrZero(app_major) = 117) as view_cart_C_117, 
                add_cart_C_117/view_cart_C_117*100 as cr_C_117, 

                uniqIf(uid, test_segment='A' and event_type_id = 2 and toInt32OrZero(app_major) = 118) as add_cart_A_118, 
                uniqIf(uid, test_segment='A' and event_type_id = 1 and toInt32OrZero(app_major) = 118) as view_cart_A_118, 
                add_cart_A_118/view_cart_A_118*100 as cr_A_118,

                uniqIf(uid, test_segment='C' and event_type_id = 2 and toInt32OrZero(app_major) = 118) as add_cart_C_118, 
                uniqIf(uid, test_segment='C' and event_type_id = 1 and toInt32OrZero(app_major) = 118) as view_cart_C_118, 
                add_cart_C_118/view_cart_C_118*100 as cr_C_118,
                
                uniqIf(uid, test_segment='A' and event_type_id = 2) as add_cart_A, 
                uniqIf(uid, test_segment='A' and event_type_id = 1) as view_cart_A, 
                add_cart_A/view_cart_A*100 as cr_A,
                
                uniqIf(uid, test_segment='C' and event_type_id = 2) as add_cart_C, 
                uniqIf(uid, test_segment='C' and event_type_id = 1) as view_cart_C, 
                add_cart_C/view_cart_C*100 as cr_C

            from frodo.event
            where created_date>='2023-01-29' 
                and test_segment IN ('A', 'C')
                and source_id = 2
                and page_type_id=521872670
                and event_type_id IN (1, 2)
            group by created_date
            order by created_date asc)
--                )
"""
```


```python
cr = eye_load(query_1)
```


```python
cr.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>cr_A</th>
      <th>cr_A_116</th>
      <th>cr_A_117</th>
      <th>cr_A_118</th>
      <th>cr_C</th>
      <th>cr_C_116</th>
      <th>cr_C_117</th>
      <th>cr_C_118</th>
      <th>created_date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>36.522489</td>
      <td>36.363636</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>36.706652</td>
      <td>37.471396</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2023-01-29</td>
    </tr>
    <tr>
      <th>1</th>
      <td>35.617883</td>
      <td>36.205128</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>35.801010</td>
      <td>36.377789</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2023-01-30</td>
    </tr>
    <tr>
      <th>2</th>
      <td>36.162519</td>
      <td>36.610374</td>
      <td>100.0</td>
      <td>NaN</td>
      <td>36.653895</td>
      <td>37.468241</td>
      <td>100.0</td>
      <td>NaN</td>
      <td>2023-01-31</td>
    </tr>
    <tr>
      <th>3</th>
      <td>35.855509</td>
      <td>36.228253</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>36.515251</td>
      <td>37.072053</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>2023-02-01</td>
    </tr>
    <tr>
      <th>4</th>
      <td>36.261843</td>
      <td>36.649907</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>36.724379</td>
      <td>37.476636</td>
      <td>0.0</td>
      <td>100.0</td>
      <td>2023-02-02</td>
    </tr>
  </tbody>
</table>
</div>




```python
cr.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>cr_A</th>
      <th>cr_A_116</th>
      <th>cr_A_117</th>
      <th>cr_A_118</th>
      <th>cr_C</th>
      <th>cr_C_116</th>
      <th>cr_C_117</th>
      <th>cr_C_118</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>38.000000</td>
      <td>38.000000</td>
      <td>34.000000</td>
      <td>20.000000</td>
      <td>38.000000</td>
      <td>38.000000</td>
      <td>34.000000</td>
      <td>22.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>36.052550</td>
      <td>35.141430</td>
      <td>33.687968</td>
      <td>31.032774</td>
      <td>36.373220</td>
      <td>35.548775</td>
      <td>37.839470</td>
      <td>38.671572</td>
    </tr>
    <tr>
      <th>std</th>
      <td>1.084888</td>
      <td>2.001971</td>
      <td>15.771369</td>
      <td>13.918096</td>
      <td>1.183716</td>
      <td>2.105987</td>
      <td>18.206277</td>
      <td>24.811428</td>
    </tr>
    <tr>
      <th>min</th>
      <td>32.502623</td>
      <td>31.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>31.899736</td>
      <td>27.007299</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>35.636363</td>
      <td>33.454274</td>
      <td>32.168746</td>
      <td>33.470807</td>
      <td>35.819836</td>
      <td>34.895987</td>
      <td>34.416094</td>
      <td>35.140620</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>36.212181</td>
      <td>35.529743</td>
      <td>35.888289</td>
      <td>35.767949</td>
      <td>36.672438</td>
      <td>36.083072</td>
      <td>36.221940</td>
      <td>36.672100</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>36.525140</td>
      <td>36.643000</td>
      <td>36.841087</td>
      <td>37.060315</td>
      <td>37.031853</td>
      <td>37.070130</td>
      <td>37.945996</td>
      <td>38.541812</td>
    </tr>
    <tr>
      <th>max</th>
      <td>37.979512</td>
      <td>38.888889</td>
      <td>100.000000</td>
      <td>50.000000</td>
      <td>38.036609</td>
      <td>38.512035</td>
      <td>100.000000</td>
      <td>100.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
def mean_qua(table, column):
    qua_02 = table[column].quantile([.2,.8])[0.2]
    qua_08 = table[column].quantile([.2,.8])[0.8]    
    return round(table[(table.loc[:, column] > table.loc[:, column].quantile([.2,.8])[0.2]) & (table.loc[:, column] < table.loc[:, column].quantile([.2,.8])[0.8])][column].mean(), 2) 

```

## Итог


```python
print('Среднее значение конверсий cr_A_116 - ', mean_qua(cr, 'cr_A_116'))
print('Среднее значение конверсий cr_С_116 - ', mean_qua(cr, 'cr_C_116'))
print('Разница конверсий С - А ', mean_qua(cr, 'cr_C_116')-mean_qua(cr, 'cr_A_116'))
```

    Среднее значение конверсий cr_A_116 -  35.33
    Среднее значение конверсий cr_С_116 -  35.95
    Разница конверсий С - А  0.6200000000000045



```python
print('Среднее значение конверсий cr_A_117 - ', mean_qua(cr, 'cr_A_117'))
print('Среднее значение конверсий cr_С_117 - ', mean_qua(cr, 'cr_C_117'))
print('Разница конверсий С - А ', mean_qua(cr, 'cr_C_117')-mean_qua(cr, 'cr_A_117'))
```

    Среднее значение конверсий cr_A_117 -  35.25
    Среднее значение конверсий cr_С_117 -  36.2
    Разница конверсий С - А  0.9500000000000028



```python
print('Среднее значение конверсий cr_A_118 - ', mean_qua(cr, 'cr_A_118'))
print('Среднее значение конверсий cr_С_118 - ', mean_qua(cr, 'cr_C_118'))
print('Разница конверсий С - А ', mean_qua(cr, 'cr_C_118')-mean_qua(cr, 'cr_A_118'))
```

    Среднее значение конверсий cr_A_118 -  35.52
    Среднее значение конверсий cr_С_118 -  36.73
    Разница конверсий С - А  1.2099999999999937



```python
print('Среднее значение конверсий cr_A - ', mean_qua(cr, 'cr_A'))
print('Среднее значение конверсий cr_С - ', mean_qua(cr, 'cr_C'))
print('Разница конверсий С - А ', mean_qua(cr, 'cr_C')-mean_qua(cr, 'cr_A'))
```

    Среднее значение конверсий cr_A -  36.14
    Среднее значение конверсий cr_С -  36.56
    Разница конверсий С - А  0.4200000000000017


## Проверка ttest

Стьюдентный критерий для парных выборок используется для сравнения средних значений двух выборок, когда каждое наблюдение в одной выборке может быть сопоставлено с наблюдением в другой выборке.


```python
query_2 = """
            select created_date,

            uniqIf(uid, test_segment='A' and event_type_id = 2 and toInt32OrZero(app_major) = 116) as add_cart_A_116, 
            uniqIf(uid, test_segment='A' and event_type_id = 1 and toInt32OrZero(app_major) = 116) as view_cart_A_116, 
            add_cart_A_116/view_cart_A_116*100 as cr_A_116,
            
            uniqIf(uid, test_segment='C' and event_type_id = 2 and toInt32OrZero(app_major) = 116) as add_cart_C_116, 
            uniqIf(uid, test_segment='C' and event_type_id = 1 and toInt32OrZero(app_major) = 116) as view_cart_C_116, 
            add_cart_C_116/view_cart_C_116*100 as cr_C_116,
            
            uniqIf(uid, test_segment='A' and event_type_id = 2 and toInt32OrZero(app_major) = 117) as add_cart_A_117, 
            uniqIf(uid, test_segment='A' and event_type_id = 1 and toInt32OrZero(app_major) = 117) as view_cart_A_117, 
            add_cart_A_117/view_cart_A_117*100 as cr_A_117,
            
            uniqIf(uid, test_segment='C' and event_type_id = 2 and toInt32OrZero(app_major) = 117) as add_cart_C_117, 
            uniqIf(uid, test_segment='C' and event_type_id = 1 and toInt32OrZero(app_major) = 117) as view_cart_C_117, 
            add_cart_C_117/view_cart_C_117*100 as cr_C_117, 
            
            uniqIf(uid, test_segment='A' and event_type_id = 2 and toInt32OrZero(app_major) = 118) as add_cart_A_118, 
            uniqIf(uid, test_segment='A' and event_type_id = 1 and toInt32OrZero(app_major) = 118) as view_cart_A_118, 
            add_cart_A_118/view_cart_A_118*100 as cr_A_118,
            
            uniqIf(uid, test_segment='C' and event_type_id = 2 and toInt32OrZero(app_major) = 118) as add_cart_C_118, 
            uniqIf(uid, test_segment='C' and event_type_id = 1 and toInt32OrZero(app_major) = 118) as view_cart_C_118, 
            add_cart_C_118/view_cart_C_118*100 as cr_C_118 

            from frodo.event
            where created_date>='2023-01-29' 
                and test_segment IN ('A', 'C')
                and source_id = 2
                and page_type_id=521872670
                and event_type_id IN (1, 2)
            group by created_date
            order by created_date asc             
"""
```


```python
uniq_uid = eye_load(query_2)
```


```python
uniq_uid.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>add_cart_A_116</th>
      <th>add_cart_A_117</th>
      <th>add_cart_A_118</th>
      <th>add_cart_C_116</th>
      <th>add_cart_C_117</th>
      <th>add_cart_C_118</th>
      <th>cr_A_116</th>
      <th>cr_A_117</th>
      <th>cr_A_118</th>
      <th>cr_C_116</th>
      <th>cr_C_117</th>
      <th>cr_C_118</th>
      <th>created_date</th>
      <th>view_cart_A_116</th>
      <th>view_cart_A_117</th>
      <th>view_cart_A_118</th>
      <th>view_cart_C_116</th>
      <th>view_cart_C_117</th>
      <th>view_cart_C_118</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>33</th>
      <td>123</td>
      <td>189</td>
      <td>2313</td>
      <td>113</td>
      <td>176</td>
      <td>2355</td>
      <td>37.160121</td>
      <td>30.781759</td>
      <td>33.751642</td>
      <td>32.944606</td>
      <td>30.397237</td>
      <td>35.086412</td>
      <td>2023-03-03</td>
      <td>331</td>
      <td>614</td>
      <td>6853</td>
      <td>343</td>
      <td>579</td>
      <td>6712</td>
    </tr>
    <tr>
      <th>34</th>
      <td>93</td>
      <td>154</td>
      <td>2280</td>
      <td>103</td>
      <td>149</td>
      <td>2276</td>
      <td>31.000000</td>
      <td>31.557377</td>
      <td>35.552783</td>
      <td>34.448161</td>
      <td>31.702128</td>
      <td>35.303242</td>
      <td>2023-03-04</td>
      <td>300</td>
      <td>488</td>
      <td>6413</td>
      <td>299</td>
      <td>470</td>
      <td>6447</td>
    </tr>
    <tr>
      <th>35</th>
      <td>106</td>
      <td>140</td>
      <td>2447</td>
      <td>103</td>
      <td>162</td>
      <td>2420</td>
      <td>37.192982</td>
      <td>30.107527</td>
      <td>35.780085</td>
      <td>35.034014</td>
      <td>34.322034</td>
      <td>35.814711</td>
      <td>2023-03-05</td>
      <td>285</td>
      <td>465</td>
      <td>6839</td>
      <td>294</td>
      <td>472</td>
      <td>6757</td>
    </tr>
    <tr>
      <th>36</th>
      <td>86</td>
      <td>120</td>
      <td>2201</td>
      <td>101</td>
      <td>130</td>
      <td>2205</td>
      <td>33.992095</td>
      <td>32.085561</td>
      <td>34.166408</td>
      <td>32.165605</td>
      <td>31.784841</td>
      <td>33.439490</td>
      <td>2023-03-06</td>
      <td>253</td>
      <td>374</td>
      <td>6442</td>
      <td>314</td>
      <td>409</td>
      <td>6594</td>
    </tr>
    <tr>
      <th>37</th>
      <td>48</td>
      <td>53</td>
      <td>1049</td>
      <td>37</td>
      <td>66</td>
      <td>1009</td>
      <td>32.214765</td>
      <td>29.943503</td>
      <td>32.628305</td>
      <td>27.007299</td>
      <td>34.736842</td>
      <td>31.890013</td>
      <td>2023-03-07</td>
      <td>149</td>
      <td>177</td>
      <td>3215</td>
      <td>137</td>
      <td>190</td>
      <td>3164</td>
    </tr>
  </tbody>
</table>
</div>




```python
alpha = 0.05
```


```python
sns.distplot(uniq_uid['cr_A_116']);
sns.distplot(uniq_uid['cr_C_116']);
```


    
![png](output_86_0.png)
    


$\begin{equation*}
 \begin{cases}
   H_0 :\text{Средние конверсии равны}\\
   H_1 :\text{Средние конверсии отличаются}
 \end{cases}
\end{equation*}$


```python
results = st.ttest_ind(uniq_uid['cr_A_116'], uniq_uid['cr_C_116'], equal_var=False)
print('p-значение: ', results.pvalue)

if (results.pvalue < alpha):
    print("Отвергаем нулевую гипотезу")
else:
    print("Не получилось отвергнуть нулевую гипотезу")
```

    p-значение:  0.390288920919761
    Не получилось отвергнуть нулевую гипотезу


$\begin{equation*}
 \begin{cases}
   H_0 :\text{Средняя конверсии в группе А и группе С ровна}\\
   H_1 :\text{Средняя коверсия в группе С больше средней конверсии группы А}
 \end{cases}
\end{equation*}$


```python
results = st.ttest_rel(uniq_uid['cr_C_116'], uniq_uid['cr_A_116'])

# тест односторонний: p-value будет в два раза меньше
print('p-значение: ', results.pvalue / 2)

# тест односторонний влево:
# отвергаем гипотезу только если выборочное среднее значимо меньше предполагаемого значения
if (results.pvalue / 2 < alpha) and (uniq_uid['cr_C_116'].mean() > uniq_uid['cr_A_116'].mean()):
    print("Отвергаем нулевую гипотезу")
else:
    print("Не получилось отвергнуть нулевую гипотезу")
```

    p-значение:  0.12120710481621237
    Не получилось отвергнуть нулевую гипотезу


## Итог

🤔 \
<span style="color:blue"> 
Разница конверсий статистически не значима, **и не превышает стандартное отклоение** составляет:\
       * версия моб. приложения = 116    - 0.62%\
       * версия моб. приложения = 117    - 0.95%\
       * версия моб. приложения = 118    - 1.20%\
       * версия моб. приложения >= 116    - 0.42%</span>

# <div class="alert alert-success"> <b>Конверсия спасибо за заказ</div>

## Запрос


```python
query_8 = """
    select test_segment, event_type_id, uniq(uid) as count_user_order
    from 
        (select arrayJoin(sids) AS sid, uid, test_segment, event_type_id
        from frodo.event 
        where created_date>='2023-01-29'
            and test_segment in ('A','C')
            and event_type_id = 6
            and toInt32OrZero(app_major) >= 116
        ) as table_1
    full join    
        (select sid, uid, test_segment, event_type_id
        from frodo.event 
        where created_date>='2023-01-29'
            and test_segment in ('A','C')
            and event_type_id = 2
            and toInt32OrZero(app_major) >= 116
        ) as table_2
    using (sid, uid, test_segment, event_type_id)
    group by test_segment, event_type_id
"""
```


```python
df = eye_load(query_8)
```


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count_user_order</th>
      <th>event_type_id</th>
      <th>test_segment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>45283</td>
      <td>2</td>
      <td>A</td>
    </tr>
    <tr>
      <th>1</th>
      <td>15916</td>
      <td>6</td>
      <td>A</td>
    </tr>
    <tr>
      <th>2</th>
      <td>45436</td>
      <td>2</td>
      <td>C</td>
    </tr>
    <tr>
      <th>3</th>
      <td>15962</td>
      <td>6</td>
      <td>C</td>
    </tr>
  </tbody>
</table>
</div>



## zet_proportion проверка

$\begin{equation*}
 \begin{cases}
   H_0 :\text{Пропорции равны}\\
   H_1 :\text{Пропорция сегмента А больше пропорции сегмента C}
 \end{cases}
\end{equation*}$


```python
import numpy as np
from statsmodels.stats.proportion import proportions_ztest
```


```python
count = np.array([df.iloc[0,0], df.iloc[1,0]])
nobs = np.array([df.iloc[2,0], df.iloc[3,0]])
stat, pval = proportions_ztest(count, nobs, alternative = 'larger')
print('{0:0.3f}'.format(pval), '{0:0.3f}'.format(stat))

```

    0.823 -0.928


## Итог

🤔 \
<span style="color:blue"> 
Разница конверсий статистически не значима, **конверсия сегмента А ровна конверсии сегмента С** составляет:\
       * версия моб. приложения сегмент А >= 116    - 35.15%\
       * версия моб. приложения сегмент С >= 116    - 35.13%</span>    


```python
print('Конверсия заказ/карточка группы А', round(df.iloc[1,0]/df.iloc[0,0]*100, 2), '%')
print('Конверсия заказ/карточка группы C', round(df.iloc[3,0]/df.iloc[2,0]*100, 2), '%')

```

    Конверсия заказ/карточка группы А 35.15 %
    Конверсия заказ/карточка группы C 35.13 %


# <div class="alert alert-success"> <b>(карточка товара) если возможно, то как изменилась покладка из положения экрана ниже строки с элементом "Сравнить" (т.е стали ли чаще добавлять товар в корзину не возвращаясь к началу экрана где мы сейчас выводим стоимость)</div>

🤔 \
<span style="color:blue">Данную конверсию сегментов А и С нет возможности рассмотреть.</span>    

# <div class="alert alert-success"> <b>(экран отзывов) уменьшились ли выходы с экрана отзывов в карточку товара для покладки товара в корзину, или стали чаще добавлять с экрана отзывов</div>

добавления минус удаление со страницы отзывов по сегментам.

🤔 \
<span style="color:blue">Конверсию экран **отзывов / корзина** сегментов А и С рассмотрел выше. Она выросла в 118 версии(большего всего пользователй в этой версии по сравнению с 116 и 117) мобильного приложения на 3,5%. Думаю нет необходимости рассмаотривать конверисю **экран отзывов → карточка / покладка** .</span>    

# <div class="alert alert-success"> <b>Поверим сплитовние сегметов А и С</div>

## <div class="alert alert-info"> <b>Распередление уникальных польхователй по топ 5 источникам и топ 5 городам</div>

### Запрос 


```python
query_4 = """
select  
    uniqIf(uid, test_segment='A') as uniq_A,
    
    uniqIf(uid, test_segment='C') as uniq_C,
    
    uniqIf(uid, test_segment='A' and source in (select source
                                                from
                                                    (select  source, uniq(uid)
                                                    from frodo.event 
                                                    where created_date>='2023-01-29'  
                                                        and test_segment IN ('A', 'C')
                                                        and source_id = 2
                                                    group by source
                                                    order by uniq(uid) desc
                                                    limit 5))) as uniq_A_source,
                                                    
    uniqIf(uid, test_segment='C' and source in (select source
                                                from
                                                    (select  source, uniq(uid)
                                                    from frodo.event 
                                                    where created_date>='2023-01-29'  
                                                        and test_segment IN ('A', 'C')
                                                        and source_id = 2
                                                    group by source
                                                    order by uniq(uid) desc
                                                    limit 5))) as uniq_C_source,
                                                    
    uniqIf(uid, test_segment='A' and settlement_id in (select settlement_id
                                                from
                                                    (select  settlement_id, uniq(uid)
                                                    from frodo.event 
                                                    where created_date>='2023-01-29'  
                                                        and test_segment IN ('A', 'C')
                                                        and source_id = 2
                                                    group by settlement_id
                                                    order by uniq(uid) desc
                                                    limit 5))) as uniq_A_settlement,
                                                    
    uniqIf(uid, test_segment='C' and settlement_id in (select settlement_id
                                                from
                                                    (select  settlement_id, uniq(uid)
                                                    from frodo.event 
                                                    where created_date>='2023-01-29'  
                                                        and test_segment IN ('A', 'C')
                                                        and source_id = 2
                                                    group by settlement_id
                                                    order by uniq(uid) desc
                                                    limit 5))) as uniq_C_settlement
from frodo.event 
where created_date>='2023-02-29'  
    and test_segment IN ('A', 'C')
    and source_id = 2
"""
```


```python
split_uid = eye_load(query_4)
```

### Итог


```python
display(split_uid[['uniq_A','uniq_C','uniq_A_source','uniq_C_source','uniq_A_settlement','uniq_C_settlement']])
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>uniq_A</th>
      <th>uniq_C</th>
      <th>uniq_A_source</th>
      <th>uniq_C_source</th>
      <th>uniq_A_settlement</th>
      <th>uniq_C_settlement</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>39220</td>
      <td>38938</td>
      <td>39213</td>
      <td>38927</td>
      <td>9901</td>
      <td>10128</td>
    </tr>
  </tbody>
</table>
</div>


## <div class="alert alert-info"> <b>Конверсии по сегментам</div>

### <div class="alert alert-warning"> <b>Запрос: Конверсия - покладка в корзину / просмотр карточки</div>


```python
query_5 = """
    select *, count_add_cart/count_item_view as cr
    from 
        (-- добавление в корзину
        select test_segment, uniq(uid) as count_add_cart 
        from frodo.event 
        where created_date>='2023-01-29' 
            and test_segment IN ('A', 'B', 'I', 'C', 'F')
            and source_id = 2
            and page_type_id=521872670
            and event_type_id = 2
            GROUP BY test_segment
        order by uniq(uid) desc) as table_1 
        
    inner join
    
        (-- просмотр товара 
        select test_segment, uniq(uid) as count_item_view 
        from frodo.event 
        where created_date>='2023-01-29' 
        and test_segment IN ('A', 'B', 'I', 'C', 'F')
        and source_id = 2
        and page_type_id=521872670
        and event_type_id = 17
        GROUP BY test_segment
        order by uniq(uid) desc) as  table_2
    
    using test_segment
"""
```


```python
test = eye_load(query_5)
```

### Итог


```python
display(test)
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count_add_cart</th>
      <th>count_item_view</th>
      <th>cr</th>
      <th>test_segment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>41962</td>
      <td>75208</td>
      <td>0.557946</td>
      <td>C</td>
    </tr>
    <tr>
      <th>1</th>
      <td>41791</td>
      <td>75109</td>
      <td>0.556405</td>
      <td>F</td>
    </tr>
    <tr>
      <th>2</th>
      <td>41720</td>
      <td>74896</td>
      <td>0.557039</td>
      <td>A</td>
    </tr>
    <tr>
      <th>3</th>
      <td>41667</td>
      <td>74935</td>
      <td>0.556042</td>
      <td>I</td>
    </tr>
    <tr>
      <th>4</th>
      <td>41362</td>
      <td>73773</td>
      <td>0.560666</td>
      <td>B</td>
    </tr>
  </tbody>
</table>
</div>


### <div class="alert alert-warning"> <b>Запрос: Конверсия - покладка в корзину / просмотр страницы отзывов</div>


```python
query_5 = """
    select *, count_add_cart/count_item_view as cr
    from 
        (-- добавление в корзину
        select test_segment, uniq(uid) as count_add_cart 
        from frodo.event 
        where created_date>='2023-01-29' 
            and test_segment IN ('A', 'B', 'I', 'C', 'F')
            and source_id = 2
            and page_type_id=1769007887
            and event_type_id = 2
            GROUP BY test_segment
        order by uniq(uid) desc) as table_1 
        
    inner join
    
        (-- просмотр товара 
        select test_segment, uniq(uid) as count_item_view 
        from frodo.event 
        where created_date>='2023-01-29' 
        and test_segment IN ('A', 'B', 'I', 'C', 'F')
        and source_id = 2
        and page_type_id=1769007887
        and event_type_id = 1
        GROUP BY test_segment
        order by uniq(uid) desc) as  table_2
    
    using test_segment
"""
```


```python
test = eye_load(query_5)
```

### Итог


```python
display(test)
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count_add_cart</th>
      <th>count_item_view</th>
      <th>cr</th>
      <th>test_segment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>6630</td>
      <td>35714</td>
      <td>0.185641</td>
      <td>C</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5210</td>
      <td>35664</td>
      <td>0.146086</td>
      <td>A</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5143</td>
      <td>35829</td>
      <td>0.143543</td>
      <td>I</td>
    </tr>
    <tr>
      <th>3</th>
      <td>5135</td>
      <td>35691</td>
      <td>0.143874</td>
      <td>F</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5131</td>
      <td>35413</td>
      <td>0.144890</td>
      <td>B</td>
    </tr>
  </tbody>
</table>
</div>


### <div class="alert alert-warning"> <b>Запрос: Конверсия - покладка в избранное / просмотр карточки</div>


```python
query_5 = """
    select *, count_add_cart/count_item_view as cr
    from 
        (-- добавление в корзину
        select test_segment, uniq(uid) as count_add_cart 
        from frodo.event 
        where created_date>='2023-01-29' 
            and test_segment IN ('A', 'B', 'I', 'C', 'F')
            and source_id = 2
            and page_type_id=521872670
            and event_type_id = 3
            GROUP BY test_segment
        order by uniq(uid) desc) as table_1 
        
    inner join
    
        (-- просмотр товара 
        select test_segment, uniq(uid) as count_item_view 
        from frodo.event 
        where created_date>='2023-01-29' 
        and test_segment IN ('A', 'B', 'I', 'C', 'F')
        and source_id = 2
        and page_type_id=521872670
        and event_type_id = 17
        GROUP BY test_segment
        order by uniq(uid) desc) as  table_2
    
    using test_segment
"""
```


```python
test = eye_load(query_5)
```

### Итог


```python
display(test)
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count_add_cart</th>
      <th>count_item_view</th>
      <th>cr</th>
      <th>test_segment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>17121</td>
      <td>74896</td>
      <td>0.228597</td>
      <td>A</td>
    </tr>
    <tr>
      <th>1</th>
      <td>16886</td>
      <td>75115</td>
      <td>0.224802</td>
      <td>F</td>
    </tr>
    <tr>
      <th>2</th>
      <td>16878</td>
      <td>74935</td>
      <td>0.225235</td>
      <td>I</td>
    </tr>
    <tr>
      <th>3</th>
      <td>16846</td>
      <td>73776</td>
      <td>0.228340</td>
      <td>B</td>
    </tr>
    <tr>
      <th>4</th>
      <td>16727</td>
      <td>75208</td>
      <td>0.222410</td>
      <td>C</td>
    </tr>
  </tbody>
</table>
</div>


### <div class="alert alert-warning"> <b>Запрос: Конверсия - покладка в корзину / просмотр карточки Новые клиенты, Старые клиенты</div>


```python
query_6 = """
    select *, count_add_cart/count_item_view as cr 
    from 
        (-- добавление в корзину
        select test_segment, uniq(uid) as count_add_cart 
        from frodo.event 
        where created_date>='2023-01-29' 
            and test_segment IN ('A', 'B', 'I', 'C', 'F')
            and source_id = 2
            and page_type_id=521872670
            and event_type_id = 2
            and uid in (select uid as news_users
                        from dwh.session_rep3
                            where date(started_at) >= '2023-01-29' 
                                and has(
                                        is_new_user,
                                        1
                                        )
                                    )
        GROUP BY test_segment
        order by uniq(uid) desc) as table_1 
        
    inner join
    
        (-- просмотр товара 
        select test_segment, uniq(uid) as count_item_view 
        from frodo.event 
        where created_date>='2023-01-29'  
            and test_segment IN ('A', 'B', 'I', 'C', 'F')
            and source_id = 2
            and page_type_id = 521872670
            and event_type_id = 17
            and uid in (select uid as news_users
                        from dwh.session_rep3
                            where date(started_at) >= '2023-01-29' 
                                and has(
                                        is_new_user,
                                        1
                                        )
                                    )

        GROUP BY test_segment
        order by uniq(uid) desc) as  table_2
    using test_segment
"""

query_7 = """
    select *, count_add_cart/count_item_view as cr 
    from 
        (-- добавление в корзину
        select test_segment, uniq(uid) as count_add_cart 
        from frodo.event 
        where created_date>='2023-01-29' 
            and test_segment IN ('A', 'B', 'I', 'C', 'F')
            and source_id = 2
            and page_type_id=521872670
            and event_type_id = 2
            and uid in (select uid as news_users
                        from dwh.session_rep3
                            where date(started_at) >= '2023-01-29' 
                                and has(
                                        is_new_user,
                                        0
                                        )
                                    )
        GROUP BY test_segment
        order by uniq(uid) desc) as table_1 
        
    inner join
    
        (-- просмотр товара 
        select test_segment, uniq(uid) as count_item_view 
        from frodo.event 
        where created_date>='2023-01-29'  
            and test_segment IN ('A', 'B', 'I', 'C', 'F')
            and source_id = 2
            and page_type_id = 521872670
            and event_type_id = 17
            and uid in (select uid as news_users
                        from dwh.session_rep3
                            where date(started_at) >= '2023-01-29' 
                                and has(
                                        is_new_user,
                                        0
                                        )
                                    )

        GROUP BY test_segment
        order by uniq(uid) desc) as  table_2
    using test_segment
"""
```


```python
test = eye_load(query_6)
test_1 = eye_load(query_7)
```

### Итог


```python
display('Новые юзеры', test)
display('Старые юзеры', test_1)
```


    'Новые юзеры'



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count_add_cart</th>
      <th>count_item_view</th>
      <th>cr</th>
      <th>test_segment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>6630</td>
      <td>35714</td>
      <td>0.185641</td>
      <td>C</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5210</td>
      <td>35664</td>
      <td>0.146086</td>
      <td>A</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5143</td>
      <td>35829</td>
      <td>0.143543</td>
      <td>I</td>
    </tr>
    <tr>
      <th>3</th>
      <td>5135</td>
      <td>35691</td>
      <td>0.143874</td>
      <td>F</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5131</td>
      <td>35413</td>
      <td>0.144890</td>
      <td>B</td>
    </tr>
  </tbody>
</table>
</div>



    'Старые юзеры'



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count_add_cart</th>
      <th>count_item_view</th>
      <th>cr</th>
      <th>test_segment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>41828</td>
      <td>74759</td>
      <td>0.559505</td>
      <td>C</td>
    </tr>
    <tr>
      <th>1</th>
      <td>41663</td>
      <td>74662</td>
      <td>0.558021</td>
      <td>F</td>
    </tr>
    <tr>
      <th>2</th>
      <td>41580</td>
      <td>74429</td>
      <td>0.558653</td>
      <td>A</td>
    </tr>
    <tr>
      <th>3</th>
      <td>41520</td>
      <td>74484</td>
      <td>0.557435</td>
      <td>I</td>
    </tr>
    <tr>
      <th>4</th>
      <td>41233</td>
      <td>73307</td>
      <td>0.562470</td>
      <td>B</td>
    </tr>
  </tbody>
</table>
</div>


### <div class="alert alert-warning"> <b>Запрос: Конверсия - покладка в корзину / просмотр карточки по источникам</div>


```python
query_5 = """
    select *, count_add_cart/count_item_view as cr
    from 
        (-- добавление в корзину
        select test_segment, source, uniq(uid) as count_add_cart 
        from frodo.event 
        where created_date>='2023-01-29' 
            and test_segment IN ('A', 'B', 'I', 'C', 'F')
            and source_id = 2
            and page_type_id=521872670
            and event_type_id = 2
            GROUP BY test_segment, source
        order by uniq(uid) desc
        limit 35) as table_1 
        
    inner join
    
        (-- просмотр товара 
        select test_segment, source, uniq(uid) as count_item_view 
        from frodo.event 
        where created_date>='2023-01-29' 
        and test_segment IN ('A', 'B', 'I', 'C', 'F')
        and source_id = 2
        and page_type_id=521872670
        and event_type_id = 17
        GROUP BY test_segment, source
        order by uniq(uid) desc
        limit 35) as  table_2
    
    using (test_segment, source)
"""
```


```python
test = eye_load(query_5)
test.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count_add_cart</th>
      <th>count_item_view</th>
      <th>cr</th>
      <th>source</th>
      <th>test_segment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>41359</td>
      <td>74341</td>
      <td>0.556342</td>
      <td>direct</td>
      <td>C</td>
    </tr>
    <tr>
      <th>1</th>
      <td>41132</td>
      <td>74239</td>
      <td>0.554048</td>
      <td>direct</td>
      <td>F</td>
    </tr>
    <tr>
      <th>2</th>
      <td>41052</td>
      <td>73997</td>
      <td>0.554779</td>
      <td>direct</td>
      <td>I</td>
    </tr>
    <tr>
      <th>3</th>
      <td>41034</td>
      <td>74018</td>
      <td>0.554379</td>
      <td>direct</td>
      <td>A</td>
    </tr>
    <tr>
      <th>4</th>
      <td>40738</td>
      <td>72939</td>
      <td>0.558522</td>
      <td>direct</td>
      <td>B</td>
    </tr>
  </tbody>
</table>
</div>



### Итог


```python
display(test.pivot_table(index = 'source', columns = 'test_segment', values = 'cr', aggfunc='mean'))
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>test_segment</th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>F</th>
      <th>I</th>
    </tr>
    <tr>
      <th>source</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th></th>
      <td>0.298669</td>
      <td>0.294648</td>
      <td>0.304126</td>
      <td>0.301441</td>
      <td>0.303413</td>
    </tr>
    <tr>
      <th>android</th>
      <td>0.322838</td>
      <td>0.329765</td>
      <td>0.328220</td>
      <td>0.319703</td>
      <td>0.334975</td>
    </tr>
    <tr>
      <th>direct</th>
      <td>0.554379</td>
      <td>0.558522</td>
      <td>0.556342</td>
      <td>0.554048</td>
      <td>0.554779</td>
    </tr>
    <tr>
      <th>ios</th>
      <td>0.311313</td>
      <td>0.283534</td>
      <td>0.282714</td>
      <td>0.277995</td>
      <td>0.291801</td>
    </tr>
    <tr>
      <th>none</th>
      <td>0.275986</td>
      <td>0.255725</td>
      <td>0.288591</td>
      <td>0.288732</td>
      <td>0.313531</td>
    </tr>
    <tr>
      <th>push</th>
      <td>0.198835</td>
      <td>0.173438</td>
      <td>0.193818</td>
      <td>0.183555</td>
      <td>0.186912</td>
    </tr>
    <tr>
      <th>vk</th>
      <td>0.222222</td>
      <td>0.218487</td>
      <td>0.268908</td>
      <td>0.240310</td>
      <td>0.197368</td>
    </tr>
  </tbody>
</table>
</div>


# Изменения в релизах 116, 117, 118

Из интересного в релизах 115 и 116 было:

    • Добавили кнопку «Аналоги» для товаров, которые недоступны в выбранном регионе.
    • Исправили проблему виджета с активным заказом на главном экране, сделали его доступным всем пользователям.
    • Доработали фильтр торговых марок в избранном — выделили СТМ от других.
    • На экране после оформления заказа появился баннер с популярной категорией.


Выложили 117 релиз мобильного приложения, а значит скоро вам прилетит новая версия в которой:

    - приложение будет работать стабильнее, исправлены несколько ошибок.
    - появится возможность редактировать и удалять свои вопросы к товарам. 
    - вы найдёте новые популярные фильтры в каталоге, а значит подобрать нужный товар или подарок к предстоящим праздником станет легче =)


В 118 релизе приложения мы исправили ошибки и добавили некоторые ваши пожелания:

    - В корзине возникала проблема, когда вы хотели снять галочку с товара, а нажимали на сам товар. Мы увеличили область нажатия на галочку, надеемся, станет удобно!

    - Начиная с этой версии будем напоминать про обновление приложения. В профиле появится баннер, если у вас установлена старая версия программы.

# <div class="alert alert-success"> <b>Общий вывод</div>

🤔 \
<span style="color:blue">Думаю, **стоит внести данные изменение в приложение**. Конверсия экран отзывов / корзина выросла, конверсия карточка / корзина не провалилась. + https://docs.google.com/document/d/1XhoLvTt2k4FRPB6IWWpnckoXxdni9zCFx7To30t37Fs/edit показало, что пользователям такое изменение более наглядно предоставляет информацию о товаре, цене, его кол-ве.</span> 
