import pywikibot

site = pywikibot.Site('en', 'wikipedia')

all_pages = site.allpages()

for page in all_pages:
	if page.exists():
		text = page.text
		new_text = text.replace('Python', 'Python programming language')
		if text != new_text:
			page.text = new_text
			page.save('Bot edit: clarified "Python" to "Python programming language"')
