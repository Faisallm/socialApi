from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

# we want to force to force the user to send the data in a schema that we expect.
# to create that schema, we need pydantic

class Post(BaseModel):
    title: str
    content: str
    # published of type boolean with default value of true.
    # whether this is provided in the body or not.
    # hence it is also optional field.
    published: bool = True
    # Optional int field of default value None
    # to create optional fields, we need to create default values.
    rating: Optional[int] = None
    
    
my_posts = [{"title": "Top Beaches in Lasgidi", "content": "Check out these awesome beaches", "id": 1}, \
    {"title": "Favourite Foods", "content": "I like pizza", "id": 2}]


def find_post(id):
    for post in my_posts:
        if post['id'] == id:
            return post
        
    return "This post does not exist"

# the order of path operations matter.

# this is like the homepage
# out http get method
@app.get('/')
def root():
    return {"message": "Faisal's API"}

# get all posts
@app.get('/posts')
def get_posts():
    return {"data": my_posts}

# getting a single post
# id: int (was done to convert post to integer.)
@app.get('/posts/{id}')
def get_post(id: int):
    # the id is given as str...
    # we shouldn't forget to convert to int.
    post = find_post(id)
    return {"post_detail": post}
    

# the name of the function never matters.
# variable payload
# of type python dictionary
# data stored in Body(...)

# when we use pydantic new_post: Post.
# fastapi automatically validates the data for us.
@app.post('/posts')
def create_post(post: Post):
    # convert pydantic model to dictionary
    post_dict = post.dict()
    # assign a random id between 0 and 1 million
    post_dict['id'] = randrange(0, 1000000)
    # save the new post to memory
    my_posts.append(post_dict)
    # return the new post to the user.
    print(my_posts)
    return {"data": post_dict}

