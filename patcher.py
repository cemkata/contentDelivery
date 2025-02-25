from zipfile import ZipFile 
import os
import shutil
from config import contentFolder

def replace_in_file(toReplace_list, destination_file):
    for r in toReplace_list:
        search_text = r[0]
        replace_text = r[1]
        # Opening our text file in read only 
        # mode using the open() function 
        with open(destination_file, 'r', encoding="utf8") as file: 
          
            # Reading the content of the file 
            # using the read() function and storing 
            # them in a new variable 
            data = file.read() 
          
            # Searching and replacing the text 
            # using the replace() function 
            data = data.replace(search_text, replace_text) 
          
        # Opening our text file in write only 
        # mode to write the replaced content 
        with open(destination_file, 'w', encoding="utf8") as file: 
          
            # Writing the replaced data in our 
            # text file 
            file.write(data)

def patching(Tree = 1, Cards = 1, Quiz = 1):
    cwd = os.getcwd()
    print("Patching the applications.")
    print("Please wait.")
    if Tree == 1:
        ##############################################
        ## pathing folderTreeView/file_orginiser.py ##
        ##############################################
        source = os.path.join(cwd, "folderTreeView", "file_orginiser.py")
        destination = os.path.join(cwd, "folderTreeView", "file_orginiser_patched.py")
        shutil.copy(source, destination)
        toReplace = [("""template('""","""template('folderTreeView/"""),
        ("""RecycleBinEnabled =""", """RecycleBinEnabled = False #""")]
        replace_in_file(toReplace, destination)

        ##############################################
        ## pathing folderTreeView/folderTreeView.py ##
        ##############################################
        source = os.path.join(cwd, "folderTreeView", "folderTreeView.py")
        destination = os.path.join(cwd, "folderTreeView", "folderTreeView_patched.py")
        shutil.copy(source, destination)
        toReplace = [('''cnfgFile = "config.ini"''', '''cnfgFile = "./folderTreeView/config_patched.ini"'''),
        ('''port = config['DEFAULT']['Port']''', ""),
        ('''host = config['DEFAULT']['ip']''', ""),
        ('''ip_pattern = re.compile('(?:^|\b(?<!\.))(?:1?\d\d?|2[0-4]\d|25[0-5])(?:\.(?:1?\d\d?|2[0-4]\d|25[0-5])){3}(?=$|[^\w.])')''', ""),
        ('''if not ip_pattern.match(host):''', ""),
        ('''raise KeyError('Server IP address')''', ""),
        ('''fileOrganaserFlag.lower() == "true"''', "False"),
        ('''cnfgFile = "config.ini"''','''cnfgFile = ".\folderTreeView\config.ini"'''),
        ("""template('""","""template('folderTreeView/"""),
        ('''import file_orginiser''','''import folderTreeView.file_orginiser_patched as file_orginiser'''),
        ("""return static_file(filepath, root='./views/static')""","""return static_file(filepath, root='./views/folderTreeView/static')"""),
        ("""return static_file(filepath,  root='./views/ui')""","""return static_file(filepath, root='./views/folderTreeView/ui')"""),
        ("""@app.route('/files/<filepath:path>')""", "")]
        replace_in_file(toReplace, destination)
    
        ##############################################
        ## pathing folderTreeView/config.ini        ##
        ##############################################
        source = os.path.join(cwd, "folderTreeView", "config.ini")
        destination = os.path.join(cwd, "folderTreeView", "config_patched.ini")
        shutil.copy(source, destination)
        toReplace = [('''skipPath = ''', '''skipPath = ./folderTreeView/'''),
        ('''skipPrefix = ''', '''skipPrefix = ./folderTreeView/'''),
        ('''skipExtension = ''', '''skipExtension = ./folderTreeView/''')]
        replace_in_file(toReplace, destination)

    if Cards == 1:
        ##############################################
        ## pathing flashcards/flashcards.py         ##
        ##############################################
        source = os.path.join(cwd, "flashcards", "flashcards.py")
        destination = os.path.join(cwd, "flashcards", "flashcards_patched.py")
        shutil.copy(source, destination)
        toReplace = [('''from config import * # App config is loaded here''', '''from flashcards.config import * # App config is loaded here"'''),
        ('''if __name__ == '__main__':''', '''\nif not os.path.exists(database):\n   createDB()\nif __name__ == '__main__':'''),
        ('''print("Done!")''','''print("Done with creating DB for flashcards!")'''),
        ("""return static_file(filepath, root='./views/static')""","""return static_file(filepath, root='./views/flashcards/static')"""),
        ("""template('""","""template('flashcards/"""),
        ('''template("''','''template("flashcards/'''),
        ('''redirect("/showflashcards''','''redirect("./showflashcards'''),
        ("""return static_file(filepath, root='./views/ui')""","""return static_file(filepath, root='./views/flashcards/ui')""")]
        replace_in_file(toReplace, destination)

    if Quiz == 1:
        ##############################################
        ## pathing simpleQuizEngine/config.py       ##
        ##############################################
        source = os.path.join(cwd, "simpleQuizEngine", "config.py")
        destination = os.path.join(cwd, "simpleQuizEngine", "config_patched.py")
        shutil.copy(source, destination)
        toReplace = [('''config_files''', '''simpleQuizEngine/config_files'''),
                     ('''serverAddres = config['DEFAULT']['ip']''', '''serverAddres = "localhost"'''),
                     ('''serverPort = config.getint('DEFAULT', 'Port')''', '''serverPort = 80''')]
        replace_in_file(toReplace, destination)

        ###############################################
        ## pathing simpleQuizEngine/versionGetter.py ##
        ###############################################
        source = os.path.join(cwd, "simpleQuizEngine", "versionGetter.py")
        destination = os.path.join(cwd, "simpleQuizEngine", "versionGetter_patched.py")
        shutil.copy(source, destination)
        toReplace = [('''version.nfo''', '''./simpleQuizEngine/version.nfo''')]
        replace_in_file(toReplace, destination)

        ###############################################################
        ## pathing simpleQuizEngine/importQuestionsHelper.py         ##
        ###############################################################
        source = os.path.join(cwd, "simpleQuizEngine", "importQuestionsHelper.py")
        destination = os.path.join(cwd, "simpleQuizEngine", "importQuestionsHelper_patched.py")
        shutil.copy(source, destination)
        toReplace = [('''from config ''', '''from simpleQuizEngine.config_patched '''),
                     ('''from versionGetter ''', '''from simpleQuizEngine.versionGetter_patched ''')]
        replace_in_file(toReplace, destination)

        ##############################################
        ## pathing simpleQuizEngine/quiz.py         ##
        ##############################################
        source = os.path.join(cwd, "simpleQuizEngine", "quiz.py")
        destination = os.path.join(cwd, "simpleQuizEngine", "quiz_patched.py")
        shutil.copy(source, destination)
        toReplace = [('''from config ''', '''from simpleQuizEngine.config_patched '''),
                     ('''from versionGetter ''', '''from simpleQuizEngine.versionGetter_patched '''),
                     ('''from importQuestionsHelper ''', '''from simpleQuizEngine.importQuestionsHelper_patched '''),
                     ('''def main():''', '''print("Starting dump wizard "+ str(ver))\ndef main():'''),
                     ("""template('""","""template('simpleQuizEngine/"""),
                     ('''template("''','''template("simpleQuizEngine/'''),
                     ('''redirect("/editor''','''redirect("/simpleQuizEngine/editor'''),
                     #("""redirect('""","""redirect("."""),
                     ("""return static_file(filepath, root='./views/static')""","""return static_file(filepath, root='./views/simpleQuizEngine/static')""")]
        replace_in_file(toReplace, destination)

def migrating(Tree = 1, Cards = 1, Quiz = 1):
    cwd = os.getcwd()
    print("Migrating templates.")
    import glob
    if Quiz == 1:
        ##############################################
        ## pathing simpleQuizEngine templates       ##
        ##############################################
        source = os.path.join(cwd, "simpleQuizEngine", "views")
        destination = os.path.join(cwd, "views", "simpleQuizEngine")
        shutil.rmtree(destination, ignore_errors=True)
        shutil.copytree(source, destination, dirs_exist_ok=True)
        toReplace = [("""% include('footer.tpl')""","""% include('simpleQuizEngine/footer.tpl')"""),
                     ("""/static""","""/simpleQuizEngine/static""")
                     ]
        for tpl in glob.glob(destination+"/*.tpl"):
            replace_in_file(toReplace, tpl)
        source = './views/simpleQuizEngine/footer.tpl'
        toReplace = [("""from versionGetter import getVersion""","""from simpleQuizEngine.versionGetter_patched import getVersion""")]
        replace_in_file(toReplace, source)
        source = './views/simpleQuizEngine/showquestions.tpl'
        toReplace = [("""/editor/""","""./""")]
        replace_in_file(toReplace, source)
        source = './views/simpleQuizEngine/static/nicEditorMyExtension.js'
        toReplace = [("""iconsPath : '/static/nic/new_nicEditorIcons.png'""","""iconsPath : '/simpleQuizEngine/static/nic/new_nicEditorIcons.png'""")]
        replace_in_file(toReplace, source)
        source = './views/simpleQuizEngine/index.tpl'
        toReplace = [("""saveFile('/main/get""","""saveFile('/simpleQuizEngine/main/get""")]
        replace_in_file(toReplace, source)

    if Tree == 1:
        ##############################################
        ## pathing folderTreeView templates         ##
        ##############################################
        source = os.path.join(cwd, "folderTreeView", "views")
        destination = os.path.join(cwd, "views", "folderTreeView")
        shutil.rmtree(destination, ignore_errors=True)
        shutil.copytree(source, destination, dirs_exist_ok=True)
        toReplace = [("""/static""","""/folderTreeView/static""")]
        for tpl in glob.glob(destination+"/*.tpl"):
            replace_in_file(toReplace, tpl)

        destination = os.path.join(cwd, "views", "folderTreeView", "files.tpl")
        toReplace = [("""/ui""","""/folderTreeView/ui""")]
        replace_in_file(toReplace, destination)
        destination = os.path.join(cwd, "views", "folderTreeView", "ui", "js", "myScripts.js")
        toReplace = [("""const rootPath = "/files";""","""const rootPath = "/folderTreeOrganiser";""")]
        replace_in_file(toReplace, destination)

        toReplace = [('''/getFiles''','''/folderTreeView/getFiles'''),
        ('''addleaf(treeMenu, treeValues, "");''','''addleaf(treeMenu, treeValues, ".");''')
        ]
        destination = os.path.join(cwd, "views", "folderTreeView", "static", "treemenu.js")
        replace_in_file(toReplace, destination)
        destination = os.path.join(cwd, "views", "folderTreeView", "static", "treemenu.old.js")
        replace_in_file(toReplace, destination)

    if Cards == 1:
        ##############################################
        ## pathing flashcards templates             ##
        ##############################################
        source = os.path.join(cwd, "flashcards", "views")
        destination = os.path.join(cwd, "views", "flashcards")
        shutil.rmtree(destination, ignore_errors=True)
        shutil.copytree(source, destination, dirs_exist_ok=True)
        toReplace = [("""% include('__header.tpl')""","""% include('flashcards/__header.tpl')"""),
        ("""% include('__footer.tpl')""","""% include('flashcards/__footer.tpl')"""),
        ("""% from config import ver""","""% from flashcards.config import ver""")]
        for tpl in glob.glob(destination+"/*.tpl"):
            replace_in_file(toReplace, tpl)

        destination = os.path.join(cwd, "views", "flashcards", "__header.tpl")
        toReplace = [("""/static""","""/flashcards/static/""")]
        replace_in_file(toReplace, destination)

    return

    ##############################################
    ## pathing favicon                          ##
    ##############################################
    destination = os.path.join(cwd, "views")
    toReplace = [("""</title>""",'''</title>\n<link rel="icon" type="image/x-icon" href="/favicon.ico">''')]
    for tpl in glob.glob(destination+"*/*.tpl"):
        replace_in_file(toReplace, tpl)

def configuring(Tree = 1, Cards = 1, Quiz = 1):
    cwd = os.getcwd()
    print("Configuring.")
    if Cards == 1:
        destination = os.path.join(cwd, "flashcards", "config.py")

        toReplace = [('''databaseFile''',f'''databaseFile = "{contentFolder}/flashcards/flashcards.db"#''')]
        replace_in_file(toReplace, destination)
        
    if Quiz == 1:
        destination = os.path.join(cwd, "simpleQuizEngine", "config_files", "config.ini")
        toReplace = [('''examFolder''',f'''examFolder={contentFolder}/exams/\n;''')]
        replace_in_file(toReplace, destination)
    
    if Tree == 1:
        destination = os.path.join(cwd, "folderTreeView", "config_patched.ini")
        toReplace = [('''serverRoot''',f'''serverRoot={contentFolder}/files/\n;'''),
                     ('''updateInterval = -1''','''updateInterval = 0''')]
        replace_in_file(toReplace, destination)

        destination = os.path.join(cwd, "folderTreeView", "file_orginiser_patched.py")
        toReplace = [('''mediaRootFolder = ""''',f'''mediaRootFolder="{contentFolder}/files/"  #''')]
        replace_in_file(toReplace, destination)

def finishingUP(FLAG = "DONE_PATCHING"):
    cwd = os.getcwd()
    ####################################################
    ## Create the flag to skip patching on next start ##
    ####################################################
    with open(FLAG, 'w') as file: 
        file.write("")

def removeFlag(FLAG = "DONE_PATCHING"):
    os.remove(FLAG)

def installModul(mod_name, basedir = '.\\', extractPath = ""):
    # loading the temp.zip and creating a zip object
    with ZipFile(os.path.join(basedir, "_zips", mod_name + "-main.zip"), 'r') as zObject: 
        # Extracting all the members of the zip  
        # into a specific location. 
        zObject.extractall(os.path.join(basedir, extractPath)) 

    os.rename(os.path.join(basedir, extractPath, mod_name + "-main"),
                os.path.join(basedir, extractPath, mod_name))

def cleanUp(mod_name, basedir = '.\\', extractPath = ""):
    shutil.rmtree(os.path.join(basedir, extractPath, mod_name + "-main"), ignore_errors=True)


class wrongSelectionError(Exception):
    def __init__(self):
        self.message = "Wrong selection"
        super().__init__(self.message)
        
    def __str__(self):
        return f"{self.message}"

def select_moduls():
    print("Select modules:")
    print("[f]lashcards")
    print("f[o]lderTreeView")
    print("[s]impleQuizEngine")
    print("[a]ll")
    answers = ['No', 'Yes']
    while True:
        print("Enter selection as single line")
        print("i.e 'fo' for 'flashcards + folderTreeView'")
        print("or 'so' for 'simpleQuizEngine + folderTreeView'")
        print("")
        inStr = input("Your input: ")
        try:
            if 'f' in inStr or 'F' in inStr:
                Cards = 1
                inStr = inStr.replace('f', '')
                inStr = inStr.replace('F', '')
            else:
                Cards = 0
            if 'o' in inStr or 'O' in inStr:
                Tree = 1
                inStr = inStr.replace('o', '')
                inStr = inStr.replace('O', '')
            else:
                Tree = 0
            if 's' in inStr or 'S' in inStr:
                Quiz = 1
                inStr = inStr.replace('s', '')
                inStr = inStr.replace('S', '')
            else:
                Quiz = 0 
            if 'a' in inStr or 'A' in inStr:
                if len(inStr) != 1:
                    raise wrongSelectionError()
                Quiz = 1
                Tree = 1
                Cards = 1
                inStr = inStr.replace('a', '')
                inStr = inStr.replace('A', '')
            if len(inStr) == 0:
                print("")
                print("Your selection:")
                print("Modul            | Status")
                print("=========================")
                print("flashcards       | " + answers[Cards])
                print("folderTreeView   | " + answers[Tree])
                print("simpleQuizEngine | " + answers[Quiz])
                while True:
                    print("")
                    ans=input("Are you happy with the selection? y/n  ")
                    if ans == "y" or ans == "Y":
                        return (Tree, Cards, Quiz)
                    elif ans == "n" or ans == "N":
                        break
            else:
                raise wrongSelectionError()
        except wrongSelectionError as e:
            print("")
            print("/!\ /!\ /!\\")
            print(e)
            print("")
            
            
def install_moduls(Tree = 1, Cards = 1, Quiz = 1):
    modul_list = []
    if Cards == 1:
        modul_list.append("flashcards")
    if Quiz == 1:
        modul_list.append("simpleQuizEngine")
    if Tree == 1:
        modul_list.append("folderTreeView")
        
    for m in modul_list:
        if not os.path.exists(m):
            print("installing " + m)
            installModul(m)
        else:
            print("cleaning up " + m)
            cleanUp(m)
            print("installing " + m)
            installModul(m)

def uninstall_moduls(Tree = 1, Cards = 1, Quiz = 1):
    modul_list = []
    if Cards == 1:
        modul_list.append("flashcards")
    if Quiz == 1:
        modul_list.append("simpleQuizEngine")
    if Tree == 1:
        modul_list.append("folderTreeView")

    cwd = os.getcwd()
    for m in modul_list:
        destination = os.path.join(cwd, m)
        shutil.rmtree(destination, ignore_errors=True)
        destination = os.path.join(cwd, "views", m)
        shutil.rmtree(destination, ignore_errors=True)

if __name__ == '__main__':

    choise = -1
    while choise < 0 and choise < 5:
        print("Select option:")
        print("[1] Clean install/reinstall")
        print("[2] Reconfigure")
        print("[3] Uninstall")
        if os.path.isfile("DONE_PATCHING"):
            print("[4] Re-install/upgrade module")
        choise = input()
        try:
            choise = int(choise)
            if not os.path.isfile("DONE_PATCHING"):
                if choise == 4:
                    choise = -1
            
        except:
            print("Wrong selection!")
            choise = -1
    print("")
    if choise == 1:
        install_moduls()
        patching()
        migrating()
        configuring()
        finishingUP()
    elif choise == 2:
        configuring()
    elif choise == 3:
        uninstall_moduls()
        removeFlag()
        exit()
    elif choise == 4:
        Tree, Cards, Quiz = select_moduls()
        print(Tree, Cards, Quiz)
        print("")
        print("Deleting old instalation")
        uninstall_moduls(Tree, Cards, Quiz)
        removeFlag()
        install_moduls(Tree, Cards, Quiz)
        patching(Tree, Cards, Quiz)
        migrating(Tree, Cards, Quiz)
        configuring(Tree, Cards, Quiz)
        finishingUP()
        
    print("Done now you can start with mainScript.py")
    input()
