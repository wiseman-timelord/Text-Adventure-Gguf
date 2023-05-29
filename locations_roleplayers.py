# Filename: locations_roleplayers.py

class Roleplayer:
    def __init__(self, name, description, maturity):
        self.name = name
        self.description = description
        self.maturity = maturity

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_maturity(self):
        return self.maturity

class Location:
    def __init__(self, name, description, maturity, roleplayers):
        self.name = name
        self.description = description
        self.maturity = maturity
        self.roleplayers = roleplayers

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_maturity(self):
        return self.maturity

    def get_roleplayers(self):
        return self.roleplayers

    def add_roleplayer(self, roleplayer):
        self.roleplayers.append(roleplayer)

    def remove_roleplayer(self, roleplayer):
        self.roleplayers.remove(roleplayer)

locations = {
    'house': Location('House', 'A cozy little house.', 'clean', [Roleplayer('gang', 'A group of friends.', 'moderate'), Roleplayer('friends', 'Your close friends.', 'clean'), Roleplayer('strangers', 'People you do not know.', 'lewd')]),
    'street': Location('Street', 'A busy city street.', 'moderate', [Roleplayer('police', 'Officers maintaining law and order.', 'clean'), Roleplayer('gang', 'A group of friends.', 'moderate'), Roleplayer('strangers', 'People you do not know.', 'lewd')]),
    'park': Location('Park', 'A peaceful city park.', 'clean', [Roleplayer('friends', 'Your close friends.', 'clean'), Roleplayer('strangers', 'People you do not know.', 'lewd')]),
    'woods': Location('Woods', 'A dark and mysterious woods.', 'lewd', [Roleplayer('gang', 'A group of friends.', 'moderate'), Roleplayer('strangers', 'People you do not know.', 'lewd')]),
    'pub': Location('Pub', 'A lively pub.', 'moderate', [Roleplayer('friends', 'Your close friends.', 'clean'), Roleplayer('police', 'Officers maintaining law and order.', 'clean'), Roleplayer('strangers', 'People you do not know.', 'lewd')]),
    'lake': Location('Lake', 'A serene lake.', 'clean', [Roleplayer('friends', 'Your close friends.', 'clean'), Roleplayer('strangers', 'People you do not know.', 'lewd')]),
    'car': Location('Car', 'A fast-moving car.', 'moderate', [Roleplayer('friends', 'Your close friends.', 'clean'), Roleplayer('police', 'Officers maintaining law and order.', 'clean'), Roleplayer('gang', 'A group of friends.', 'moderate')]),
    'van': Location('Van', 'A suspicious van.', 'lewd', [Roleplayer('gang', 'A group of friends.', 'moderate'), Roleplayer('strangers', 'People you do not know.', 'lewd')])
}
