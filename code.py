import pywikibot

site = pywikibot.Site('en', 'wikipedia')

# Creates a generator object of all the articles in the site object, .articles() returns all the articles in the site object as a generator object
all_pages = site.allpages()

for page in all_pages:
	if page.exists():
		text = page.text
		new_text = text.replace('Python', 'Python programming language')
		if text != new_text:
			page.text = new_text
			page.save('Bot edit: clarified "Python" to "Python programming language"')
