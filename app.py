import gradio as gr
import openai

# Replace with your actual OpenAI API Key
openai.api_key = 'your-openai-api-key'

def chat_with_gpt(prompt):
    """Send a prompt to OpenAI GPT-4 and return the response."""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    reply = response['choices'][0]['message']['content']
    return reply

demo = gr.Interface(
    fn=chat_with_gpt,
    inputs=gr.Textbox(lines=2, placeholder="Enter your message here..."),
    outputs="text",
    title="AGI Voice Assistant",
    description="Chat with an AGI-like assistant powered by OpenAI GPT-4."
)

if __name__ == "__main__":
    demo.launch()
