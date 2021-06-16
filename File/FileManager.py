def ReadFile(path):
    file = open(path, 'r')
    file_content = file.read()
    file.close()
    return file_content


def WriteFile(path, content):
    file = open(path, 'w')
    file.write(content)
    file.close()
