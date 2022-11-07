def get_count_char(str_):
    str_ = str_.lower()
    slovar = dict()
    for each in range(len(str_)):
        if str_[each].isalpha():             #если буква
            if str_[each] not in slovar:            #если не в словаре
                slovar[str_[each]] = 1
            else:                                #если в словаре
                slovar[str_[each]] += 1
    return slovar


def percents(slov):
    total = sum(slov.values())
    for each in slov:
         slov[each] = f"{slov[each] * 100 / total} %"
    return slov

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))

