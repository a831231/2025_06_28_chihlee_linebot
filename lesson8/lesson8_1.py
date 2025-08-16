import gradio as gr

def greet(name, intensity):
    #return "Hello, " + name + "!" * int(intensity)
    return name + "您好" + "!" * int(intensity)

demo = gr.Interface(
    fn=greet,
    inputs=["text", "slider"],
    outputs=["text"],
)

demo.launch()
