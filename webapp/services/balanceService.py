from datetime import datetime
from webapp.models.userBalance import UserBalance
from webapp.models.userMessage import UserMessage
from django.contrib.auth.models import User


class BalanceService:
    def __init__(self, balance: UserBalance, user: User):
        self.balance_object = balance
        self.user = user

    def replenishment(self, amount: float):
        self.balance_object.balance += amount
        self.balance_object.save()
        return UserMessage.objects.create(user=self.user,
                                          message="Пополнение баланса на {0}".format(amount),
                                          date=datetime.now())

    def expenditure(self, amount: float):
        balance = self.balance_object.balance
        if balance + amount < 0:
            raise ValueError('Недостаточно средств!')
        else:
            self.balance_object.balance += amount
        self.balance_object.save()
        return UserMessage.objects.create(user=self.user,
                                          message="Покупка на сумму {0}".format(abs(amount)),
                                          date=datetime.now())
