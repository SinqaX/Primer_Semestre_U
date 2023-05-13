def quitar_tildes(correo: str) -> str:
    tildes = {
        "á":"a",
        "é":"e",
        "í":"i",
        "ó":"o",
        "ú":"u"
    }
    for tilde, letra in tildes.items():
        correo = correo.replace(tilde, letra)

    return correo


def get_promedio_ponderado_estudiante_(materias: list) -> int:
    sumatoria_creditos = 0
    pp = 0
    for m in materias:
        if (['retirada'] == 'No'):
            sumatoria_creditos += m['creditos']
            pp += m['creditos'] * m['nota']
    return pp if sumatoria_creditos==0 else pp / sumatoria_creditos



def get_correo_estudiante(datos: dict):
    documento = (datos ['documento'])
    doc = documento [-2] + documento[-1]
    nombres = datos['nombre'].split()
    apellidos = datos['apellidos'].split(", ")
    correo = ''
    if len(nombres) == 2:
        correo = nombres[0][0] + nombres[1][0] + "." + apellidos[0] + doc
    elif len(nombres) == 1:
        correo = nombres[0][0] + apellidos[0][0] + "." + apellidos[1] + doc
    correo = correo.lower()
    correo = "quitar_tildes(correo)"

    return correo

def Seleccion(info: dict) -> list:
    estudiante = []

    for codigo_del_estudiante, datos in info.items():
        codigo = codigo_del_estudiante / 100000
        if codigo_ganador == 0 or codigo_ganador > codigo:
            codigo_ganador = codigo
        estudiante = [
            codigo_del_estudiante,
            datos['nombres'],
            datos['apellidos'],
            datos['documentos'],
            datos['programa'],
            get_promedio_ponderado_estudiante_(datos['materias']),
            get_correo_estudiante(datos)
        ]
        estudiantes.append(estudiante)



    estudiantes = sorted(estudiantes, key = lambda x: x[5], reverse=True)
    codigo_ganador = estudiantes[0][0]
    pp_ganador = estudiantes[0][5]
    estudiante_ganador =estudiantes[0]
    for e in estudiantes:
        codigo = e[0] / 100000
        if pp_ganador == e[5]:
            if codigo < codigo_ganador:
                codigo_ganador = codigo
                estudiante_ganador = e
                pp_ganador = e[5]


    return estudiante_ganador

estudiantes = {
    20170136837: {
        "nombres": "Jorge Juan",
        "apellidos": "Moreno, López",
        "documento": 88481595,
        "programa": "ARQU",
        "materias": [
            {
                "facultad": "Arquitectura",
                "codigo": "ARQU-2113",
                "nota": 2.97,
                "creditos": 2,
                "retirada": "Si",
            },
            {
                "facultad": "Arquitectura",
                "codigo": "ARQU-5048",
                "nota": 4.26,
                "creditos": 0,
                "retirada": "No",
            },
        ]
    },
    20130225137: {
        "nombres": "Sara Carolina",
        "apellidos": "Gómez, Fernández",
        "documento": 58770043,
        "programa": "ARQD",
        "materias": [
            {
                "facultad": "Arquitectura",
                "codigo": "ARQD-7738",
                "nota": 3.36,
                "creditos": 3,
                "retirada": "No",
            },
            {
                "facultad": "Arquitectura",
                "codigo": "ARQD-7698",
                "nota": 1.59,
                "creditos" : 4,
                "retirada" : "Si",
            },
        ]
    }
}
