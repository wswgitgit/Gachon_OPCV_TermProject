import os
import sys
from config import AUDIO_PATH
from stt_module import run_stt
from timeline_module import build_timeline, calc_timeline_scores
from plot_module import plot_timeline_scores

def main():
    if not os.path.exists(AUDIO_PATH):
        print(f"오디오 파일을 찾을 수 없습니다: {AUDIO_PATH}")
        print("config.py의 AUDIO_PATH 경로를 확인하거나 파일을 해당 위치에 넣어주세요.")
        return
    try:
        segments = run_stt(AUDIO_PATH)
    except Exception as e:
        print(f" STT 변환 중 문제가 발생했습니다: {e}")
        return
    timeline = build_timeline(segments)
    second_scores = calc_timeline_scores(timeline)

    # 아래의 코드는 STT 결과를 분석하기 위한 코드입니다. STT 욕설이 추출이 안되는 경우에 사용하면 좋을 것 같습니다. 
    print("\n--- STT 결과 확인 ---")
    for seg in segments:
        print(f"[{seg['start']:.1f}s] {seg['text']}")
    
if __name__ == "__main__":
    main()
