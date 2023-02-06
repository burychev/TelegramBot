def func(message):
    layout = dict(zip(map(ord, "qwertyuiop[]asdfghjkl;'zxcvbnm,./`"
                               'QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?~'),
                               "йцукенгшщзхъфывапролджэячсмитьбю.ё"
                               'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,Ё'))
    result = (message.translate(layout))
    return(result)
