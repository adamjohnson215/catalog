from flask import Flask

app = Flask (__name__)

# Create route for main and categories pages
@app.route('/')
@app.route('/categories/')
def showCategories():
	return 'This is the page that returns a list of categories!'

# Create route for adding a new category
@app.route('/categories/new/')

# Create route for editing a category
@app.route('/categories/<int:category_id>/edit/')

# Create route for deleting a category
@app.route('/categories/<int:category_id>/delete/')

# Create route to show a category's items
@app.route('/categories/<int:category_id>/')
@app.route('/categories/<int:category_id>/items/')

# Create route for adding a new item to a category
@app.route('/categories/<int:category_id>/new/')

# Create route for editing an item in a category
@app.route('/categories/<int:category_id>/items/<int:item_id>/edit')
def editItem(category_id, item_id):
	return 'This page will have a form to edit item %s in category %s' %(item_id, category_id)

# Create route for deleting an item in a category
@app.route('/categories/<int:category_id>/items/<int:item_id>/delete')
def deleteItem(category_id, item_id):
	return 'This page will have a form to delete item %s from category %s' %(item_id, category_id)


# Main function runs a webserver on localhost:8000
if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0', port = 8000)