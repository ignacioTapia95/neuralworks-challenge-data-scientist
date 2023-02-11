def temporada_alta(fecha_i, return_values:list=[1,0]):
    
    '''
    Determina si la fecha programada del vuelo pertenece a temporada alta.
    
    Temporada Alta:
        1) Entre 15-DIC y 03-MAR
        2) Entre 15-JUL y 31-JUL
        3) Entre 11-SEP y 30-SEP

    Parameters
    ----------
    fecha_i : date, datetime, timestamp
        Fecha y hora programada del vuelo 
    return_values : list, default:[1,0]
        Lista con la definición de valor verdadero o falso. Si la fecha se encuentra en la definición de
        temporada alta, retorna list[0] de lo contrario list[1]. Por defecto [1,0].

    Returns
    -------
    return_values:
        return_values[0] si la fecha está en temporada alta
        return_values[1] si la fecha no está en temporada alta
    '''
    
    month = fecha_i.month
    day = fecha_i.day
    
    # Temporada Alta 1
    if (month==12 and day>=15) or (month<3) or (month==3 and day<=3):
        return return_values[0]
    
    # Temporada Alta 2
    elif month==7 and (15<=day<=31):
        return return_values[0]
    
    # Temporada Alta 3
    elif month==9 and (11<=day<=30):
        return return_values[0]
    
    else:
        return return_values[1]
    
    
def periodo_dia(fecha_i):
    
    '''
    Determina a qué periodo del día (mañana, tarde, noche) pertenece la hora programada del vuelo.
    
    Periodo del Día:
        1) Mañana: entre las 05:00:00 y las 11:59:59
        2) Tarde: entre las 12:00:00 y las 18:59:59
        3) Noche: entre las 19:00:00 y las 04:59:59

    Parameters
    ----------
    fecha_i : date, datetime, timestamp
        Fecha y hora programada del vuelo 

    Returns
    -------
    periodo : string
        1) mañana: si fecha_i.hour entre las 05:00:00 y las 11:59:59
        2) tarde: si fecha_i.hour entre las 12:00:00 y las 18:59:59
        3) noche: si fecha_i.hour entre las 19:00:00 y las 04:59:59
    '''
    
    
    flight_time = fecha_i.hour
    
    if 5 <= flight_time < 12:
        return 'mañana'
    elif 12 <= flight_time < 19:
        return 'tarde'
    else:
        return 'noche'