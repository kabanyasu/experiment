import os 
import re
from collections import defaultdict
import xml.etree.ElementTree as ET
from xbrl import XbrlParser, GAAP, GAAPSerializer
import pandas as import pd
import requests

class XbrlParser():
    def __init__(self, xbrl_filename):
        self.xbrl_filename = xbrl_filename
        self.base_filename = xbrl_filename.replace('.xbrl','')
        self.dei = ""
        self.facts = None
        
