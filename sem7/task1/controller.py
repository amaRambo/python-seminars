import view, sum, div, div_bal, div_int, mult, sub

def button():
    mode = view.get_value('Режимы:\n1 - работа с рациональными числами\n2 - работа с комлпексными числами\nВыбери: ')
    if mode == 1:
        value_a = view.get_value('Введите число: ')
        value_b = view.get_value('Введите число: ')
        sign = view.get_sign()
        if sign == '+':
            sum.init(value_a, value_b)
            result = sum.num_sum()
            view.show_answer(result)
        elif sign == '-':
            sub.init(value_a, value_b)
            result = sub.num_sub()
            view.show_answer(result)
        elif sign == '*':
            mult.init(value_a, value_b)
            result = mult.num_mult()
            view.show_answer(result)
        elif sign == '/':
            div.init(value_a, value_b)
            result = div.num_div()
            view.show_answer(result)
        elif sign == '//':
            div_int.init(value_a, value_b)
            result = div_int.num_div_int()
            view.show_answer(result)
        elif sign == '%':
            div_bal.init(value_a, value_b)
            result = div_bal.num_div_bal()
            view.show_answer(result)
        else:
            view.view_data('Такой операции нет')
    elif mode == 2:
        value_a = view.get_complex_value('Введите число: ')
        value_b = view.get_complex_value('Введите число: ')
        sign = view.get_sign()
        if sign == '+':
            sum.init(value_a, value_b)
            result = sum.num_sum()
            view.show_answer(result)
        elif sign == '-':
            sub.init(value_a, value_b)
            result = sub.num_sub()
            view.show_answer(result)
        elif sign == '*':
            mult.init(value_a, value_b)
            result = mult.num_mult()
            view.show_answer(result)
        elif sign == '/':
            div.init(value_a, value_b)
            result = div.num_div()
            view.show_answer(result)
        else:
            view.view_data('Такой операции нет')
    else:
        view.view_data('Такой операции нет')
