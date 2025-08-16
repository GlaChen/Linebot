## Block架構

import gradio as gr



with gr.Blocks() as demo: #Blocks就是一個區塊
    name_textbox = gr.Textbox(label="姓名",placeholder="請輸入姓名")
    output_textbox = gr.Textbox(label="輸出",placeholder="輸出結果會顯示在這裡")
    greet_button = gr.Button("打招呼") #建立一個按鈕

    @greet_button.click(
        inputs=[name_textbox],
        outputs=[output_textbox]
    ) #使用@裝飾器就不需要呼叫fn=greet，只要把greet函數定義在下面即可
    def greet(name):
        return name + "你好！"

demo.launch()