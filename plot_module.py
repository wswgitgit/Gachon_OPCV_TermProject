import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
#만약 모듈끼리의 충돌이 일어난다면 위의 주석을 풀고 실행해주세요.
#보안에서의 CRT_SECURE_NO_WARNIGS과 비슷한 경고 무시 명령입니다.


#타임라인 모듈의 calc_timeline_scores의 반환값을 파라미터로 받아
#그래프를 출력하는 메소드입니다.

import matplotlib.pyplot as ppl
from matplotlib import font_manager
from config import SAVE_PATH

#김예준: 윈도우를 쓰시는 분들은 아래의 코드를 작성해 plot의 글꼴이 깨지지 않게 하세요. 
font_path = "C:\Windows\Fonts\malgun.ttf"
if os.path.exists(font_path):
    font_name = font_manager.FontProperties(fname=font_path).get_name()
    ppl.rcParams["font.family"] = font_name
else:
    print("[경고] 지정한 한글 폰트를 찾지 못했습니다. font_path를 확인하세요:", font_path)

# 마이너스 기호 깨짐 방지
ppl.rcParams["axes.unicode_minus"] = False

def plot_timeline_scores(minute_scores: dict, save_path: str = SAVE_PATH):
    minutes = sorted(minute_scores.keys())
    scores = [minute_scores[m] for m in minutes]

    ppl.figure(figsize=(8, 4))
    ppl.bar(minutes, scores)
    ppl.title("시간대별 욕설 점수")
    ppl.xlabel("시간 (분 단위)")
    ppl.ylabel("점수")
    ppl.xticks(minutes)
    ppl.grid(axis="y", linestyle="--", alpha=0.5)
    ppl.tight_layout()

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    ppl.savefig(save_path, dpi=300)
    ppl.show()
