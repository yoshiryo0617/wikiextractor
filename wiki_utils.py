segment_seperator = "========"

def get_segment_seperator(level,name):
    return segment_seperator + "," + str(level) + "," +name

def get_list_token():
    return "***LIST***"

def get_formula_token():
    return "***formula***"

def get_codesnipet_token():
    return "***codice***"
