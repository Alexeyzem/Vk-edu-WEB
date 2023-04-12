import random

QUESTIONS = [
    {
        'id' : i,
        'title': f'Question {i+1}',
        'text': f'Text {i+1}',
        'count_answer' : i+1,
        'answers':[
            {
                'ans_id':j,
                'text' : f'Answer{j+1}',
            } for j in range (i+1)
        ],
        'tags':[
            {
                'tags_id':j,
                'text' :f'Tags{j+1}',
            } for j in range(i+1)
        ],
        'like': random.randint(0,100)
    } for i in range(10)
]

