from google import genai
import os
# from IPython.display import display, Markdown, Latex
import markdown

client = genai.Client(api_key=os.environ['GEMINI_API_KEY'])

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="AI是如何工作的(請使用繁體中文回答)?"
)

generated_text = markdown.markdown(response.text)
print(response.text)
#display(Markdown(generated_text))