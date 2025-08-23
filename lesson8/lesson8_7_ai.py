import gradio as gr
from google import genai
from google.genai import types

client = genai.Client()

with gr.Blocks() as demo:
    gr.Markdown("## Text to Summarization(總結)")
    style_radio = gr.Radio(choices=['小學','商業','專業','口語化','條列式'], label="風格",value="口語化")
    input_text = gr.Textbox(
        label="請輸入文章",
        lines=10,
        submit_btn=True
    )
    output_md = gr.Markdown()

    @input_text.submit(inputs=[style_radio, input_text], outputs=[output_md])
    def summarize(style, text):
        if style=="口語化":
            style = "請使用口語化的風格\n"
        elif style == "小學":
            style = "請使用小學生看的懂的語法\n"
        elif style == "商業":
            style = "請使用商業文章的風格\n"
        elif style == "條列式":
            style = "請條列式重點\n"
        elif style == "專業":
            style = "請使用專業的風格\n"
        
        response = client.models.generate_content_stream(
            model="gemini-2.5-flash",
            config= types.GenerateContentConfig(
                system_instruction=f"""
                你是一個專業的總結助手，也是一個繁體中文的高手,請根據用戶提供的文章內容進行總結。
                你需要根據用戶選擇的風格進行總結，並且確保總結的內容清晰、簡潔且易於理解。
                目前使用者選擇的是{style}。

                所有的回覆必需是markdown的語法
                """
            ),
            contents = [text]
        )
        
        summary = f"風格: {style}\n\n"
        for chunk in response:
            if chunk.text:
                summary += chunk.text
                yield summary

demo.launch()