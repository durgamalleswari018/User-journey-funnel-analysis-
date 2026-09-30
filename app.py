from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>User Journey Funnel Analysis</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 900px;
                margin: 50px auto;
                padding: 20px;
            }
            h1 {
                color: #1f4e79;
            }
            .card {
                padding: 20px;
                border: 1px solid #ddd;
                border-radius: 10px;
                margin-top: 20px;
            }
        </style>
    </head>
    <body>
        <h1>User Journey Funnel Analysis</h1>

        <div class="card">
            <h2>Project Overview</h2>
            <p>
                This project analyzes user journey and funnel performance
                to understand how users move through different stages.
            </p>
        </div>

        <div class="card">
            <h2>Analysis</h2>
            <p>
                The original Python analysis is available in the
                project notebook on GitHub.
            </p>
        </div>

        <div class="card">
            <h2>Source Code</h2>
            <a href="https://github.com/durgamalleswari018/User-journey-funnel-analysis-">
                View GitHub Repository
            </a>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
