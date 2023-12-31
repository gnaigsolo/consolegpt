from openai import OpenAI

client = OpenAI()

def get_response(message, way_to_response):
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system",
       "content": way_to_response},
      {"role": "user", "content": message}
    ]
  )
  return completion.choices[0].message.content



if __name__ =='__main__' :
  role = input('Role that you want GPT to act: ')
  while True:
    my_message = input('You: ')
    response = get_response(my_message, role)
    print("GPT:",response)
