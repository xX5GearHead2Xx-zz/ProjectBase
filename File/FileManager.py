import sys


def ReadFile(path):
    try:
        file = open(path, 'r')
        file_content = file.read()
        file.close()
        return file_content
    except:
        print(sys.exc_info())
        return None


def WriteFile(path, content):
    try:
        file = open(path, 'w')
        file.write(content)
        file.close()
        return True
    except:
        print(sys.exc_info())
        return False
