import gradio as gr

def greet(name, intensity): #定義一個功能greet，接受兩個參數name和intensity，相對應inputs就需要有2個輸入
    return name + "你好" + "!" * int(intensity) + " 你今天好吗？"

demo = gr.Interface(
    fn=greet,
    inputs=["text", "slider"],  #inputs指定輸入類型，第一個是文字輸入，第二個是滑桿輸入
    outputs=["text"],
)

demo.launch(share=True) #share=True允許在網路上分享這個介面給大家，會自動產生網址，期限7天。
