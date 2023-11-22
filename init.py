import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1900,1000))
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
black = (0,0,0)
bleu_acier = (42, 65, 101)
white = (255,255,255)
marron_rougeatre = (97,59,40)

#Search Bar
search_font = pygame.font.Font(None, 32)
search_text = ''

search_rect = pygame.Rect(800, 20, 140, 32)
search_color = pygame.Color('lightskyblue3')
search_active = False

#CheckBox
checked = False


rectangle = pygame.Rect(250,160,600,200)
rectangle_1 = pygame.Rect(260,170,580,180)


non_reactifs = {
    (0, 0): "H",(13, 1): "C", (14, 1): "N", (15, 1): "O", (16, 1): "F",
    (14, 2): "P", (15, 2): "S", (16, 2): "Cl",(15, 3): "Se",
    (16, 3): "Br",(16, 4): "I"
}

metaux_alcalin = {
    (0, 1): "Li",(0, 2): "Na",(0, 3): "K",
    (0, 4): "Rb",(0,5) : "Cs",(0,6) : "Fr"
}
metaux_alcalino = {
    (1, 1): "Be",(1, 2): "Mg",(1, 3): "Ca",
    (1, 4): "Sr", (1,5) : "Ba", (1,6) : "Ra"
}

meteaux_de_transition = {
    (2, 3): "Sc", (3, 3): "Ti", (4, 3): "V", (5, 3): "Cr", (6, 3): "Mn", (7, 3): "Fe",
    (8, 3): "Co", (9, 3): "Ni", (10, 3): "Cu", (11, 3): "Zn",(2, 4): "Y", (3, 4): "Zr",
    (4, 4): "Nb", (5, 4): "Mo", (6, 4): "Tc", (7, 4): "Ru",(8, 4): "Rh", (9, 4): "Pd",
    (10, 4): "Ag", (11, 4): "Cd",(3,5) : "Hf" , (4,5) : "Ta" , (5,5) : "W",(6,5) : "Re",
    (7,5) : "Os" , (8,5) : "Ir" , (9,5) : "Pt", (10,5) : "Au" , (11,5) : "Hg" ,
    (3,6) : "Rf" , (4,6) : "Db" , (5,6) : "Sg",(6,6) : "Bh", (7,6) : "Hs" ,
}

metaloide = {
    (12, 1): "B",(13, 2): "Si",(13, 3): "Ge", (14, 3): "As",
    (14,4): "Sb", (15, 4): "Te"
}

meteaux_post_transition = {
    (12, 2): "Al",(12, 3): "Ga",(12, 4): "In", (13, 4): "Sn",
    (12,5) : "Ti" , (13,5) : "Pb",
    (14,5) : "Bi", (15,5) : "Po" , (16,5) : "At" ,
}

propriete_inconnue = {
    (8,6) : "Mt" , (9,6) : "Ds", (10,6) : "Rg" , (11,6) : "Cn" ,
    (12,6) : "Nh" , (13,6) : "Fi",(14,6) : "Mc", (15,6) : "Lv" ,
    (16,6) : "Ts" , (17,6) : "Og"
}

lanthanide = {
    (3,7) : "Ce", (4,7) : "Pr" , (5,7) : "Nd" , (6,7) : "Pm",
    (7,7) : "Sm" , (8,7) : "Eu" , (9,7) : "Gd" , (10,7) : "Tb",
    (11,7) : "Dy", (12,7) : "Ho" , (13,7) : "Er" , (14,7) : "Tm",
    (15,7): "Yb", (16,7) : "Lu",
}

actinide = {
    (2,6) : "Ac",(3,8) : "Th", (4,8) : "Pa" , (5,8) : "U" ,
    (6,8) : "Np", (7,8) : "Pu" , (8,8) : "Am" , (9,8) : "Cm" , (10,8) : "Bk",
    (11,8) : "Cf", (12,8) : "Es" , (13,8) : "Fm" , (14,8) : "Md", (15,8): "No", (16,8) : "Lr"
}

gaz_noble = {
    (17,0) : "He", (17,1) : "Ne", (17,2) : "Ar", (17,3) : "Kr",
    (17,4) : "Xe", (17,5) : "Rn"
}

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
    (2, 5): ["La", "57", "Lanthane", "138.91"],
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
    (2, 6): ["Ac", "89", "Actinium", "227"],
    (3, 6): ["Rf", "104", "Rutherfordium", "267"],
    (4, 6): ["Db", "105", "Dubnium", "270"],
    (5, 6): ["Sg", "106", "Seaborgium", "271"],
    (6, 6): ["Bh", "107", "Bohrium", "270"],
    (7, 6): ["Hs", "108", "Hassium", "277"],
    (8, 6): ["Mt", "109", "Meitnerium", "276"],
    (9, 6): ["Ds", "110", "Darmstadtium", "281"],
    (10, 6): ["Rg", "111", "Roentgenium", "280"],
    (11, 6): ["Cn", "112", "Copernicium", "285"],
    (12, 6): ["Nh", "113", "Nihonium", "284"],
    (13, 6): ["Fi", "114", "Flerovium", "289"],
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
    for i in range(18):
        for j in range(9):
            if i in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16] and j in [0]:
                pygame.draw.rect(screen, black,(10 + i * 100, 150 + j * 80, 60, 60))
            elif i in [0] and j in [0] or i in [3,4,5,6,7,8,9,10,11,12,13,14,15,16] and j in [7] :
                pygame.draw.rect(screen, bleu_cobalt, (10 + i * 100, 150 + j * 80, 60, 60))
            elif i in [2,3,4,5,6,7,8,9,10,11] and j in [0,1,2] or i in [0,1,2,17] and j in [7,8]:
                pygame.draw.rect(screen, black, (10 + i * 100, 150 + j * 80, 60, 60))
            elif i in [13,14,15,16] and j in [1] or i in [14,15,16] and j in [2] or i in [15,16] and j in [3] or i in [16] and j in [4]:
                pygame.draw.rect(screen, bleu_acier, (10 + i * 100, 150 + j * 80, 60, 60))
            elif i in [0] and j in [1,2,3,4,5,6]:
                pygame.draw.rect(screen, bleu_nuit, (10 + i * 100, 150 + j * 80, 60, 60))
            elif i in [1] and j in [1,2,3,4,5,6] or i in [17] and j in [0,1,2,3,4,5]:
                pygame.draw.rect(screen, bourgogne, (10 + i * 100, 150 + j * 80, 60, 60))
            elif i in [2,3,4,5,6,7,8,9,10,11] and j in [3,4] or  i in [3,4,5,6,7,8,9,10,11] and j in [5] or  i in [3,4,5,6,7] and j in [6]:
                pygame.draw.rect(screen, purple, (10 + i * 100, 150 + j * 80, 60, 60))
            elif i in [2] and j in [5]:
                pygame.draw.rect(screen, bleu_cobalt, (10 + i * 100, 150 + j * 80, 60, 60))
            elif i in [7,8,9,10,11,12,13,14,15,16,17] and j in [6]:
                pygame.draw.rect(screen, gris_ardois, (10 + i * 100, 150 + j * 80, 60, 60))
            elif i in [12] and j in [2,3,4,5] or i in [13] and j in [4,5] or i in [13,14,15,16] and j in [5]:
                pygame.draw.rect(screen, dark_green, (10 + i * 100, 150 + j * 80, 60, 60))
            else:
                pygame.draw.rect(screen, marron_rougeatre, (10 + i * 100, 150 + j * 80, 60, 60))

            if (i, j) in element_chimiques:
                elm_chimique = element_chimiques[(i, j)][0]
            else:
                elm_chimique = ""

            text_surface = font.render(elm_chimique, True, (255, 255, 255))

            text_rect = text_surface.get_rect()
            text_rect.center = (10 + i * 100 + 30, 150 + j * 80 + 30)

            screen.blit(text_surface, text_rect)


def non_reactif(check_states):
    for i in range(18):
        for j in range(9):
            if (i,j) in non_reactifs:
                if not check_states:
                    pygame.draw.rect(screen, black, (10 + i * 100, 150 + j * 80, 60, 60))

def metaux_alcalins(check_states):
    for i in range(18):
        for j in range(9):
            if (i,j) in metaux_alcalin:
                if not check_states:
                    pygame.draw.rect(screen, black, (10 + i * 100, 150 + j * 80, 60, 60))

def metaux_alcalinos(check_states):
    for i in range(18):
        for j in range(9):
            if (i,j) in metaux_alcalino:
                if not check_states:
                    pygame.draw.rect(screen, black, (10 + i * 100, 150 + j * 80, 60, 60))

def meteaux_de_transitions(check_states):
    for i in range(18):
        for j in range(9):
            if (i,j) in meteaux_de_transition:
                if not check_states:
                    pygame.draw.rect(screen, black, (10 + i * 100, 150 + j * 80, 60, 60))

def metaloides(check_states):
    for i in range(18):
        for j in range(9):
            if (i,j) in metaloide:
                if not check_states:
                    pygame.draw.rect(screen, black, (10 + i * 100, 150 + j * 80, 60, 60))


def meteaux_post_transitions(check_states):
    for i in range(18):
        for j in range(9):
            if (i,j) in meteaux_post_transition:
                if not check_states:
                    pygame.draw.rect(screen, black, (10 + i * 100, 150 + j * 80, 60, 60))

def propriete_inconnues(check_states):
    for i in range(18):
        for j in range(9):
            if (i,j) in propriete_inconnue:
                if not check_states:
                    pygame.draw.rect(screen, black, (10 + i * 100, 150 + j * 80, 60, 60))

def lanthanides(check_states):
    for i in range(18):
        for j in range(9):
            if (i,j) in lanthanide:
                if not check_states:
                    pygame.draw.rect(screen, black, (10 + i * 100, 150 + j * 80, 60, 60))

def actinides(check_states):
    for i in range(18):
        for j in range(9):
            if (i,j) in actinide:
                if not check_states:
                    pygame.draw.rect(screen, black, (10 + i * 100, 150 + j * 80, 60, 60))

def gaz_nobles(check_states):
    for i in range(18):
        for j in range(9):
            if (i,j) in gaz_noble:
                if not check_states:
                    pygame.draw.rect(screen, black, (10 + i * 100, 150 + j * 80, 60, 60))



checked_pos = [(50, 900), (50, 930), (300, 900),
               (300, 930),(600,900),(600,930),(900,900),
               (900,930), (1200,900),(1200,930)]
check_states = [True, True, True, True,True, True, True, True, True, True]
textes = ["non_reactifs", "metaux_alcalins", "metaux_alcalino","meteaux_de_transition", "metaloides", "meteaux_post_transition",
          "propriete_inconnues", "lanthanides", "actinides", "gaz_nobles"]

def coordonnees(souris_pos):
    x,y = souris_pos
    i = (x - 10) // 100
    j = (y - 150) // 80
    return int(i), int(j)

def informations_sup(souris_pos, dic):
    (i,j) = coordonnees(souris_pos)
    cle = (i,j)
    if cle in dic:
        value = dic[cle]
        return True
    else:
        return False

def affiche_rect():
    pygame.draw.rect(screen,white,(250,160,600,200))
    pygame.draw.rect(screen,black, (260,170,580,180))


def dessine_checkbox(checked_pos, check_states):
    for i in range(len(checked_pos)):
        (x,y) = checked_pos[i]
        pygame.draw.rect(screen, (0,255,0),(x,y,20,20))

        if check_states[i]:
            pygame.draw.rect(screen, (0,255,0),(x,y,20,20))
        else:
            pygame.draw.rect(screen, (255,0,0),(x,y,20,20))


        font = pygame.font.Font(None, 24)


        text = font.render(textes[i], True, white)

        screen.blit(text, (x + 20 + 10, y))

def affiche_masque_element(check_states):
    if not check_states[0]:
        non_reactif(False)
    if not check_states[1]:
        metaux_alcalins(False)
    if not check_states[2]:
        metaux_alcalinos(False)
    if not check_states[3]:
        meteaux_de_transitions(False)
    if not check_states[4]:
        metaloides(False)
    if not check_states[5]:
        meteaux_post_transitions(False)
    if not check_states[6]:
        propriete_inconnues(False)
    if not check_states[7]:
        lanthanides(False)
    if not check_states[8]:
        actinides(False)
    if not check_states[9]:
        gaz_nobles(False)



def dessine_search_bar():
    pygame.draw.rect(screen, search_color, search_rect)

    text_surface = search_font.render(search_text, True, (255, 255, 255))
    screen.blit(text_surface, (search_rect.x+5, search_rect.y+5))
    search_rect.w = max(100, text_surface.get_width()+10)


def recherche_text(texte):
    for coords, details in element_chimiques.items():
        if texte.lower() in [info.lower() for info in details]:
            print("oui")
            return True
    return None

def recherche_elm():
    pygame.draw.rect(screen, black, (10 + i * 100, 150 + j * 80, 60, 60))


screen.fill(black)
dessine_tableau()
dessine_checkbox(checked_pos, check_states)
affiche_masque_element(check_states)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            for i in range(len(checked_pos)):
                (check_x, check_y) = checked_pos[i]
                if check_x <= x <= check_x + 20 and check_y <= y <= check_y + 20:
                    check_states[i] = not check_states[i]
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                souris_pos = pygame.mouse.get_pos()
                if informations_sup(souris_pos,element_chimiques) == True:
                    affiche_rect()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if search_rect.collidepoint(event.pos):
                search_active = True
            else:
                search_active = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if not recherche_text(search_text):
                    recherche_elm()
            if event.key == pygame.K_BACKSPACE:
                search_text = search_text[:-1]
            else:
                search_text += event.unicode


    #Proprieter Tableau
    dessine_search_bar()

    #affiche_rect()
    pygame.display.update()

pygame.quit()
exit()

