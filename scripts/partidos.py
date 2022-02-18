
import mysql.connector
import database


def anyadirDatos( cnx, file ):

    file.readline()

    try:
        cursor = cnx.cursor()

        for linea in file:
            codigo, equipo_local, equipo_visitante, puntos_local, puntos_visitante, temporada = linea.split(";")
            temporada = temporada.replace("\n", "")

            add_partidos = ( "INSERT INTO partidos (codigo, equipo_local, equipo_visitante, puntos_local, puntos_visitante, temporada) VALUES(%s, %s, %s, %s, %s, %s)" )

            cursor.execute( add_partidos, (codigo, equipo_local, equipo_visitante, puntos_local, puntos_visitante, temporada) )
            cnx.commit()

    except mysql.connector.Error as err:
        print( err )


if __name__ == '__main__':

    cnx = database.connect_db()
    archivo = open( 'loadData/partidos.csv', 'r' )
    anyadirDatos( cnx, archivo )
    database.close_db( cnx )