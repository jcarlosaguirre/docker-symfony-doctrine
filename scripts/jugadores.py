
import mysql.connector
import database


def anyadirDatos( cnx, file ):

    file.readline()

    try:
        cursor = cnx.cursor()

        for linea in file:
            codigo, nombre, procedencia, altura, peso, posicion, nombre_equipo = linea.split(";")
            nombre_equipo = nombre_equipo.replace("\n", "")

            add_jugadores = ( "INSERT INTO jugadores (codigo, nombre, procedencia, altura, peso, posicion, nombre_equipo) VALUES(%s, %s, %s, %s, %s, %s, %s)" )

            cursor.execute( add_jugadores, (codigo, nombre, procedencia, altura, peso, posicion, nombre_equipo) )
            cnx.commit()

    except mysql.connector.Error as err:
        print( err )


if __name__ == '__main__':

    cnx = database.connect_db()
    archivo = open( 'loadData/jugadores.csv', 'r' )
    anyadirDatos( cnx, archivo )
    database.close_db( cnx )