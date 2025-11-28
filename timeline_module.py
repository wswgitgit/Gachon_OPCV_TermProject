#음성 파일에서 텍스트로 전환하는 모듈입니다.
#25.11.24 기준 5분짜리 음성파일까지 테스트 후 정상 작동 됨을 확인했습니다.

from config import TIME_SIZE, PENALTY

#타임라인 생성 메소드
def build_timeline(segments, time_size: int = TIME_SIZE):
    timeline = {}
    for seg in segments:
        minute = int(seg["start"] // time_size)
        timeline.setdefault(minute, []).append(seg["text"])
    return timeline

#한 문장의 비속어(PENATY에 존재하는...) 검사 후 점수(정수) 반환
def calc_penalty_for_text(text: str, penalty_dict: dict = PENALTY) -> int:
    return sum(text.count(word) * point for word, point in penalty_dict.items())

#각 타임라인의 비속어 점수를 집계 후 결과 딕셔너리를 반환
def calc_timeline_scores(timeline: dict, penalty_dict: dict = PENALTY) -> dict:
    scores = {}
    for minute, texts in timeline.items():
        #하나의 타임라인의 문장을 순서대로 검사 후
        total = sum(calc_penalty_for_text(t, penalty_dict) for t in texts)
        #집계값을 딕셔너리 형태로 저
        scores[minute] = total
    return scores
