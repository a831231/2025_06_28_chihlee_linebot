import gradio as gr



with gr.Blocks() as demo:
    name_textbox = gr.Textbox(label="姓名",placeholder="請輸入姓名")
    output_textbox = gr.Textbox(label="輸出",placeholder="輸出結果會顯示在這裡")
    greet_button = gr.Button("打招呼")
    @greet_button.click( 
        inputs=[name_textbox], 
        outputs=[output_textbox]
    )
    def greet(name):
        return name + "您好~"   

demo.launch()