
class Shop:
    def __init__(self, name:str, typing:str, is_open:bool=False, bank_account:int=-1):
        self.name = name
        self.typing = typing
        self.is_open = is_open
        self._bank_account = bank_account

    @staticmethod
    def is_intager(value):
        return isinstance(value, int)

    @property
    def bank_account(self):
        return self._bank_account

    @bank_account.setter
    def bank_account(self, value):
        if Shop.is_intager(value) and (10000 < value < 99999):
            _bank_account = value
        else:
            raise ValueError("ошибка банковского аккаунта")



def main():
    myshop = Shop(name="5ка", typing="универмаг", is_open=False, bank_account=0)
    myshop.is_open = True
    myshop.bank_account(10001)
    print(myshop.bank_account)

if __name__ == '__main__':
    main()
