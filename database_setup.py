import sys 
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

#Create a category table in the database with an id, name and description
class Category(Base):
	__tablename__ = 'category'
	
	id = Column(Integer, primary_key = True)
	name = Column(String(80), nullable = False)
	description = Column(String(250))

#Make the category table serializable	
	@property
	def serialize(self):
		return {
			'name' : self.name
			'id' : self.id
			'description' : self.description
		}

		
#Create a item table in the database with an id, name, description
# and additional data in regard to its category
class CategoryItem(Base):
	__tablename__ = 'category_item'
	
	name = Column(String(80), nullable = False)
	id = Column(Integer, primary_key = True)
	description = Column(String(250))
	price = Column(String(10))
	category = relationship(Category)
	category_id = Column(Integer, ForeignKey('category.id'))
	
#Make the category_item table serializable	
	@property
	def serialize(self):
		return {
			'name' : self.name
			'id' : self.id
			'description' : self.description
			'category' : self.category
		}
		
		
#######insert at end of file#######
engine = create_engine('sqlite:///itemcatalog.db')

Base.metadata.create_all(engine)