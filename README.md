# Large-Document-Translator
This translator can be used to translate .txt files to your desired language storing it in another .txt file.

For files that are less than 50 pages such as reports this code can be run on your local machine.

Because of the time taken to complete the process it is recommended to use a hosted virtual machine for any book length documents.

### Wishlist
- ☐ Expanded functionality to include PDF 
- ☐ Making the processing more efficient
- ☐ More wishlist items needed 

## Installation Guide
Install the OpenAI package for interacting with the API and dotenv to load environment variables:
```
pip install openai
pip install python-dotenv
```

Modify the environment variables to fit your use case. Rename the ".env.example" file to ".env". Then change the variables to fit your use case:
```
MY_API_KEY=<Your API Key>
INPUT_FILE_PATH=<Your Input File Path>
OUTPUT_FILE_PATH=<Your Output File Path>
INPUT_LANGUAGE=<Your Input Language>
OUTPUT_LANGUAGE=<Your Output Language>
```

## Running on a Hosted Virtual Machine
To keep the code running on a virtual machine it is recommended to use nohup allowing you to disconnect and reconnect when it is convenient:
```
nohup python main.py &
```