import random
import via.data
from via.location import Location

class Valley:

    plan = None

    def generate(self):
        self.plan = []
        self._create_plan()

        self._grow_shape(via.data.tiles['mountain'])
        self._grow_noiselike(
            via.data.tiles['void'],
            via.data.tiles['mountain'],
            via.data.tiles['plain']
        )
        self._grow_cellular(via.data.tiles['plain'])

        self._grow_bushlike(
            via.data.tiles['wasteland'],
            [self._get_wasteland_source()],
            [],
            2
        )

        self._convert_mountains_next_to_plains_to_hills()

        river_source = self._get_river_source()
        river_tiles, current_river_location = self._grow_walklike(
            via.data.tiles['river'],
            river_source,
            30,
            [],
            self._get_river_target_directions
        )
        self.set_tile(river_source, via.data.tiles['spring'])

        ungrowable_marsh_tiles = [via.data.tiles['river'],
                                  via.data.tiles['spring']]
        self._grow_bushlike(
            via.data.tiles['marsh'], [random.choice(river_tiles)],
            ungrowable_marsh_tiles, 2
        )
        self._grow_bushlike(
            via.data.tiles['marsh'], [random.choice(river_tiles)],
            ungrowable_marsh_tiles, 2
        )

        ungrowable_forest_tiles = [
            via.data.tiles['river'],
            via.data.tiles['spring']
        ]

        self._grow_weedlike(
            via.data.tiles['forest'],
            self._get_random_location(),
            10,
            ungrowable_forest_tiles
        )

        glade = self._get_random_location()

        self._grow_weedlike(
            via.data.tiles['forest'],
            glade,
            10,
            ungrowable_forest_tiles
        )

        self.set_tile(glade, via.data.tiles['glade'])

        road_tiles, current_road_location = self._grow_walklike(
            via.data.tiles['road'],
            Location(0, 0),
            80,
            [via.data.tiles['spring'], via.data.tiles['glade']],
            self._get_road_target_directions
        )
        self.set_tile(current_road_location, via.data.tiles['fortress'])

        ungrowable_mountain_tiles = [
            via.data.tiles['spring'],
            via.data.tiles['glade'],
            via.data.tiles['fortress'],
            via.data.tiles['river'],
            via.data.tiles['road']
        ]

        mountain_source = Location(
            random.choice(
                range(
                    0, int(via.data.plan['width'] * 0.3)
                )
            ),
            random.choice(
                range(
                    int(via.data.plan['height'] / 2),
                    via.data.plan['height']
                )
            )
        )

        self._grow_weedlike(
            via.data.tiles['mountain'],
            mountain_source,
            15,
            ungrowable_mountain_tiles
        )

        mountain_source = Location(
            random.choice(
                range(
                    int(via.data.plan['width'] * 0.7),
                    via.data.plan['width']
                )
            ),
            random.choice(
                range(
                    int(via.data.plan['height'] / 2),
                    via.data.plan['height']
                )
            )
        )

        self._grow_weedlike(
            via.data.tiles['mountain'],
            mountain_source,
            15,
            ungrowable_mountain_tiles
        )

        self.set_tile(mountain_source, via.data.tiles['volcano'])

        self._convert_inaccessible_tiles(via.data.tiles['void'])

    def get_tile(self, location):
        return self.plan[location.y][location.x]

    def set_tile(self, location, tile):
        self.plan[location.y][location.x] = tile

    def is_traversable(self, location):
        return self.get_tile(location)['is_traversable']

    def _create_plan(self):
        for row_index in range(0, via.data.plan['height']):
            self.plan.append([])
            for column_index in range(0, via.data.plan['width']):
                self.plan[row_index].append(via.data.tiles['void'])

    def _grow_noiselike(self, tile_to_convert, tile1, tile2):
        for row_index, row in enumerate(self.plan):
            for column_index, column in enumerate(row):
                location = Location(column_index, row_index)
                if self.get_tile(location) == tile_to_convert:
                    if random.random() < 0.5:
                        self.set_tile(location, tile1)
                    else:
                        self.set_tile(location, tile2)

    def _grow_shape(self, tile):
        for column_index in range(0, via.data.plan['width']):
            self.plan[0][column_index] = tile
            self.plan[1][column_index] = tile
            self.plan[via.data.plan['height'] - 1][column_index] = tile
            self.plan[via.data.plan['height'] - 2][column_index] = tile
        for row_index in range(0, via.data.plan['height']):
            self.plan[row_index][0] = tile
            self.plan[row_index][1] = tile
            self.plan[row_index][via.data.plan['width'] - 1] = tile
            self.plan[row_index][via.data.plan['width'] - 2] = tile

        shape_sources = []
        for i in range(0, 10):
            shape_sources.append(Location(
                random.choice(range(0, via.data.plan['width'])),
                random.choice((2, 18))
            ))
        self._grow_bushlike(
            tile,
            shape_sources,
            [],
            random.choice(range(5, 10))
        )

    def _grow_cellular(self, tile):
        for row_index, row in enumerate(self.plan):
            for column_index, column in enumerate(row):
                location = Location(column_index, row_index)
                if self.get_tile(location) == tile:
                    neighbours = location.get_neighbours().values()
                    neighbouring_plains = 0
                    for neighbour in neighbours:
                        if self.get_tile(neighbour) == tile:
                            neighbouring_plains += 1
                    if neighbouring_plains >= 4:
                        self.set_tile(location, tile)
                else:
                    neighbours = location.get_neighbours().values()
                    neighbouring_plains = 0
                    for neighbour in neighbours:
                        if self.get_tile(neighbour) == tile:
                            neighbouring_plains += 1
                    if neighbouring_plains >= 5:
                        self.set_tile(location, tile)

    def _get_wasteland_source(self):
        return Location(
            random.choice(range(0, via.data.plan['width'])),
            random.choice(range(int(via.data.plan['height'] * 0.5), via.data.plan['height']))
        )

    def _grow_bushlike(self, tile, source_tiles, ungrowable_tiles, total_iterations, current_iteration = 0):
        if current_iteration > total_iterations:
            return

        added_tiles = []
        for source_tile in source_tiles:
            neighbours = source_tile.get_cardinal_neighbours().values()
            for neighbour in neighbours:
                neighbour_tile = self.get_tile(neighbour)
                if (
                    neighbour_tile != tile and
                    neighbour_tile not in ungrowable_tiles
                ):
                    self.set_tile(neighbour, tile)
                    if random.random() < 0.8:
                        added_tiles.append(neighbour)

        current_iteration += 1
        return self._grow_bushlike(tile, added_tiles, ungrowable_tiles, total_iterations, current_iteration)

    def _convert_mountains_next_to_plains_to_hills(self):
        for row_index, row in enumerate(self.plan):
            for column_index, column in enumerate(row):
                location = Location(column_index, row_index)

                if self.get_tile(location) != via.data.tiles['mountain']:
                    continue

                neighbours = location.get_neighbours().values()
                neighbouring_plains = 0
                for neighbour in neighbours:
                    if self.get_tile(neighbour) == via.data.tiles['plain']:
                        neighbouring_plains += 1

                if (
                    row_index != 0 and
                    row_index != via.data.plan['height'] - 1 and
                    column_index != 0 and
                    column_index != via.data.plan['width'] - 1 and
                    neighbouring_plains >= 2
                ):
                    self.set_tile(location, via.data.tiles['hill'])

    def _grow_walklike(self, tile, source, total_length, ungrowable_tiles, target_direction_callback):
        self.set_tile(source, tile)
        current_tile_location = source

        current_length = 0
        added_tiles = []

        while (current_length < total_length):
            target_directions = target_direction_callback(
                source,
                current_tile_location
            )
            neighbours = current_tile_location.get_cardinal_neighbours()
            next_direction = random.choice(list(neighbours))

            if (
                random.random() < 0.9 and
                next_direction not in target_directions
            ):
                continue

            current_tile_location = neighbours[next_direction]
            current_tile = self.get_tile(current_tile_location)
            if (
                current_tile != tile and
                current_tile not in ungrowable_tiles
            ):
                self.set_tile(current_tile_location, tile)
                added_tiles.append(current_tile_location)
                current_length += 1

        return (added_tiles, current_tile_location)

    def _get_river_target_directions(self, source, current_tile_location):
        target_directions = []
        if source.x > via.data.plan['width'] / 2:
            target_directions.append('west')
        else:
            target_directions.append('east')

        if source.y > via.data.plan['height'] / 2:
            target_directions.append('north')
        else:
            target_directions.append('south')
        return target_directions

    def _get_road_target_directions(self, source, current_tile_location):
        target_directions = ['south', 'east']
        if (random.random() < 0.9 and current_tile_location.y > 15):
            target_directions[0] = 'north'
        elif (random.random() < 0.9 and current_tile_location.y < 5):
            target_directions[0] = 'south'
        else:
            target_directions[0] = 'east'
        return target_directions

    def _get_river_source(self):
        edges = []
        for row_index in range(0, via.data.plan['height']):
            for column_index in range(0, via.data.plan['width']):
                if (
                    row_index == 0 or
                    row_index == via.data.plan['height'] - 1 or
                    column_index == 0 or
                    column_index == via.data.plan['width'] - 1
                ):
                    edges.append(Location(column_index, row_index))
        return random.choice(edges)

    def _get_random_location(self):
        return Location(
            random.choice(range(0, via.data.plan['width'])),
            random.choice(range(0, via.data.plan['height']))
        )

    def _grow_weedlike(self, tile, source, total_size, ungrowable_tiles):
        current_size = 0
        added_tiles = [source]
        for added_tile in added_tiles:
            neighbours = added_tile.get_neighbours().values()
            new_tile_locations = random.sample(list(neighbours), 3)
            for new_tile_location in new_tile_locations:
                new_tile = self.get_tile(new_tile_location)
                if (
                    new_tile != tile and
                    new_tile not in ungrowable_tiles
                ):
                    added_tiles.append(new_tile_location)
                    self.set_tile(new_tile_location, tile)
                    current_size += 1
                    if (current_size > total_size):
                        break

    def _convert_inaccessible_tiles(self, tile):
        for row_index, row in enumerate(self.plan):
            for column_index, column in enumerate(row):
                location = Location(column_index, row_index)
                neighbours = location.get_neighbours().values()
                has_only_mountain_neighbours = True

                if self.get_tile(location) == via.data.tiles['volcano']:
                    continue

                for neighbour in neighbours:
                    if (
                        self.get_tile(neighbour) != via.data.tiles['mountain'] and
                        self.get_tile(neighbour) != tile
                    ):
                        has_only_mountain_neighbours = False

                if has_only_mountain_neighbours:
                    self.set_tile(location, tile)
