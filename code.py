import pywikibot

site = pywikibot.Site('en', 'wikipedia')

# Creates a generator object of all the articles in the site object, .articles() returns all the articles in the site object as a generator object
all_pages = site.allpages()

# Iterates over all the page not just the first 10
for page in all_pages:
	if page.exists():
		text = page.text
		new_text = text.replace('Python', 'Python programming language')
		if text != new_text:
			page.text = new_text
			page.save('Bot edit: clarified "Python" to "Python programming language"')

# Would you recommend running this bot for a large number of articles without restriction or human supervision?
#
# No, it's not recommended
#
#  Why?
#
# Might unintentionally change the text's meaning or introduce mistakes.
# Risks breaching Wikipedia's automated editing policies.
# Can flood the site with edits quickly, overloading servers and risking a bot account ban.
