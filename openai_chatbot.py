import os
from openai import OpenAI

OPENAI_API_KEY = "OPENAI__KEY"
client = OpenAI(api_key=OPENAI_API_KEY)


file = client.files.create(
        file=open("xyz.pdf", "rb")
        purpose = 'assistants'
)

#creating the assistant

assistant = client.beta.assistants.create(
    name="Nature Expert",
    instructions = "You answer questions related to nature and tell the user facts"
    tools = [{"type": "retrieval"}],
    model = "gpt-3.5-turbo",
    file_ids = file.id 
)

#creating a thread
 #creating thread

thread = client.beta.threads.create()
## print(thread) 

# adding a message to a thread

message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role='user',
    content='what is nature'
)

#RUNNING THE ASSISTANT

run = client.beta.threads.runs.create(
    thread_id = thread.id,
    assistant_id = assistant.id
)

#displaying the assistant's response

run = client.beta.threads.runs.retrieve(
    thread_id = thread.id,
    run_id = run.id
)

messages = client.beta.threads.messages.list(
    thread_id = thread.id
)

#printing all the messages till now

for message in reversed(messages.data):
    print(message.role + ": " + message.content[0].text.value)


