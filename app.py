from flask import Flask, render_template
from natsort import natsorted
import glob

app = Flask(__name__)

@app.route('/')
def home():
    # Auto-grab templates
    tech_list = glob.glob('templates/tech/[!_]*.html')
    tech_list = list(map(lambda s : s.replace('templates/', '', 1), tech_list))
    tech_list = natsorted(tech_list)

    return render_template('index.html', tech_list=tech_list)