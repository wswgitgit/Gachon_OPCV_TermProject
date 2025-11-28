# 설정값: 시간 단위와 비속어 점수 사전
TIME_SIZE = 60  # 1분 단위
PENALTY = {
    "개짜증나": 2,
    "XX": 3,
    "망했네": 1,
    "개노답": 2,
}

# 예시 입력 데이터 (start: 초 단위, text: 문장)
segments = [
    {"start": 12.3, "text": "이건 진짜 개짜증나"},
    {"start": 15.8, "text": "뭐야 이 XX"},
    {"start": 61.2, "text": "완전 망했네"},
    {"start": 62.5, "text": "개노답"},
    {"start": 125.0, "text": "헐... 이건 좀 심한데"},
]

# 타임라인 생성 함수
def build_timeline(segments, time_size=TIME_SIZE):
    timeline = {}
    for seg in segments:
        minute = int(seg["start"] // time_size)
        timeline.setdefault(minute, []).append(seg["text"])
    return timeline

# 문장별 비속어 점수 계산 함수
def calc_penalty_for_text(text, penalty_dict=PENALTY):
    return sum(text.count(word) * point for word, point in penalty_dict.items())

# 타임라인별 점수 집계 함수
def calc_timeline_scores(timeline, penalty_dict=PENALTY):
    scores = {}
    for minute, texts in timeline.items():
        total = sum(calc_penalty_for_text(t, penalty_dict) for t in texts)
        scores[minute] = total
    return scores

# 실행 흐름
def analyze_hot_minutes(segments, time_size=TIME_SIZE, penalty_dict=PENALTY, threshold=3):
    timeline = build_timeline(segments, time_size)
    scores = calc_timeline_scores(timeline, penalty_dict)

    print("\n 시간대별 비속어 점수:")
    for minute, score in sorted(scores.items()):
        print(f"{minute}분: 점수 = {score}")

    print("\n 과열된 시간대 (점수 ≥ {}):".format(threshold))
    for minute in sorted(scores):
        if scores[minute] >= threshold:
            print(f"- {minute}분대 (점수: {scores[minute]})")

# 실행
analyze_hot_minutes(segments)
# 설정값: 시간 단위와 비속어 점수 사전

