from flask import Flask, request 


app= Flask(__name__)
@app.route('/')
def home_page():
    html=""" 
    <html> 
        <body> 
            <h1> Hello!</h1>
            <p> welcome to my app</p>
            <a href= '/hello'> go to hello page</a>
        </body>
    </html>
    """
    return html

@app.route('/welcome')
def sayhello():
    return 'welcome'

@app.route('/welcome/home')
def saywelcomeback():
    return 'welcome home'

@app.route('/welcome/back')
def saywelcomebackagain():
    return 'welcome back'