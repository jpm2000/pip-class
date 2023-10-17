import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return[1,2,3,4,5]

@app.get('/contact')
def get_list():
    return{'name': 'Platzi'} 

@app.get('/response', response_class=HTMLResponse)
def get_list():
    return"""
    <html>
            <head>
                <title>Esta es una prueba de HTML con fastAPI</title>
            </head>
            <body>
                <h1>Cree un servidor web</h1>
            </body>
            <p>Aca puedo escribir mas cosas</p>
        </html>
    """

def run():
    store.get_categories()

if __name__ == '__main__':
    run()