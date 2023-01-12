import random

swearlist = ["pussy", "idiot", "piece of shit", "twat", "wanker", "son of a bitch", "son of a whore", "whore", "bitch", "holy raspberry", "cunt", "you blob", "ťuťu", "mother of Jesus"]

questions = open("questions.txt", "r")
data = questions.read()
question_list = data.split("\n")

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