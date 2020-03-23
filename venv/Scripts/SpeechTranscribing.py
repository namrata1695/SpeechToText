import speech_recognition as speech_recog

class SpeechTranscribing:
    sample_audio = speech_recog.AudioFile('C:/Users/Namrata/PycharmProjects/untitled/OSR_us_000_0018_8k.wav');
    recog = speech_recog.Recognizer()
    with sample_audio as audio_file:
        audio_content = recog.record(audio_file)

    print('Transcribing : ')
    print(recog.recognize_google(audio_content));