
class Barber():
    def __init__(self, id, name='none', city='none', speciality='none', gender='none', rankin='none') -> None:
        self.id = id
        self.name = name
        self.city = city
        self.speciality = speciality
        self.gender = gender
        self.rankin = rankin

    def to_JSON(self):
        return {
            'id': self.id,
            'name': self.name,
            'city': self.city,
            'speciality': self.speciality,
            'gender': self.gender,
            'rankin': self.rankin
        }
