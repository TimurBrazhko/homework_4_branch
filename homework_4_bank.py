class SavingAccount: pass


class CheckingAccount: pass


class BankAccount(CheckingAccount,SavingAccount): pass


class Stock: pass


class Bond: pass


class Security(Stock, Bond): pass


class RealEstate: pass


class InterestBearingItem(BankAccount, Security): pass


class Asset(BankAccount, RealEstate, Security): pass


class InsurableItem(BankAccount, RealEstate): pass

