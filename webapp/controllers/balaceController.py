from webapp.serializers.userBalanceSerializer import UserBalanceSerializer
from webapp.serializers.userMessageSerializer import UserMessageSerializer
from webapp.models.userBalance import UserBalance
from webapp.services.balanceService import BalanceService
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class BalanceController(GenericAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return UserBalance.objects.get(user=user)

    def get(self, request, *args, **kwargs):
        data = UserBalanceSerializer(self.get_queryset()).data
        return Response(data, status=200)

    def patch(self, request, *args, **kwargs):
        balance = BalanceService(self.get_queryset(), request.user)

        try:
            amount = float(request.query_params.get('amount'))
        except ValueError:
            return Response(status=400)

        user_message = None

        try:
            if amount > 0:
                user_message = balance.replenishment(amount)
            elif amount < 0:
                user_message = balance.expenditure(amount)
            else:
                return Response('Пополнение на ноль невозможно', status=400)
        except ValueError as e:
            return Response(str(e), status=400)
        except Exception as e:
            return Response(str(e), status=500)

        return Response(UserMessageSerializer(user_message).data, status=201)
