import google.generativeai as genai

genai.configure(api_key="AIzaSyA55gd8_goVDUG89JfFW92hls4RPe0R1pg")

models = genai.list_models()
for model in models:
    print(f"Model: {model.name}")
    print(f"  Base Model: {model.base_model_id if hasattr(model, 'base_model_id') else 'N/A'}")
    print(f"  Description: {model.description if hasattr(model, 'description') else 'N/A'}")
    print("-" * 50)
