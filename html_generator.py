from datetime import datetime

def generate_html():
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    html_content = f"""
    <html>
    <head>
        <title>DevOps Page</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #0f172a;
                color: #e2e8f0;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
                text-align: center;
            }}
            h1 {{
                font-size: 3em;
                margin-bottom: 0.3em;
            }}
            h2 {{
                font-weight: normal;
                color: #94a3b8;
                margin-top: 0;
                margin-bottom: 1.5em;
            }}
            img {{
                max-width: 90%;
                height: auto;
                border-radius: 12px;
                box-shadow: 0 4px 20px rgba(0,0,0,0.4);
            }}
        </style>
    </head>
    <body>
        <h1>Hello DevOps</h1>
        <h2>{timestamp}</h2>
        <h2>Sorry for the delay :)</h2>
        <img src="https://i.gifer.com/OAJr.gif" alt="Funny gif" />
    </body>
    </html>
    """
    with open("index.html", "w") as f:
        f.write(html_content)
