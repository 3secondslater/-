from audio import Audio
from grid import Grid
from blocks import *
import random
import pygame


# 모든 블록 클래스 목록 (인스턴스 아님 — 매번 새로 생성하기 위해 클래스만 보관)
BLOCK_CLASSES = [IBlock, JBlock, LBlock, OBlock, SBlock, TBlock, ZBlock]


class Game: # 게임 로직 담당 클래스
    def __init__(self): # 게임 초기화
        self.grid = Grid() # 게임판 초기화
        self.current_block = self.get_random_block() # 현재 블록 랜덤 선택
        self.next_block = self.get_random_block() # 다음 블록 랜덤 선택
        self.game_over = False
        self.score = 0
        self.audio = Audio()

    def update_score(self, lines_cleared, move_down_points): # 점수 업데이트, lines_cleared는 한 번에 제거된 줄 수, move_down_points는 블록이 아래로 이동할 때마다 추가되는 점수
        if lines_cleared == 1: # 한 줄 제거 시 100점
            self.score += 100 
        elif lines_cleared == 2: # 두 줄 제거 시 300점
            self.score += 300
        elif lines_cleared == 3: # 세 줄 제거 시 500점
            self.score += 500
        elif lines_cleared == 4: # 네 줄 제거 시 800점
            self.score += 800


    def get_random_block(self): # 랜덤 블록 선택 (순수 랜덤 — 같은 블록이 연속으로 나올 수 있음)
        block_class = random.choice(BLOCK_CLASSES) # 7개 클래스 중 하나 선택
        return block_class() # 매번 새 인스턴스 생성 (current/next가 같은 객체가 되는 걸 방지)

    def move_left(self):
        self.current_block.move(0, -1) # 왼쪽으로 이동
        if self.block_inside() == False or self.block_fits() == False: 
            self.current_block.move(0, 1) 

    def move_right(self):
        self.current_block.move(0, 1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, -1)

    def move_down(self):
        self.current_block.move(1, 0)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(-1, 0)
            self.lock_block()

    def lock_block(self):
        tiles = self.current_block.get_cell_positions()
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        rows_cleared = self.grid.clear_full_rows()
        if rows_cleared > 0:
            self.update_score(rows_cleared, 0)
            self.audio.play_clear()
        if self.block_fits() == False:
            self.game_over = True
    
    def hard_drop(self):
        while True:
            self.current_block.move(1, 0)
            if self.block_inside() == False or self.block_fits() == False:
                self.current_block.move(-1, 0)
                self.lock_block()
                break
        

    def reset(self):
        self.grid.reset()
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0

    def block_fits(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_empty(tile.row, tile.column) == False:
                return False
        return True

    def rotate(self):
        self.current_block.rotate()
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.undo_rotation()

    def block_inside(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_inside(tile.row, tile.column) == False:
                return False
        return True

    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen, 11, 11)

        if self.next_block.id == 3:
            self.next_block.draw(screen, 255, 290)
        elif self.next_block.id == 4:
            self.next_block.draw(screen, 255, 280)
        else:
            self.next_block.draw(screen, 270, 270)
