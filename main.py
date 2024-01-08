from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()


# the order of path operations matter.

# this is like the homepage
# out http get method
@app.get('/')
def root():
    return {"message": "Faisal's API"}

@app.get('/posts')
def get_posts():
    return {"data": "This is your posts"}

# the name of the function never matters.
# variable payload
# of type python dictionary
# data stored in Body(...)
@app.post('/createposts')
def create_post(payload: dict = Body(...)):
    # extracting data sent with post request and returning it
    return {"new_post": f"Title: {payload['title']}, Content: {payload['content']}"}

# we want to force to force the user to send the data in a schema that we expect.