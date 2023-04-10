import json
import current_date
import rand_checker

def lambda_handler(event, context):
    print('Received event:', json.dumps(event, indent=2))

    rule_name = event['source']

    if rule_name == 'rule1':
        # execute code for rule1
        print('Executing code for rule1...')
        print(sum(1, 2, 3, 4, 5))
    elif rule_name == 'rule2':
        # execute code for rule2
        print('Executing code for rule2...')
        print(current_date.get_current_date())
    elif rule_name == 'rule3':
        # execute code for rule3
        print('Executing code for rule3...')
        print(rand_checker.randAlert())
    elif rule_name == 'rule4':
        # execute code for rule4
        print('Executing code for rule4...')
    elif rule_name == 'rule5':
        # execute code for rule5
        print('Executing code for rule5...')
    else:
        print(f'Unknown event source: {rule_name}')

    return {
        'statusCode': 200,
        'body': json.dumps('Lambda function executed successfully')
    }

#lambda_handler({'source': 'rule2'}, None)

class Person:
  def __init__(self, name="test", age=2):
    self.name = name
    self.age = age
  def __str__(self):
    return f"Person: {self.name}, {self.age}"

p1 = Person("John")

print(p1.name)
print(p1.age) 

#https://stackoverflow.com/questions/60035940/one-lambda-function-or-multiple-lambda-functions


