from dotenv import load_dotenv
import os

load_dotenv('.env')

TOKEN: str = os.getenv('TOKEN')
ADMIN_ID = 1049516806
questions_count = {}