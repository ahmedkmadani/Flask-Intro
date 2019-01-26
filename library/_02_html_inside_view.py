form flask import Flask 


app = Flask(_name_)


@app.route(/)
def hello_world():
	html = """ 
		<html>
			<h1>Welcome to our Library!</h1>
			{authors_ul}
			# <ul>
			# 	<li>Aron</li>
			# 	<li>Ahmed</li>
			# 	<li>Chevez</li>
			# 	<li>Ibra</li>
			# </ul>
		</html>
	"""
	authors = ['Aron', 'Ahmed', 'Chevez', 'Ibra']

	authors_list = "<ul>"
	authors_list += "\n".join(["<li>{author}</li>".format(author=author) for author in authors])
	authors_list += "</ul>"
	print(authors_list)

	return html.format(authors_ul=authors_list)
 