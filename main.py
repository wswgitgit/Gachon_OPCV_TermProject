from config import AUDIO_PATH
from stt_module import run_stt
from timeline_module import build_timeline, calc_timeline_scores
from plot_module import plot_timeline_scores

def main():
    segments = run_stt(AUDIO_PATH)
    timeline = build_timeline(segments)
    minute_scores = calc_timeline_scores(timeline)
    print(minute_scores)
    plot_timeline_scores(minute_scores)

if __name__ == "__main__":
    main()
