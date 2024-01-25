import response_messages

def help_response(message: str) -> str:
    return  response_messages.help_message

def wrong_input_response():
    return 'Dear Capitalist please use correct commands! Type $help for clarification'


