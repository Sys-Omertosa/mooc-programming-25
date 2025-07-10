# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.persons = []

    def add(self, person : Person):
        self.persons.append(person)

    def is_empty(self):
        if self.persons:
            return False
        return True

    def print_contents(self):
        print(f"There are {len(self.persons)} persons in the room,"
              f" and their combined height is {sum(person.height for person in self.persons)} cm")
        for person in self.persons:
            print(f"{person.name} ({person.height} cm)")

    def shortest(self):
        if self.is_empty():
            return None
        return min(self.persons, key=lambda x:x.height)

    def remove_shortest(self):
        if self.is_empty():
            return None
        shortest = self.shortest()
        self.persons.remove(shortest)
        return shortest

room = Room()

room.add(Person("Lea", 183))
room.add(Person("Kenya", 172))
room.add(Person("Nina", 162))
room.add(Person("Ally", 166))
room.print_contents()

print()

removed = room.remove_shortest()
print(f"Removed from room: {removed.name}")

print()

room.print_contents()