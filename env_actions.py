from dotenv import load_dotenv
import os


#~>


#<·
load_dotenv()

def main() -> None:
    if not os.environ.get('test'):
        ... # eliminar _databases/*
