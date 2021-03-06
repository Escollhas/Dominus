from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api


def init_app(app: Flask):
    api = Api(app)
    JWTManager(app)

    from app.views import Notices

    api.add_resource(Notices, "/notices", endpoint="/notices", methods=["GET", "POST"])
    api.add_resource(
        Notices,
        "/notices/<notice_id>",
        endpoint="/notices/<notice_id>",
        methods=["GET", "DELETE", "PATCH"],
    )

    from app.views import Login

    api.add_resource(Login, "/login", endpoint="/login", methods=["POST"])

    from app.views import Users

    api.add_resource(Users, "/signup", endpoint="/signup", methods=["POST"])
    api.add_resource(Users, "/users", endpoint="/users", methods=["GET"])
    api.add_resource(
        Users,
        "/users/<user_id>",
        endpoint="/users/<user_id>",
        methods=["GET", "DELETE", "PATCH"],
    )

    from app.views import Events

    api.add_resource(Events, "/events", endpoint="/events", methods=["POST", "GET"])
    api.add_resource(
        Events,
        "/events/<int:event_id>",
        endpoint="/events/<int:event_id>",
        methods=["PATCH", "DELETE", "GET"],
    )

    from app.views import Invitations

    api.add_resource(
        Invitations,
        "/invitations/<int:invitation_id>",
        endpoint="/invitations/<int:invitation_id>",
        methods=["PATCH", "DELETE", "GET"],
    )

    api.add_resource(
        Invitations,
        "/invitations",
        endpoint="/invitations",
        methods=["GET", "POST"]
    )

    from app.views import PollOptions

    api.add_resource(
        PollOptions, "/poll_options", endpoint="/poll_options", methods=["GET", "POST"]
    )
    api.add_resource(
        PollOptions,
        "/poll_options/<poll_option_id>",
        endpoint="/poll_options/<int:poll_option_id>",
        methods=["DELETE", "PATCH", "GET"],
    )

    from app.views import Polls

    api.add_resource(Polls, "/polls", endpoint="/polls", methods=["POST", "GET"])
    api.add_resource(
        Polls,
        "/polls/<poll_id>",
        endpoint="/polls/<int:poll_id>",
        methods=["DELETE", "PATCH", "GET"],
    )

    from app.views import PollsVotes

    api.add_resource(
        PollsVotes, "/polls_votes", endpoint="/polls_votes", methods=["GET", "POST"]
    )

    from app.views import Homes

    api.add_resource(Homes, "/homes", endpoint="/homes", methods=["GET", "POST"])
    api.add_resource(
        Homes,
        "/homes/<home_id>",
        endpoint="/homes/<home_id>",
        methods=["GET", "DELETE", "PATCH"],
    )

    from app.views import Fees

    api.add_resource(Fees, "/fees", endpoint="/fees", methods=['GET', 'POST'])
    api.add_resource(Fees, "/fees/<int:fee_id>", endpoint="/fees/<int:fee_id>", methods=['GET', 'PATCH', 'DELETE'])