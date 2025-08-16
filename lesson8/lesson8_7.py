import gradio as gr

with gr.Blocks() as demo:
    gr.Markdown("## Text to Summarization(總結)")
    style_radio = gr.Radio(choices=['學術', '商業','口語化','條列式'], label="風格")
    input_text = gr.Textbox(
        label="請輸入文章",
        lines=10,
        submit_btn=True
    )
    output_md = gr.Markdown()

    @input_text.submit(inputs=[style_radio, input_text], outputs=[output_md])
    def summarize(style, text):
        if style == "口語化":
            style = "請使用口語化的風格\n"
        if style == "學術":
            style = "請使用專業學術的風格\n"
        if style == "商業":
            style = "請使用商業文章的風格\n"
        if style == "條列式":
            style = "請條列式重點\n"       

        summary = f"風格: {style}\n\n{text}"
        return summary
    

demo.launch()