"""
Service package initialization
"""
from flask import Flask
import service.routes  # This should be at the top with other imports

app = Flask(__name__)

# Rest of your initialization code
