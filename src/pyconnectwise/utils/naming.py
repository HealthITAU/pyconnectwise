def to_snake_case(string: str) -> str:
     return ('_' if string.startswith('_') else '') + ''.join(['_' + i.lower() if i.isupper() else i for i in string.lstrip('_')]).lstrip('_')

def to_camel_case(string: str) -> str:
    string_split = string.split("_")
    return string_split[0] + "".join(word.capitalize() for word in string_split[1:])

def to_title_case_preserve_case(string: str) -> str:
     return string[:1].upper() + string[1:]