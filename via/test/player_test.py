import sure
import copy
import via.data
import via.tool
import via.dungeon
import via.error
from via.player import Player
from via.location import Location
from unittest.mock import Mock

class TestPlayer:

    def setup(self):
        self.dungeon = Mock(spec_set = via.tool.Dungeon)
        self.message = Mock(spec_set = via.tool.Message)
        self.sus = Player(self.dungeon, self.message)

    def test_player_has_attributes(self):
        self.sus.name.should.be.none
        self.sus.race.should.be.none
        self.sus.profession.should.be.none
        self.sus.experience_points.should.be(0)
        self.sus.health.should.be(0)
        self.sus.health_max.should.be(0)
        self.sus.mana.should.be(0)
        self.sus.mana_max.should.be(0)
        self.sus.branch.should.be('valley')
        self.sus.level.should.be(0)
        self.sus.location.should.a(Location)
        self.sus.time_played.should.be(0)
        self.sus.turns_played.should.be(0)

    def test_generating_a_player(self):
        self.sus.mana = None
        self.sus.generate('name')
        self.sus.name.should.be('name')
        self.sus.race.should.be.within(list(via.data.races.values()))
        self.sus.profession.should.be.within(list(via.data.professions.values()))
        self.sus.health.should.be.within(6, 18)
        self.sus.health_max.should.be(self.sus.health)
        self.sus.mana.should.be.within(0, 19)
        self.sus.mana_max.should.be(self.sus.mana)

    def test_moving(self):
        self.sus.location = Mock(spec_set = Location)
        self.sus.location.get_neighbour.return_value = 'neighbour'
        dungeon = Mock(spec_set = via.dungeon.Valley)
        self.dungeon.get.return_value = dungeon

        self.sus.move('south')

        self.dungeon.get.assert_called_with('valley', 0)
        dungeon.is_traversable.assert_called_with('neighbour')
        self.sus.location.should.be('neighbour')

    def test_moving_out_of_the_map(self):
        self.sus.location = Mock(spec_set = Location)
        self.sus.location.get_neighbour = Mock(
            side_effect=via.error.LocationRangeError
        )
        self.sus.move('south')
        self.message.add.assert_called_with('You are unable to move that way.')

    def test_finishing_the_turn(self):
        self.sus.finish_turn()
        self.sus.turns_played.should.be(1)

    def test_generating_health(self):
        self.sus.race = via.data.races['human']
        self.sus.profession = via.data.professions['ranger']
        self.sus._generate_health().should.be.within(
            via.data.races['human']['health_min'] +
            via.data.professions['ranger']['health_bonus_min'],
            via.data.races['human']['health_max'] +
            via.data.professions['ranger']['health_bonus_max'] + 1,
        )

    def test_generating_mana(self):
        self.sus.race = via.data.races['human']
        self.sus.profession = via.data.professions['ranger']
        self.sus._generate_mana().should.be.within(0, 6)
