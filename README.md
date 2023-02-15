# Challenge Data Scientist NeuralWorks

Postulante: Ignacio Tapia  
Febrero 2023

### Problema
El problema consiste en predecir la probabilidad de atraso de los vuelos que aterrizan o despegan del aeropuerto de Santiago de Chile (SCL). Para eso les entregamos un dataset usando datos públicos y reales donde cada fila corresponde a un vuelo que aterrizó o despegó de SCL.

### Desafío

**1. ¿Cómo se distribuyen los datos? ¿Qué te llama la atención o cuál es tu conclusión sobre esto?**

Para entender la distribución de los registros en el dataset, se propine una análisis univariado de las variables Vuelos por Ciudad de Origen (SIGLAORI), Vuelos por Ciudad de Destino (SIGLADES), Evolución de la proporción de vuelos (Nacionales e Internacionales) a lo largo del tiempo, Vuelos por Operados, Cantidad de Vuelos por día, día de la semana y mes.

##### SIGLAORI - SIGLADES

![labelname :: Figura 1](https://github.com/ignacioTapia95/neuralworks-challenge-data-scientist/blob/main/notebooks/results/img/01_DATA_DISTR_VUELOS_SIGLAOR-SIGLADES.png)

Un aspecto interesamte de la distribución de los datos es que sólo se tiene información relativa sólo para una Ciudad de Origen (SIGLAORI): Santiago de Chile. Esto lleva a inferir que los registros de la base de datos (y por lo tanto los delays correspondientes) pertenecen solamente a "Despegues" más no a "Aterrizajes". En en lado derecho de la figura precedente, se aprecia que, a diferencia de la ciudad de origen, se tienen múltiples ciudades de destino (SIGLADES), sin embargo, la cantidad de vuelos por ciudad de destino no es homogenea, cuestión que podría afectar el uso de esta variable en un modelo predictivo.

Si ahondamos más en la distribución de los datos de la ciudad de destino, podemos apreciar que, al menos dentro del top-10 de ciudades destino más frecuentes, existe una leve tendencia hacia los destinos nacionales (aún cuando el TOP-1 es Buenos Aires, Argentina). Ya que existe tanta heterogeneidad en la frecuencia de los destinos, será relevante entender el comportamiento de los datos a nivel "agregado". Para ello se utiliza la variable "TIPOVUELO" que nos ayudará a entender cuál es la proproción de vuelos nacionales vs los vuelos internacionales. 

##### Distribución de Vuelos Nacionales vs Internacionales

![labelname :: Figura 2](https://github.com/ignacioTapia95/neuralworks-challenge-data-scientist/blob/main/notebooks/results/img/01_DATA_DISTR_VUELOS_NACIONAL-INTERNACIONAL.png)

La figura de "Evolución Proporción de Vuelos (Nacional e Internacional) por Mes" nos muestra que existe un comportamiento más o menos constante en el tiempo en cuanto a la proporción de vuelos nacionales vs internacionales. Los vuelos nacionales representan, en promedio, el 54% del total de vuelos vs el 46% de vuelos internacionales. La diferencia entre estos dos grupos es estadísticamente significativa (t-stat: 24.52, p-value<0.001). Dado que, operacionalemente podrían existir protocolos distintos en vuelos nacionales e internacionales, esta variable podría ser de gran interés al momento de modelar el delay de despegue.

##### Distribución de Vuelos por Operador

![labelname :: Figura 3](https://github.com/ignacioTapia95/neuralworks-challenge-data-scientist/blob/main/notebooks/results/img/01_DATA_DISTR_VUELOS_OPERADOR.png)

Si bien TIPOVUELO podría ser un factor relevante a considerar para predecir el delay de despegue, cada aerolínea se ajusta a protocolos internos que podrían diferir entre estas, afectando así los tiempos despegupe. Nuevamente, la distribución de los grupos (aerolínas) es bastante heterogenea. Cerca del 60% de los vuelos los concentra Grupo LATAM, lo cuál podría sesgar al modelo provocando un pobre desempeño al tratar de predecir el delay de aerolíneas con menos participación o viceversa, las compañías con menos participación introducen "ruido" al modelo afectando su poder predectivo sobre los vuelos del Grupo LATAM. Sólo para cuantíficar la deferencia en la participación de estos grupos, después del Grupo LATAM, la aerolínea con mayor participación es Sky Airline, con apenas un 20% de los vuelos. El 20% restante se distribuye entre las otras 20 aerolíneas.

Además se propone un análisis bivariado entre OPERADOR y TIPOVUELO. Podemos apreciar que el los vuelos nacional son manejados por 4 aerolineas (Grupo LATAM, Sky Airline, JetSmart SPA y Latin American Wings). Si bien aquí la distrinución entre los grupos sigue siendo bastante heterogenea, esta tiene a moderarse (un poco) con respecto a la distribución global. En vuelos nacionales, Grupo LATAM sigue concentrando aproximadamente el 60% de los vuelos, pero su inmediato competidor es Sky Airline con un 30% aproximadamente.

##### Distribución de Vuelos por Fecha

![labelname :: Figura 4](https://github.com/ignacioTapia95/neuralworks-challenge-data-scientist/blob/main/notebooks/results/img/01_DATA_DISTR_VUELOS_FECHA.png)

Como es de esperarse, la cantidad de despegues se comporta de forma estacional, teniendo peacks en los meses de diciembre a febrero y un no despreciable aumento en el mes de Julio. Ahora bien, el segundo semestre tienen comportamiento (en cantidad) bastante similar a la época éstival. Dado que sólo se tiene un año de muestra (2017) no es posible inferir si esto se trata de un comportamiento normal o es más bien una excepción a la regla.

Más adelante veremos que existen algunas fechas que se consideran "temporada alta" y "temporada baja", pero que, para esta muestra de datos, no necesariamente presentan diferencias significativas entre ellas.

##### Distribución de Vuelos por Día de la Semana

![labelname :: Figura 5](https://github.com/ignacioTapia95/neuralworks-challenge-data-scientist/blob/main/notebooks/results/img/01_DATA_DISTR_VUELOS_DIA-SEMANA.png)

La gráfica anterior nos muestra una visible diferencia en la cantidad de vuelos promedio existentes en días hábiles (luneas a viernes) y los realizados durante los fines de semana.


**2. Genera las columnas adicionales y luego expórtelas en un archivo synthetic_features.csv**

|Nueva Variable|Descripción|
|-|-|
|Temporada_alta | 1 si Fecha-I está entre 15-Dic y 3-Mar, o 15-Jul y 31-Jul, o 11-Sep y 30-Sep, 0 si no.|
|dif_min | diferencia en minutos entre Fecha-O y Fecha-I |
|atraso_15 | 1 si dif_min > 15, 0 si no.|
|periodo_dia | mañana (entre 5:00 y 11:59), tarde (entre 12:00 y 18:59) y noche (entre 19:00 y 4:59), en base a Fecha-I .|

https://github.com/ignacioTapia95/neuralworks-challenge-data-scientist/blob/main/data/output/synthetic_features.csv


**3. ¿Cómo se compone la tasa de atraso por destino, aerolínea, mes del año, día de la semana, temporada, tipo de vuelo? ¿Qué variables esperarías que más influyeran en predecir atrasos?**

Hasta el momento hemos analizados solamente la distribución de las variables independientes, las cuales nos ayudará a modela el delay de despegue. Ahora pasaremos a un análisis bivariado, en donde podamos comparar aquellos grupos que identificamos en estas variables, con respecto a la variable de delay.

Es importante tener en consideración que 2 cada 10 vuelos que despegan en Santiago de Chile lo hacen con delay mayor a 15 minutos. Teniendo esto en cuenta, veámos cómo se comporta este indice dependiente de la ciudad de destinto.

##### Tasa de Atraso 15 minutos por Ciudad de Destino
![labelname :: Figura 6](https://github.com/ignacioTapia95/neuralworks-challenge-data-scientist/blob/main/notebooks/results/img/02_DELAY_ANALYSIS_CIUDAD-DESTINO.png)

¡Es sorprendente apreciar que las 3 ciudades al tope del gráfico tienen un 100% de vuelos con delay! Pero no nos olvidemos que la frecuencia de vuelos hacia ciertos destinos es muy baja, por lo que debemos revisar estos casos. 

|SIGLADES|CANTIDAD_VUELOS|TASA_ATRASO|DESV_EST| 			
|--|--|--|--|
|Quito          |	2 |	1.000000 |	0.000000|
|Puerto Stanley |1    |	1.000000 |	NaN|
Cochabamba      |	1 |	1.000000 |	NaN|
|Ushuia         |	6 |	0.666667 |0.516398|
|Sydney         |194  | 0.582474 |	0.494427|

Las primeras 3 ciudades tienen a lo más 2 despegues desde Santiago. Si tomamos este historial e intentamos predecir si es que existirá una atraso en el siguiente vuelo hacia estos destinos, probablemente la predicción sea afirmativa. Sin embargo, esta predicción se basa en una muestre de tamaño 2 (a lo más), por lo que carece de rigurisiad. Tendremos que tener mucho cuidado con la ciudad de origen al momento de predecir.

##### Tasa de Atraso 15 minutos por Operador

![labelname :: Figura 7](https://github.com/ignacioTapia95/neuralworks-challenge-data-scientist/blob/main/notebooks/results/img/02_DELAY_ANALYSIS_OPERADOR.png)

Pareciera ser que, para las aerolineas, ahora si tenemos un comportamiento más esperable en el nivel de delay, es decir, no tenemos ni tasas 0% ni tasas 100% de delay, es más la tasa de delay más pequeña corresponda a la aerolinea Aeromexico con una tasa del 0.28% (n=351 vuelos) (3 de cada 1000 vuelos tienen delay), mientras que la aerolinea con mayor delay es PLus Ultra Lineas Aereas con una tasa del 61% (n=49 vuelos).


##### Tasa de Atraso 15 minutos por Mes

![labelname :: Figura 8](https://github.com/ignacioTapia95/neuralworks-challenge-data-scientist/blob/main/notebooks/results/img/02_DELAY_ANALYSIS_MES.png)

Los meses de alta demanda (mes 7 y 12) tienen a su vez una mayor tasa de delay de despegue. 