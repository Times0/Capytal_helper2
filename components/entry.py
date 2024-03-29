import pygame
import pyperclip


class TextInputBox(pygame.sprite.Sprite):
    def __init__(self, x, y, w, font):
        super().__init__()
        self.color = 0, 0, 0
        self.backcolor = 240, 240, 240
        self.pos = (x, y)
        self.width = w
        self.font = font
        self.active = False
        self.text = ""
        self.draw()

    def draw(self):
        t_surf = self.font.render(self.text, True, self.color, self.backcolor)
        self.image = pygame.Surface((max(self.width, t_surf.get_width() + 10), t_surf.get_height() + 10),
                                    pygame.SRCALPHA)
        if self.backcolor:
            self.image.fill(self.backcolor)
        self.image.blit(t_surf, (5, 5))
        pygame.draw.rect(self.image, self.color, self.image.get_rect().inflate(-2, -2), 2)
        self.rect = self.image.get_rect(topleft=self.pos)

    def update(self, event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN and not self.active:
                self.active = self.rect.collidepoint(event.pos)
            if event.type == pygame.KEYDOWN and self.active:
                if (event.key == pygame.K_v) and (event.mod & pygame.KMOD_CTRL):
                    self.text = pyperclip.paste()

                elif event.key == pygame.K_RETURN:
                    self.active = False
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.draw()


class Label(pygame.sprite.Sprite):
    def __init__(self, text, x, y, font, color):
        super().__init__()
        self.text = text
        self.pos = x, y
        self.font = font
        self.color = color

        t_surf = self.font.render(self.text, True, self.color)
        self.image = pygame.Surface((t_surf.get_width() + 10, t_surf.get_height() + 10), pygame.SRCALPHA)
        self.rect = self.image.get_rect(topleft=self.pos)
        self.image.blit(t_surf, (5, 5))

    def upd(self, c_dir: str) -> None:
        import os
        if c_dir != "":
            self.text = f"Fichier correction : {os.path.basename(c_dir)}"
            t_surf = self.font.render(self.text, True, self.color)
            self.image = pygame.Surface((t_surf.get_width() + 10, t_surf.get_height() + 10), pygame.SRCALPHA)
            self.rect = self.image.get_rect(topleft=self.pos)
            self.image.blit(t_surf, (5, 5))

    def draw(self, screen):
        screen.blit(self.image, self.rect)
