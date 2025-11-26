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
    minute_scores = calc_timeline_scores(timeline)
    
    print("\n--- 시간대별 비속어 점수 집계 ---")
    for minute, score in minute_scores.items():
        print(f"{minute}분 대: {score}점")
    
    plot_timeline_scores(minute_scores)

if __name__ == "__main__":
    main()
