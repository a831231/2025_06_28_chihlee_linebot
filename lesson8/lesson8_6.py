import gradio as gr

#建立一個gradio的Block的架構
with gr.Blocks() as demo:
    gr.Markdown("## 公司內部機器人")
    #建立輸入框
    input_text = gr.Textbox(label="請輸入訊息", placeholder="請輸入問題", submit_btn=True)
    
    #建立gradio.Accordion
    with gr.Accordion("可以點選以下常用問題", open=True):
        gr.Examples(
            examples=[
                "你們的公司在哪裡？",
                "你們的產品有哪些？",
                "你們的服務時間是什麼時候？"
            ],
            inputs=input_text
        )
    
    #建立輸出框
    output_text = gr.Textbox(label="機器人回覆", 
                             placeholder="這裡會顯示機器人的回覆", 
                             interactive=False)

    @input_text.submit(inputs=[input_text],outputs=[output_text])
    def respond(message):
        # 模擬機器人回覆
        return "這是機器人的回覆"

demo.launch()