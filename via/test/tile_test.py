from via.tile import Void

class TestVoid:

    def setup(self):
        self.sus = Void()

    def test_has_a_name(self):
        self.sus.name.should.be('void')

    def test_can_check_if_traversable(self):
        self.sus.is_traversable().should.be(True)

    def test_has_traversable_time(self):
        self.sus.get_time_to_traverse().should.be(100)
