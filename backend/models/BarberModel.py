from database.db import get_connection
from .entities.Barber import Barber


class BarberModel():

    @classmethod
    def get_barbers(self):

        try:
            connection = get_connection()
            print("se conecto")
            barbers = []

            with connection.cursor() as cursor:
                cursor.execute("select * from barbers")
                resultset = cursor.fetchall()

                for row in resultset:
                    barber = Barber(row[0], row[1], row[2],
                                    row[3], row[4], row[5])
                    barbers.append(barber.to_JSON())

            connection.close()
            return barbers
        except Exception as ex:
            print(ex)
            raise Exception(ex)

    @classmethod
    def get_barber(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM Barbers WHERE id = %s", (id,))
                row = cursor.fetchone()
                print('fila:', row)

                barber = None
                if row != None:
                    print("pase")
                    barber = Barber(row[0], row[1], row[2],
                                    row[3], row[4], row[5])
                    print('barber sin parsear', barber)
                    barber = barber.to_JSON()
                    print('barber con parsear', barber)
            connection.close()
            return barber
        except Exception as ex:
            print(ex)
            raise Exception(ex)

    @classmethod
    def add_barber(self, barber):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                print(barber)
                cursor.execute("""INSERT INTO barbers (name, city, speciality, gender, rankin) VALUES (%s, %s, %s, %s, %s)""", (
                    barber.name, barber.city, barber.speciality, barber.gender, barber.rankin))
                print('insertando')
                affected_rows = cursor.rowcount
                connection.commit()
                print(affected_rows)
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception('error', ex)

    @classmethod
    def update_barber(self, barber):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE barbers SET name = %s, city = %s, speciality = %s, gender = %s, rankin = %s
                                WHERE id = %s""", (barber.name, barber.city, barber.speciality, barber.gender, barber.rankin, barber.id))
                affected_rows = cursor.rowcount
                connection.commit()
                print(affected_rows)

            connection.close()
            return affected_rows
        except Exception as ex:
            print(ex)
            raise Exception(ex)

    @classmethod
    def delete_barber(self, barber):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM barbers WHERE id = %s", (barber.id))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
