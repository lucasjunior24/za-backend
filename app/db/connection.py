from mongoengine import *
from app.util.config import DB_URL


connect(host=DB_URL)