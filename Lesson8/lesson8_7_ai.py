import gradio as gr
from google import genai
from google.genai import types

client = genai.Client()

with gr.Blocks() as demo:
    gr.Markdown("## Text to Summarization(總結)")
    #建立radio選項，radio是多選一。
    style_radio = gr.Radio(choices=['學術','商業','專業','口語化','條列式'], label="風格")
    input_text = gr.Textbox(
        label="請輸入文章",
        lines=10,
        submit_btn=True
    )
    #output_md = gr.Markdown()
    #建立輸出框
    output_text = gr.Textbox(
        label="機器人回覆",
        placeholder="機器人會在這裡回覆您的問題",
        interactive=False)

    @input_text.submit(inputs=[style_radio, input_text], outputs=[output_text])
    def summarize(style, text):
        # 在這裡處理摘要邏輯
        if style == "口語化":
            style = "口語化的風格\n"
        elif style == "學術":
            style = "學術的風格\n"
        elif style == "商業":
            style = "商業的風格\n"
        elif style == "專業":
            style = "專業的風格\n"
        elif style == "條列式":
            style = "條列式重點\n"

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            config= types.GenerateContentConfig(
                system_instruction=f"""
                你是一個專業的文章總結師，請根據以下風格對文章進行總結，並使用繁體中文回答。
                你需要根據用戶選擇的風格進行總結，並且確保總結的內容清晰、簡潔且易於理解。
                目前使用者選擇的風格是：{style}。

                所有的回覆必需是Markdown的語法
                """
            ),
            contents=[text]
        )
        
        summary = f"風格: {style}\n\n文章摘要:\n{response.text}"
        return summary

demo.launch()