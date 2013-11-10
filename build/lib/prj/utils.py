from prj.resources import Root
from schema import TopicSchema

def slugfy(field):
	'''
	Create slugs for posts
	field = url (mongodb)
	'''
	return field.lower().replace(' ','-')

def count(request):
	count = request.db['topic'].count()
	return count