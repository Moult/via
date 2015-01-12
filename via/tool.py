import via.data
import via.dungeon
import via.error

class Dungeon:

    def __init__(self):
        self.dungeons = {}

    def get(self, name, level):
        if (name not in self.dungeons):
            self.dungeons[name] = {}
        if len(self.dungeons[name]) > level:
            return self.dungeons[name][level]
        dungeon = getattr(via.dungeon, name.capitalize())()
        dungeon.generate()
        self.dungeons[name][level] = dungeon
        return dungeon

class Message:

    def __init__(self):
        self.messages = []

    def add(self, message):
        self.messages.append(message)

    def get(self):
        if not self.messages:
            return ['No messages.']
        else:
            return self.messages
