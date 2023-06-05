import random
import operator
import textove_soubory


kahoot = ["robert", "hugo", "jeníček", "mařenka", "sněhurka", "mechanický králíček", "klobouček", "mrkvička"]   # kahoot names

boobs = "boobs", "booba", "boob", "boobies"  #list for command boobies

swearlist = open("./textove_soubory/swearwords.txt")
data = swearlist.read()
swearlist_list = data.split("\n")       #swearlist 

quotes = open("./textove_soubory/quotes.txt")
data = quotes.read()
quotes_list = data.split("\n")   

questions = open("./textove_soubory/questions.txt")
data = questions.read()
question_list = data.split("\n")        #topic questions 

def handle_response(message) -> str:
    p_message = message.lower()
    
    if operator.contains(p_message, "hey"): #if msg contains hey print haia
        return 'Haia ^^'

    if operator.contains(p_message, "roll"):    #roll dice
        return str(random.randint(1,6))
    
    if operator.contains(p_message, "d20"):    #roll dice
        return str(random.randint(1,20))
    
    if operator.contains(p_message, "help"):        #print list of commands
        return "`roll - random 1-6 number\nhey - haia ^^\nask stuff - random question\nkahoot - kahoot name\nquote - random quote \nhelp - commands`"
    
    if p_message in swearlist_list:     # answeing random swearword 
        return str(random.choice(swearlist_list))
    
    if operator.contains(p_message, "ask"):        # asks a question
        return str(random.choice(question_list))
    
    if operator.contains(p_message, "kahoot"):  #print kahoot name
        return str(random.choice(kahoot))
    
    if p_message in boobs:  #boooba
        return "heh, boobs"
    
    if operator.contains(p_message, "boo"):     #boo command
        return '*so scared o.o*'
    
    if operator.contains(p_message, "quote"):       #random quote
        return str(random.choice(quotes_list))
    
    
