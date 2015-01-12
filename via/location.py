import via.data
import via.error

class Location:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coordinates = (x, y)

    def get_neighbour(self, direction):
        if direction == 'east':
            neighbour = (self.x + 1, self.y)
        elif direction == 'south':
            neighbour = (self.x, self.y + 1)
        elif direction == 'west':
            neighbour = (self.x - 1, self.y)
        elif direction == 'north':
            neighbour = (self.x, self.y - 1)
        elif direction == 'northeast':
            neighbour = (self.x + 1, self.y - 1)
        elif direction == 'northwest':
            neighbour = (self.x - 1, self.y - 1)
        elif direction == 'southeast':
            neighbour = (self.x + 1, self.y + 1)
        elif direction == 'southwest':
            neighbour = (self.x - 1, self.y + 1)

        if (neighbour[0] < 0 or
            neighbour[1] < 0 or
            neighbour[0] > via.data.plan['width'] - 1 or
            neighbour[1] > via.data.plan['height'] - 1):
            raise via.error.LocationRangeError

        return type(self)(neighbour[0], neighbour[1])

    def get_neighbours(self):
        return self._get_neighbours_in_directions(
            ('northwest', 'north', 'northeast', 'east',
            'southeast', 'south', 'southwest', 'west')
        )

    def get_cardinal_neighbours(self):
        return self._get_neighbours_in_directions(
            ('north', 'east', 'south', 'west')
        )

    def _get_neighbours_in_directions(self, directions):
        neighbours = {}

        for direction in directions:
            try:
                neighbours[direction] = self.get_neighbour(direction)
            except via.error.LocationRangeError:
                pass

        return neighbours
