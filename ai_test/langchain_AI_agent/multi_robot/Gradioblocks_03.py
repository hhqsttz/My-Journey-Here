

import gradio as gr

from langchain_core.messages import AIMessage, HumanMessage

from multi_robot.history_02 import final_chain1



def f1 (chat_history,user_message):
    if user_message:
        chat_history.append({"role": "user", "content": user_message})
    return chat_history,""
def f2 (chat_history):
    chat_history.append({"role": "assistant", "content": ""})

    # 遍历 stream() 生成器
    for token in final_chain1.stream(chat_history[-1]["content"]):
        chat_history[-1]["content"] += token  # 每个 token 更新 AI 消息
        yield chat_history




with gr.Blocks(title="多模态聊天机器人",theme=gr.themes.Soft(),fill_width=True,fill_height=True) as demo:
    chatbot = gr.Chatbot(type="messages",label="对话框",scale=8)
    with gr.Row():
        t = gr.Textbox(label="输入文本框",placeholder="请输入...",info="000",scale=8)
        s = gr.Button("发送",variant="primary") #variant按钮的风格

        s.click(
            fn=f1,
            inputs=[chatbot,t],
            outputs=[chatbot,t],
        ).then(fn=f2,
               inputs=[chatbot],
               outputs=[chatbot],
        )

        t.submit(
            fn=f1,
            inputs=[chatbot,t],
            outputs=[chatbot,t],
        ).then(fn=f2,
               inputs=[chatbot],
               outputs=[chatbot],
        )


    emp = []
    e = gr.Examples(
        examples=emp,
        inputs=t
    )

if __name__ == '__main__':

    demo.launch()
