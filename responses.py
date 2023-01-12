import random

def handle_response(message) -> str:
    p_message = message.lower()
    
    if p_message == 'hey':
        return 'Haia ^^'
    
    if p_message == 'roll':
        return str(random.randint(1,6))
    
    if p_message == 'help':        
        return "`roll - random 1-6 number\nhey - haia ^^\nask stuff - random question\nfuck you - random swear  word\nhelp - commands !`"
    
    if p_message == 'fuck you':     # answeing random swearword 
        return str(random.choice(swearlist))
    
    if p_message == 'ask stuff':        # asks a question
        return str(random.choice(question_list))