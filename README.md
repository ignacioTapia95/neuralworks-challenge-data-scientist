# Challenge Data Scientist NeuralWorks

Postulante: Ignacio Tapia
Febrero 2023

### Problema
El problema consiste en predecir la probabilidad de atraso de los vuelos que aterrizan o despegan del aeropuerto de Santiago de Chile (SCL). Para eso les entregamos un dataset usando datos públicos y reales donde cada fila corresponde a un vuelo que aterrizó o despegó de SCL.

### Desafío

1. ¿Cómo se distribuyen los datos? ¿Qué te llama la atención o cuál es tu conclusión sobre esto?  

Para entender la distribución de los registros en el dataset, se propine una análisis univariado de las variables Vuelos por Ciudad de Origen (SIGLAORI), Vuelos por Ciudad de Destino (SIGLADES), Evolución de la proporción de vuelos (Nacionales e Internacionales) a lo largo del tiempo, Vuelos por Operados, Cantidad de Vuelos por día, día de la semana y mes.

![labelname :: Figura 1](https://github.com/ignacioTapia95/neuralworks-challenge-data-scientist/blob/main/notebooks/results/img/01_DATA_DISTR_VUELOS_SIGLAOR-SIGLADES.png)

Un aspecto

Además se propone un análisis bivariado entre OPERADOR y SIGLADES. 