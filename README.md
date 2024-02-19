# the-ai-among-us

This repo holds code to run the game The AI Among Us. 

## Installation

For local development, install the python package with 
```
poetry install
```

The project uses [dynaconf](https://www.dynaconf.com) to manage environment variables. Create a `.secrets.toml` file under `the-ai-among-us/src/ai_among_us/config` with the command
```
touch the-ai-among-us/src/ai_among_us/config/.secrets.toml
```

The file should look like this:
```toml
[default]
openai_api_key = "<your openai api key here>"

[local]

[dev]

[qa]

[prod]
```
