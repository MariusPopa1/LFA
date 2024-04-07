def assign(elements):
    numbers = []
    for element in elements:
        if len(element) == 1:
            numbers[element] = "1 "  # Always Show
        elif element.count('|') != 0:
            element.replace('|', ' ')
            numbers[element] = "2 "   # Choose one
        elif element.count('*') != 0:
            numbers[element] += "3 "   # 0 up to 5
        elif element.count('?') != 0:
            numbers[element] += "4 "   # Maybe show
        elif element.count('+') != 0:
            numbers[element] += "5 "   # 1 up to 5

    return numbers
