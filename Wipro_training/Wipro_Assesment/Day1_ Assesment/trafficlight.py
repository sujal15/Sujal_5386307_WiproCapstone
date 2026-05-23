light = input('Enter the color')
match light:
    case 'Red':
        print('Stop')
    case 'Yellow':
        print('Wait')
    case 'Green':
        print('Go')
    case _:
        print('Invalid')