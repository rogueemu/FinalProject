from flask import Flask, render_template

class Webpage:
    pageCount = 0

    def __init__(self, type, url):
        self.type = type
        self.url = url
        Webpage.pageCount += 1
        
    #later on, it will ask someone if they want to go to a webpage or something
    def introduce_self(self):
        print("My webpage is  127.0.0.1:7000/" + self.url)
    #will probaly start the website or something
    def start_webpage(self):
        return
#makes the school class
class School:
    schoolCount = 0

    def __init__(self, name, url):
        School.schoolCount += 1
        self.url = url
        self.name = name

    def introduce_self(self):
        print(self.name + "'s webpage is at 127.0.0.1:7000/" + self.url)

    def list_classes(name):
        print(name.List)

    def start_webpage(self):
        @app.route('/' + self.url)
        def url():
            return render_template(self.url + '.html')
        
        
        
        

        
        


woodlandM = School("Woodland Middle School", 'woodlandM')

woodlandM.introduce_self()
    
