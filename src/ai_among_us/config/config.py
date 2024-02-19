
from dynaconf import Dynaconf
from pathlib import Path

this_file = Path(__file__)
config_dir = this_file.parent
settings_file_path = config_dir / "settings.toml"
secrets_file_path = config_dir / ".secrets.toml"


settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=[settings_file_path, secrets_file_path],
    environments=True,
)

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load these files in the order.
