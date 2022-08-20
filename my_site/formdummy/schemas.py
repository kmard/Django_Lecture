REVIEW_SCHEMA = {
    '$schema':'http://json-schema.org/schema#',
    'type':'object',
    'properties':{
        'feedback':{
            'type':'string',
            'minLenght':3,
            'maxLenght':10,
        },
        'grade':{
            'type':'integer',
            'minimum':1,
            'maximum':100
        },
    },
    'required':['feedback','grade'],
}