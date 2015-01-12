import via.data
import via.dungeon
from via.location import Location
from via.tool import Dungeon, Message

class TestDungeon:

    def setup(self):
        self.sus = Dungeon()

    def test_has_dungeons(self):
        self.sus.dungeons.should.equal({})

    def test_get_existing_dungeon(self):
        self.sus.dungeons = {'name': ['dungeon']}
        self.sus.get('name', 0).should.equal('dungeon')

    def test_get_new_dungeon(self):
        dungeon = self.sus.get('valley', 0)
        dungeon.should.be.a(via.dungeon.Valley)
        self.sus.dungeons['valley'][0].should.be(dungeon)
        dungeon.plan.should_not.be.none

class TestMessage:

    def setup(self):
        self.sus = Message()

    def test_has_messages(self):
        self.sus.messages.should.equal([])

    def test_add_message(self):
        self.sus.add('message')
        self.sus.messages.should.equal(['message'])

    def test_get_all(self):
        self.sus.get().should.equal(['No messages.'])
        self.sus.messages = ['message']
        self.sus.get().should.equal(['message'])
