import response_messages
import backend

def help_response(message: str) -> str:
    return  response_messages.help_message
                            
def plot_response(message: str):
    backend.getPlot(message)
    return 'mega.png'

def huh(message: str):
    return 'Huh?'

