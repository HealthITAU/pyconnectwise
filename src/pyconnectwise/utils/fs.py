
def save_py_file(filepath:str, content:str):
    if '.py' not in filepath:
        filepath += '.py'
    with open(filepath, 'w') as f:
        f.write(content)