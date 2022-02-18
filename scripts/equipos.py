
import mysql.connector
import database


def anyadirDatos( cnx, file ):

    file.readline()

    try:
        cursor = cnx.cursor()

        for linea in file:
            nombre, ciudad, conferencia, division = linea.split(";")
            division = division.replace("\n", "")

            add_equipo = ( "INSERT INTO equipos (nombre, ciudad, conferencia, division) VALUES(%s, %s, %s, %s)" )

            cursor.execute( add_equipo, (nombre, ciudad, conferencia, division) )
            cnx.commit()

    except mysql.connector.Error as err:
        print( err )


if __name__ == '__main__':

    cnx = database.connect_db()
    archivo = open( 'loadData/equipos.csv', 'r' )
    anyadirDatos( cnx, archivo )
    database.close_db( cnx )


