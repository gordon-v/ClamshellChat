def get_response(message: str) -> str: #returns string
    p_message = message.lower()

    #Check string and generate response accordingly
    if 'hello' in p_message:
        return 'hai :3'

    if 'hi' in p_message:
       return 'haiiiii'

    if 'hai' in p_message:
        return 'haiiiiiiiii:3333:33:333:3333'
    if 'nig' in p_message:
       return '📸'

    return ''

