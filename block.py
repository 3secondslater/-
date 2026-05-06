from colors import Colors
import pygame
from position import Position


class Block:
    def __init__(self, id): # 블록 ID (0~6) - 각 블록마다 고유한 ID를 부여하여 색상과 모양을 구분
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.row_offset = 0
        self.column_offset = 0
        self.rotation_state = 0
        self.colors = Colors.get_cell_colors() # 블록 ID에 따른 색상 매핑 (0~6 → 7가지 색상)

    def move(self, rows, columns): # 블록 이동 (낙하/좌우 이동) - 오프셋에 행/열 이동량을 더하는 방식
        self.row_offset += rows
        self.column_offset += columns

    def get_cell_positions(self): # 현재 회전 상태의 타일 위치를 가져와서 오프셋을 적용한 실제 위치 리스트로 반환
        tiles = self.cells[self.rotation_state]
        moved_tiles = []
        for position in tiles:
            position = Position(position.row + self.row_offset, position.column + self.column_offset)
            moved_tiles.append(position)
        return moved_tiles

    def rotate(self): # 시계 방향으로 회전 (회전 상태 인덱스 증가)
        self.rotation_state += 1
        if self.rotation_state == len(self.cells):
            self.rotation_state = 0

    def undo_rotation(self): # 회전이 안 되는 경우 원래 상태로 되돌리는 메서드
        self.rotation_state -= 1
        if self.rotation_state == -1:
            self.rotation_state = len(self.cells) - 1

    def draw(self, screen, offset_x, offset_y): # next 블록은 offset_x=320, offset_y=215로 그려짐
        tiles = self.get_cell_positions()
        for tile in tiles:
            tile_rect = pygame.Rect(
                offset_x + tile.column * self.cell_size,
                offset_y + tile.row * self.cell_size,
                self.cell_size - 1,
                self.cell_size - 1,
            )
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)
