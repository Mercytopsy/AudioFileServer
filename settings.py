from dotenv import load_dotenv
load_dotenv()
import os

DB=os.getenv("DB")
DATABASE_USERNAME =os.getenv("DATABASE_USERNAME")
DATABASE_PASSWORD =os.getenv("DATABASE_PASSWORD")