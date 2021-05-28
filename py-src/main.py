"""
The main module for the damage counter
"""

MODULE_NAME = 'torg-basic-targeting'


def get_token_or_actor_from_message(message):
    """
    Recovers the actor or the token actor from a message
    """
    actor = None
    if message.data.speaker.token:
        # If we can find a token the best
        token = canvas.tokens.js_get(message.data.speaker.token)  # noqa
        if token:
            actor = token.actor
    if not token:
        actor = game.actors.js_get(memoryview.data.speaker.actor)  # noqa
    return actor


def find_skill(actor, string):
    """
    Finds a skill in an actor from its translated name
    """
    for skill in Object.js_keys(actor.data.data.skills):  # noqa
        if string == game.i18n.localize("torgeternity.skills." + skill):  # noqa
            return skill


def modify_message(message, html):
    """
    Changes message adding a cross (targeting icon)
    """
    target_element = ' <i class="fas fa-crosshairs tbt-crosshair"></i>'
    html.find('.skill-roll-result').append(target_element)
    # Get the skill real skill name
    chat_title = html.find(".skill-chat-title").text()
    skill = find_skill(get_token_or_actor_from_message(message),
                       chat_title[:-5])
    console.log(skill)
    # TODO: Call a function when the target_element is clicked, with the
    # skill as a paramether


def on_ready():
    """
    Foundry is ready
    """
    print("Torg basic targeting is active")


Hooks.once("ready", on_ready)  # noqa
Hooks.on("renderChatMessage", modify_message)  # noqa
