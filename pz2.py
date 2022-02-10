def thesaurus(*names):
    employee = {}
    for name in names:
        key = name[0].capitalize()
        if key not in employee:
            employee[key] = []
        employee[key].append(name)
    return employee


print(thesaurus("Иван", "Мария", "Петр", "Илья"))