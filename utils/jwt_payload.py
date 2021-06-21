# from user.api.v1.serializers.user import UserSerializer


def jwt_response_payload_handler(token, user=None, request=None):
    """
    Returns the response data for both the login and refresh views.
    Override to return a custom response such as including the
    serialized representation of the User.

    Example:

    def jwt_response_payload_handler(token, user=None, request=None):
        return {
            'token': token,
            'user': UserSerializer(user, context={'request': request}).data
        }

    """

    # user = UserSerializer(user, context={'request': request}).data
    return {
        'token': token,
        'user_id': user['id']
    }
