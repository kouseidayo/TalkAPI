import vertexai
from vertexai.language_models import TextGenerationModel
import json

def is_json(data):
    try:
        json.loads(data)
        return True
    except ValueError:
        return False

def interview(
    temperature: float,
    project_id: str,
    location: str,
    max_output_tokens: float,
    top_k: float,
    top_p: float,
    model_name: str,
    prompt
) -> str:
    """Ideation example with a Large Language Model"""

    vertexai.init(project=project_id, location=location)
    # TODO developer - override these parameters as needed:
    parameters = {
        "temperature": temperature,  # Temperature controls the degree of randomness in token selection.
        "max_output_tokens": max_output_tokens,  # Token limit determines the maximum amount of text output.
        "top_p": top_p,  # Tokens are selected from most probable to least until the sum of their probabilities equals the top_p value.
        "top_k": top_k,  # A top_k of 1 means the selected token is the most probable among all tokens.
    }

    model = TextGenerationModel.from_pretrained(model_name)
    response = model.predict(
        prompt,
        **parameters,
    )
    
    # 文字列がJSON形式かどうかの判断
    if is_json(response.text):
        return response.text
    else:
        return json.loads(response.text.replace("'", "\""))


if __name__ == '__main__':
    print(
        interview(
        temperature=0.2,
        project_id='formal-province-366012',
        location='asia-northeast1',
        max_output_tokens=256,
        top_k=40,
        top_p=0.8,
        model_name="text-bison@001",
        prompt='あなたの名前は？'
        )
    )