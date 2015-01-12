import urwid
import via.data
import via.tool
import via.widget
from via.player import Player

def main():

    dungeon = via.tool.Dungeon()
    message = via.tool.Message()

    player = Player(dungeon, message)
    player.generate('Moult')
    renderer = Renderer(dungeon, player)

    dungeon = via.widget.Dungeon(renderer.render())
    messages = via.widget.Messages(message)
    statistics = via.widget.Statistics(player)

    def show_or_exit(key):
        if key == 'Q':
            dungeon.popup_quit()
        elif key == 'h':
            player.move('west')
        elif key == 'j':
            player.move('south')
        elif key == 'k':
            player.move('north')
        elif key == 'l':
            player.move('east')
        elif key == 'y':
            player.move('northwest')
        elif key == 'u':
            player.move('northeast')
        elif key == 'b':
            player.move('southwest')
        elif key == 'n':
            player.move('southeast')
        elif key == 'tab':
            if widget_pile.focus_position == len(widget_pile.contents) - 1:
                widget_pile.focus_position = 0
            else:
                widget_pile.focus_position += 1

        player.finish_turn()
        dungeon.display(renderer.render())
        messages.update()
        statistics.update()

    widget_pile = urwid.Pile([
        ('weight', 1, messages),
        (22, dungeon),
        ('weight', 1, statistics)
    ])
    widget_pile.focus_position = 1

    loop = urwid.MainLoop(widget_pile, via.widget.palette, unhandled_input=show_or_exit)
    loop.run()

class Renderer:

    def __init__(self, dungeon, player):
        self.dungeon = dungeon
        self.player = player

    def render(self):
        dungeon = self.dungeon.get(self.player.branch, self.player.level)

        ascii_plan = []
        for row in dungeon.plan:
            ascii_row = []
            for column in row:
                ascii_row.append(via.data.ascii['tiles'][column['name']])
            ascii_plan.append(ascii_row)


        ascii_plan[self.player.location.y][self.player.location.x] = via.data.ascii['monsters']['player']

        rendered_plan = []
        for ascii_row in ascii_plan:
            for ascii_column in ascii_row:
                rendered_plan.append((urwid.AttrSpec(ascii_column['foreground'],
                                                     ascii_column['background']), ascii_column['symbol']))
            rendered_plan.append('\n')

        rendered_plan.pop()

        return rendered_plan

if __name__ == '__main__':
    main()
