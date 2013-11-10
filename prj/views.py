from pyramid.view import view_config
from pyramid.renderers import render_to_response
from pyramid_simpleform import Form
from pyramid_simpleform.renderers import FormRenderer
from pyramid.httpexceptions import HTTPNotFound, HTTPFound
from pyramid.response import Response
import datetime

#my
from prj.resources import Root
from schema import TopicSchema
from prj.utils import slugfy,count

def my_view(request):
	return {}

@view_config(route_name='home')
def home(request):
	'''
	Render initial page with all topics (paginated)
	'''

	topics = request.db['topic'].find()
	
	return render_to_response('templates/home.html',
							 {'topics':topics,
							  'count':count(request)},
							  request=request)

@view_config(route_name='new_topic')
def new_topic(request):
	'''
	Create New Topic
	Render form and validate automatically.
	See Schema -> TopicSchema For understand.

	
	'''
	form = Form(request,schema=TopicSchema)
	if form.validate():
		topic = form.data['title']
		author = form.data['author']
		desc = form.data['description']
		date = datetime.datetime.now()
		url = slugfy(topic)
		topic_tuple = {'title' : topic, 
					   'url' : url, 
					   'author': author,
					   'description': desc,
					   'topic_date':date.strftime("%d/%m/%Y"),
					  }
		request.db['topic'].insert(topic_tuple)
		return HTTPFound(location='/')

	return render_to_response('templates/new_topic.html',
							 {'form' : FormRenderer(form),
							  'count':count(request)},
							  request=request)

@view_config(route_name='find')
def find(request):
	'''
	Search Topics. Get All topics contain 
	String from POST. (using mongoDB regex)
	If not POST, go home!
	
	'''
	if request.method == "POST":
		if request.POST.get('find'):
			topics = request.db['topic'].find({"title": 
											  {'$regex': request.POST.get('find'), 
											   '$options': 'i'
											  }});	
		else:
			topics = False	

		return render_to_response('templates/search.html',
								 {'topics':topics,
								 'count':count(request)},
								 request=request)
	return HTTPFound(location='/')

@view_config(route_name='view_topic')
def view_topic(request,topic_slug):
	'''
	Show selected Topic with author, description
	and all messages.
	
	'''
	view_topic = request.db['topic'].find_one({'url':topic_slug.matchdict['url']})
	answers = request.db['answer'].find({'topic_index': topic_slug.matchdict['url'] })
	
		

	return render_to_response('templates/view_topic.html',
							 {'view_topic':view_topic,
							  'answers' : answers,
							  'count':count(request),
							  },
							 request=request)


@view_config(route_name="new_answer")
def new_answer(request):
	'''
	Create new answer associate a topic.
	'''
	if request.method == "POST":
		author = request.POST.get('author')
		content = request.POST.get('content')
		date = datetime.datetime.now()
		answer_tuple = {
					   'author': author,
					   'content': content,
					   'votes' : 0,
					   'topic_index' : request.matchdict['url'],
					   'answer_date' : date.strftime("%d/%m/%Y"),
					  }
		request.db['answer'].insert(answer_tuple)
		return HTTPFound(location='/topic/'+request.matchdict['url'])
	return HTTPFound(location='/')


@view_config(route_name="vote_up")
def vote_up(request):
	'''
	incremet Vote for answer. Call ajax mehtod
	'''
	# votes = request.db['answer'].find({'_id': 'ObjectId("'+request.matchdict["id"]+'")'})
	#.update({ '$inc' : { 'votes' : +1 }})
	
	return HTTPFound(location='/topic/'+request.matchdict['url'])


@view_config(route_name='last_five')
def last_five(request):
	'''
	Get last 5 inserted topics. 
	flag_five - set h1 in Home.html if last_five called.
	(write less)
	'''
	flag_five = True
	topics = request.db['topic'].find() \
								.sort([("$natural", -1),("topic_date", -1)]) \
								.limit(5)
	

	return render_to_response('templates/home.html',
							  {'topics':topics,
							   'flag_five':flag_five,
							   'count':count(request)},
							  request=request)
