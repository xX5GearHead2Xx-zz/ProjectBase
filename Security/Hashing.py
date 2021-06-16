import sys
from Crypto.Hash import SHA256
from Crypto.Hash import BLAKE2s
from Crypto.Hash import BLAKE2b


class SHA256Provider:
    def __init__(self, salt):
        self.salt = salt

    def HashString(self, data):
        try:
            sha_object = SHA256.new(bytes(data, 'utf-8'))
            sha_object.update(bytes(self.salt, 'utf-8'))
            return sha_object.hexdigest()
        except:
            raise(sys.exc_info())


class Blake2sProvider:
    def __init__(self, salt):
        self.salt = salt

    def HashString(self, data):
        try:
            bla_object = BLAKE2s.new(bytes(data, 'utf-8'))
            bla_object.update(bytes(self.salt))
            return bla_object.hexdigest()
        except:
            raise(sys.exc_info())


class Blake2bProvider:
    def __init__(self, salt):
        self.salt = salt

    def HashString(self, data):
        try:
            bla_object = BLAKE2b.new(bytes(data, 'utf-8'))
            bla_object.update(bytes(self.salt))
            return bla_object.hexdigest()
        except:
            raise(sys.exc_info())
