import os

API_ID    = os.environ.get("API_ID", "20937734")
API_HASH  = os.environ.get("API_HASH", "eeb2040e50b0532a3fd97f386cd6d131")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8370955321:AAFUjQAT_45i5PWecLMHPQH-e2gUenXogbQ") 
WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
