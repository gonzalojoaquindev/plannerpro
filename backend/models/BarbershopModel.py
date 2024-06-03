from database.db import get_connection
from .entities.Barbershop import Barbershop


class BarbershopModel():

    @classmethod
    def get_barbershops(self):

        try:
            connection = get_connection()
            print("se conecto")
            barbershops = []

            with connection.cursor() as cursor:
                cursor.execute("select * from barbershops")
                resultset = cursor.fetchall()

                for row in resultset:
                    barbershop = Barbershop(row[0], row[1], row[2],
                                            row[3], row[4], row[5], row[6], row[7], row[8],
                                            row[9], row[10])
                    barbershops.append(barbershop.to_JSON())

            connection.close()
            return barbershops
        except Exception as ex:
            print(ex)
            raise Exception(ex)

    @classmethod
    def get_barbershop(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM Barbershops WHERE id = %s", (id,))
                row = cursor.fetchone()
                print('fila:', row)

                barbershop = None
                if row != None:
                    print("pase")
                    barbershop = Barbershop(row[0], row[1], row[2],
                                            row[3], row[4], row[5], row[6], row[7], row[8],
                                            row[9], row[10])
                    print('barber sin parsear', barbershop)
                    barbershop = barbershop.to_JSON()
                    print('barber con parsear', barbershop)
            connection.close()
            return barbershop
        except Exception as ex:
            print(ex)
            raise Exception(ex)

    @classmethod
    def add_barbershop(self, barbershop):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                print(barbershop)
                cursor.execute("""INSERT INTO barbershops (name, city, address, services, attention_hours, branch_office, logo , rating , img , description ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", (
                    barbershop.name, barbershop.city, barbershop.address, barbershop.services, barbershop.attention_hours, barbershop.branch_office, barbershop.logo, barbershop.rating, barbershop.img, barbershop.description))
                print('insertando')
                affected_rows = cursor.rowcount
                connection.commit()
                print(affected_rows)
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception('error', ex)

    @classmethod
    def update_barbershop(self, barbershop):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE barbershops SET name = %s, city = %s, address = %s, services = %s, attention_hours = %s, branch_office = %s, logo = %s, rating = %s, img = %s, description = %s
                                WHERE id = %s""", (barbershop.name, barbershop.city, barbershop.address, barbershop.services, barbershop.attention_hours, barbershop.branch_office, barbershop.logo, barbershop.rating, barbershop.img, barbershop.description, barbershop.id))
                affected_rows = cursor.rowcount
                connection.commit()
                print(affected_rows)

            connection.close()
            return affected_rows
        except Exception as ex:
            print(ex)
            raise Exception(ex)

    @classmethod
    def delete_barbershop(self, barbershop):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM barbershops WHERE id = %s", (barbershop.id))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
