###!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from bottle import Bottle, route, run, template, ServerAdapter
try:
    from paste import httpserver
    from paste.translogger import TransLogger
    PASTE_SERVER = True
except ModuleNotFoundError:
    PASTE_SERVER = False

from config import serverAddres, serverPort, newTab, showUsers, showUsersComand

if not os.path.isfile("DONE_PATCHING"):
    print("Please firsth install by start patcher.py")
    input()

import folderTreeView.folderTreeView_patched as folderTreeView
import folderTreeView.file_orginiser_patched as file_orginiser
import flashcards.flashcards_patched as flashcards
import simpleQuizEngine.quiz_patched as simpleQuizEngine
import staticFiles

ver = 0.6

apps_moduls = [(staticFiles, '/'), \
 (flashcards, '/flashcards/'), \
 (folderTreeView, '/folderTreeView/'),\
 (file_orginiser, '/folderTreeOrganiser/'),\
 (simpleQuizEngine, '/simpleQuizEngine/')\
]

app_names = [
(('/simpleQuizEngine/main/', "View avalable quizes"), ('/simpleQuizEngine/editor/', "Open editor")),
(('/flashcards/', "View flashcards"), ('/flashcards/be/', "Open flashcards editor")),
(('/folderTreeView/', "View files/documents"), ('/folderTreeOrganiser/', "Open files organiser"))
]

app = Bottle()

for module in apps_moduls:
    app.mount(module[1], module[0].app)

@app.route('/')
def index():
    return template("index", app_names = app_names, newTab = newTab, showUsers = showUsers)

if showUsers:
    @app.route('/show_logged_in_users')
    def index():
        result = subprocess.run(showUsersComand, stdout=subprocess.PIPE)
        return template('users', result=result.stdout)

class MyWSGIRefServer(ServerAdapter):
    def run(self, handler):
        handler = TransLogger(handler, setup_console_handler = (not self.quiet))
        httpserver.serve(handler,
                         host = self.host,
                         port=str(self.port), **self.options)
    def stop(self):
        pass
    def __repr__(self):
        return "PasteServer()"

print(" ")
print(" ")
print(f"mainScript {ver}")

if PASTE_SERVER:
    server_custom = MyWSGIRefServer(host=serverAddres, port=serverPort)
    app.run(server = server_custom, debug=True)
else:
    app.run(host = serverAddres, port = serverPort, debug=True)
