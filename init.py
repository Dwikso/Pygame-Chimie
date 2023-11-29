import pygame
from sys import exit

pygame.init()
width = 1900
height = 1000
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Tableau Périodique')
font_element = pygame.font.Font(None, 36)
font_poids = pygame.font.Font(None, 16)

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
    (15,7): "Yb", (16,7) : "Lu", (2, 7): "La"
}

actinide = {
    (2,8) : "Ac",(3,8) : "Th", (4,8) : "Pa" , (5,8) : "U" ,
    (6,8) : "Np", (7,8) : "Pu" , (8,8) : "Am" , (9,8) : "Cm" , (10,8) : "Bk",
    (11,8) : "Cf", (12,8) : "Es" , (13,8) : "Fm" , (14,8) : "Md", (15,8): "No", (16,8) : "Lr"
}

gaz_noble = {
    (17,0) : "He", (17,1) : "Ne", (17,2) : "Ar", (17,3) : "Kr",
    (17,4) : "Xe", (17,5) : "Rn"
}

element_chimiques = {
    (0, 0): ["H", "1", "Hydrogène", "1.0078", "1s1"],
    (17, 0): ["He", "2", "Hélium", "4.0026", "1s2"],
    (0, 1): ["Li", "3", "Lithium", "6.941", "[He] 2s1"],
    (1, 1): ["Be", "4", "Béryllium", "9.0122", "[He] 2s1"],
    (12, 1): ["B", "5", "Bore", "10.81", "[He] 2s2 2p1"],
    (13, 1): ["C", "6", "Carbone", "12.011", "[He] 2s2 2p2"],
    (14, 1): ["N", "7", "Azote", "14.007", "[He] 2s2 2p3"],
    (15, 1): ["O", "8", "Oxygène", "15.999", "[He] 2s2 2p4"],
    (16, 1): ["F", "9", "Fluor", "18.998", "[He] 2s2 2p5"],
    (17, 1): ["Ne", "10", "Néon", "20.180", "[He] 2s2 2p6"],
    (0, 2): ["Na", "11", "Sodium", "22.990", "[Ne] 3s1"],
    (1, 2): ["Mg", "12", "Magnésium", "24.305", "[Ne] 3s2"],
    (12, 2): ["Al", "13", "Aluminium", "26.982", "[Ne] 3s2 3p1"],
    (13, 2): ["Si", "14", "Silicium", "28.085", "[Ne] 3s2 3p2"],
    (14, 2): ["P", "15", "Phosphore", "30.974", "[Ne] 3s2 3p3"],
    (15, 2): ["S", "16", "Soufre", "32.06", "[Ne] 3s2 3p4"],
    (16, 2): ["Cl", "17", "Chlore", "35.45", "[Ne] 3s2 3p5"],
    (17, 2): ["Ar", "18", "Argon", "39.948", "[Ne] 3s2 3p6"],
    (0, 3): ["K", "19", "Potassium", "39.098", "[Ar] 4s1"],
    (1, 3): ["Ca", "20", "Calcium", "40.078", "[Ar] 4s2"],
    (2, 3): ["Sc", "21", "Scandium", "44.956", "[Ar] 3d1 4s2"],
    (3, 3): ["Ti", "22", "Titane", "47.867", "[Ar] 3d2 4s2"],
    (4, 3): ["V", "23", "Vanadium", "50.942", "[Ar] 3d3 4s2"],
    (5, 3): ["Cr", "24", "Chrome", "51.996", "[Ar] 3d4 4s2"],
    (6, 3): ["Mn", "25", "Manganèse", "54.938", "[Ar] 3d5 4s2"],
    (7, 3): ["Fe", "26", "Fer", "55.845", "[Ar] 3d6 4s2"],
    (8, 3): ["Co", "27", "Cobalt", "58.933", "[Ar] 3d7 4s2"],
    (9, 3): ["Ni", "28", "Nickel", "58.693", "[Ar] 3d8 4s2"],
    (10, 3): ["Cu", "29", "Cuivre", "63.546", "[Ar] 3d9 4s2"],
    (11, 3): ["Zn", "30", "Zinc", "65.38", "[Ar] 3d10 4s2"],
    (12, 3): ["Ga", "31", "Gallium", "69.723", "[Ar] 3d10 4s2 4p1"],
    (13, 3): ["Ge", "32", "Germanium", "72.630", "[Ar] 3d10 4s2 4p2"],
    (14, 3): ["As", "33", "Arsenic", "74.922", "[Ar] 3d10 4s2 4p3"],
    (15, 3): ["Se", "34", "Sélénium", "78.971", "[Ar] 3d10 4s2 4p4"],
    (16, 3): ["Br", "35", "Brome", "79.904", "[Ar] 3d10 4s2 4p5"],
    (17, 3): ["Kr", "36", "Krypton", "83.798", "[Ar] 3d10 4s2 4p6"],
    (0, 4): ["Rb", "37", "Rubidium", "85.468", "[Kr] 5s1"],
    (1, 4): ["Sr", "38", "Strontium", "87.62", "[Kr] 5s2"],
    (2, 4): ["Y", "39", "Yttrium", "88.906", "[Kr] 4d1 5s2"],
    (3, 4): ["Zr", "40", "Zirconium", "91.224", "[Kr] 4d2 5s2"],
    (4, 4): ["Nb", "41", "Niobium", "92.906", "[Kr] 4d3 5s2"],
    (5, 4): ["Mo", "42", "Molybdène", "95.95", "[Kr] 4d4 5s2"],
    (6, 4): ["Tc", "43", "Technétium", "98", "[Kr] 4d5 5s2"],
    (7, 4): ["Ru", "44", "Ruthénium", "101.07", "[Kr] 4d6 5s2"],
    (8, 4): ["Rh", "45", "Rhodium", "102.91", "[Kr] 4d7 5s2"],
    (9, 4): ["Pd", "46", "Palladium", "106.42", "[Kr] 4d8 5s2"],
    (10, 4): ["Ag", "47", "Argent", "107.87", "[Kr] 4d9 5s2"],
    (11, 4): ["Cd", "48", "Cadmium", "112.41", "[Kr] 4d10 5s2"],
    (12, 4): ["In", "49", "Indium", "114.82", "[Kr] 4d10 5s2 5p1"],
    (13, 4): ["Sn", "50", "Étain", "118.71", "[Kr] 4d10 5s2 5p2"],
    (14, 4): ["Sb", "51", "Antimoine", "121.76", "[Kr] 4d10 5s2 5p3"],
    (15, 4): ["Te", "52", "Tellure", "127.60", "[Kr] 4d10 5s2 5p4"],
    (16, 4): ["I", "53", "Iode", "126.90", "[Kr] 4d10 5s2 5p5"],
    (17, 4): ["Xe", "54", "Xénon", "131.29", "[Kr] 4d10 5s2 5p6"],
    (0, 5): ["Cs", "55", "Césium", "132.91", "[Xe] 6s1"],
    (1, 5): ["Ba", "56", "Baryum", "137.33", "[Xe] 6s2"],
    (2, 7): ["La", "57", "Lanthane", "138.91", "[Xe] 5d1 6s2"],
    (3, 5): ["Hf", "72", "Hafnium", "178.49", "[Xe] 4f14 5d2 6s2"],
    (4, 5): ["Ta", "73", "Tantale", "180.95", "[Xe] 4f14 5d3 6s2"],
    (5, 5): ["W", "74", "Tungstène", "183.84", "[Xe] 4f14 5d4 6s2"],
    (6, 5): ["Re", "75", "Rhénium", "186.21", "[Xe] 4f14 5d5 6s2"],
    (7, 5): ["Os", "76", "Osmium", "190.23", "[Xe] 4f14 5d6 6s2"],
    (8, 5): ["Ir", "77", "Iridium", "192.22", "[Xe] 4f14 5d7 6s2"],
    (9, 5): ["Pt", "78", "Platine", "195.08", "[Xe] 4f14 5d9 6s1"],
    (10, 5): ["Au", "79", "Or", "196.97", "[Xe] 4f14 5d10 6s1"],
    (11, 5): ["Hg", "80", "Mercure", "200.59", "[Xe] 4f14 5d10 6s2"],
    (12, 5): ["Ti", "81", "Thallium", "204.38", "[Xe] 4f14 5d10 6s2 6p1"],
    (13, 5): ["Pb", "82", "Plomb", "207.2", "[Xe] 4f14 5d10 6s2 6p2"],
    (14, 5): ["Bi", "83", "Bismuth", "208.98", "[Xe] 4f14 5d10 6s2 6p3"],
    (15, 5): ["Po", "84", "Polonium", "209", "[Xe] 4f14 5d10 6s2 6p4"],
    (16, 5): ["At", "85", "Astate", "210", "[Xe] 4f14 5d10 6s2 6p5"],
    (17, 5): ["Rn", "86", "Radon", "222", "[Xe] 4f14 5d10 6s2 6p⁶6"],
    (0, 6): ["Fr", "87", "Francium", "223", "[Rn] 7s1"],
    (1, 6): ["Ra", "88", "Radium", "226", "[Rn] 7s2"],
    (2, 8): ["Ac", "89", "Actinium", "227", "[Rn] 6d1 7s2"],
    (3, 6): ["Rf", "104", "Rutherfordium", "267", "[Rn] 5f14 6d2 7s2"],
    (4, 6): ["Db", "105", "Dubnium", "270", "[Rn] 5f14 6d3 7s2"],
    (5, 6): ["Sg", "106", "Seaborgium", "271", "[Rn] 5f14 6d4 7s2"],
    (6, 6): ["Bh", "107", "Bohrium", "270", "[Rn] 5f14 6d5 7s2"],
    (7, 6): ["Hs", "108", "Hassium", "277", "[Rn] 5f14 6d6 7s2"],
    (8, 6): ["Mt", "109", "Meitnerium", "276", "[Rn] 5f14 6d7 7s2"],
    (9, 6): ["Ds", "110", "Darmstadtium", "281", "[Rn] 5f14 6d8 7s2"],
    (10, 6): ["Rg", "111", "Roentgenium", "280", "[Rn] 5f14 6d10 7s1"],
    (11, 6): ["Cn", "112", "Copernicium", "285", "[Rn] 5f14 6d10 7s2"],
    (12, 6): ["Nh", "113", "Nihonium", "284", "[Rn] 5f14 6d10 7s2 7p1"],
    (13, 6): ["Fl", "114", "Flerovium", "289", "[Rn] 5f14 6d10 7s2 7p2"],
    (14, 6): ["Mc", "115", "Moscovium", "288", "[Rn] 5f14 6d10 7s2 7p3"],
    (15, 6): ["Lv", "116", "Livermorium", "293", "[Rn] 5f14 6d10 7s2 7p4"],
    (16, 6): ["Ts", "117", "Tennessine", "294", "[Rn] 5f14 6d10 7s2 7p5"],
    (17, 6): ["Og", "118", "Oganesson", "294", "[Rn] 5f14 6d10 7s2 7p⁶"],
    (3, 7): ["Ce", "58", "Cérium", "140.12", "[Xe] 4f1 5d1 6s2"],
    (4, 7): ["Pr", "59", "Praséodyme", "140.91", "[Xe] 4f3 6s2"],
    (5, 7): ["Nd", "60", "Néodyme", "144.24", "[Xe] 4f4 6s2"],
    (6, 7): ["Pm", "61", "Prométhium", "145", "[Xe] 4f5 6s2"],
    (7, 7): ["Sm", "62", "Samarium", "150.36", "[Xe] 4f6 6s2"],
    (8, 7): ["Eu", "63", "Europium", "151.96", "[Xe] 4f7 6s2"],
    (9, 7): ["Gd", "64", "Gadolinium", "157.25", "[Xe] 4f7 5d1 6s2"],
    (10, 7): ["Tb", "65", "Terbium", "158.93", "[Xe] 4f9 6s2"],
    (11, 7): ["Dy", "66", "Dysprosium", "162.50", "[Xe] 4f10 6s2"],
    (12, 7): ["Ho", "67", "Holmium", "164.93", "[Xe] 4f14 6s2"],
    (13, 7): ["Er", "68", "Erbium", "167.26", "[Xe] 4f12 6s2"],
    (14, 7): ["Tm", "69", "Thulium", "168.93", "[Xe] 4f13 6s2"],
    (15, 7): ["Yb", "70", "Ytterbium", "173.04", "[Xe] 4f14 6s2"],
    (16, 7): ["Lu", "71", "Lutécium", "174.97", "[Xe] 4f14 5d1 6s2"],
    (3, 8): ["Th", "90", "Thorium", "232.04", "[Rn] 6d2 7s2"],
    (4, 8): ["Pa", "91", "Protactinium", "231.04", "[Rn] 5f2 6d1 7s2"],
    (5, 8): ["U", "92", "Uranium", "238.03", "[Rn] 5f3 6d1 7s2"],
    (6, 8): ["Np", "93", "Neptunium", "237", "[Rn] 5f4 6d1 7s2"],
    (7, 8): ["Pu", "94", "Plutonium", "244", "[Rn] 5f5 6d1 7s2"],
    (8, 8): ["Am", "95", "Américium", "243", "[Rn] 5f6 6d1 7s2"],
    (9, 8): ["Cm", "96", "Curium", "247", "[Rn] 5f7 6d1 7s2"],
    (10, 8): ["Bk", "97", "Berkélium", "247", "[Rn] 5f9 6d1 7s2"],
    (11, 8): ["Cf", "98", "Californium", "251", "[Rn] 5f10 6d1 7s2"],
    (12, 8): ["Es", "99", "Einsteinium", "252", "[Rn] 5f11 6d1 7s2"],
    (13, 8): ["Fm", "100", "Fermium", "257", "[Rn] 5f12 6d1 7s2"],
    (14, 8): ["Md", "101", "Mendélévium", "258", "[Rn] 5f12 6d1 7s1"],
    (15, 8): ["No", "102", "Nobélium", "259", "[Rn] 5f14 6d1 7s2"],
    (16, 8): ["Lr", "103", "Lawrencium", "262", "[Rn] 5f14 6d1 7s2 7p1"],
}




def dessine_tableau():
    for i in range(18):
        for j in range(9):
            #if i in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16] and j in [0]:
            #pygame.draw.rect(screen, black,(10 + i * 100, 150 + j * 80, 60, 60))
            if i in [0] and j in [0] or i in [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16] and j in [7] :
                pygame.draw.rect(screen, bleu_cobalt, (10 + i * 100, 150 + j * 80, 60, 60))
            #elif i in [2,3,4,5,6,7,8,9,10,11] and j in [0,1,2] or i in [0,1,17] and j in [7,8]:
            #pygame.draw.rect(screen, black, (10 + i * 100, 150 + j * 80, 60, 60))
            elif i in [13,14,15,16] and j in [1] or i in [14,15,16] and j in [2] or i in [15,16] and j in [3] or i in [16] and j in [4]:
                pygame.draw.rect(screen, bleu_acier, (10 + i * 100, 150 + j * 80, 60, 60))
            elif i in [0] and j in [1,2,3,4,5,6]:
                pygame.draw.rect(screen, bleu_nuit, (10 + i * 100, 150 + j * 80, 60, 60))
            elif i in [1] and j in [1,2,3,4,5,6] or i in [17] and j in [0,1,2,3,4,5]:
                pygame.draw.rect(screen, bourgogne, (10 + i * 100, 150 + j * 80, 60, 60))
            elif i in [2,3,4,5,6,7,8,9,10,11] and j in [3,4] or  i in [3,4,5,6,7,8,9,10,11] and j in [5] or  i in [3,4,5,6,7] and j in [6]:
                pygame.draw.rect(screen, purple, (10 + i * 100, 150 + j * 80, 60, 60))
            #elif i in [2] and j in [5,6]:
            #pygame.draw.rect(screen, black, (10 + i * 100, 150 + j * 80, 60, 60))
            elif i in [7,8,9,10,11,12,13,14,15,16,17] and j in [6]:
                pygame.draw.rect(screen, gris_ardois, (10 + i * 100, 150 + j * 80, 60, 60))
            elif i in [12] and j in [2,3,4,5] or i in [13] and j in [4,5] or i in [13,14,15,16] and j in [5]:
                pygame.draw.rect(screen, dark_green, (10 + i * 100, 150 + j * 80, 60, 60))
            elif i in [12] and j in [1] or i in [13] and j in [2] or i in [13,14] and j in [3] or i in [14,15] and j in [4]:
                pygame.draw.rect(screen, marron_cafe, (10 + i * 100, 150 + j * 80, 60, 60))
            elif i in [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16] and j in [8] :
                pygame.draw.rect(screen, marron_rougeatre, (10 + i * 100, 150 + j * 80, 60, 60))



            #Afiche la lettre
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


def coordonnees(souris_pos):
    x,y = souris_pos
    i = (x - 10) // 100
    j = (y - 150) // 80
    return int(i), int(j)

def informations_sup(souris_pos, dic):
    (i, j) = coordonnees(souris_pos)
    cle = (i, j)
    if cle in dic:
        value = dic[cle]
        return value
    else:
        return None


def affiche_rect(infos):
    if infos is not None:
        pygame.draw.rect(screen, white, (250, 160, 600, 200))
        pygame.draw.rect(screen, black, (260, 170, 580, 180))


        font = pygame.font.Font(None, 36)
        y = 190

        for info in infos:
            text_surface = font.render(info, True, white)
            text_rect = text_surface.get_rect()
            text_rect.center = (550, y)
            screen.blit(text_surface, text_rect)
            y += 30 #Evite que le texte soit sur la meme ligne


def dessine_search_bar():
    pygame.draw.rect(screen, search_color, search_rect)

    text_surface = search_font.render(search_text, True, black)
    screen.blit(text_surface, (search_rect.x+5, search_rect.y+5))
    search_rect.w = max(100, text_surface.get_width()+10)
    active = False

def recherche_elm(texte):
    resultats_recherche = []


    for coords, details in element_chimiques.items():
        if texte.lower() in [info.lower() for info in details]:
            resultats_recherche.append(coords)

    for coords, details in element_chimiques.items():
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




screen.fill(black)
dessine_tableau()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEMOTION:
            souris_pos = pygame.mouse.get_pos()
            infos = informations_sup(souris_pos, element_chimiques)
            coords = ((souris_pos[0] - 10) // 100, (souris_pos[1] - 150) // 80)
            if infos and screen.get_at((10 + coords[0] * 100 + 30, 150 + coords[1] * 80 + 30)) != black:
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
                elif pygame.K_a <= event.key <= pygame.K_z or pygame.K_0 <= event.key <= pygame.K_9:
                    search_text += event.unicode


    #Proprieter Tableau
    dessine_search_bar()

    #affiche_rect()
    pygame.display.update()



pygame.quit()
exit()