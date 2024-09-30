from .factory import create_ui, create_api, create_app

""" UWSGI Entry Points """
ui = create_ui()
api = create_api()
app = create_app()
