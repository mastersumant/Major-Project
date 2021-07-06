# Intelligent document summarizer
Intelligent document summarizer in Python

## Documentation
Find the extensive documentation in the python notebook provided by the name [summarizer.ipynb](summarizer.ipynb) in the project.

## Running the code
### Libraries

Please make sure that you have the following libraries installed in your system-
  
        numpy

        matplotlib

        networkx

        nltk

        sklearn

        PyPDF2
        
        Django

If you have anaconda then you only need to worry about nltk, PyPDF2 and Django. Otherwise you may need to install other libraries. It is super easy to install them.
Once you have installed every library mentioned above, you are ready to go.

### Download the project and extract the zip into a folder of your choice
Clone/Download this project and extract it into your desired folder.

### Run the code
Run manage.py on Anaconda
By Typing : python manage.py runserver
by default django will take IP address as "127.0.0.1" and Port as "8000"

When asked for file input, please provide the name of any file already in the directory whose summary you want to create.

I have included 5 sample files: Artificial Intelligence.txt,data structure.txt,story1.txt, story2.txt, story3.pdf for analyizing the summarizer.

After Creating django server you need to open Any browser of your choice like chrome,firefox,etc and follow the below steps to get the summary:
1. Enter url: http://127.0.0.1:8000/summary/ in browser.
2. Give title of the story.
3. Choose file from your system to the Django interface.
4. Select type of summary "Short Term" or "Long Term". 
5. If any information enter was wrong the press reset button.
6. If No, then press submit button.
7. To Play the story press 🔊 icon on the screen.
8. To pause the story press 🔇 icon on the screen.
9. To resume the stroy from the same point press 🔉 icon on the screen.
10. In the bottom you can check number of words before and after the summarizer.
