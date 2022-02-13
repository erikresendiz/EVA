# import module
import requests
import bs4

def question(question):
	question = question.split(" ")
	question = "+".join(question)
	# Generating the url
	url = "https://google.com/search?q=" + question

	# Sending HTTP request
	request_result = requests.get( url )

	# Pulling HTTP data from internet
	soup = bs4.BeautifulSoup( request_result.text
							, "html.parser" )

	# Finding temperature in Celsius.
	# The temperature is stored inside the class "BNeawe".
	answer = soup.find( "div" , class_='BNeawe' ).text
	
	return( answer )

