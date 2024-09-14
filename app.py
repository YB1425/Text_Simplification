import gradio as gr
from transformers import pipeline

simplifier = pipeline("text2text-generation", model="t5-base")

def text_simplifying(text, max_len):
    simplified = simplifier(f"simplified: {text}", max_length=max_len, min_length=30, do_sample=False)
    return simplified[0]['generated_text']


interface = gr.Interface(
    fn=text_simplifying,
    inputs=[
        gr.Textbox(lines=5, placeholder="Enter complex text here..."),
        gr.Slider(minimum=30, maximum=200, value=100, label="Max Length")
    ],
    outputs="text",
    title="Text Simplification",
    description="Simplify complex text using Hugging Face's text-to-text pipeline."
)


interface.launch()
