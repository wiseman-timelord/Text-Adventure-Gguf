# Filename: locations_roleplayers.py

class Location:
    def __init__(self, name, description, items, roleplayers):
        self.name = name
        self.description = description
        self.items = items
        self.roleplayers = roleplayers

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_items(self):
        return self.items

    def get_roleplayers(self):
        return self.roleplayers

locations = {
    'house': Location('House', 'A cozy little house.', ['book', 'lamp'], ['gang', 'friends', 'strangers']),
    'street': Location('Street', 'A busy city street.', ['coin', 'newspaper'], ['police', 'gang', 'strangers']),
    'park': Location('Park', 'A peaceful city park.', ['flower', 'bench'], ['friends', 'strangers']),
    'woods': Location('Woods', 'A dark and mysterious woods.', ['stick', 'stone'], ['gang', 'strangers']),
    'pub': Location('Pub', 'A lively pub.', ['beer', 'dart'], ['friends', 'police', 'strangers']),
    'lake': Location('Lake', 'A serene lake.', ['fish', 'boat'], ['friends', 'strangers']),
    'car': Location('Car', 'A fast-moving car.', ['map', 'key'], ['friends', 'police', 'gang']),
    'van': Location('Van', 'A suspicious van.', ['toolbox', 'rope'], ['gang', 'strangers'])
}
