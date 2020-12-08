from src.dependencies import Session


# Copied from microcosm_postgres package
class SessionContext:
    
    session = None
    
    def __init__(self, app_name, testing):
        self.app_name = app_name
        self.testing = testing
        
    def open(self):
        # Fix this by having the session come from  dependencies file
        SessionContext.session = Session.session_factory(self.app_name, self.testing).create()()
        return self

    def close(self):
        if SessionContext.session:
            SessionContext.session.close()
            SessionContext.session = None

    @classmethod
    def make(cls, app_name, testing=False):
        return cls(app_name, testing).open()

    # Required dunder methods for context
    def __enter__(self):
        return self.open()

    def __exit__(self, *args, **kwargs):
        self.close()