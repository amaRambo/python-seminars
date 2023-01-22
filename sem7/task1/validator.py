def is_num(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

def is_complex(str):
    try:
        complex(str)
        return True
    except ValueError:
        return False