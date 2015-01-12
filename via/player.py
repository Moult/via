import random
import via.data
import via.error
from via.location import Location

class Player:

    def __init__(self, dungeon, message):
        self._dungeon = dungeon
        self._message = message
        self.name = None
        self.race = None
        self.profession = None
        self.experience_points = 0
        self.health = 0
        self.health_max = 0
        self.mana = 0
        self.mana_max = 0
        self.branch = 'valley'
        self.level = 0
        self.location = Location(0, 0)
        self.time_played = 0
        self.turns_played = 0

    def generate(self, name):
        self.name = name
        self.race = random.choice(list(via.data.races.values()))
        self.profession = random.choice(list(via.data.professions.values()))
        self.health = self.health_max = self._generate_health()
        self.mana = self.mana_max = self._generate_mana()

    def move(self, direction):
        dungeon = self._dungeon.get(self.branch, self.level)

        try:
            destination = self.location.get_neighbour(direction)
        except via.error.LocationRangeError:
            return self._message.add('You are unable to move that way.')

        if dungeon.is_traversable(destination):
            self.location = destination

    def finish_turn(self):
        self.turns_played += 1

    def _generate_health(self):
        return random.randint(
            self.race['health_min'] + self.profession['health_bonus_min'],
            self.race['health_max'] + self.profession['health_bonus_max']
        )

    def _generate_mana(self):
        return random.randint(
            self.race['mana_min'] + self.profession['mana_bonus_min'],
            self.race['mana_max'] + self.profession['mana_bonus_max']
        )
