
class Person(object):
    def __init__(self, params):
        self.name = params['name']
        self.interests = params['interests']
        self.supplies = {}

    def add_supply(self, supply, count):
        if supply not in self.supplies:
            self.supplies[supply] = count
        else:
            self.supplies[supply] += count


person = Person({'name': 'Hector', 'interests': [
                'sewing', 'millinery', 'drawing']})

print(person.name == 'Hector')
print(person.interests == ["sewing", "millinery", "drawing"])
print(person.supplies == {})


class Craft(object):
    def __init__(self, name, supplies_required):
        self.name = name
        self.supplies_required = supplies_required


craft = Craft(
    'knitting', {'yarn': 20, 'scissors': 1, 'knitting_needles': 2})
result1 = {'yarn': 20, 'scissors': 1, 'knitting_needles': 2}

print(craft.name == "knitting")
print(craft.supplies_required == result1)


class Event():
    def __init__(self, name, crafts, attendees):
        self.name = name
        self.crafts = crafts
        self.attendees = attendees

    def attendee_names(self):
        names = []

        for attendee in self.attendees:
            names.append(attendee.name)

        return names
        # map(lambda attendee: attendee.name, self.attendees)
        # list(names)

    def craft_with_most_supplies(self):
        max_value = 0

        for quantity in self.crafts.values():
            if quantity > max_value:
                max_value = quantity

        return max_value


event = Event("Carla's Craft Connection", [craft], [person])

print(event.name == "Carla's Craft Connection")
print(event.crafts == [craft])
print(event.attendees == [person])
person.add_supply('fabric', 4)
person.add_supply('scissors', 1)
print(person.supplies == {"fabric": 4, "scissors": 1})
person.add_supply('fabric', 3)
print(person.supplies == {"fabric": 7, "scissors": 1})

hector = Person({'name': 'Hector', 'interests': [
                'sewing', 'millinery', 'drawing']})
toni = Person({'name': 'Toni', 'interests': ['sewing', 'knitting']})
sewing = Craft('sewing', {'fabric': 5, 'scissors': 1,
                          'thread': 1, 'sewing_needles': 1})
knitting = Craft(
    'knitting', {'yarn': 20, 'scissors': 1, 'knitting_needles': 2})
event2 = Event("Carla's Craft Connection", [sewing, knitting], [hector, toni])

print(event2.attendee_names())
print(event2.attendee_names() == ["Hector", "Toni"])
print(event2.craft_with_most_supplies() == "sewing")
print(event2.supply_list() == [
      "fabric", "scissors", "thread", "sewing_needles", "yarn", "knitting_needles"])
print(hector.can_build(sewing) == false)

hector.add_supply('fabric', 7)
hector.add_supply('thread', 1)

print(hector.can_build(sewing) == false)
hector.add_supply('scissors', 1)
hector.add_supply('sewing_needles', 1)

print(hector.can_build(sewing))
