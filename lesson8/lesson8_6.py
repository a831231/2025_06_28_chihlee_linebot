import gradio as gr
from google import genai

client = genai.Client()

#建立一個gradio的Block的架構
with gr.Blocks() as demo:
    gr.Markdown("## 公司內部機器人")
    #建立輸入框
    input_text = gr.Textbox(label="請輸入訊息", placeholder="請輸入問題", submit_btn=True)
    
    #建立gradio.Accordion
    with gr.Accordion("可以點選以下常用問題", open=True):
        gr.Examples(
            examples=[
                "台灣首都在哪裡？",
                "台灣人口多少？",
                "台灣面積有多大？"
            ],
            inputs=input_text
        )
    
    #建立輸出框
    output_text = gr.Textbox(label="機器人回覆", 
                             placeholder="這裡會顯示機器人的回覆", 
                             interactive=False)

    @input_text.submit(inputs=[input_text],outputs=[output_text])
    def respond(message):
        # 在這裡處理用戶輸入的訊息
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[message]
        )
        return response.text

demo.launch()