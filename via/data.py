plan = {
    'width': 80,
    'height': 20
}

ascii = {
    'tiles': {
        'void': {
            'symbol': ' ',
            'foreground': '',
            'background': ''
        },
        'plain': {
            'symbol': '"',
            'foreground': 'dark green',
            'background': ''
        },
        'marsh': {
            'symbol': '"',
            'foreground': '#df0',
            'background': ''
        },
        'hill': {
            'symbol': '^',
            'foreground': 'g78',
            'background': ''
        },
        'mountain': {
            'symbol': '^',
            'foreground': 'white,bold',
            'background': ''
        },
        'volcano': {
            'symbol': 'O',
            'foreground': 'light red,bold,underline',
            'background': ''
        },
        'fortress': {
            'symbol': 'O',
            'foreground': 'yellow,bold,underline',
            'background': ''
        },
        'glade': {
            'symbol': 'O',
            'foreground': '#af6,bold,underline',
            'background': ''
        },
        'spring': {
            'symbol': 'O',
            'foreground': '#adf,bold,underline',
            'background': ''
        },
        'river': {
            'symbol': '=',
            'foreground': 'light blue',
            'background': ''
        },
        'road': {
            'symbol': '=',
            'foreground': 'brown,bold',
            'background': ''
        },
        'forest': {
            'symbol': '&',
            'foreground': '#6d0',
            'background': ''
        },
        'wasteland': {
            'symbol': '~',
            'foreground': 'brown',
            'background': ''
        }
    },
    'monsters': {
        'player': {
            'symbol': '@',
            'foreground': '#000',
            'background': '#fff'
        }
    }
}

tiles = {
    'void': {
        'name': 'void',
        'is_traversable': True,
        'time_to_traverse': 100
    },
    'plain': {
        'name': 'plain',
        'is_traversable': True,
        'time_to_traverse': 100
    },
    'marsh': {
        'name': 'marsh',
        'is_traversable': True,
        'time_to_traverse': 100
    },
    'hill': {
        'name': 'hill',
        'is_traversable': True,
        'time_to_traverse': 100
    },
    'mountain': {
        'name': 'mountain',
        'is_traversable': False,
        'time_to_traverse': 100
    },
    'volcano': {
        'name': 'volcano',
        'is_traversable': True,
        'time_to_traverse': 100
    },
    'fortress': {
        'name': 'fortress',
        'is_traversable': True,
        'time_to_traverse': 100
    },
    'glade': {
        'name': 'glade',
        'is_traversable': True,
        'time_to_traverse': 100
    },
    'spring': {
        'name': 'spring',
        'is_traversable': True,
        'time_to_traverse': 100
    },
    'river': {
        'name': 'river',
        'is_traversable': True,
        'time_to_traverse': 100
    },
    'road': {
        'name': 'road',
        'is_traversable': True,
        'time_to_traverse': 100
    },
    'forest': {
        'name': 'forest',
        'is_traversable': True,
        'time_to_traverse': 100
    },
    'wasteland': {
        'name': 'wasteland',
        'is_traversable': True,
        'time_to_traverse': 100
    }
}

races = {
    'human': {
        'name': 'Human',
        'health_min': 8,
        'health_max': 12,
        'mana_min': 0,
        'mana_max': 4
    },
    'elf': {
        'name': 'Elf',
        'health_min': 6,
        'health_max': 8,
        'mana_min': 4,
        'mana_max': 8
    },
    'dwarf': {
        'name': 'Dwarf',
        'health_min': 9,
        'health_max': 14,
        'mana_min': 0,
        'mana_max': 6
    }
}

professions = {
    'ranger': {
        'name': 'Ranger',
        'health_bonus_min': 1,
        'health_bonus_max': 3,
        'mana_bonus_min': 0,
        'mana_bonus_max': 1
    },
    'wizard': {
        'name': 'Wizard',
        'health_bonus_min': 0,
        'health_bonus_max': 1,
        'mana_bonus_min': 5,
        'mana_bonus_max': 10
    },
    'burglar': {
        'name': 'Burglar',
        'health_bonus_min': 0,
        'health_bonus_max': 1,
        'mana_bonus_min': 1,
        'mana_bonus_max': 4
    }
}
