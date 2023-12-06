import pygame
from sys import exit

#Prorietes de la fenetre
pygame.init()
width = 1900
height = 1000
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Tableau Périodique')
font_element = pygame.font.Font(None, 36)
font_poids = pygame.font.Font(None, 16)

#Couleurs
bleu_nuit = (36, 77, 87)
bourgogne = (98, 46, 57)
bleu_indigo = (63, 57, 95)
bleu_cobalt = (0, 74, 119)
marron_cafe = (82, 62, 27)
gris_ardois = (70, 71, 76)
rouge_brique = (97, 59, 40)
dark_green = (47, 77, 71)
purple = (67, 60, 101)
black = (0,0,0)
bleu_acier = (42, 65, 101)
white = (255,255,255)
marron_rougeatre = (97,59,40)
rouge_fonce = (212, 15, 77)

#Search Bar
search_font = pygame.font.Font(None, 32)
search_text = 'Rechercher un éléments'

search_rect = pygame.Rect(800, 20, 140, 32)
search_color = pygame.Color('white')
active = False

#CheckBox
checked = False


#Dico contenant tout les informations 
element_chimiques = {
    (0, 0): ["H", "1", "Hydrogène", "1.0078"],
    (17, 0): ["He", "2", "Hélium", "4.0026"],
    (0, 1): ["Li", "3", "Lithium", "6.941"],
    (1, 1): ["Be", "4", "Béryllium", "9.0122"],
    (12, 1): ["B", "5", "Bore", "10.81"],
    (13, 1): ["C", "6", "Carbone", "12.011"],
    (14, 1): ["N", "7", "Azote", "14.007"],
    (15, 1): ["O", "8", "Oxygène", "15.999"],
    (16, 1): ["F", "9", "Fluor", "18.998"],
    (17, 1): ["Ne", "10", "Néon", "20.180"],
    (0, 2): ["Na", "11", "Sodium", "22.990"],
    (1, 2): ["Mg", "12", "Magnésium", "24.305"],
    (12, 2): ["Al", "13", "Aluminium", "26.982"],
    (13, 2): ["Si", "14", "Silicium", "28.085"],
    (14, 2): ["P", "15", "Phosphore", "30.974"],
    (15, 2): ["S", "16", "Soufre", "32.06"],
    (16, 2): ["Cl", "17", "Chlore", "35.45"],
    (17, 2): ["Ar", "18", "Argon", "39.948"],
    (0, 3): ["K", "19", "Potassium", "39.098"],
    (1, 3): ["Ca", "20", "Calcium", "40.078"],
    (2, 3): ["Sc", "21", "Scandium", "44.956"],
    (3, 3): ["Ti", "22", "Titane", "47.867"],
    (4, 3): ["V", "23", "Vanadium", "50.942"],
    (5, 3): ["Cr", "24", "Chrome", "51.996"],
    (6, 3): ["Mn", "25", "Manganèse", "54.938"],
    (7, 3): ["Fe", "26", "Fer", "55.845"],
    (8, 3): ["Co", "27", "Cobalt", "58.933"],
    (9, 3): ["Ni", "28", "Nickel", "58.693"],
    (10, 3): ["Cu", "29", "Cuivre", "63.546"],
    (11, 3): ["Zn", "30", "Zinc", "65.38"],
    (12, 3): ["Ga", "31", "Gallium", "69.723"],
    (13, 3): ["Ge", "32", "Germanium", "72.630"],
    (14, 3): ["As", "33", "Arsenic", "74.922"],
    (15, 3): ["Se", "34", "Sélénium", "78.971"],
    (16, 3): ["Br", "35", "Brome", "79.904"],
    (17, 3): ["Kr", "36", "Krypton", "83.798"],
    (0, 4): ["Rb", "37", "Rubidium", "85.468"],
    (1, 4): ["Sr", "38", "Strontium", "87.62"],
    (2, 4): ["Y", "39", "Yttrium", "88.906"],
    (3, 4): ["Zr", "40", "Zirconium", "91.224"],
    (4, 4): ["Nb", "41", "Niobium", "92.906"],
    (5, 4): ["Mo", "42", "Molybdène", "95.95"],
    (6, 4): ["Tc", "43", "Technétium", "98"],
    (7, 4): ["Ru", "44", "Ruthénium", "101.07"],
    (8, 4): ["Rh", "45", "Rhodium", "102.91"],
    (9, 4): ["Pd", "46", "Palladium", "106.42"],
    (10, 4): ["Ag", "47", "Argent", "107.87"],
    (11, 4): ["Cd", "48", "Cadmium", "112.41"],
    (12, 4): ["In", "49", "Indium", "114.82"],
    (13, 4): ["Sn", "50", "Étain", "118.71"],
    (14, 4): ["Sb", "51", "Antimoine", "121.76"],
    (15, 4): ["Te", "52", "Tellure", "127.60"],
    (16, 4): ["I", "53", "Iode", "126.90"],
    (17, 4): ["Xe", "54", "Xénon", "131.29"],
    (0, 5): ["Cs", "55", "Césium", "132.91"],
    (1, 5): ["Ba", "56", "Baryum", "137.33"],
    (2, 7): ["La", "57", "Lanthane", "138.91"],
    (3, 5): ["Hf", "72", "Hafnium", "178.49"],
    (4, 5): ["Ta", "73", "Tantale", "180.95"],
    (5, 5): ["W", "74", "Tungstène", "183.84"],
    (6, 5): ["Re", "75", "Rhénium", "186.21"],
    (7, 5): ["Os", "76", "Osmium", "190.23"],
    (8, 5): ["Ir", "77", "Iridium", "192.22"],
    (9, 5): ["Pt", "78", "Platine", "195.08"],
    (10, 5): ["Au", "79", "Or", "196.97"],
    (11, 5): ["Hg", "80", "Mercure", "200.59"],
    (12, 5): ["Ti", "81", "Thallium", "204.38"],
    (13, 5): ["Pb", "82", "Plomb", "207.2"],
    (14, 5): ["Bi", "83", "Bismuth", "208.98"],
    (15, 5): ["Po", "84", "Polonium", "209"],
    (16, 5): ["At", "85", "Astate", "210"],
    (17, 5): ["Rn", "86", "Radon", "222"],
    (0, 6): ["Fr", "87", "Francium", "223"],
    (1, 6): ["Ra", "88", "Radium", "226"],
    (2, 8): ["Ac", "89", "Actinium", "227"],
    (3, 6): ["Rf", "104", "Rutherfordium","267"],
    (4, 6): ["Db", "105", "Dubnium", "270"],
    (5, 6): ["Sg", "106", "Seaborgium", "271"],
    (6, 6): ["Bh", "107", "Bohrium", "270"],
    (7, 6): ["Hs", "108", "Hassium", "277"],
    (8, 6): ["Mt", "109", "Meitnerium", "276"],
    (9, 6): ["Ds", "110", "Darmstadtium", "281"],
    (10, 6): ["Rg", "111", "Roentgenium", "280"],
    (11, 6): ["Cn", "112", "Copernicium", "285"],
    (12, 6): ["Nh", "113", "Nihonium", "284"],
    (13, 6): ["Fl", "114", "Flerovium", "289"],
    (14, 6): ["Mc", "115", "Moscovium", "288"],
    (15, 6): ["Lv", "116", "Livermorium", "293"],
    (16, 6): ["Ts", "117", "Tennessine", "294"],
    (17, 6): ["Og", "118", "Oganesson", "294"],
    (3, 7): ["Ce", "58", "Cérium", "140.12"],
    (4, 7): ["Pr", "59", "Praséodyme", "140.91"],
    (5, 7): ["Nd", "60", "Néodyme", "144.24"],
    (6, 7): ["Pm", "61", "Prométhium", "145"],
    (7, 7): ["Sm", "62", "Samarium", "150.36"],
    (8, 7): ["Eu", "63", "Europium", "151.96"],
    (9, 7): ["Gd", "64", "Gadolinium", "157.25"],
    (10, 7): ["Tb", "65", "Terbium", "158.93"],
    (11, 7): ["Dy", "66", "Dysprosium", "162.50"],
    (12, 7): ["Ho", "67", "Holmium", "164.93"],
    (13, 7): ["Er", "68", "Erbium", "167.26"],
    (14, 7): ["Tm", "69", "Thulium", "168.93"],
    (15, 7): ["Yb", "70", "Ytterbium", "173.04"],
    (16, 7): ["Lu", "71", "Lutécium", "174.97"],
    (3, 8): ["Th", "90", "Thorium", "232.04"],
    (4, 8): ["Pa", "91", "Protactinium", "231.04"],
    (5, 8): ["U", "92", "Uranium", "238.03"],
    (6, 8): ["Np", "93", "Neptunium", "237"],
    (7, 8): ["Pu", "94", "Plutonium", "244"],
    (8, 8): ["Am", "95", "Américium", "243"],
    (9, 8): ["Cm", "96", "Curium", "247"],
    (10, 8): ["Bk", "97", "Berkélium", "247"],
    (11, 8): ["Cf", "98", "Californium", "251"],
    (12, 8): ["Es", "99", "Einsteinium", "252"],
    (13, 8): ["Fm", "100", "Fermium", "257"],
    (14, 8): ["Md", "101", "Mendélévium", "258"],
    (15, 8): ["No", "102", "Nobélium", "259"],
    (16, 8): ["Lr", "103", "Lawrencium", "262"],
}

def dessine_tableau():
    """
    Dessine le tableau Periodique 
    """
    for i in range(18):
        for j in range(9):
            if i in [0] and j in [0] or i in [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16] and j in [7] :
                pygame.draw.rect(screen, bleu_cobalt, (10 + i * 100, 150 + j * 80, 60, 60))
            elif i in [13,14,15,16] and j in [1] or i in [14,15,16] and j in [2] or i in [15,16] and j in [3] or i in [16] and j in [4]:
                pygame.draw.rect(screen, bleu_acier, (10 + i * 100, 150 + j * 80, 60, 60))
            elif i in [0] and j in [1,2,3,4,5,6]:
                pygame.draw.rect(screen, bleu_nuit, (10 + i * 100, 150 + j * 80, 60, 60))
            elif i in [1] and j in [1,2,3,4,5,6] or i in [17] and j in [0,1,2,3,4,5]:
                pygame.draw.rect(screen, bourgogne, (10 + i * 100, 150 + j * 80, 60, 60))
            elif i in [2,3,4,5,6,7,8,9,10,11] and j in [3,4] or  i in [3,4,5,6,7,8,9,10,11] and j in [5] or  i in [3,4,5,6,7] and j in [6]:
                pygame.draw.rect(screen, purple, (10 + i * 100, 150 + j * 80, 60, 60))
            elif i in [7,8,9,10,11,12,13,14,15,16,17] and j in [6]:
                pygame.draw.rect(screen, gris_ardois, (10 + i * 100, 150 + j * 80, 60, 60))
            elif i in [12] and j in [2,3,4,5] or i in [13] and j in [4,5] or i in [13,14,15,16] and j in [5]:
                pygame.draw.rect(screen, dark_green, (10 + i * 100, 150 + j * 80, 60, 60))
            elif i in [12] and j in [1] or i in [13] and j in [2] or i in [13,14] and j in [3] or i in [14,15] and j in [4]:
                pygame.draw.rect(screen, marron_cafe, (10 + i * 100, 150 + j * 80, 60, 60))
            elif i in [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16] and j in [8] :
                pygame.draw.rect(screen, marron_rougeatre, (10 + i * 100, 150 + j * 80, 60, 60))

            #Afiche le symbole
            if (i, j) in element_chimiques:
                elm_chimique = element_chimiques[(i, j)][0]
            else:
                elm_chimique = ""

            text_surface = font_element.render(elm_chimique, True, (255, 255, 255))

            text_rect = text_surface.get_rect()
            text_rect.center = (10 + i * 100 + 30, 150 + j * 80 + 30)

            screen.blit(text_surface, text_rect)

            #Affiche le poids
            if (i, j) in element_chimiques:
                elm_poids = element_chimiques[(i, j)][3]
            else:
                elm_poids = ""


            text_surface = font_poids.render(elm_poids, True, (255, 255, 255))

            text_rect = text_surface.get_rect()
            text_rect.center = (-3 + i * 100 + 30, 173 + j * 80 + 30)

            screen.blit(text_surface, text_rect)




def coordonnees(souris_pos):
    """
    Recuperes les coordonnées de la souris
    souris_pos -> int
    """
    x,y = souris_pos
    i = (x - 10) // 100
    j = (y - 150) // 80
    return int(i), int(j)


def informations_sup(souris_pos, dic):
    """
    Verifie si quand il y a survol sur un rectangle l'element est dans element_chimiques 
    est recuperer toutes les information les concernant
    souris_pos -> int
    dic -> dic
    """
    (i, j) = coordonnees(souris_pos)
    cle = (i, j)
    if cle in dic:
        value = dic[cle]
        symbole = dic[cle][0]
        config = get_config(symbole)
        return value, config
    else:
        return None
    
    
def affiche_rect(infos):
    """
    Affiche un rectangle avec les information supplementaire qui sont la liste element_chimiques
    """
    if infos  is not None:
        pygame.draw.rect(screen, white, (250, 160, 600, 200))
        pygame.draw.rect(screen, black, (260, 170, 580, 180))


        font = pygame.font.Font(None, 36)
        y = 190
        

        for info in infos:
            if type(info) == list: #Evite que le texte soit afficher sous forme de list
                for element in info:
                    text_surface = font.render(element, True, white)
                    text_rect = text_surface.get_rect()
                    text_rect.center = (550, y)
                    screen.blit(text_surface, text_rect)
                    y += 30 #Evite que le texte soit sur la meme ligne
            else:
                text_surface = font.render(info, True, white)
                text_rect = text_surface.get_rect()
                text_rect.center = (550, y)
                screen.blit(text_surface, text_rect)
                


def dessine_search_bar():
    """
    Dessine la barre de recherche
    """
    pygame.draw.rect(screen, search_color, search_rect)

    text_surface = search_font.render(search_text, True, black)
    screen.blit(text_surface, (search_rect.x+5, search_rect.y+5))
    search_rect.w = max(100, text_surface.get_width()+10)
    active = False

def electron_core(n,x):
    electron_config = ""
    electrons_remaining = n
    orbitals = [
    ("1s", 2),
    ("2s", 2),
    ("2p", 6),
    ("3s", 2),
    ("3p", 6),
    ("4s", 2),
    ("3d", 10),
    ("4p", 6),
    ("5s", 2),
    ("4d", 10),
    ("5p", 6),
    ("6s", 2),
    ("4f", 14),
    ("5d", 10),
    ("6p", 6),
    ("7s", 2),
    ("5f", 14),
    ("6d", 10),
    ("7p", 6),
    ]

    for y in range(0,x):
        orbitals.pop(0)

        for orbital, max_electrons in orbitals:
            if electrons_remaining <= 0:
                break
            if electrons_remaining < max_electrons:
                electron_config += f"{orbital}{electrons_remaining} "
                electrons_remaining = 0
            else:
                electron_config += f"{orbital}{max_electrons} "
                electrons_remaining -= max_electrons
    return electron_config

def electron_configuration(Z):
    couches=["[He] ","[Ne] ","[Ar] ","[Kr] ","[Xe] ","[Rn] "]
    if (Z<=2) :
        n=Z
        couche=electron_core(n,1)
    elif (Z>2 and Z<=10) :
        n=Z-2
        couche = couches[0]+electron_core(n,1)
    elif (Z>10 and Z<=18) :
        n=Z-10
        couche = couches[1]+electron_core(n,3)
    elif (Z>18 and Z<=36) :
        n=Z-18
        couche = couches[2]+electron_core(n,6)
    elif (Z>36 and Z<=54) :
        n=Z-36
        couche = couches[3]+electron_core(n,9)
    elif (Z>54 and Z<=86) :
        n=Z-54
        couche = couches[4]+electron_core(n,12)
    elif (Z>86 and Z<=118) :
        n=Z-86
        couche = couches[5]+electron_core(n,1)
    return couche



def get_config(element):
    """
    Verifi si un element est dans le dictionnaire si il y est on peut obtenir sa configuration electroniques
    dictionnaire -> {[list]}
    element -> str
    """
    for infos in element_chimiques.values():
        symbole = infos[0]
        numero_atomique = int(infos[1])
        if element == symbole:
            couche_electronique = electron_configuration(numero_atomique)
            return str(couche_electronique)

def recherche_elm(texte):
    """
    Verifie que l'element/symbole/mot rerchercher est dans le dico element_chimiques
    ensuite l'ajoute dans la liste puis affiche tout les rectangle qui contient soit le mots/symbole si il y en a plusieurs
    texte -> str
    """
    resultats_recherche = []

    for coords, details in element_chimiques.items():
        if texte.lower() in details[0].lower() or texte.lower() in details[2].lower():
            resultats_recherche.append(coords)
            
    
        if coords in resultats_recherche:
            pygame.draw.rect(screen, rouge_fonce, (10 + coords[0] * 100, 150 + coords[1] * 80, 60, 60))
            text_surface = font_element.render(element_chimiques[coords][0], True, white)
            text_surface_2 = font_poids.render(element_chimiques[coords][3], True, white)
            text_rect = text_surface.get_rect()
            text_rect_2 = text_surface_2.get_rect()
            text_rect.center = (10 + coords[0] * 100 + 30, 150 + coords[1] * 80 + 30)
            text_rect_2.center = (-3 + coords[0] * 100 + 30, 173 + coords[1] * 80 + 30)
            screen.blit(text_surface, text_rect)
            screen.blit(text_surface_2, text_rect_2)
        else:
            pygame.draw.rect(screen, black, (10 + coords[0] * 100, 150 + coords[1] * 80, 60, 60))

#Propriete tableau
screen.fill(black)
#Affiche la tableau
dessine_tableau()


#Boucle principale
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEMOTION:
            souris_pos = pygame.mouse.get_pos()
            infos = informations_sup(souris_pos, element_chimiques)
            coords = ((souris_pos[0] - 10) // 100, (souris_pos[1] - 150) // 80)
            if infos and screen.get_at((10 + coords[0] * 100 + 30, 150 + coords[1] * 80 + 30)) != black: #Evite que si des rectangle sont passer en noir il puisse interagir avec la souris
                affiche_rect(infos)

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            souris_x, souris_y = event.pos
            active = search_rect.x < souris_x + search_rect.width and \
                     search_rect.y < souris_y + search_rect.height
            if active:
                search_text = ""

        if event.type == pygame.KEYUP:
            if active:
                if event.key == pygame.K_RETURN:
                    if search_text == "":
                        print("Entrez une valeur")
                    else:
                        recherche_elm(search_text)
                elif event.key == pygame.K_BACKSPACE:
                    search_text = search_text[:-1]
                    dessine_tableau()
                elif pygame.K_a <= event.key <= pygame.K_z or pygame.K_0 <= event.key <= pygame.K_9: #vérifie si la touche de clavier associée à l'événement event est une lettre minuscule (a à z) ou un chiffre (0 à 9).
                    search_text += event.unicode

    #Affiche la barre de recherche
    dessine_search_bar()

    #affiche_rect()
    pygame.display.update()

pygame.quit()
exit()