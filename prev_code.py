# Imports the pywikibot library, which provides tools for interacting Wikipedia
import pywikibot

# Creates a Site object, which represents the English Wikipedia, first parameter is the language code, second parameter is the site code
site = pywikibot.Site('en','wikipedia')
# Creates a Category object, which represents the Python programming language category, first parameter is the Site object, second parameter is the category name
category = pywikibot.Category(site, 'Category:Python (programming language)')
# Creates a generator object of all the articles in the category, .articles() returns all the articles in the category as a generator object
articles = category.articles()

# Iterates over the first 10 articles in the category
for page in list(articles)[:10]:
	# Checks if the page exists
	if page.exists():
		# Gets the text of the page
		text = page.text
		# Replaces all instances of 'Python' with 'Python programming language'
		new_text = text.replace('Python', 'Python programming language')
	# Checks if the text was changed
	if text != new_text:
		# Saves the new text to the page
		page.text = new_text
		# Saves the page with an edit summary
		page.save('Bot edit: clarified "Python" to "Python programming language"')