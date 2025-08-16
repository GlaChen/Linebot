##建立一個gradio的Blocks架構
##功能：
##1.建立姓名輸入框
##2.建立輸出框
##3.建立按鈕

import gradio as gr

def greet(name):
    return name + "你好！"

with gr.Blocks() as demo:  # Blocks就是一個區塊
    name_textbox = gr.Textbox(label="姓名", placeholder="請輸入姓名")
    output_textbox = gr.Textbox(label="輸出", placeholder="輸出結果會顯示在這裡")
    greet_button = gr.Button("打招呼")  # 建立一個按鈕

    greet_button.click(fn=greet,
                       inputs=[name_textbox],
                       outputs=[output_textbox])

demo.launch()  # 啟動Gradio介面