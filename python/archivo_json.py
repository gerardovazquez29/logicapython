from pathlib import Path
import json

data = {
    "app": "demo",
    "version": 1,
    "features": ["auth","cache"],
    "debug": False,
    "db": {"host": "localhost","port": 5432}
}

# Crea el archivo json
Path("config.json").write_text(
    json.dumps(data,ensure_ascii=False, indent=2, sort_keys=True),encoding="utf-8"
)

# lee el archivo json en terminal y automaticamente se cierra
with open("config.json","r", encoding="utf-8") as archivo:
    archivo_config = json.load(archivo)
print(archivo_config["db"]["host"]) # localhost # nomas lee una parte del json
print(archivo_config) # lee todo el contenido json
print(type(archivo_config))
