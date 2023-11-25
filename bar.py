import pygame
import sys

pygame.init()

# Paramètres de la fenêtre
largeur, hauteur = 800, 600
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Barre de recherche Pygame")

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

# Police
font = pygame.font.Font(None, 36)

def barre_de_recherche():
    input_rect = pygame.Rect(200, 300, 140, 32)
    texte = "Recherche..."
    texte_surface = font.render(texte, True, NOIR)
    active = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                active = input_rect.x < mouse_x < input_rect.x + input_rect.width and \
                         input_rect.y < mouse_y < input_rect.y + input_rect.height
                if active:
                    texte = ""  # Efface le texte lorsque la barre de recherche devient active
            elif event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        return texte
                    elif event.key == pygame.K_BACKSPACE:
                        texte = texte[:-1]
                    else:
                        texte += event.unicode

        # Mise à jour de l'affichage
        fenetre.fill(BLANC)

        # Dessiner la barre de recherche
        pygame.draw.rect(fenetre, NOIR, input_rect, 2)
        texte_surface = font.render(texte, True, NOIR)
        width = max(200, texte_surface.get_width()+10)
        input_rect.w = width
        fenetre.blit(texte_surface, (input_rect.x+5, input_rect.y+5))

        pygame.display.flip()

# Utilisation de la fonction
resultat_recherche = barre_de_recherche()
print("Résultat de la recherche:", resultat_recherche)
