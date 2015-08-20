from flask import Flask

app = Flask (__name__)

# routes for main and categories pages
@app.route('/')
@app.route('/categories/')
# Create 
def showCategories():
	return 'This is the page that returns a list of categories!'

# Create route for adding a new category
@app.route('/category/new/')
def newCategory():
	return 'This page will have a form to create a new category'

# Create route for editing a category
@app.route('/category/<int:category_id>/edit/')
def editCategory(category_id):
	return 'This page will have a form to edit category %s' % category_id

# Create route for deleting a category
@app.route('/category/<int:category_id>/delete/')
def deleteCategory(category_id):
	return 'This page will have a form to delete category %s' % category_id

# Create route to show a category's items
@app.route('/category/<int:category_id>/')
@app.route('/category/<int:category_id>/items/')
def showItem(category_id):
	return 'This page will return all items in category %s' % category_id

# Create route for adding a new item to a category
@app.route('/category/<int:category_id>/item/new/')
def newItem(category_id):
	return 'This page will have a form to add a new item in category %s' % category_id

# Create route for editing an item in a category
@app.route('/category/<int:category_id>/item/<int:item_id>/edit')
def editItem(category_id, item_id):
	return 'This page will have a form to edit item %s in category %s' %(item_id, category_id)

# Create route for deleting an item in a category
@app.route('/category/<int:category_id>/item/<int:item_id>/delete')
def deleteItem(category_id, item_id):
	return 'This page will have a form to delete item %s from category %s' %(item_id, category_id)


# Main function runs a webserver on localhost:8000
if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0', port = 8000)