month = 4
match month:
    case 1 | 2 | 3 | 4 | 5 | 6:
        print("It is first half of the year")
    case _:
        print("It is second half of the year")