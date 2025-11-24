#음성 파일을 텍스트로 변환
import whisper

def run_stt(audio_path: str):
    #load_model 메소드의 파라미터는 변환 모델의 종류를 의미
    #다른 모델도 존재하지만 아직 시험하지 않았음.
    model = whisper.load_model("base")  
    result = model.transcribe(audio_path)
    #반환 값의 key 부분인 "segments"은 건드리시면 안됩니다.
    return result["segments"]
