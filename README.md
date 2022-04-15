# automationHomework

mac:

1. brew.sh, install brew 
2. brew install @python3.7 and brew install --cask firefox
3. clone https://github.com/dangh597/automationHomework.git
4. cd automationHomework
5. sudo pip3 install -r Tests/requirements.txt
6. cp geckodriver-v.31.0-macos.tar/geckodriver /usr/bin
7. sudo chmod 755 /usr/bin/geckodriver
8. python3 -m unittest Tests/<testfile.py>

linux:

1. sudo yum install python3 / sudo apt-get install python3
2. sudo yum install git and sudo yum install firefox
3. git clone https://github.com/dangh597/automationHomework.git
4. cd automationHomework 
5. sudo pip3 install -r Tests/requirements.txt
6. cp geckodriver-v.31.0-linux64.tar/geckodriver /usr/bin 
7. sudo chmod 755 /usr/bin/geckodriver
8. python3 -m unittest Tests/<testfile.py>

windows:

1. Install python either from https://www.python.org/downloads/ or from windows store
2. Make sure to include python path in system variables
3. clone https://github.com/dangh597/automationHomework.git
4. Install firefox
5. cd automationHomework
6. pip3 install -r Tests/requirements.txt
7. python3 -m unittest Tests/<testfile.py>
