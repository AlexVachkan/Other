# Изменения в карточке товара

![image](/uploads/0c1a0e67a0bfc4763efeb5ba05658837/image.png)

# Изменения на странице отзывов товара.

![image](/uploads/e6378d6a46349243238d2ef621d0d199/image.png)

**Основная проверяемая гипотеза:**
Если стоимость товара, и его количество будет всегда на виду, то увеличится конверсия в покладку товаров в корзину с карточки и с страницы отзывов.

**Целевая метрика:** 1. Конверсия карточка/корзина; 2. Конверсия страница баннера/корзина.

**Вспомогательная метрика:** 1. Конверсия спасибо за заказ; 2. Конверсия отказы клиентов после добавления в корзину сегментов А и С. 

**Результаты тестирования:**

Гипотезу нельзя опровергнуть.. Конверсия страница отзывов/корзина увеличилась. Конверсия карточка/корзина не изменилась.

**Мотивация решения:**

Изменение кнопки корзины на страницы отзывов в мобильном приложение положительно отразилось на конверсии пользователей. В карточке товара изменение кнопки корзины не повлияло на конверсию, но ux-исследование показало, что информация на кнопке лучше воспринимается.

**Подробное исследование**
https://jupyter.sima-land.local/user/vechk_aa/lab/workspaces/auto-h/tree/analytics/Vechkanov/ab_reports_1336.ipynb

# <div class="alert alert-success"> <b>Конверсия отказы клиентов после добавления в корзину сегментов А и С</div>


|test_segment |min_qty_category | users|
|----------|------------|---------|
|A     |       Группа     |       109748|
|      |       Одиночный   |      406655|
|B     |       Группа       |     112508|
|      |       Одиночный    |     418351|


![image](https://user-images.githubusercontent.com/108777771/223948462-96906e2d-af6a-4715-a7a7-357af5564543.png)


## Итог

🤔 \
<span style="color:blue"> 
Гипотеза - 'отказы клиентов, после добавления товара в корзину товар стали меньше удалять'.\
Разница конверсий добавление в корзину / отказ в групповых товарах и одиночных товарах в сегментах A и C отсутсвует. </span>

# <div class="alert alert-success"> <b>Посчитаем среднии конверсии отзывы/покладка групп А и С с обрезанием выбросов</div>


<div>
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


<div>
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

## Проверка ttest

Стьюдентный критерий для парных выборок используется для сравнения средних значений двух выборок, когда каждое наблюдение в одной выборке может быть сопоставлено с наблюдением в другой выборке.


<div>
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

   H_0 : Средняя конверсии в группе А и группе С ровна\
   H_1 : Средняя коверсия в группе С больше средней конверсии группы А

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


# <div class="alert alert-success"> <b>Посчитаем среднии конверсии карточка/покладка групп А и С с обрезанием выбросов</div>

<div>
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

<div>
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

## Проверка ttest

Стьюдентный критерий для парных выборок используется для сравнения средних значений двух выборок, когда каждое наблюдение в одной выборке может быть сопоставлено с наблюдением в другой выборке.



<div>
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
   H_0 : Средняя конверсии в группе А и группе С ровна\
   H_1 : Средняя коверсия в группе С больше средней конверсии группы А


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

<div>

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


   H_0 : Пропорции равны\
   H_1 : Пропорция сегмента А больше пропорции сегмента C

   pval = 0.823 


## Итог

🤔 \
<span style="color:blue"> 
Разница конверсий статистически не значима, **конверсия сегмента А ровна конверсии сегмента С** составляет:\
       * версия моб. приложения сегмент А >= 116    - 35.15%\
       * версия моб. приложения сегмент С >= 116    - 35.13%</span>    

# <div class="alert alert-success"> <b>(карточка товара) если возможно, то как изменилась покладка из положения экрана ниже строки с элементом "Сравнить" (т.е стали ли чаще добавлять товар в корзину не возвращаясь к началу экрана где мы сейчас выводим стоимость)</div>

🤔 \
<span style="color:blue">Данную конверсию сегментов А и С нет возможности рассмотреть.</span>    

# <div class="alert alert-success"> <b>(экран отзывов) уменьшились ли выходы с экрана отзывов в карточку товара для покладки товара в корзину, или стали чаще добавлять с экрана отзывов</div>

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>mean_add_del_A</th>
      <th>mean_add_del_C</th>
      <th>mean_add_del_A_116</th>
      <th>mean_add_del_C_116</th>
      <th>mean_add_del_A_117</th>
      <th>mean_add_del_C_117</th>
      <th>mean_add_del_A_118</th>
      <th>mean_add_del_C_118</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>170.05</td>
      <td>238.275</td>
      <td>70.7</td>
      <td>100.225</td>
      <td>58.7</td>
      <td>81.025</td>
      <td>40.9</td>
      <td>57.25</td>
    </tr>
  </tbody>
</table>
</div>



## Итог

🤔 \
<span style="color:blue"> 
Видно, что средняя разница добавления в корзину и потом удаление в сегменте А меньше чем в сегменте С. т.е. в сегменте С остается больше товаров в корзине, что подтверждает увеличение конверсии из страницы отзывов/корзина</span>  
