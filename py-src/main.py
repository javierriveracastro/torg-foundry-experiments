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
        actor = game.actors.js_get(message.data.speaker.actor)  # noqa
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
    if not game.user.isGM:  # noqa
        return
    roll_result_html = html.find('.skill-roll-result')
    try:
        roll_result = int(roll_result_html.text())
    except ValueError:
        return
    target_html = (' <i class="fas fa-crosshairs tbt-crosshair"></i>')
    roll_result_html.append(target_html)
    # Get the skill real skill name
    chat_title = html.find(".skill-chat-title").text()
    skill = find_skill(get_token_or_actor_from_message(message),
                       chat_title[:-5])

    def show_defenses(event):
        """
        Shows the target defenses and its difference with the current roll
        """
        if not canvas:  # noqa
            return
        if canvas.tokens.controlled.lenght < 1:  # noqa
            return
        DEFENSES = ['dodge', 'meleeWeapons', 'unarmedCombat', 'intimidation',
                    'maneuver', 'taunt', 'trick']
        content = "<p>Resultado: {}</p>".format(roll_result)
        for token in canvas.tokens.controlled:  # noqa
            content += '<p>{}</p>'.format(token.actor.data.js_name)
            skills = dict(token.actor.data.data.skills)
            for defense in DEFENSES:
                trans_skill = game.i18n.localize(  # noqa
                    "torgeternity.skills." + defense)
                current_skill = skills.get(defense)
                content += '- {} ({}) = <strong>{}</strong><br>'.format(
                    trans_skill, current_skill.value,
                    roll_result - current_skill.value)

        chatData = {'user': game.user._id,  # noqa
                    'type': CONST.CHAT_MESSAGE_TYPES.OOC,  # noqa
                    'whisper': ChatMessage.getWhisperRecipients("GM"),  # noqa
                    'speaker': ChatMessage.getSpeaker(),  # noqa
                    'content': content}
        ChatMessage.create(chatData)  # noqa

    html.find('.tbt-crosshair').click(show_defenses)
    # skill as a paramether


def on_ready():
    """
    Foundry is ready
    """
    print("Torg basic targeting is active")


Hooks.once("ready", on_ready)  # noqa
Hooks.on("renderChatMessage", modify_message)  # noqa
