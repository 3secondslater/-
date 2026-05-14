

import pygame #기본 내장 모듈이라 from없이 그냥 진행
import sys
from game import Game  # 게임 로직이 담긴 Game 클래스
from ui import UI  # UI(창, 폰트, 점수판, Next 박스, 메뉴) 담당 클래스
from audio import Audio  # 사운드 담당 클 클래스에서 모듈을 불러온다 from 클래스 import 모듈
pygame.init()  # Pygame 초기화 - 폰트나 창을 만들기 전에 반드시 호출

audio = Audio() # 사운드 시스템 초기화 및 배경음악 재
ui = UI()  # 창 생성 + 폰트/텍스트/박스 초기화
clock = pygame.time.Clock()
game = Game()


GAME_UPDATE_EVENT = pygame.USEREVENT
MOUSELEFT = 1
MOUSEWHEEL = 2
MOUSERIGHT = 3
MOUSEWHEELUP = 4
MOUSEWHEELDOWN = 5
GAME_UPDATE_INTERVAL = 200

pygame.time.set_timer(GAME_UPDATE_EVENT, GAME_UPDATE_INTERVAL)  # GAME_UPDATE_INTERVAL ms마다 자동 낙하 이벤트 발생 #pygame.time.set_timer(event, millis, loops=0) 에서 event는 발생시킬 이벤트의 종류, millis는 이벤트가 발생하는 간격(밀리초), loops는 이벤트가 반복되는 횟수 (0이면 무한 반복) 여기서는 GAME_UPDATE_INTERVAL ms마다 GAME_UPDATE_EVENT 이벤트가 발생하도록 설정

# 앱 상태: "menu"=시작 화면, "playing"=게임 진행 중, "paused"=일시정지
def playing_keydown(event,game,audio):# 게임 진행 중 키 입력 처리 함수, event는 키 입력 이벤트 객체, game은 Game 클래스 인스턴스, audio는 Audio 클래스 인스턴스
    
    keydown_actions = None
   
    match event.key: 
        case _ if game.game_over:
            game.game_over = False
            game.reset()
        case pygame.K_ESCAPE:  
            keydown_actions = "escape"
        case pygame.K_LEFT:
            keydown_actions = "k_left"
            game.move_left()
        case pygame.K_RIGHT:
            keydown_actions = "k_right"
            game.move_right()
        case pygame.K_DOWN:
            keydown_actions = "k_down"   
            game.move_down()
        case pygame.K_UP:
            game.rotate()
            keydown_actions = "k_up"
            audio.play_rotate()
        case pygame.K_SPACE:
            game.hard_drop()
            keydown_actions = "k_space"
    return keydown_actions

app_state = "menu"

while True:
    for event in pygame.event.get(): # 이벤트 루프 - 모든 이벤트 처리 (키보드, 마우스, 창 닫기 등)
        if event.type == pygame.QUIT: # 창 닫기 버튼 클릭 시 종료함
            pygame.quit()
            sys.exit()

        # 메뉴 : 스타트 버튼 클릭 → 게임 시작  
        
        match app_state:
            case "menu":
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == MOUSELEFT and ui.is_start_clicked(event.pos): # 클릭한 위치가 스타트 버튼 영역 안에 있는지 검사하는 함수 호출 pos는 클릭한 위치의 좌표 (x, y) 튜플로 전달됨
                    app_state = "playing"  # 버튼 클릭 → 게임 시작

        #  플레이잉 : 방향키로 블록 이동/회전, ESC로 일시정지, 자동 낙하 타이머, 게임오버 시 리셋
            case "playing":
                if event.type == pygame.KEYDOWN:
                    new_state = playing_keydown(event,game,audio)
                    if new_state == "escape":
                        app_state = "paused" 


                elif event.type == GAME_UPDATE_EVENT and not game.game_over:
                    game.move_down()
           

        # 일시정지 상태 나타내는 부분
            case "paused":
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:  # 키다운 이벤트에서 ESC키가 눌렸을 때 
                    new_state = playing_keydown(event,game,audio)
                    if new_state == "escape":
                        app_state = "playing"  # ESC 다시 누르면 재개 
                        
                    
    # === Drawing ===
    if app_state == "menu":
        ui.draw_menu()  # 메뉴 화면
    else:
        ui.draw(game.score, game.game_over)  # 배경 + 점수판 + Next 박스
        game.draw(ui.screen)  # 보드 + 현재/다음 블록
        if app_state == "paused":
            ui.draw_pause_overlay()  # 게임 화면 위에 어두운 오버레이 + "PAUSED" 텍스트

    pygame.display.update()
    clock.tick(60)
    

#def tick(self, framerate: float = 0, /) -> int:

self는 첫번째 매개변수로 Clock 클래스의 인스턴스를 가리킵니다. framerate는 선택적 매개변수로, 초당 프레임 수를 나타내는 부동 소수점 숫자입니다. 
기본값은 0으로, 이 경우 프레임 속도 제한이 없습니다. 
/는 위치 전용 매개변수를 나타내며, framerate는 위치 인수로만 전달될 수 있음을 의미합니다.
int는 이 메서드가 정수를 반환한다는 것을 나타냅니다. 반환되는 정수는 이전 틱에서 경과된 시간(밀리초)입니다.

위에 click.tick() 
이전 tick 호출 이후로 경과된 시간(밀리초)을 반환합니다.
framerate 인수가 0보다 크면, tick()은 프레임 속도를 framerate로 제한하기 위해 필요한 경우 지연을 추가합니다. 예를 들어, tick(60)은 초당 최대 60 프레임으로 실행되도록 합니다. 
이 경우 tick()은 프레임 속도를 제한하기 남은 시간을 sleep()을 사용하여 지연한 후, 이전 tick 호출 이후로 경과된 시간(밀리초)을 반환합니다.
dt = clock.tick(60) 16ms 정도가 반환됩니다. 이는 60 FPS로 실행될 때 각 프레임이 약 16.67ms마다 업데이트된다는 것을 의미합니다.
clock.get_fps() 메서드는 현재 프레임 속도를 반환합니다. 예를 들어, clock.get_fps()가 60을 반환하면 현재 프레임 속도가 초당 60 프레임임을 나타냅니다.
clock.get_time() 메서드는 이전 tick 호출 이후로 경과된 시간(밀리초)을 반환합니다. 예를 들어, clock.get_time()이 16을 반환하면 이전 tick 호출 이후로 약 16ms가 경과했음을 나타냅니다.
clock.get_rawtime() 메서드는 tick()이 프레임 속도를 제한하기 위해 추가한 지연을 포함하여, 이전 tick 호출 이후로 경과된 실제 시간(밀리초)을 반환합니다. 예를 들어, clock.get_rawtime()이 20을 반환하면 tick()이 프레임 속도를 제한하기 위해 약 4ms의 지연을 추가했음을 나타냅니다

