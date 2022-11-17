from http import client
from pymongo import MongoClient
from app.core.settings import settings
import cloudinary

cloudinary.config( 
  cloud_name = "daw9jmdyj", 
  api_key = "517953978165256", 
  api_secret = "5v_903FmwZSVpFf95dx1NlkGeGE" 
)

client = MongoClient(settings.MONGO_URI)

db   = client.muebleria_saldana