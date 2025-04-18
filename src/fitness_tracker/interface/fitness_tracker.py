"""
Program main menu interface.
"""
import sys
from typing import Any, Callable, Dict


class FitnessTracker:
    menu = None

    def __init__(self, components: dict[str, any]):
        self.components = components

    def display_menu(self):
        print("Main Menu")
        for key, (desc, _) in self.menu.items():
            print(f"{key}: {desc.capitalize()}")

    def get_choice(self):
        while True:
            self.display_menu()
            choice = input("Enter choice (1-5): ").strip()
            if choice in self.menu:
                if choice == "5":
                    self._exit()
                self.menu[choice][1]()

    def main_menu(self):
        self.menu: Dict[str, tuple[str, Callable[[], None]]] = {
            "1": ("exercises", self.exercise_menu),
            "2": ("categories", self.category_menu),
            "3": ("routines", self.routine_menu),
            "4": ("goals", self.goal_menu),
            "5": ("exit", self._exit)
        }
        self.get_choice()

    def exercise_menu(self):
        view = self.components.get("exercise_view")(self.components)
        self.menu: Dict[str, tuple[str, Callable[[], None]]] = {
            "1": ("add exercise", view.new_exercise),
            "2": ("view exercises", view.view_exercises),
            "3": ("edit exercise", view.edit_exercise),
            "4": ("remove exercise", view.remove_exercise),
            "5": ("return to main menu", self.main_menu)
        }
        self.get_choice()

    def category_menu(self):
        view = self.components.get("category_view")(self.components)
        self.menu: Dict[str, tuple[str, Callable[[], None]]] = {
            "1": ("add category", view.new_category),
            "2": ("view categories", view.view_categories),
            "3": ("edit category", view.edit_category),
            "4": ("remove category", view.remove_category),
            "5": ("return to main menu", self.main_menu)
        }
        self.get_choice()

    def routine_menu(self):
        view = self.components.get("routine_view")(self.components)
        self.menu: Dict[str, tuple[str, Callable[[], None]]] = {
            "1": ("add routine", view.new_routine),
            "2": ("view routines", view.view_routines),
            "3": ("edit routine", view.edit_routine),
            "4": ("remove routine", view.remove_routine),
            "5": ("return to main menu", self.main_menu)
        }
        self.get_choice()

    def goal_menu(self):
        view = self.components.get("goal_view")(self.components)
        self.menu: Dict[str, tuple[str, Callable[[], None]]] = {
            "1": ("add goal", view.new_goal),
            "2": ("view routines", view.view_goal),
            "3": ("edit routine", view.edit_goal),
            "4": ("remove routine", view.remove_goal),
            "5": ("return to main menu", self.main_menu)
        }
        self.get_choice()

    @staticmethod
    def _exit():
        print("Shutting down...")
        sys.exit()
