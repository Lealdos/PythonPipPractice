import Store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [1,2,3,]


@app.get('/contact', response_class=HTMLResponse )
def get_lista():
    return """
        <h1>Hi this is the contact page</h1>
        <p>first paragraph</p>
    """

def run():
    Store.get_categories()

if __name__=="__main__":
    run()