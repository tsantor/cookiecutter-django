from rest_framework import serializers

# from megamify.core.analytics import tasks
# from megamify.core.analytics.models import APICall


class MySerializer(serializers.Serializer):
    def get_request_ip_address(self):
        return self.context.get("ip_address")

    def get_request_endpoint_url(self):
        return self.context.get("endpoint_url")

    def get_view_name(self):
        return self.context.get("endpoint_name")

    def get_requet_method_type(self):
        request = self.context.get("request")
        return request.method

    # def set_api_call(self, game, user, player):

    #     request_user_type = APICall.USER_TYPE_ACCOUNT_USER
    #     if user.is_player:
    #         request_user_type = APICall.USER_TYPE_PLAYER

    #     # save API call data
    #     tasks.set_api_call(
    #         game.account,
    #         game,
    #         self.get_view_name(),
    #         self.get_request_endpoint_url(),
    #         self.get_request_ip_address(),
    #         self.get_requet_method_type(),
    #         user=user,
    #         player=player,
    #         request_user_type=request_user_type,
    #     )


class MyModelSerializer(serializers.ModelSerializer):
    def get_request_ip_address(self):
        view = self.context.get("view")
        return view.get_request_ip_address()

    def get_request_endpoint_url(self):
        view = self.context.get("view")
        return view.get_request_endpoint_url()

    def get_view_name(self):
        view = self.context.get("view")
        return view.get_view_name()

    def get_requet_method_type(self):
        request = self.context.get("request")
        return request.method

    # def set_api_call(self, game, user, player):

    #     request_user_type = APICall.USER_TYPE_ACCOUNT_USER
    #     if user.is_player:
    #         request_user_type = APICall.USER_TYPE_PLAYER

    #     # save API call data
    #     tasks.set_api_call(
    #         game.account,
    #         game,
    #         self.get_view_name(),
    #         self.get_request_endpoint_url(),
    #         self.get_request_ip_address(),
    #         self.get_requet_method_type(),
    #         user=user,
    #         player=player,
    #         request_user_type=request_user_type,
    #     )
