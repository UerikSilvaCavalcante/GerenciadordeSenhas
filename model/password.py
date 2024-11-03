from datetime import datetime
from pathlib import Path
class BaseModel:
    BASE_DIR= Path(__file__).resolve().parent.parent;
    DB_DIR = BASE_DIR / 'db'
    def save(self):
        table_path = Path(self.DB_DIR / f'{self.__class__.__name__}.txt')
        if not table_path.exists():
            table_path.touch()
        # print("Ola mundo")

        with open(table_path, 'a') as file:
            password = '|'.join(list(map(lambda x: str(x), self.__dict__.values())))

            file.write(password + '\n')

    @classmethod
    def get(cls):
        table_path = Path(cls.DB_DIR / f'{cls.__name__}.txt')
        if not table_path.exists():
            return []
        with open(table_path, 'r') as file:
            # return file.readlines()
            results = []
            atributos = vars(cls())

            # print(atributos)
            for line in file.readlines():
                password = line.strip().split('|')
                results.append(dict(zip(atributos.keys(), password)))
            return results
             

class Password(BaseModel):
    def __init__(self, domain=None, password=None, expire = False):
        self.domain = domain
        self.password = password
        self.created_at = datetime.now().isoformat()

