import gradio as gr
from google import genai    #引入Google GenAI庫

client = genai.Client() #已經在系統中建立API KEY，所以這裡不需要再設定API KEY。

#建立gradio Blocks架構
with gr.Blocks() as demo:
    gr.Markdown("## 公司內部機器人")
    #建立輸入框
    input_text = gr.Textbox(label="請輸入訊息", placeholder="請輸入問題", submit_btn=True)

    #建立gradio.Accordion
    with gr.Accordion("======懶的輸入可以點選以下問題======", open=False):
        gr.Examples(
            examples=[
                "請問台灣的首都是哪裡？",
                "請問台灣的國土面積有多大？",
                "請問台灣的人口有多少？",
            ],
            inputs=input_text
        )

    #建立輸出框
    output_text = gr.Textbox(
        label="機器人回覆",
        placeholder="機器人會在這裡回覆您的問題",
        interactive=False)
    
    @input_text.submit(inputs=[input_text],outputs=[output_text])
    def respond(message):
        # 在這裡處理用戶輸入的訊息
        response = client.models.generate_content(  # 使用Google GenAI模型生成內容
            model="gemini-2.5-flash",
            contents=[message]
        )
        #return "這是機器人的回覆"
        return response.text
    
demo.launch()