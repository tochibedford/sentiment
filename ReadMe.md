# Sentiment analysis with HuggingFace's roberta model

## Tochi Bedford

With this script I've written you can pass in an arbitrary number of files to perform sentiment analysis on and it will print out the results on the terminal. This script can be repurposed for Branbox's task

- Clone this repo
- Change working directory into to be inside of your clone `cd path/to/cloned/repo`
- Setup a virtual environment and activate it:

```bat
C:\cloned\repo> python -m venv venv && venv\Scripts\activate.bat
```

- Install requirements: `pip install -r requirements.txt`
- Now you can run:

```bat
C:\cloned\repo> python main.py read.txt read2.txt read3.txt "C:\path\to\some\other\file.txt"
read.txt: [0.0016173  0.01060592 0.98777676]
read2.txt: [0.80997515 0.16189244 0.02813241]
read3.txt: [0.0016173  0.01060592 0.98777676]
C:\path\to\some\other\file.txt: [0.80997515 0.16189244 0.02813241]
```
