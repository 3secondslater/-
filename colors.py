class Colors:
    dark_grey = (26, 31, 40) # 배경색
    orange = (255, 127, 0) # L블록
    blue = (0, 0, 255) # J블록
    cyan = (0, 255, 255) # I블록
    yellow = (255, 255, 0) # O블록
    green = (0, 255, 0) # S블록
    purple = (128, 0, 128) # T블록
    red = (255, 0, 0) # Z블록
    white = (255, 255, 255)
    dark_blue = (20, 20, 30)
    light_blue = (50, 50, 70)

    @classmethod
    def get_cell_colors(cls):
        return [cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue] 
    #@classmethode ㄴ데코레이터는 함수의 기능을 추가하는 역할이다. get_cell_colors(cls): 에서cls 는 클래스 자기 자신을 뜻함 즉 여기서는 Colors가 되겠지

   