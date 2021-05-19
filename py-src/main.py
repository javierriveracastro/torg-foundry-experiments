"""
The main module for the damage counter
"""

MODULE_NAME = 'torg-basic-targeting'


def on_ready():
    """
    Foundry is ready
    """
    print("Torg basic targeting is active")


Hooks.once("ready", on_ready)  # noqa
