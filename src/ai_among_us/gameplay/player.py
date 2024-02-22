import uuid



class Player:
    def __init__(self, name: str):
        self.name = name
        self.id = uuid.uuid4()


    def submit_gameplay_prompt(self):
        # get input from the player
        # give it to the gameplay server
        pass

    def submit_gameplay_response(self):
        # get input from the player
        # give it to the gameplay server
        pass
