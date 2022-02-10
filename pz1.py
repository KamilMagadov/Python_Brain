num_eng = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
           5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'}
num_rus = {0: 'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
           6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять', 10: 'десять'}


def nam_translate(namb):
    for val in num_eng.values():
        if namb == val:
            namb.translate(num_rus)
            return namb.capitalize()


nam_translate('one')