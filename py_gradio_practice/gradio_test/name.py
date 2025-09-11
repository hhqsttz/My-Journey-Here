import time

from fastapi import FastAPI
import gradio as gr


def Hello (name:str):
    l=""
    res = f"Hello {name}"
    for i in res:
        l+=i
        time.sleep(0.2)
        yield l


instance = gr.Interface(
    fn= Hello,
    inputs= "text",
    outputs="text",
    title="问候",
    description="这是一个流式输出的问候的组件"
)

instance.launch()