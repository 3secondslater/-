class Colors:
    dark_grey = (26, 31, 40)
    orange = (255, 127, 0) # L블록
    blue = (0, 0, 255) # J블록
    cyan = (0, 255, 255) # I블록
    yellow = (255, 255, 0) # O블록
    green = (0, 255, 0) # S블록
    purple = (128, 0, 128) # T블록
    red = (255, 0, 0) # Z블록
    white = (255, 255, 255)
    dark_blue = (20, 20, 30) # 배경색
    light_blue = (50, 50, 70)

    @classmethod
    def get_cell_colors(cls):
        return [cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue] 
    #@classmethode ㄴ데코레이터는 함수의 기능을 추가하는 역할이다. get_cell_colors(cls): 에서cls 는 클래스 자기 자신을 뜻함 즉 여기서는 Colors가 되겠지
    #리스트의 첫번째 인자로 클래스를 받음. 즉 리스트 안의 값은 모두 클래스. 나중에 상속했을 때 자식 클래스의 값을 가져올 수 없다.
    #만약 classmethod를 쓰지 않고 직접 return[Colors.dark_grey, Colors.green, ] 이런 식으로 작성했다면 상속해도 부모의 색상만 나오게 된다
    #색약 모드 같은걸 만들 시 dit 
    #@classmethod는 나를 부른 클래스가 누군지 cls로 알려줘 라는 약속. 상속받은 자식이 호출되면 자식의 속성을 보러 감.

#def get_cell_colors(self):
    #return [self.dark_grey, self.green, self.red, self.orange, self.yellow, self.purple, self.cyan, self.blue]
#Colors.get_cell_colors() 는 classmethod를 사용할 때 가능한 호출
#Colors().get_cell_colors()로 인스턴스를 만들어야 호출 가능 메모리에 객체가 잇어야지

   #colorblindclors.get_cell_colors() 함수
    #메서드는 부모의 것이지만, 색상은 자식 것 
    #파이썬은 자식에게 없는 메서드를 부모에서 가져옴 
    
#class ColorblindColors:
    #dark_grey = (26, 31, 40)
    #orange = (255, 127, 0)
    #blue = (0, 0, 255)
    #cyan = (0, 255, 255)
    #yellow = (255, 255, 0)
    #green = (0, 255, 0)
    #purple = (128, 0, 128)
    #red = (255, 0, 0)
    #white = (255, 255, 255)
    #dark_blue = (20, 20, 30)
    #light_blue = (50, 50, 70)
    #ColorblindColors.get_cell_colors()로 부르면 cls = colorblindColors가 되어서 오버드라이드 된 색만 골라서 리스트가 만들어진다.
    #이런식으로 팔레트를 구현
