import random 

def get_intent(text): 
    return 

def get_response_by_intent(intent): 
    return 

def get_response_generatively(text): 
    return 

def get_failure_phrase(): 
    phrases = [ 
        'Непонятно, перефразируйте, пожалуйста', 
        'Извини, я всего лишь бот' 
    ] 
    return random.choice(phrases) 

def bot(request): 
    # NLU 
    intent = get_intent(request) 
    # Генерация ответа 
    if intent: 
        return get_response_by_intent(intent) 
    response = get_response_generatively(request) 
    if response: 
        return responce 
    get_failure_phrase()
