import io
import os
import codecs
import datetime

# Imports the Google Cloud client library
from google.cloud import speech

# Instantiates a client
client = speech.SpeechClient()

with open("sample-2.wav", "rb") as audio_file:
    content = audio_file.read()

audio = speech.RecognitionAudio(content=content)
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    language_code="en-US",
)

operation = client.long_running_recognize(config=config, audio=audio)

print('Waiting for operation to complete...')
operationResult = operation.result()

d = datetime.datetime.today()
today = d.strftime("%Y%m%d-%H%M%S")
fout = codecs.open('output{}.txt'.format(today), 'a')

for result in operationResult.results:
    for alternative in result.alternatives:
        fout.write(u'{}\n'.format(alternative.transcript))
fout.close()
