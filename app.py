from flask import Flask, render_template, request
from scanner import scan_target

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    report = None
    error = None
    
    if request.method == 'POST':
        target_url = request.form.get('url')
        if target_url:
            try:
                report = scan_target(target_url)
            except Exception as e:
                error = f"Error: {str(e)}"
        else:
            error = "Please enter a valid URL."

    return render_template('index.html', report=report, error=error)

if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port=5000, debug=True)
