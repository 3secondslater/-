import pygame
import sys
from game import Game  # 게임 로직이 담긴 Game 클래스
from ui import UI  # UI(창, 폰트, 점수판, Next 박스, 메뉴) 담당 클래스

pygame.init()  # Pygame 초기화 - 폰트나 창을 만들기 전에 반드시 호출

ui = UI()  # 창 생성 + 폰트/텍스트/박스 초기화
clock = pygame.time.Clock()
game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)  # 200ms마다 자동 낙하 이벤트 발생

# 앱 상태: "menu"=시작 화면, "playing"=게임 진행 중, "paused"=일시정지
app_state = "menu"

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # 메뉴 : 스타트 버튼 클릭 → 게임 시작  
        if app_state == "menu":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # 좌클릭만
                if ui.is_start_clicked(event.pos):
                    app_state = "playing"  # 버튼 클릭 → 게임 시작

        #  플레이잉 : 방향키로 블록 이동/회전, ESC로 일시정지, 자동 낙하 타이머, 게임오버 시 리셋
        elif app_state == "playing":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # ESC: 게임 진행 중일 때만 일시정지로 전환 (게임오버 상태에선 무시)
                    if game.game_over == False:
                        app_state = "paused"
                else:
                    # ESC가 아닌 키 처리 (게임오버 리셋 + 방향키)
                    if game.game_over == True:
                        game.game_over = False
                        game.reset()
                    if event.key == pygame.K_LEFT and game.game_over == False:
                        game.move_left()
                    if event.key == pygame.K_RIGHT and game.game_over == False:
                        game.move_right()
                    if event.key == pygame.K_DOWN and game.game_over == False:
                        game.move_down()
                        game.update_score(0, 1)
                    if event.key == pygame.K_UP and game.game_over == False:
                        game.rotate()
            if event.type == GAME_UPDATE and game.game_over == False:
                game.move_down()

        # === 일시정지 상태: ESC만 받음 (자동 낙하 타이머도 무시) ===
        elif app_state == "paused":
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
