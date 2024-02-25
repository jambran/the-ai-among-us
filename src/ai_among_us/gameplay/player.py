import uuid
from pydantic import BaseModel

class PlayerInfo(BaseModel):
    name: str
    id: uuid.UUID

class Player:
    def __init__(self, name: str):
        self.player_info = PlayerInfo(
            id=uuid.uuid4(),
            name=name,
        )


    def submit_gameplay_prompt(self):
        # get input from the player
        # give it to the gameplay server
        pass

    def submit_gameplay_response(self):
        # get input from the player
        # give it to the gameplay server
        pass
