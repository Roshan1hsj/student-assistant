STUDENT ASSISTANT

•	This is a simple school project made with python.

INSTALLATIONS:

•	Download and Install Python3

•	It is recommended to use a virtual environment

•	Once virtual environment is set up, use pip to install the dependencies by running the command

pip install -r requirements.txt

(MAKE SURE TO INSTALL  REQUIREMENTS.TXT IN YOUR PYTHON PROJECT) 

THE YOUTUBE DOWNLOADER IS RAISING SOME ERRORS

in order to solve the problem, you should go in the cipher.py file and replace the line 30, which is:

var_regex = re.compile(r"^\w+\W")
With that line:

var_regex = re.compile(r"^\$*\w+\W")
After that, it worked again. OR VISIT https://stackoverflow.com/questions/70776558/pytube-exceptions-regexmatcherror-init-could-not-find-match-for-w-w
