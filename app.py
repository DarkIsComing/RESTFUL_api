from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required
from security import authenticate, identity
app=Flask(__name__)
app.config["SECRET_KEY"]='123'
api=Api(app)
items=[
]

jwt=JWT(app, authenticate, identity)

class Item(Resource):
    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x:x['name']==name, items), None)
        return {'item': item}, 200 if item else 404 

  
    def post(self,name):
        if next(filter(lambda x:x['name']==name, items),None):
            return  {'message':"item '{}' is already exists".format(name)}, 400                                        
        data=request.get_json()
        print(data)
        item={
            'name': name,
            'price':data['price']
            }
        items.append(item)
        print(items)
        return item, 201
        
    def delete(self,name):
        global items
        items=list(filter(lambda x:x['name']!=name, items))
        return {'message':"Item DElETED"}

    def put(self,name):
        data=request.get_json()
        item=next(filter(lambda x:x['name']==name, items),None)
        if item is None:
            item={'name':name,'price':data['price']}
            items.append(item)
        else:
            item.update(data)
        return item


     
class ItemList(Resource):
    def get(self):
        return {'items': items}


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

if __name__=="__main__":
    app.run()
    
