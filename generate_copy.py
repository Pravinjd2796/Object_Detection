import openai
# from transformers import pipeline


# openai.api_key = 'sk-proj-I9vW6pHBBUgAToK52BOAT3BlbkFJsyKBDVRzo1tAcruCckHg'
# # Load the GPT model
# generator = pipeline('text-generation', model='gpt-3.5-turbo')

# def generate_copywriting(results):
#     text_prompt = "Create a social media post based on these detections: "
#     for result in results:
#         text_prompt += f"{result['class']} at frame {result['frame']}, "
    
#     generated_text = generator(text_prompt, max_length=100)
#     return generated_text[0]['generated_text']


# import openai

# Set your API key
# openai.api_key = 'sk-proj-I9vW6pHBBUgAToK52BOAT3BlbkFJsyKBDVRzo1tAcruCckHg'

# def generate_copywriting(results):
#     text_prompt = "Create a social media post based on these detections: "
#     for result in results:
#         text_prompt += f"{result['class']} at frame {result['frame']}, "
    
#     # Call OpenAI's API for text generation
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": text_prompt}
#         ]
#     )
#     return response.choices[0].message['content'].strip()


import openai

# Set your OpenAI API key
openai.api_key = 'sk-proj-I9vW6pHBBUgAToK52BOAT3BlbkFJsyKBDVRzo1tAcruCckHg'

def generate_copywriting(results):
    text_prompt = "Create a social media post based on these detections: "
    for result in results:
        text_prompt += f"{result['class']} at frame {result['frame']}, "
    
    # Call OpenAI's API for text generation
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a creative copywriter for social media posts."},
                {"role": "user", "content": text_prompt}
            ]
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        print(f"Error generating copywriting: {e}")
        return "Error generating copywriting."
