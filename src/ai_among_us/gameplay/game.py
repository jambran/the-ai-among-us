from random import random

from .player import Player
from pydantic import BaseModel
from pathlib import Path

def load_default_responses():
    resources_dir = Path(__file__).parent / "resources"
    default_responses_path = resources_dir / "gameplay_prompts.csv"
    with open(default_responses_path, "r") as f:
        lines = f.readlines()
    return lines

class Vote(BaseModel):
    voter_name: str
    votee_name: str
    response_string: str



class Game:
    """
    For now, an entire game consists of:

    Lobby:
    - one player initiates the lobby
    - other players join the lobby
    - the initiating player starts the game when all players are in

    Game:
    - select a random player to submit the prompt (or use an AI generated prompt)
    - each player writes their response
    - the AI writes its response
    - when all responses are in, reveal the responses to all players
    - players select the response the AI generated
    - authors of responses are revealed
    - points are tallied?
    """
    default_responses = load_default_responses()
    def __init__(self):
        self.players: list[Player] = []
        # status to indicate whether gameplay has started
        self.are_all_players_in = False

        self.prompt = None  # initially none, to be filled by player when game starts

        # responses are stored on the player object
        self.votes = list[Vote]

        # maps player name to times they identified the ai correctly
        self.points: dict[str, int] = {}


    def add_player(self, player: Player):
        self.players.append(player)
        self.points[player.name] = 0


    def start(self):
        self.are_all_players_in = True

    def set_prompt(self, prompt: str):
        self.prompt = prompt

    def _fetch_prompt_from_default_list(self):
        return random.choice(self.default_responses)