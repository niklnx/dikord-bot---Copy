import random
import operator


kahoot = ["robert", "hugo", "jeníček", "mařenka", "sněhurka", "mechanický králíček", "klobouček", "mrkvička"]

boobs = "boobs", "booba", "boob", "boobies"

swearlist = open("swearwords.txt")
data = swearlist.read()
swearlist_list = data.split("\n")

questions = open("questions.txt", "r")
data = questions.read()
question_list = data.split("\n")

def handle_response(message) -> str:
    p_message = message.lower()
    
    if operator.contains(p_message, "hey"):
            return 'Haia ^^'

    if operator.contains(p_message, "roll"):
        return str(random.randint(1,6))
    
    if operator.contains(p_message, "help"):        
        return "`roll - random 1-6 number\nhey - haia ^^\nask stuff - random question\nfuck you - random swear  word\nkahoot - kahoot name \nhelp - commands !`"
    
    if p_message in swearlist_list:     # answeing random swearword 
        return str(random.choice(swearlist_list))
    
    if operator.contains(p_message, "ask"):        # asks a question
        return str(random.choice(question_list))
    
    if operator.contains(p_message, "kahoot"):
        return str(random.choice(kahoot))
    
    if p_message in boobs:
        return "heh, boobs"