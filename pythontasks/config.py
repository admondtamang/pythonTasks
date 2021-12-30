import os

from dynaconf import Dynaconf

HERE = os.path.dirname(os.path.abspath(__file__))

settings = Dynaconf(
    envvar_prefix="pythontasks",
    preload=[os.path.join(HERE, "default.toml")],
    settings_files=["settings.toml", ".secrets.toml"],
    environments=["development", "production", "testing"],
    env_switcher="pythontasks_env",
    load_dotenv=False,
)


"""
# How to use this application settings

```
from pythontasks.config import settings
```

## Acessing variables

```
settings.get("SECRET_KEY", default="sdnfjbnfsdf")
settings["SECRET_KEY"]
settings.SECRET_KEY
settings.db.uri
settings["db"]["uri"]
settings["db.uri"]
settings.DB__uri
```

## Modifying variables

### On files

settings.toml
```
[development]
KEY=value
```

### As environment variables
```
export pythontasks_KEY=value
export pythontasks_KEY="@int 42"
export pythontasks_KEY="@jinja {{ this.db.uri }}"
export pythontasks_DB__uri="@jinja {{ this.db.uri | replace('db', 'data') }}"
```

### Switching environments
```
pythontasks_ENV=production pythontasks run
```

Read more on https://dynaconf.com
"""
