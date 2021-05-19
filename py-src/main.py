"""
The main module for the damage counter
"""

MODULE_NAME = 'torg-basic-targeting'


def modify_message(message, html):
    """
    Changes message adding a cross (targeting icon)
    """
    target_element = ' <i class="fas fa-crosshairs tbt-crosshair"></i>'
    html.find('.skill-roll-result').append(target_element)
    # TODO: Get the skill real skill name
    # TODO: Call a function when the target_element is clicked, with the
    # skill as a paramether


def on_ready():
    """
    Foundry is ready
    """
    print("Torg basic targeting is active")


Hooks.once("ready", on_ready)  # noqa
Hooks.on("renderChatMessage", modify_message)  # noqa
