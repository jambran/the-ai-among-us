from random import random

from .player import PlayerInfo
from pydantic import BaseModel, Field
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


class GameInfo(BaseModel):
    """
    Object to hold all state regarding a game
    """
    id: str
    players: list[PlayerInfo] = Field(default_factory=list)

    # status to indicate whether gameplay has started
    are_all_players_in: bool = False

    # initially none, to be filled by player when game starts

    prompt: str = None

    # responses are stored on the player object
    votes: list[Vote] = Field(default_factory=list)

    # maps player name to times they identified the ai correctly
    points: dict[str, int] = Field(default_factory=dict)


class Game:
    """
    Object to hold all behavior for updating a GameInfo object

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
    def __init__(self, id_: str):
        self.game_info = GameInfo(id=id_)


    def add_player(self, player: PlayerInfo):
        self.game_info.players.append(player)
        self.game_info.points[player.name] = 0


    def start(self):
        self.game_info.are_all_players_in = True

    def set_prompt(self, prompt: str):
        self.game_info.prompt = prompt

    def _fetch_prompt_from_default_list(self):
        return random.choice(self.default_responses)