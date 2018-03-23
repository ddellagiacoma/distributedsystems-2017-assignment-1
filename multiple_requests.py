from urllib import urlencode # Encode POST content into the HTTP header
import threading
from threading import Thread
from httplib import HTTPConnection # Create a HTTP connection, as a client (for POST requests to the other vessels)




def contact_vessel1():
	# The Boolean variable taht will be returned
	success = False
	# The variables must be encoded in the URL format, through urllib.urlencode
	post_content = urlencode({'entry': 'ciao1', 'delete': 0})
	# The HTTP header must contain the type of data transmitted, here URL encoded
	headers = {"Content-type": "application/x-www-form-urlencoded"}
	# Try to catch errors when contacting the vessel
	try:
		# Contact vessel:PORT_NUMBER since they all use the same port
		# Set a timeout to 30 seconds, after which the connection fails if nothing happened
		connection = HTTPConnection("%s:%d" % ('10.1.0.1', 80), timeout = 30)
		# Only use POST to send data (PUT and DELETE not supported)
		action_type = "POST"
		# Send the HTTP request
		connection.request(action_type, '/board', post_content, headers)
		# Retrieve the response
		response = connection.getresponse()
		# Check the status, the body should be empty
		status = response.status
		# If it receive a HTTP 200 - OK
		if status == 200:
			success = True
	# Catch every possible exceptions
	except Exception as e:
		print "Error while contacting %s" % '10.1.0.1'
		# Print the error given by Python
		print(e)

	# Return if succeeded or not
	return success

def contact_vessel2():
	# The Boolean variable taht will be returned
	success = False
	# The variables must be encoded in the URL format, through urllib.urlencode
	post_content = urlencode({'entry': 'ciao2', 'delete': 0})
	# The HTTP header must contain the type of data transmitted, here URL encoded
	headers = {"Content-type": "application/x-www-form-urlencoded"}
	# Try to catch errors when contacting the vessel
	try:
		# Contact vessel:PORT_NUMBER since they all use the same port
		# Set a timeout to 30 seconds, after which the connection fails if nothing happened
		connection = HTTPConnection("%s:%d" % ('10.1.0.2', 80), timeout = 30)
		# Only use POST to send data (PUT and DELETE not supported)
		action_type = "POST"
		# Send the HTTP request
		connection.request(action_type, '/board', post_content, headers)
		# Retrieve the response
		response = connection.getresponse()
		# Check the status, the body should be empty
		status = response.status
		# If it receive a HTTP 200 - OK
		if status == 200:
			success = True
	# Catch every possible exceptions
	except Exception as e:
		print "Error while contacting %s" % '10.1.0.2'
		# Print the error given by Python
		print(e)

	# Return if succeeded or not
	return success

if __name__ == '__main__':
    Thread(target = contact_vessel1).start()
    Thread(target = contact_vessel2).start()
