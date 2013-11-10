from formencode import Schema, validators


class TopicSchema(Schema):
    '''
    Schema for Topics - Important for Validations
    '''
    title = validators.String(not_empty=True, max=100)
    author = validators.String(not_empty=True)
    description = validators.String(not_empty=True)

