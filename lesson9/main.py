from flask import Flask,render_template_string

app = Flask(__name__)

@app.route("/")
def index():
    html = '''
    <!DOCTYPE html>
    <html lang="zh-TW">
    <head>
        <meta charset="UTF-8">
        <title>Gemini 小助手 Chatbot</title>
        <style>
            body { font-family: Arial, sans-serif; background: #f5f5f5; }
            .container { max-width: 900px; margin: 40px auto; background: #fff; padding: 40px; border-radius: 10px; box-shadow: 0 2px 8px #ccc; }
            h1 { text-align: center; }
            #result { min-height: 120px; background: #f0f0f0; margin-top: 20px; padding: 18px; border-radius: 5px; }
            .btn { padding: 12px 28px; margin: 6px; border: none; border-radius: 5px; cursor: pointer; font-size: 18px; }
            .btn-start { background: #4CAF50; color: #fff; }
            .btn-clear { background: #f44336; color: #fff; }
            #question { width: 100%; padding: 12px; border-radius: 5px; border: 1px solid #ccc; font-size: 16px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Gemini 小助手 Chatbot</h1>
            <input type="text" id="question" placeholder="請輸入您的問題..." />
            <div>
                <button class="btn btn-start" onclick="startChat()">開始</button>
                <button class="btn btn-clear" onclick="clearAll()">清除</button>
            </div>
            <div id="result"></div>
        </div>
        <script>
            function startChat() {
                const q = document.getElementById('question').value.trim();
                if (!q) { alert('請輸入問題'); return; }
                document.getElementById('result').innerHTML = '請稍候...';
                fetch('/chat', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ question: q })
                })
                .then(res => res.json())
                .then(data => {
                    document.getElementById('result').innerHTML = data.html || data.text || '無回應';
                })
                .catch(() => {
                    document.getElementById('result').innerHTML = '發生錯誤，請稍後再試';
                });
            }
            function clearAll() {
                document.getElementById('question').value = '';
                document.getElementById('result').innerHTML = '';
            }
        </script>
    </body>
    </html>
    '''
    return render_template_string(html)