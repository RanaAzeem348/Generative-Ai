# from openai import OpenAI

# client = OpenAI(api_key="")

# user_input = input("Ask something: ")

# response = client.responses.create(
#     model="gpt-5",
#     input=user_input
# )

# print(response.output_text)
# Simple Mock AI Chatbot





# User se input lena
user_prompt = input("Ask something: ")

#  response generate karna

response = f"You asked: {user_prompt}"

# Response display karna
print("\nAI Response:")
print(response)