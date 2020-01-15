from flask import Flask, request
from flask_restful import Resource, Api
# Resource is just a thing that our API can return and create.
# Resource are usually mapped into database tables as well,

app = Flask(__name__)
# flask is going to be our app and our app is gonna have all these routes
# as we saw in the last section 
# and then we can create new routes
# and assign methods to them and things like that.

# And we're gonna create something else which is gonna be the API.
# And the API as you can see is imported from flask_restful
# and that's just going to allow us to very easily add these resources to it.
api = Api(app)
# for this resource you can get, put, post, and delete and so on.

#we're going to use an in-memory database,w hich is just a Python list
items = []

# The API works with resources and every resource has to be a class.
#  class student then inherits from the class resource.
class Item(Resource):
    def get(self, name):
        # Get is going to look in items list and retrieve an item
        # that matches the name that has been requested.
        # All it has to do is iterate over this list and return the appropriate item.
        for item in items:
            if item['name'] == name:
                return item
                # we'd no longer need to do JSONify when talking with flask restful 
                # because flask restful does it for us, so we can just return dictionaries.
        # what happens if we don't find the item with a specific name.
        # as we know, all Python methods return none by default
        # what we have to do is change that return none to be something like item is none.
        return {'item': None}, 404
        # The error code for not found is 404.
        # This is a common interview question as well.
        # What's the most popular http status code?
        # And the most popular is not 404, it is 200.


    # so now we have our resource and what we've sent is that this resource can only
    # be accessed with a get method.

    def post(self, name):
        # The first thing we have to do is to go up here and make sure to import request.
        # That is going to be when somebody such as postman
        # makes a request to our API, that request is in this variable.
        # So, that request is going to have a JSON payload, a body attached to it.
        # So, we're going to say data equals request.get JSON.
        # If the request does not attach a JSON payload or the request does not have the proper content-type header,
        
        # data = request.get_json()
        # if your clients are going to give you JSON or not, you can prevent this from giving you an error. 
        # There are two things you that you can pass this method that are really useful.
        
        # data = request.get_json(force=True)
        # force=True means that you do not need the content-type header.
        # It will just look in the content and it will format it even if the content type header
        # is not set to be application/JSON.
        # This is nice, but it's also dangerous

        # The other one that is also quite handy sometimes is silent equals true and what this does is
        # it doesn't give an error, it just basically returns none.
        data = request.get_json(silent=True)

        item = {'name': name, 'price': data['price']}
        items.append(item)
        # that'll put this dictionary as one of the elements in this list at the very end of the list.
        # Finally, we also want to tell the client, in this case, Postman, but it could be a mobile app
        # or web app, that we have processed this addition, that we have created this item and added it to our database,
        # in this case, our list.        
        # In order to do that, we're going to just return item so that the application knows that this has happened.

        # Something else to remember is that creating
        # also has its own http status code, 
        # 200 OK is for when the server just kind of returns some data and says everything's okay.
        # 201 is for created.
        return item, 201

        # Notice there is also a very similar status code called 202, which is accepted,
        # and the accepted code is when you are delaying the creation.
        # For example, if creating the object takes a long time,
        # you may say, "I'm gonna create this object,
        # "return 202, and the object that's created then
        # "after five or 10 minutes."
        # The client doesn't have to wait five or 10 minutes,
        # but it knows that you have accepted the creation of that.
        # It may then fail, but that's out with the client's control.
        # So, hopefully all of that makes sense.
        # Using the right status codes is very important
        # because it is a very quick way of clients,
        # like web applications or mobile applications,

# 73. Class item list is gonna be on new resource,
class ItemList(Resource):
    def get(self):
        return {'items': items}
        # items is a list which contains all our items.

# tell our API, okay , This resource that we've created, the student,
# now is gonna be accessible via our API,
api.add_resource(Item, '/item/<string:name>')

# Don't forget to add the resource item list, and make sure to give it the correct endpoint,
api.add_resource(ItemList, '/items')

# finally app.run and port=5000, this is not necessary, that's the default
app.run(port=5000, debug=True)
    # 73. Now when you get on error message,
    # when something really goes wrong in your application,


