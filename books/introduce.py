

def introduce(title, names):
    message = f'{title}: '
    for index, name in enumerate(names):
        if index > 0:
            message += ', '
    if index == len(names) - 1:
        message += 'and '
        message += name

    print(message)

introduce('The Three Stooges', ['Moe', 'Larry', 'Shemp'])
introduce('The Three Stooges', ['Larry', 'Curly', 'Moe'])
introduce( 'Teenage Mutant Ninja Turtles',
['Donatello', 'Raphael', 'Michelangelo', 'Leonardo']
)