import substance_painter
from silex_client.action.action_query import ActionQuery
from silex_client.core.context import Context
from silex_client.resolve.config import Config

def create_menus():
    # Get action names from the config
    actions = [item["name"] for item in Config().actions]

    #Create Menu
    print("Creating Menus!")

Context.get().start_services()
create_menus()