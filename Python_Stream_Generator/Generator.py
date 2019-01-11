#pip install essential-generators
#https://pypi.org/project/essential-generators/
from essential_generators import DocumentGenerator

def generate_Documents():
	gen = DocumentGenerator()
	
	gen.init_word_cache(5)
	gen.init_sentence_cache(5)
	
	gen.word_cache = ['Is', 'this', 'working', 'pls', 'work']
	gen.sentence_cache = ['This is a great step in the right direction', 'Every moment is the paradox of now or never', 'World will judge you on this moment']
	
	print(gen.word_cache)
	print(gen.sentence_cache)
	
	template = {
	'id': 'guid',
	'status': ['online', 'offline', 'dnd', 'anonymous'],
	'age': 'small_int',
	'homepage': 'url',
	'name': 'name',
	'headline': 'sentence',
	'text': 'paragraph'
	}
	
	gen.set_template(template)
	documents = gen.documents(10)
	
	print(documents[0])


if __name__== "__main__":
  generate_Documents()