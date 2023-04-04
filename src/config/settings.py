import os
from dotenv import load_dotenv
load_dotenv()

baseurl = 'https://moodle.cse.buet.ac.bd/'
id = os.environ.get('moodle_id')
pwd = os.environ.get('moodle_pwd')
local_output_dir = os.environ.get('local_output_dir')