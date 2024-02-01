from datetime import datetime
import re


class Transaction:
    def __init__(self, dictionary):
        self.to = None
        self.description = None
        self.date = None
        self.operationAmount = None
        for key, value in dictionary.items():
            # замена имени ключа, так как from имя метода, который вызывается через точку
            if key == 'from':
                key = 'out_of'
            if not isinstance(value, (list, tuple)):
                setattr(self, key, Transaction(value) if isinstance(value, dict) else value)

    def __repr__(self):
        return (f"{self.get_date()} {self.get_description()}"
                f"\n{self.get_from()} -> {self.get_to()} "
                f"\n{self.operationAmount.amount} {self.operationAmount.currency.name} \n")

    def get_date(self):
        trn_date = datetime.fromisoformat(self.date).strftime("%d.%m.%Y")
        return trn_date

    def get_description(self):
        return self.description

    def get_to(self):
        str_ = re.sub(r'\d', '*', self.to[:-4]) + self.to[-4:]
        return str_

    def get_from(self):
        if hasattr(self, 'out_of'):
            str_ = self.out_of
        else:
            str_ = ""
        chars = re.findall(r'[а-яА-Яa-zA-Z\W]+', str_)
        nums = re.findall(r'\d+', str_)
        if len(nums) > 0:
            nums1 = [nums[0][:6]]
            nums2 = [nums[0][-4:]]
            stars = ['*'*len(nums[0][6:-4])]
            chars = chars + nums1 + stars + nums2
        from_str = ''.join(chars)
        return from_str
