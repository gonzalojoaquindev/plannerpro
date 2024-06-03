
class Barbershop():
    def __init__(self, id, name='none', city='none', address='none', services='none', attention_hours='none', branch_office='none', logo='none', rating='none', img='none', description='none') -> None:
        self.id = id
        self.name = name
        self.city = city
        self.address = address
        self.services = services
        self.attention_hours = attention_hours
        self.branch_office = branch_office
        self.logo = logo
        self.rating = rating
        self.img = img
        self.description = description

    def to_JSON(self):
        return {
            'id': self.id,
            'name': self.name,
            'city': self.city,
            'address': self.address,
            'services': self.services,
            'attention_hours': self.attention_hours,
            'branch_office': self.branch_office,
            'logo': self.logo,
            'rating': self.rating,
            'img': self.img,
            'description': self.description
        }
