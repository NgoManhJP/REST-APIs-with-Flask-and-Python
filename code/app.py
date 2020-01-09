from flask import Flask
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

# The API works with resources and every resource has to be a class.
#  class student then inherits from the class resource.
class Student(Resource):
    def get(self, name):
        return {'student': name}
    # so now we have our resource and what we've sent is that this resource can only
    # be accessed with a get method.

# tell our API, okay , This resource that we've created, the student,
# now is gonna be accessible via our API,
api.add_resource(Student, '/student/<string:name>')

# finally app.run and port=5000, this is not necessary, that's the default
app.run(port=5000)
