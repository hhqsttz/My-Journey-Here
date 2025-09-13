import time



import gradio as gr


def do_it (name:str):
    res=""

    for a in name:

        res+=a
        time.sleep(0.1)
        yield res


instance = gr.Interface(
    fn= do_it,
    inputs= gr.Textbox(label="请输入"),
    outputs=gr.Textbox(label="输出结果"),
    title="进度条"

)

instance.launch()