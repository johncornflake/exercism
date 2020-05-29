def constructVerse(current_start, vkey):
    verses = f'On the {vkey[current_start-1][1]} day of Christmas my true love gave to me: '
    if current_start == 1: return verses + vkey[0][0] + '.'

    for i in range(current_start, 0, -1):
        if i > 1: verses += f'{vkey[i-1][2]} {vkey[i-1][0]}, '
        if i == 1: verses += f'and {vkey[i-1][0]}.'

    return verses

def recite(start_verse, end_verse):
    if start_verse and end_verse not in range(1,13) or start_verse > end_verse:
        raise ValueError('Invalid range given')

    vkey = [('a Partridge in a Pear Tree', 'first', ''),
            ('Turtle Doves','second', 'two'),
            ('French Hens', 'third', 'three'),
            ('Calling Birds', 'fourth', 'four'),
            ('Gold Rings', 'fifth', 'five'),
            ('Geese-a-Laying', 'sixth', 'six'),
            ('Swans-a-Swimming', 'seventh', 'seven'),
            ('Maids-a-Milking', 'eighth', 'eight'),
            ('Ladies Dancing', 'ninth', 'nine'),
            ('Lords-a-Leaping', 'tenth', 'ten'),
            ('Pipers Piping', 'eleventh', 'eleven'),
            ('Drummers Drumming', 'twelfth', 'twelve')
            ]

    song_output = []
    current_start = start_verse
    for i in range(start_verse, 13):
        verse = ''
        verse += constructVerse(current_start, vkey)
        current_start += 1
        song_output.append(verse)
        if current_start > end_verse: break

    return song_output
