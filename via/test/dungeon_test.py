from via.dungeon import Valley
from via.location import Location

class TestValley:

    def setup(self):
        self.sus = Valley()

    def test_generate(self):
        self.sus.generate()
        self.sus.plan.should_not.be.none

    def test_is_traversable(self):
        self.sus.plan = [[{'is_traversable': True}]]
        self.sus.is_traversable(Location(0, 0)).should.be(True)
