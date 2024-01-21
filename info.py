from telebot import types

locations = {
    'location1': {
        'description': 'Вы находитесь в деревне. Перед вами торговцы и дома жителей. Рядом с вами пробежала белка',
        'photo': '1.jpg',
        'options': {
            'Побежать за белкой': 'location2',
            'Пойти в лес': 'location2_1'
        }
    },
    'location2': {
        'description': 'Белка привела вас в лес. Вокруг вас деревья и темная тропинка.',
        'photo': '2.jpg',
        'options': {
            'Идти по тропинке': 'location2_2',
            'Вернуться в деревню': 'location1'
        }
    },
    'location2_1': {
        'description': 'Вы нашли часть леса, где растут странные растения.',
        'photo': '2_1.jpg',
        'options': {
            'Исследовать растения': 'location2_1_1',
            'Пойти глубже в лес': 'location2_1_2',
            'Вернуться в лес': 'location2'
        }
    },
    'location2_1_1': {
        'description': 'Вы исследуете странные растения и находите что-то интересное.',
        'photo': '2_1_1.jpg',
        'options': {
            'Продолжить исследование': 'location2_1_1_1',
            'Вернуться в лес': 'location2'
        }
    },
    'location2_1_1_1': {
        'description': 'Продолжая исследование, вы обнаруживаете скрытую тропу.',
        'photo': '2_1_1_1.jpg',
        'options': {
            'Пройти по тропе': 'location2_1_1_2',
            'Вернуться в лес': 'location2'
        }
    },
    'location2_1_1_2': {
        'description': 'Тропа приводит вас к древнему храму.',
        'photo': '2_1_1_2.jpg',
        'options': {
            'Исследовать храм': 'location2_1_1_2_1',
            'Вернуться в лес': 'location2'
        }
    },
    'location2_1_1_2_1': {
        'description': 'Вы находите древний артефакт и завершаете свое приключение! Вы выиграли! Поздравляем!',
        'photo': '2_1_1_2_1.jpg',
        'options': {'Начать игру заново': 'location1'}
    },
    'location2_1_2': {
        'description': 'Вы идете глубже в лес, но ничего интересного не находите.',
        'photo': '2_1_2.jpg',
        'options': {'Вернуться в лес': 'location2_1'}
    },
    'location2_2': {
        'description': 'Вы стоите на опушке леса, откуда виден далекий холм.',
        'photo': '2_2.jpg',
        'options': {
            'Подняться на холм': 'location2_2_1',
            'Вернуться в лес': 'location2'
        }
    },
    'location2_2_1': {
        'description': 'Вы поднимаетесь на холм и видите красивый вид на окрестности. Вы наслаждаетесь красивым видом на город, но пора идти.',
        'photo': '2_2_1.jpg',
        'options': {
            'Спрыгнуть с холма': 'location3_1',
            'Вернуться в лес': 'location2_2'
        }
    },
    'location3_1': {
        'description': 'Вы в городе. Здесь шум и суета.',
        'photo': '3_1.jpg',
        'options': {
            'Пойти на главную площадь': 'location3_3',
            'Войти в таинственное подземелье': 'location3_2'
        }
    },
    'location3_2': {
        'description': 'Вы находились у входа в таинственное подземелье, пока вас не атаковал дракон. Вы проиграли!',
        'photo': '3_2.jpg',
        'options': {'Начать игру заново': 'location1'}
    },
    'location3_3': {
        'description': 'Вы стоите на главной площади города. Здесь много народа и торговцев.',
        'photo': '3_3.jpg',
        'options': {
            'Взобраться на крышу высокого здания': 'location3_4',
            'Войти в городской центр': 'location3_5'
        }
    },
    'location3_4': {
        'description': 'Вы упали с крыши высокого здания с видом на весь город. Вы проиграли!',
        'photo': '3_4.jpg',
        'options': {'Начать игру заново': 'location1'}
    },
    'location3_5': {
        'description': 'Вы вошли в городской центр. Тут много магазинов и развлечений.',
        'photo': '3_5.jpg',
        'options': {
            'Пойти в магазин': 'location3_5_1',
            'Посетить таверну': 'location3_5_2'
        }
    },
    'location3_5_1': {
        'description': 'Вы зашли в магазин и нашли интересные предметы.',
        'photo': '3_5_1.jpg',
        'options': {
            'Вернуться в городской центр': 'location3_5',
            'Покинуть магазин': 'location3_5'
        }
    },
    'location3_5_2': {
        'description': 'Вы провели веселое время в таверне, но пора вернуться к приключениям.',
        'photo': '3_5_2.jpg',
        'options': {
            'Вернуться в городской центр': 'location3_5',
            'Покинуть таверну': 'location3_5'
        }
    },
    'location3_5_3': {
        'description': 'Вы нашли тайный проход, ведущий к таинственной пещере.',
        'photo': '3_5_3.jpg',
        'options': {
            'Войти в пещеру': 'location3_5_3_1',
            'Вернуться в городской центр': 'location3_5'
        }
    },
    'location3_5_3_1': {
        'description': 'Вы исследуете пещеру и находите древний артефакт. Поздравляем, вы выиграли!',
        'photo': '3_5_3_1.jpg',
        'options': {'Начать игру заново': 'location1'}
    }
}


