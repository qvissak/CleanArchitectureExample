from flask import Flask
from os.path import join, dirname
from dotenv import load_dotenv

# define application
app = Flask(__name__)

@app.route('/')
def index():
	return 'Yo, it\'s working! Yay!'

if __name__ == "__main__":
	# load environment variables
	DOT_ENV_PATH = join(dirname(__file__), '.env')
	load_dotenv(DOT_ENV_PATH)
	
	# launch application
	app.run()