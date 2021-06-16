import sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from base64 import b64encode
from base64 import b64decode


class AESProvider:

    def __init__(self, iv, key):
        self.iv = iv
        self.key = key

    def EncryptString(self, data):
        try:
            byte_data = bytes(data, 'utf-8')
            cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
            ct_bytes = cipher.encrypt(pad(byte_data, AES.block_size))
            ct = b64encode(ct_bytes).decode('utf-8')
            return ct
        except:
            raise(sys.exc_info()[0])

    def DecryptString(self, data):
        try:
            decoded = b64decode(data)
            cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
            pt = unpad(cipher.decrypt(decoded), AES.block_size)
            return pt
        except:
            raise(sys.exc_info())

