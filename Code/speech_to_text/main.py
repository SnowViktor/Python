import speech_recognition as sr
from pydub import AudioSegment

audio = AudioSegment.from_file("original.m4a", format="m4a")
audio.export("converted.wav", format="wav")

recognizer = sr.Recognizer()
with sr.AudioFile("converted.wav") as source:
    print("\n正在處理音檔，請稍候……")
    audio_data = recognizer.record(source)
    try:
        transcript = recognizer.recognize_google(audio_data, language="zh-TW")
        with open("transcript.txt", "w", encoding="utf-8") as f:
            f.write(transcript)
        print("轉錄結果已儲存至「transcript.txt」。")
    except sr.UnknownValueError:
        print("無法辨識語音內容。")
    except sr.RequestError:
        print("無法連接語音辨識服務。")
