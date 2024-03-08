import pygame
import os


pygame.init()


screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Music Player')


music_file = "data/sounds/moment-14023.mp3"
pygame.mixer.music.load(music_file)

music_length = pygame.mixer.Sound(music_file).get_length()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
MediumSpringGreen = (0, 250, 154)
GREEN = (57, 255, 20)
BLUE = (20, 57, 255)


font = pygame.font.Font(None, int(screen_height * 0.04))

play_text = font.render("Play", True, BLACK)
pause_text = font.render("Pause", True, BLACK)
stop_text = font.render("Stop", True, BLACK)
volume_text = font.render("Volume", True, BLACK)


button_width = 100
button_height = 40
button_spacing = 40
button_y = int((screen_height - button_height) / 2)
play_rect = pygame.Rect(200, button_y, button_width, button_height)
pause_rect = pygame.Rect(play_rect.right + button_spacing, button_y, button_width, button_height)
stop_rect = pygame.Rect(pause_rect.right + button_spacing, button_y, button_width, button_height)

volume_slider = pygame.Rect(400, 300, 200, 10)
volume_knob_radius = 10
volume_knob = pygame.Rect(int(volume_slider.left + volume_slider.width * pygame.mixer.music.get_volume()) - volume_knob_radius, volume_slider.centery - volume_knob_radius, 2 * volume_knob_radius, 2 * volume_knob_radius)

clock = pygame.time.Clock()
FPS = 30


running = True
paused = False
current_time = 0
dragging_volume = False
dragging_time = False

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_rect.collidepoint(event.pos):
                if not pygame.mixer.music.get_busy():
                    pygame.mixer.music.play()
                    current_time = 0
                else:
                    pygame.mixer.music.unpause()
                paused = False
            elif pause_rect.collidepoint(event.pos):
                if not paused:
                    pygame.mixer.music.pause()
                    paused = True
                    pause_text = font.render("Resume", True, BLACK)
                else:
                    paused = False
                    pause_text = font.render("Pause", True, BLACK)
                    pygame.mixer.music.unpause()
            elif stop_rect.collidepoint(event.pos):
                pygame.mixer.music.stop()
                current_time = 0
            elif volume_knob.collidepoint(event.pos):
                dragging_volume = True
                offset_x = event.pos[0] - volume_knob.x
            elif volume_slider.collidepoint(event.pos):
                volume_knob.centerx = event.pos[0]
                volume_knob.x = max(volume_slider.left, min(volume_slider.right - volume_knob.width, volume_knob.x))
                volume = (volume_knob.centerx - volume_slider.left) / volume_slider.width
                pygame.mixer.music.set_volume(volume)
            elif event.button == 1 and progress_rect.collidepoint(event.pos):
                dragging_time = True
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging_volume = False
            if dragging_time:
                mouse_x, mouse_y = event.pos
                current_time = (mouse_x - progress_rect.x) / progress_rect.width * music_length
                pygame.mixer.music.play(start=current_time)
                dragging_time = False
        elif event.type == pygame.MOUSEMOTION:
            if dragging_volume:
                volume_knob.centerx = event.pos[0] - offset_x
                volume_knob.x = max(volume_slider.left, min(volume_slider.right - volume_knob.width, volume_knob.x))
                volume = (volume_knob.centerx - volume_slider.left) / volume_slider.width
                pygame.mixer.music.set_volume(volume)


    if pygame.mixer.music.get_busy() and not paused and not dragging_time:
        current_time += 1 / FPS


    pygame.draw.rect(screen, MediumSpringGreen, play_rect, border_radius=2)
    pygame.draw.rect(screen, MediumSpringGreen, pause_rect, border_radius=2)
    pygame.draw.rect(screen, MediumSpringGreen, stop_rect, border_radius=2)


    screen.blit(play_text, (play_rect.centerx - play_text.get_width() // 2, play_rect.centery - play_text.get_height() // 2))
    screen.blit(pause_text, (pause_rect.centerx - pause_text.get_width() // 2, pause_rect.centery - pause_text.get_height() // 2))
    screen.blit(stop_text, (stop_rect.centerx - stop_text.get_width() // 2, stop_rect.centery - stop_text.get_height() // 2))


    pygame.draw.rect(screen, MediumSpringGreen, volume_slider)
    pygame.draw.circle(screen, BLACK, volume_knob.center, volume_knob_radius)

    screen.blit(volume_text, (int(volume_slider.left - volume_text.get_width() - 10), int(volume_slider.centery - volume_text.get_height() // 2)))


    current_time_text = font.render(f"Time: {current_time:.0f}s", True, BLACK)
    music_length_text = font.render(f"Length: {music_length:.0f}s", True, BLACK)
    screen.blit(current_time_text, (int(screen_width * 0.2) - current_time_text.get_width() // 2, int(screen_height * 0.2)))
    screen.blit(music_length_text, (int(screen_width * 0.8) - music_length_text.get_width() // 2, int(screen_height * 0.2)))


    progress_width = int(screen_width * 0.6)
    progress_rect = pygame.Rect(int(screen_width * 0.2), int(screen_height * 0.3), progress_width, int(screen_height * 0.05))
    pygame.draw.rect(screen, MediumSpringGreen, progress_rect)
    if music_length > 0:
        progress_inner_width = int(progress_width * (current_time / music_length))
        progress_inner_rect = pygame.Rect(progress_rect.left, progress_rect.top, progress_inner_width, progress_rect.height)
        pygame.draw.rect(screen, BLUE, progress_inner_rect)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
