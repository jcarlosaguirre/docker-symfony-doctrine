
import mysql.connector
import database


def anyadirDatos( cnx, file ):

    file.readline()

    try:
        cursor = cnx.cursor()

        for linea in file:
            temporada, jugador, puntos_por_partido, asistencias_por_partido, tapones_por_partido, rebotes_por_partido = linea.split(";")
            rebotes_por_partido = rebotes_por_partido.replace("\n", "")

            add_estadisticas = ( "INSERT INTO estadisticas (temporada, jugador, puntos_por_partido, asistencias_por_partido, tapones_por_partido, rebotes_por_partido) VALUES(%s, %s, %s, %s, %s, %s)" )

            cursor.execute( add_estadisticas, (temporada, jugador, puntos_por_partido, asistencias_por_partido, tapones_por_partido, rebotes_por_partido) )
            cnx.commit()

    except mysql.connector.Error as err:
        print( err )


if __name__ == '__main__':

    cnx = database.connect_db()
    archivo = open( 'loadData/estadisticas.csv', 'r' )
    anyadirDatos( cnx, archivo )
    database.close_db( cnx )