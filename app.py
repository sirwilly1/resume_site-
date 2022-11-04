import oyaml as yaml
from flask import Flask
from flask import render_template
from flask import send_file
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/')
def index():
    website_data = yaml.full_load(open('config.yaml'))

    return render_template('index.html', data=website_data)

@app.route('/download')
def download_file():
	path = "static/resume.PDF"
	return send_file(path, as_attachment=True)



if __name__ == '__main__':
    app.run(debug=True, port=5000)