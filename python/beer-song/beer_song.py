def recite(start, take=1):
    rem = start
    song = []
    for i in range(0, take):
        s = 's' if rem > 1 else ''
        if rem == 0:
            song.extend(['No more bottles of beer on the wall, no more bottles of beer.',
                     f'Go to the store and buy some more, 99 bottles of beer on the wall.'])
        else:
            song.append(f'{rem} bottle{s} of beer on the wall, {rem} bottle{s} of beer.')
            rem -= 1
            if rem == 1:
                song.append('Take one down and pass it around, 1 bottle of beer on the wall.')
            elif rem == 0:
                song.append(f'Take it down and pass it around, no more bottles of beer on the wall.')
            else:
                song.append(f'Take one down and pass it around, {rem} bottles of beer on the wall.')

        if i+1 < take: song.append('')

    return song
