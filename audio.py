import pygame

class Audio:
    def __init__(self): # 사운드 시스템 초기화 및 배경음악 재생 - pygame.mixer 모듈을 사용하여 사운드 시스템을 초기화하고, 배경음악 파일을 로드하여 무한 반복 재생
        bgn_music_path = ".\\sounds\\music.ogg" # 배경음악 파일 경로
        rotate_sound_path = ".\\sounds\\rotate.ogg" # 블록 회전 사운드 파일 경로
        clear_sound_path = ".\\sounds\\clear.ogg" # 줄 제거 사운드 파일 경로
        # 경로 지정할때  pathlib 을 사용할 것을 권장 이게 뭘까(import pathlib) # 상대경로로 씁시다
        pygame.mixer.init() # 사운드 시스템 초기화
        
        self.bgn_music = pygame.mixer.Sound(bgn_music_path) # 배경음악 로드
        self.rotate_sound = pygame.mixer.Sound(rotate_sound_path) # 회전 사운드 로드
        self.clear_sound = pygame.mixer.Sound(clear_sound_path) # 줄 제거 사운드
    
    def play_bgn_music(self): # 배경음악 재생
        self.bgn_music.play(loops=-1) # 무한 반복 재생 (0은 한 번 재생, -1은 무한 반복)
    def play_rotate(self): # 블록 회전 사운드 재생
        self.rotate_sound.play() # 한 번 #.play(loops=0, maxtime=0, fade_ms=0) 여기서는 기본값으로 한 번 재생
    def play_clear(self): # 줄 제거 사운드 재생
        self.clear_sound.play(0) # 한 번
        
