# Python Tetris

pygame으로 만든 테트리스 게임.

## 스크린샷

| 시작 화면 | 게임 진행 | 일시정지 |
|---|---|---|
| ![menu](screenshots/menu.png) | ![playing](screenshots/playing.png) | ![paused](screenshots/paused.png) |

## 실행

```bash
pip install pygame
python main.py
```

## 조작

| 키 | 동작 |
|---|---|
| ← → | 좌우 이동 |
| ↓ | 빠른 낙하 |
| ↑ | 회전 |
| SPACE | 즉시 낙하 |
| ESC | 일시정지 / 재개 |
| 마우스 좌클릭 | 시작 화면에서 START 버튼 |

게임오버 후 아무 키나 누르면 재시작.

## 파일 구성

| 파일 | 역할 |
|---|---|
| `main.py` | 진입점. 이벤트 루프, 상태 기계 (menu / playing / paused) |
| `game.py` | 게임 로직. 블록 이동/회전/락, 점수, 게임오버 판정 |
| `grid.py` | 20×10 보드. 셀 상태, 줄 지우기 |
| `block.py` | 블록 베이스 클래스. 회전, 이동, 충돌 좌표 계산 |
| `blocks.py` | 7가지 테트로미노 (I, J, L, O, S, T, Z) |
| `position.py` | (row, column) 좌표 객체 |
| `ui.py` | 창, 폰트, 점수판, 메뉴, 일시정지 오버레이 |
| `colors.py` | 색상 팔레트 |
| `audio.py` | 배경음, 효과음 사운드 |

## 설계 포인트

- 셀에는 색상 대신 **블록 ID(int)** 저장 → 색은 별도 매핑
- 블록 회전은 알고리즘 대신 **dict로 4가지 상태 미리 정의**
- 이동·회전은 **"시도 후 검증"** 패턴 (안 맞으면 되돌림)
- 블록 랜덤은 **순수 랜덤** — 같은 블록 연속 가능
