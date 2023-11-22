import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1800, 1000))
pygame.display.set_caption('Tableau Périodique')
font = pygame.font.Font(None, 36)

bleu_nuit = (36, 77, 87)
bourgogne = (98, 46, 57)
bleu_indigo = (63, 57, 95)
bleu_cobalt = (0, 74, 119)
marron_cafe = (82, 62, 27)
gris_ardois = (70, 71, 76)
rouge_brique = (97, 59, 40)
dark_green = (47, 77, 71)
purple = (67, 60, 101)
black = (0, 0, 0)
bleu_acier = (42, 65, 101)
white = (255, 255, 255)
marron_rougeatre = (97, 59, 40)

# CheckBox
checked = False

rectangle = pygame.Rect(250, 160, 600, 200)
rectangle_1 = pygame.Rect(260, 170, 580, 180)

rectangles = [
    (250, 160, 600, 200),
    (260, 170, 580, 180)
]

non_reactifs = {
    (0, 0): "H", (13, 1): "C", (14, 1): "N", (15, 1): "O", (16, 1): "F",
    (14, 2): "P", (15, 2): "S", (16, 2): "Cl", (15, 3): "Se",
    (16, 3): "Br", (16, 4): "I"
}

metaux_alcalin = {
    (0, 1): "Li", (0, 2): "Na", (0, 3): "K",
    (0, 4): "Rb", (0, 5): "Cs", (0, 6): "Fr"
}
metaux_alcalino = {
    (1, 1): "Be", (1, 2): "Mg", (1, 3): "Ca",
    (1, 4): "Sr", (1, 5): "Ba", (1, 6): "Ra"
}

meteaux_de_transition = {
    (2, 3): "Sc", (3, 3): "Ti", (4, 3): "V", (5, 3): "Cr", (6, 3): "Mn", (7, 3): "Fe",
    (8, 3): "Co", (9, 3): "Ni", (10, 3): "Cu", (11, 3): "Zn", (2, 4): "Y", (3, 4): "Zr",
    (4, 4): "Nb", (5, 4): "Mo", (6, 4): "Tc", (7, 4): "Ru", (8, 4): "Rh", (9, 4): "Pd",
    (10, 4): "Ag", (11, 4): "Cd", (3, 5): "Hf", (4, 5): "Ta", (5, 5): "W", (6, 5): "Re",
    (7, 5): "Os", (8, 5): "Ir", (9, 5): "Pt", (10, 5): "Au", (11, 5): "Hg",
    (3, 6): "Rf", (4, 6): "Db", (5, 6): "Sg", (6, 6): "Bh", (7, 6): "Hs",
}

metaloide = {
    (12, 1): "B", (13, 2): "Si", (13, 3): "Ge", (14, 3): "As",
    (14, 4): "Sb", (15, 4): "Te"
}

meteaux_post_transition = {
    (12, 2): "Al", (12, 3): "Ga", (12, 4): "In", (13, 4): "Sn",
    (12, 5): "Ti", (13, 5): "Pb",
    (14, 5): "Bi", (12, 6): "Nh", (13, 6): "Fl", (14, 6): "Mc",
    (15, 6): "Lv"
}

halogene = {
    (17, 2): "F", (17, 3): "Cl", (17, 4): "Br", (17, 5): "I", (17, 6): "At"
}

gaz_edel = {
    (18, 1): "He", (18, 2): "Ne", (18, 3): "Ar", (18, 4): "Kr",
    (18, 5): "Xe", (18, 6): "Rn"
}

lanthanide = {
    (4, 9): "La", (5, 9): "Ce", (6, 9): "Pr", (7, 9): "Nd", (8, 9): "Pm",
    (9, 9): "Sm", (10, 9): "Eu", (11, 9): "Gd", (12, 9): "Tb", (13, 9): "Dy",
    (14, 9): "Ho", (15, 9): "Er", (16, 9): "Tm", (17, 9): "Yb", (18, 9): "Lu"
}

actinide = {
    (4, 10): "Ac", (5, 10): "Th", (6, 10): "Pa", (7, 10): "U", (8, 10): "Np",
    (9, 10): "Pu", (10, 10): "Am", (11, 10): "Cm", (12, 10): "Bk", (13, 10): "Cf",
    (14, 10): "Es", (15, 10): "Fm", (16, 10): "Md", (17, 10): "No", (18, 10): "Lr"
}

element_chimiques = {**non_reactifs, **metaux_alcalin, **metaux_alcalino, **meteaux_de_transition,
                     **metaloide, **meteaux_post_transition, **halogene, **gaz_edel, **lanthanide, **actinide}

# Ajoutez une variable pour suivre l'indice du rectangle survolé
hovered_rect = None

def informations_sup(position, elements):
    for rect, element in elements.items():
        if element is not None:
            pygame.draw.rect(screen, white, rect, 0)
            pygame.draw.rect(screen, black, rect, 2)
            text = font.render(f"{element}", True, black)
            screen.blit(text, rect)

# Fonction pour dessiner le tableau périodique
def dessine_tableau():
    global hovered_rect  # Ajoutez cette ligne pour modifier la variable globale

    for i in range(18):
        for j in range(9):
            rect = pygame.Rect(10 + i * 100, 150 + j * 80, 60, 60)

            # Vérifiez si la souris est sur le rectangle actuel
            if rect.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, white, rect, 0)  # Remplissage blanc pour la mise en surbrillance
                pygame.draw.rect(screen, black, rect, 3)  # Bordure noire pour la mise en surbrillance
                hovered_rect = (i, j)
            else:
                hovered_rect = None

            pygame.draw.rect(screen, bleu_acier, rect, 0)
            pygame.draw.rect(screen, white, rect, 2)
            element = element_chimiques.get((i, j), None)
            if element is not None:
                text = font.render(f"{element}", True, white)
                screen.blit(text, rect)

# Boucle principale
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill(bleu_nuit)

    dessine_tableau()

    # Mettez à jour la fonction informations_sup pour utiliser hovered_rect
    if hovered_rect is not None:
        informations_sup(pygame.mouse.get_pos(), {hovered_rect: element_chimiques.get(hovered_rect, None)})

    pygame.display.flip()

pygame.quit()
exit()
