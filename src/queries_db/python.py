def checkPlaySuffle(playList):

    assert isinstance(playList, dict)

    # creo una lista con los valores del diccionario playList,
    # es decir, los titulos de las canciones.
    listaCanciones = list(playList.values())

    # chequeo que cada titulo solo aparezca una vez en la lista
    for item in listaCanciones:
        if listaCanciones.count(item) > 1:
            return False
    return True
