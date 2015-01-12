import sure
import via.data
import via.error
from via.location import Location

class TestLocation:

    def test_has_coordinates(self):
        Location(0, 1).x.should.be(0)
        Location(0, 1).y.should.be(1)
        Location(0, 1).coordinates.should.equal((0, 1))

    def test_get_neighbour(self):
        Location(0, 0).get_neighbour('east').coordinates.should.equal((1, 0))
        Location(0, 0).get_neighbour('south').coordinates.should.equal((0, 1))
        Location(1, 0).get_neighbour('west').coordinates.should.equal((0, 0))
        Location(0, 1).get_neighbour('north').coordinates.should.equal((0, 0))
        Location(0, 1).get_neighbour('northeast').coordinates.should.equal((1, 0))
        Location(1, 1).get_neighbour('northwest').coordinates.should.equal((0, 0))
        Location(0, 0).get_neighbour('southeast').coordinates.should.equal((1, 1))
        Location(1, 0).get_neighbour('southwest').coordinates.should.equal((0, 1))
        (
            Location(0, 0).get_neighbour.when.called_with('north')
            .should.throw(via.error.LocationRangeError)
        )
        (
            Location(via.data.plan['width'], via.data.plan['height'])
            .get_neighbour.when.called_with('south')
            .should.throw(via.error.LocationRangeError)
        )

    def test_get_neighbours(self):
        neighbours = Location(1, 1).get_neighbours()
        neighbours['northwest'].coordinates.should.equal((0, 0))
        neighbours['north'].coordinates.should.equal((1, 0))
        neighbours['northeast'].coordinates.should.equal((2, 0))
        neighbours['east'].coordinates.should.equal((2, 1))
        neighbours['southeast'].coordinates.should.equal((2, 2))
        neighbours['south'].coordinates.should.equal((1, 2))
        neighbours['southwest'].coordinates.should.equal((0, 2))
        neighbours['west'].coordinates.should.equal((0, 1))

        neighbours = Location(0, 0).get_neighbours()
        neighbours['east'].coordinates.should.equal((1, 0))
        neighbours['southeast'].coordinates.should.equal((1, 1))
        neighbours['south'].coordinates.should.equal((0, 1))

    def test_get_cardinal_neighbours(self):
        neighbours = Location(1, 1).get_cardinal_neighbours()
        neighbours['north'].coordinates.should.equal((1, 0))
        neighbours['east'].coordinates.should.equal((2, 1))
        neighbours['south'].coordinates.should.equal((1, 2))
        neighbours['west'].coordinates.should.equal((0, 1))

        neighbours = Location(0, 0).get_cardinal_neighbours()
        neighbours['east'].coordinates.should.equal((1, 0))
        neighbours['south'].coordinates.should.equal((0, 1))

