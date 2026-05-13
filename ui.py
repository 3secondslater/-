import pygame
from colors import Colors


class UI:
    def __init__(self):
        # 창 설정
        self.screen = pygame.display.set_mode((500, 620))  # 게임 창 크기 설정 # 앞에  self.를 넣는 이유는 나중에 만들어진 객체를 또 사용하기 위함, 인스턴스에 보관  아래 동일
        pygame.display.set_caption("Python Tetris")  # 창 제목 설정 # set_caption 은 두개의 인자를 받을 수 있다. (긴 제목, 짧은 제목/아이콘 제목) 여기서는 하나만 사용하였음.

        # 폰트맑은고딕 폰트, 크기 30
        self.title_font = pygame.font.SysFont("malgun gothic", 30, bold=True) 
        # 변하지 않는 텍스트는 미리 렌더링하여 surface로 저장 (매 프레임 다시 만들 필요 없음)
        self.score_surface = self.title_font.render("Score", True, Colors.white) #Colors.white 값 읽고, 문자열Score 준비, 안티엘리어싱 true 값 준비, self.title_font 객체 찾기 찾은 값들을 모두 호출 render함수 작동해서 surface 객체를 반환. 반환된 serface를 저장.
        self.next_surface = self.title_font.render("Next", True, Colors.white)
        self.game_over_surface = self.title_font.render("GAME OVER", True, Colors.white)

        # 점수판/Next 박스 위치와 크기
        self.score_rect = pygame.Rect(320, 55, 170, 60)
        self.next_rect = pygame.Rect(320, 215, 170, 180)

        # 메뉴 화면 요소
        self.menu_title_font = pygame.font.SysFont("malgun gothic", 80, bold=True)  # 큰 제목용
        self.menu_button_font = pygame.font.SysFont("malgun gothic", 40, bold=True)  # 버튼 글자용
        self.title_surface = self.menu_title_font.render("TETRIS", True, Colors.white)
        self.start_button_text = self.menu_button_font.render("START", True, Colors.white)
        self.start_button_rect = pygame.Rect(150, 350, 200, 80)  # 화면 중앙에 200x80 버튼

        # 일시정지 오버레이 (반투명 검은 배경 + "PAUSED" 텍스트)
        self.pause_text_surface = self.menu_title_font.render("PAUSED", True, Colors.white)
        self.pause_overlay = pygame.Surface((500, 620))  # 화면 전체 크기의 빈 surface
        self.pause_overlay.set_alpha(180)  # 0(투명)~255(불투명) 중 180 = 어둡게 흐림 처리
        self.pause_overlay.fill((0, 0, 0))  # 검은색으로 채움

    def draw_menu(self):
        # 배경
        self.screen.fill(Colors.dark_blue)

        # 타이틀
        title_rect = self.title_surface.get_rect(center=(250, 200))
        self.screen.blit(self.title_surface, title_rect)

        # 1 시작버튼
        pygame.draw.rect(self.screen, Colors.light_blue, self.start_button_rect, 0, 15)

        # 버튼 텍스트 (버튼 중앙에 위치시키기 위해 get_rect()로 텍스트의 사각형을 가져와서 centerx와 centery를 버튼 사각형의 중심으로 설정)
        text_rect = self.start_button_text.get_rect(center=self.start_button_rect.center)
        self.screen.blit(self.start_button_text, text_rect)

    def is_start_clicked(self, pos):
        # 클릭 좌표가 스타트 버튼 영역 안에 있는지 검사
        return self.start_button_rect.collidepoint(pos) #pygame.Rect 객체의 collidepoint() 메서드는 주어진 좌표가 사각형 내부에 있는지 검사하여 True/False 반환 

    def draw_pause_overlay(self):
        # 게임 화면 위에 어두운 막을 덮고 "PAUSED" 텍스트를 중앙에 표시
        self.screen.blit(self.pause_overlay, (0, 0))  # 화면 전체에 반투명 막
        text_rect = self.pause_text_surface.get_rect(center=(250, 310))  # 화면 정중앙
        self.screen.blit(self.pause_text_surface, text_rect)

    def draw(self, score, game_over):
        # 배경 칠하기
        self.screen.fill(Colors.dark_blue)

        # 라벨 텍스트
        self.screen.blit(self.score_surface, (365, 20, 50, 50)) # Score 텍스트 #screen.blit(그릴 이미지 객체, dest, area) 여기서 dest, 위치는 x,y값만 받음 bilt은 source의 크기를 그대로 가져오기 때문에 원래 크기 그대로 가져옴. 즉 뒤에 50 50은 의미가 없다.
        self.screen.blit(self.next_surface, (375, 180, 50, 50)) # Next 텍스트

        # 게임오버 텍스트 
        if game_over:
            self.screen.blit(self.game_over_surface, (320, 450, 50, 50))

        # 점수 박스 , 숫자 (점수는 매 프레임 새로 렌더)
        pygame.draw.rect(self.screen, Colors.light_blue, self.score_rect, 0, 10) #  점수판 박스
        score_value_surface = self.title_font.render(str(score), True, Colors.white) #  점수 텍스트 렌더링
        self.screen.blit(
            score_value_surface,
            score_value_surface.get_rect(
                centerx=self.score_rect.centerx,
                centery=self.score_rect.centery,
            ), # 점수 텍스트를 점수판 박스의 중앙에 위치시키기 위해 get_rect()로 텍스트의 사각형을 가져와서 centerx와 centery를 score_rect의 중심으로 설정
        )

        # Next 박스 (배경만)
        pygame.draw.rect(self.screen, Colors.light_blue, self.next_rect, 0, 10) # Next 블록은 게임에서 그려주기 때문에 박스만 그려줌
