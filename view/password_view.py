import string, secrets, hashlib, base64
from pathlib import Path
from cryptography.fernet import Fernet, InvalidToken
class FermetHasher:
    RANDOM_STRING_CHARS = string.ascii_letters + string.digits 
    BASE_DIR= Path(__file__).resolve().parent.parent;
    KEY_DIR = BASE_DIR / 'keys'

    def __init__(self, key):
        if not isinstance(key, bytes):
            key = key.encode()
        self.fernert = Fernet(key)

    def encrypt(self, value):
        if not isinstance(value, bytes):
            value = value.encode()
        return self.fernert.encrypt(value)
    
    def decrypt(self, value):
        if not isinstance(value, bytes):
            value = value.encode()
        try:
            return self.fernert.decrypt(value).decode()
        except InvalidToken as e:
            return "Token inválido"

    @classmethod
    def _get_random_string(cls,limit=25):
        # print(secrets.choice(cls.RANDOM_STRING_CHARS))
        string = ""
        for c in range(limit):
            string += secrets.choice(cls.RANDOM_STRING_CHARS)
        return string


    @classmethod
    def creat_key(cls, archive=False):
        value = cls._get_random_string()
        hasher = hashlib.sha256(value.encode('utf-8')).digest()
        key = base64.urlsafe_b64encode(hasher)
        # cls.archive_key(key)
        # print(key)
        if archive:
            return key, cls.archive_key(key)
        return key, None

    @classmethod
    def archive_key(cls, key):
        file = 'key.key'
        while Path(cls.KEY_DIR/file).exists():
            file = 'key_' + cls._get_random_string(5) + '.key'

        with open(cls.KEY_DIR/file, 'wb') as file:
            file.write(key)
        return file

# chave = FermetHasher._get_random_string()
# FermetHasher.creat_key(archive=True)
