# Challenge Data Scientist NeuralWorks

Postulante: Ignacio Tapia
Febrero 2023

### Problema
El problema consiste en predecir la probabilidad de atraso de los vuelos que aterrizan o despegan del aeropuerto de Santiago de Chile (SCL). Para eso les entregamos un dataset usando datos públicos y reales donde cada fila corresponde a un vuelo que aterrizó o despegó de SCL.

### Desafío

1. ¿Cómo se distribuyen los datos? ¿Qué te llama la atención o cuál es tu conclusión sobre esto?  

Para entender la distribución de los registros en el dataset, se propine una análisis univariado de las variables Vuelos por Ciudad de Origen (SIGLAORI), Vuelos por Ciudad de Destino (SIGLADES), Evolución de la proporción de vuelos (Nacionales e Internacionales) a lo largo del tiempo, Vuelos por Operados, Cantidad de Vuelos por día, día de la semana y mes.

![labelname :: Figura 1](https://github.com/ignacioTapia95/neuralworks-challenge-data-scientist/blob/main/notebooks/results/img/01_DATA_DISTR_VUELOS_SIGLAOR-SIGLADES.png)

Un aspecto interesamte de la distribución de los datos es que sólo se tiene información relativa sólo para una Ciudad de Origen (SIGLAORI): Santiago de Chile. Esto lleva a inferir que los registros de la base de datos (y por lo tanto los delays correspondientes) pertenecen solamente a "Despegues" más no a "Aterrizajes". En en lado derecho de la figura precedente, se aprecia que, a diferencia de la ciudad de origen, se tienen múltiples ciudades de destino (SIGLADES), sin embargo, la cantidad de vuelos por ciudad de destino no es homogenea, cuestión que podría afectar el uso de esta variable en un modelo predictivo.

Si ahondamos más en la distribución de los datos de la ciudad de destino, podemos apreciar que, al menos dentro del top-10 de ciudades destino más frecuentes, existe una leve tendencia hacia los destinos nacionales (aún cuando el TOP-1 es Buenos Aires, Argentina). Ya que existe tanta heterogeneidad en la frecuencia de los destinos, será relevante entender el comportamiento de los datos a nivel "agregado". Para ello se utiliza la variable "TIPOVUELO" que nos ayudará a entender cuál es la proproción de vuelos nacionales vs los vuelos internacionales. 

![labelname :: Figura 2](https://github.com/ignacioTapia95/neuralworks-challenge-data-scientist/blob/main/notebooks/results/img/01_DATA_DISTR_VUELOS_NACIONAL-INTERNACIONAL.png)

La figura de "Evolución Proporción de Vuelos (Nacional e Internacional) por Mes" nos muestra que existe un comportamiento más o menos constante en el tiempo en cuanto a la proporción de vuelos nacionales vs internacionales. Los vuelos nacionales representan, en promedio, el 54% del total de vuelos vs el 46% de vuelos internacionales. La diferencia entre estos dos grupos es estadísticamente significativa (t-stat: 24.52, p-value<0.001). Dado que, operacionalemente podrían existir protocolos distintos en vuelos nacionales e internacionales, esta variable podría ser de gran interés al momento de modelar el delay de despegue.




Además se propone un análisis bivariado entre OPERADOR y SIGLADES. 