# contentDeliver
The merges 3 of my projects in one system: flashcards folderTreeView simpleQuizEngine

It makes necesery chnages to merge the 3 applications in one. There is no need to configure any of the other applications. Just this one.
All is written in python 3 and It needs the [bottle framework](https://github.com/bottlepy/bottle). You can just put the file bootle.py in the root folder with all other python scripts or run ``pip install --requirement  requirements.txt``.

If you want multi threaded server you can install paste by runing ``pip install paste``

The configuraion is simple: port ip where to listen folder where to store the files and data bases

***config_files\config.ini***

To configure edit the file config_files\config.ini
- port - changes the server port
- ip - the ip address where to listen
- contentFolder - the folder where to save: the exam files/flashcards database/other files accesible via folderTreeView
- newTab - if the links to the apps will be opened in new page (the home page)
- showUsers = show the logged users used with ``showUsersComand``
- showUsersComand = Command line returning the logged users. You can add or modify the comands as you wish. The script will run the command and return the output
  - windows - query user
  - linux - who -l -H


How to install: 
1. Downaload the sources as zips from here and my 3 other projects here in git hub: [flashcards](https://github.com/cemkata/flashcards/), [folderTreeView](https://github.com/cemkata/folderTreeView/), [simpleQuizEngine](https://github.com/cemkata/simpleQuizEngine/)
2. Put the downloaded zip in the folder __zip: flashcards-main.zip folderTreeView-main.zip simpleQuizEngine-main.zip
3. Start patcher.py and select option

When done start the mainScript.py

For windows service you can use nssm.
For linux/macOS check in google.
