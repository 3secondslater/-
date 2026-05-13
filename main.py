

import pygame
import sys
from game import Game  # 게임 로직이 담긴 Game 클래스
from ui import UI  # UI(창, 폰트, 점수판, Next 박스, 메뉴) 담당 클래스
from audio import Audio  # 사운드 담당 클래스
pygame.init()  # Pygame 초기화 - 폰트나 창을 만들기 전에 반드시 호출

audio = Audio() # 사운드 시스템 초기화 및 배경음악 재생
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
def playing_keydown(event,game):
    match event.key:
        case _ if game.game_over:
            game.game_over = False
            game.reset()
        case pygame.K_ESCAPE:
            return "paused" 
        case pygame.K_LEFT:
            game.move_left()
        case pygame.K_RIGHT:
            game.move_right()
        case pygame.K_DOWN:
            game.move_down()
        case pygame.K_UP:
            game.rotate()
            audio.play_rotate()
        case pygame.K_SPACE:
            game.hard_drop()


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
                    new_state = playing_keydown(event,game)
                    if new_state:
                        app_state = new_state
                    
                elif event.type == GAME_UPDATE_EVENT and not game.game_over:
                    game.move_down()
           

        # 일시정지 상태 나타내는 부분
            case "paused":
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
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

