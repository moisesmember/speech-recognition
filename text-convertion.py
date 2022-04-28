#import library
#import speech_recognition as sr
#Initiаlize  reсоgnizer  сlаss  (fоr  reсоgnizing  the  sрeeсh)
#r = sr.Recognizer()
# Reading Audio file as source
#  listening  the  аudiо  file  аnd  stоre  in  аudiо_text  vаriаble
#with sr.AudioFile('I-dont-know.wav') as source:
#with sr.AudioFile('C:/dev/speech-recognition/exam.wav') as source:
#    audio_text = r.listen(source)
# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
#    try:
        # using google speech recognition
#        text = r.recognize_google(audio_text)
#        print('Converting audio transcripts into text ...')
#        print(text)
#    except:
#         print('Sorry.. run again...')

from pydub import AudioSegment # uses FFMPEG
import speech_recognition as sr
from pathlib import Path
#from pydub.silence import split_on_silence
#import io
#from pocketsphinx import AudioFile, Pocketsphinx

def process(filepath, chunksize=60000):
    #0: load mp3
    sound = AudioSegment.from_mp3(filepath)

    #1: split file into 60s chunks
    def divide_chunks(sound, chunksize):
        # looping till length l
        for i in range(0, len(sound), chunksize):
            yield sound[i:i + chunksize]
    chunks = list(divide_chunks(sound, chunksize))
    print(f"{len(chunks)} chunks of {chunksize/1000}s each")

    r = sr.Recognizer()
    #2: per chunk, save to wav, then read and run through recognize_google()
    string_index = {}
    for index,chunk in enumerate(chunks):
        # TODO io.BytesIO()
        chunk.export('C:/dev/speech-recognition/exam.wav', format='wav')
        with sr.AudioFile('C:/dev/speech-recognition/exam.wav') as source:
            audio = r.record(source)
        #s = r.recognize_google(audio, language="en-US") #, key=API_KEY) --- my key results in broken pipe
        s = r.recognize_google(audio, language="en-US")
        print(s)
        string_index[index] = s
        break
    return string_index

text = process('C:/dev/speech-recognition/exam.mp3')