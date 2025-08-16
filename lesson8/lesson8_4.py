import gradio as gr

with gr.Blocks() as demo:
    gr.Markdown("""
    #歡迎使用 Gradio
    請輸入文字,會即時顯示輸入的內容。    
    """)
    input_textbox = gr.Textbox(placeholder="請輸入文字", label="輸入框")
    output_textbox = gr.Textbox(label="輸出框", placeholder="輸入的內容會顯示在這裡")

    @input_textbox.change(
        inputs=[input_textbox],
        outputs=[output_textbox]
    )
    def update_output(text):
        return text



demo.launch()


#gr.Markdown的 #是大標題的意思
#.change上方輸入框，下方即時出現同樣的內容