import instructor
from openai import OpenAI
from app.models import VibeResponse

# Initialize the client to point to your local Ollama 'server'
# Even though it's local, we use the OpenAI-style format because it's industry standard.
client = instructor.patch(
    OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
)

def get_vibe_analysis(customer_comment: str, draft_reply: str, brand_voice: str, model_name: str = "llama3.2:1b"):
    """
    This function sends the data to Llama 3.2 and returns a structured VibeResponse.
    """
    prompt = f"""
    Brand Voice Requirement: {brand_voice}
    ---
    Customer Comment: "{customer_comment}"
    Our Current Draft: "{draft_reply}"
    ---
    Task: Critically analyze the draft's vibe and provide three distinct rewrites in the required Brand Voice.
    """

    return client.chat.completions.create(
        model=model_name,
        response_model=VibeResponse, # This is the magic part!
        messages=[{"role": "user", "content": prompt}]
    )