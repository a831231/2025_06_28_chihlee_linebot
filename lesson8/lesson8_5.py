import gradio as gr

with gr.Blocks() as demo:
    a = gr.Number(label="數字A", value=0)
    b = gr.Number(label="數字B", value=0)   

    with gr.Row():
        add_button = gr.Button("加法")
        subtract_button = gr.Button("減法")
        multiply_button = gr.Button("乘法")
        divide_button = gr.Button("除法")
    
    c = gr.Number(label="結果", value=0)

    @add_button.click(inputs=[a, b],outputs=[c])
    def add_numbers(a, b):
        return a + b

    @subtract_button.click(inputs=[a, b],outputs=[c])
    def subtract_numbers(a, b):
        return a - b

    @multiply_button.click(inputs=[a, b],outputs=[c])
    def multiply_numbers(a, b):
        return a * b

    @divide_button.click(inputs=[a, b],outputs=[c]
                         )
    def divide_numbers(a, b):
        return a / b

demo.launch()

