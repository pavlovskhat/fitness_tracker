"""
Fitness tracker application launcher.
"""
import sys
from .app import initialise


def main():
    """
    Launches the application and starts the event loop.
    """
    # try:
    components = initialise()
    start_application = components.get("fitness_tracker")(components)
    if not start_application:
        raise KeyError(
            "fitness_tracker not found in initialised components."
        )
    start_application.main_menu()
    # except Exception as e:
    #     print(f"Failed to launch Fitness Tracker: {e}")
    #     sys.exit(1)


if __name__ == "__main__":
    main()
