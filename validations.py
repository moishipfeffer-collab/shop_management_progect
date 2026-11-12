def check_empty(input):
    if input.strip():
        return True
    return False

def check_num(num,float_num: str | None = None):
    if not float_num:
        try:
            return int(num) > 0
        except ValueError:
            return False
    elif float_num:
        try:
            return float(num) > 0 
        except ValueError:
            return False
        


