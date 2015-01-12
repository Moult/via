import urwid

palette = [
    ('debug', 'black', 'dark red'),
    ('good', 'black', 'dark green'),
    ('bad', 'black', 'dark red'),
    ('neutral', 'standout', '')
]

class Messages(urwid.Filler):

    def __init__(self, message):
        self.message = message
        self.text = urwid.Text('No messages.')
        messages_border = urwid.LineBox(self.text, title='Messages')
        return super().__init__(messages_border, valign='top', height='pack')

    def update(self):
        self.text.set_text('\n'.join(self.message.get()))

class Statistics(urwid.WidgetPlaceholder):

    def __init__(self, player):
        self.player = player
        statistics = urwid.Text(self._get_state_line())
        statistics_border = urwid.LineBox(statistics, title=self._get_title())
        statistics_filler = urwid.Filler(statistics_border, valign='bottom', height='pack')
        return super().__init__(statistics_filler)

    def update(self):
        statistics = urwid.Text(self._get_state_line())
        self.statistics_border = urwid.LineBox(statistics, title=self._get_title())
        self.original_widget = urwid.Filler(self.statistics_border, valign='bottom', height='pack')

    def _get_title(self):
        return (
            self.player.name + ' the L1 '
            + self.player.race['name'].capitalize() + ' '
            + self.player.profession['name'].capitalize()
        )

    def _get_state_line(self):
        return (
            'HP: ' + str(self.player.health) + '/' + str(self.player.health_max)
            + '  MP: ' + str(self.player.mana) + '/' + str(self.player.mana_max)
            + '  T: ' + str(self.player.turns_played)
        )

class Dungeon(urwid.WidgetPlaceholder):

    def __init__(self, ascii):
        self.dungeon = urwid.Text(ascii)
        return super().__init__(self._create_dungeon_container())

    def display(self, ascii):
        self.dungeon.set_text(ascii)

    def popup_quit(self):
        self.original_widget = urwid.Overlay(
            Quit(self.cancel_quit),
            self.original_widget,
            'center', 16, 'middle', 5
        )

    def cancel_quit(self):
        self.original_widget = self._create_dungeon_container()

    def _create_dungeon_container(self):
        return urwid.Filler(
            urwid.Padding(
                urwid.LineBox(self.dungeon, title='The Valley of Via'),
                align='center', width=82
            )
        )

class Quit(urwid.LineBox):

    def __init__(self, cancel_callback):
        self.cancel_callback = cancel_callback

        save_button = urwid.Button('Save')
        surrender_button = urwid.Button('Surrender')
        cancel_button = urwid.Button('Cancel')

        urwid.connect_signal(save_button, 'click', self.save)
        urwid.connect_signal(surrender_button, 'click', self.surrender)
        urwid.connect_signal(cancel_button, 'click', self.cancel)

        quit_border = urwid.ListBox(urwid.SimpleFocusListWalker([
            urwid.AttrMap(save_button, None, focus_map='good'),
            urwid.AttrMap(surrender_button, None, focus_map='bad'),
            urwid.AttrMap(cancel_button, None, focus_map='neutral')
        ]))

        return super().__init__(quit_border, title='Quit')

    def save(self, event):
        raise urwid.ExitMainLoop()

    def surrender(self, event):
        pass

    def cancel(self, event):
        self.cancel_callback()
