"""
Fitness Tracker Settings.
"""
from pathlib import Path


class Constants:
	BASE_DIR = Path(__file__).resolve().parent.parent.parent
	DB_PATH = BASE_DIR / "config" / "fitness_tracker_db.sqlite3"
	CONFIG_PATH = BASE_DIR / "config" / "modules.json"
