from flask import g

from src.context import SessionContext


def configure_session_factory(app, app_name, testing):
    return register_session_factory(app, SessionContext.make(app_name, testing))


# copied from microcosm_flask package
def register_session_factory(app, session_factory):
    key = 'session'

    @app.before_request
    def begin_session():
        setattr(g, key, session_factory.session)

    @app.teardown_request
    def end_session(*args, **kwargs):
        # NB: session will be none if there's an error raised in `before_request`
        session = getattr(g, key, None)
        if session is not None and hasattr(session, "close"):
            session.close()

