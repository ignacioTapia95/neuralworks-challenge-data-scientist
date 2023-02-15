def temporada_alta(fecha_i, enriched=False):
    
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
    enriched : bool, default:False
        Boolean que determina el valor a retornar. Si enriched=True, entonces
        la función retorna:
            1: Entre 15-DIC y 03-MAR
            2: Entre 15-JUL y 31-JUL
            3: Entre 11-SEP y 30-SEP
            0: Para todo lo demás.
        
        Si enriched=False, entonces la función retorna 1 si la fecha de vuelo
        se encuentra en temporada alta, independiente de cuál sea esta y 0
        para todo lo demás.

    Returns
    -------
    return_values:
        1 si la fecha está en temporada alta
        0 si la fecha no está en temporada alta
    '''
    
    month = fecha_i.month
    day = fecha_i.day
    
    if enriched:
        # Temporada Alta 1
        if (month==12 and day>=15) or (month<3) or (month==3 and day<=3):
            return 1

        # Temporada Alta 2
        elif month==7 and (15<=day<=31):
            return 2

        # Temporada Alta 3
        elif month==9 and (11<=day<=30):
            return 3

        else:
            return 0
    
    elif not enriched:
        
        # Temporada Alta 1
        if (month==12 and day>=15) or (month<3) or (month==3 and day<=3):
            return 1

        # Temporada Alta 2
        elif month==7 and (15<=day<=31):
            return 1

        # Temporada Alta 3
        elif month==9 and (11<=day<=30):
            return 1

        else:
            return 0

    
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