import web 

urls = (
    #'/', 'index'
    '/hello', 'index'
)

app = web.application(urls, globals())

render = web.template.render('templates/', base='layout')

class index:
    def GET(self):
        return render.hello_form()
        
    def POST(self):
        form = web.input(name="Nobody", greet="Hello")
        greeting = "%s, %s" % (form.greet, form.name)
        return render.index(greeting=greeting)
        
    """
    From Ex 50
    def GET(self):
        greeting = "Hello Green World"
        return render.index(greeting = greeting)
    """
        
if __name__ == "__main__":
    app.run()
    
"""
From Ex 50
Read the documentation at http://webpy.org/ which is the same as the lpthw.web project.
Experiment with everything you can find there, including their example code.
Read about HTML5 and CSS3 and make some other .html and .css files for practice.
If you have a friend who knows Django and is willing to help you, then consider doing Ex 50, 51, and 52 in Django instead to see what that's like.

"""    