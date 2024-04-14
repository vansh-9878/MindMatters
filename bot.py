import openai
import sys
openai.api_key="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"
def chat_with_bot(prompt):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{"role":"user","content":prompt}]
    )
    return response.choices[0].message.content.strip()
if __name__ == "__main__":
    while True:
        user_input = input("You:").lower()
        if user_input.lower() in ["quit","exit","leave","bye"]:
            sys.exit(0)
        
        response = chat_with_bot(user_input)
        print("Chatbot:",response)
