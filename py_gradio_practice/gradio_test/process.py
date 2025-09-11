import time


from fastapi import FastAPI
import gradio as gr


def do_it (name:str,progress = gr.Progress()):
    res=""
    progress(0,desc="开始。。。")
    for a in progress.tqdm(name,desc="运行中。。。"):
        time.sleep(2)
        res+=a

    return res


instance = gr.Interface(
    fn= do_it,
    inputs= gr.Textbox(label="请输入"),
    outputs=gr.Textbox(label="输出结果"),
    title="进度条"

)

instance.launch()