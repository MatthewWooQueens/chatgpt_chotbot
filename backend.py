from openai import OpenAI

class Chatbot:
    def __init__(self):
        self.client = OpenAI(api_key = "<api-key>")
    
    def get_response(self, user_input):
        response = self.client.chat.completions.create(model="gpt-3.5-turbo",
                                            messages=[{"role":"user","content":user_input}],
                                            max_tokens=3000,
                                            temperature=0.5).choices[0].message.content
        return response
        
