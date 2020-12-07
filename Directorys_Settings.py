# # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 													  #
# 				    Proyecto R.U.N					  #
# 													  #
#	   Proyecto Final Pogramacion de Computadores     #
#													  #
#	   Universidad Nacional de Colombia - 2020 II     #
#	       Docente: Juan Diego Escobar Mejia          #
#	                      						      #
# 			       Lenguaje:  Python		     	  #
#	                      						      #
#	                 Programadores:   			      #
# 													  #
#	 Mauricio Rodriguez Becerra  - Ing. Mecatronica   #
#	 Laura Alejandra Paez Daza   - Ing. Mecatronica   #
#	 Juan Esteban Flechas Rincon - Ing. Electronica   #
#	 Alejandro Mendivelso Torres - Ing. Mecatronica   #
#												      #
# # # # # # # # # # # # # # # # # # # # # # # # # # # #

# OS [ https://docs.python.org/3/library/os.html ]
# Pygame [ https://www.pygame.org/docs/ ]

from os.path import join, dirname                           # Importamos las funciones que usaremos del paquete [ os ] módulo [ path ]
from pygame.mixer import Sound, music, init                 # Importamos las funciones y clases que usaremos del paquete [ pygame ] módulo [ mixer ]
from pygame.display import set_caption, set_icon, set_mode  # Importamos las funciones que usaremos del paquete [ pygame ] módulo [ display ]
from pygame.time import Clock                               # Importamos las clases que usaremos del paquete [ pygame ] módulo [ time]
from pygame.image import load                               # Importamos las funciones que usaremos del paquete [ pygame ] módulo [ image ]
from pygame.transform import scale

# -----------------------------------------  Creación de directorios -----------------------------------------------

game_folder = dirname(__file__)                   # con ayuda de dirname() obtenemos la ruta del archivo [ Directorys_Settings ] que en este caso se usara como ruta, de la carpeta raiz del juego
images_folder = join(game_folder,'Pixel_Art')     # Join() nos permite hacer una union entre la ruta de carpeta indicada ( en este caso la carpeta raiz ) y el nombre con la nueva carpeta, creando una nueva ruta
sounds_folder = join(game_folder,'Sounds')        # Creamos la ruta para la carpeta de sonidos
menu_subfolder = join(images_folder,'Menu')       # Creamos la ruta para la carpeta del menu
f_backgrounds = join(images_folder,'Backgrounds') # Creamos la ruta para la subcarpeta de fondos
f_vfx = join(images_folder,'VFX')                 # Creamos la ruta para la subcarpeta de efectos visuales
f_enemies = join(images_folder,'Enemies')         # Creamos la ruta para la subcarpeta de enemigos
f_items = join(images_folder,'Items')             # Creamos la ruta para la subcarpeta de items
f_vehicles = join(images_folder,'Vehicles')       # Creamos la ruta para la subcarpeta de vehiculos
f_music = join(sounds_folder,'Music')             # Creamos la ruta para la subcarpeta de musica
f_sfx = join(sounds_folder,'SFX')                 # Creamos la ruta para la subcarpeta de efectos de sonido
f_pause = join(menu_subfolder,'Pause')            # Creamos la ruta para la subcarpeta la animacion pausa
f_gameover = join(menu_subfolder,'Game_Over')     # Creamos la ruta para la subcarpeta la animacion game over
f_coin = join(menu_subfolder,'Insert_Coin')       # Creamos la ruta para la subcarpeta de la animacion insert coin
f_load = join(menu_subfolder,'Load_Game')  
f_htp = join(menu_subfolder,'How_To_Play')  
f_hs = join(menu_subfolder,'High_Score')  
f_credits = join(menu_subfolder,'Credits')  
f_vselect = join(menu_subfolder,'Vehicle_Select')  

# ----------------------------------------- Creacion de Pantalla / Reloj / FPS / Icono y Titulo --------------------

CLOCK = Clock()                                                 # Creamos un objeto de la clase Clock() que nos ayuda del metodo tick() nos da la posibilidad de controlar las actualizaciones de pantalla por segundo
FPS = 60                                                        # Establecemos el valor de imagenes por segundo usaremos para la actualizacion de pantalla, con ayuda del CLOCK
W,H = 1000,1000                                                 # Establecemos 2 variables, una para el ancho ( Width ) y otra para el alto ( Height )
SCREEN = set_mode((W,H))                                        # set_mode() inicializa una ventana del tamaño asignado por nosotros
set_caption('Racing UN')                                        # set_caption() establece un titulo en la ventana
set_icon(load(join(images_folder,'icon.png')).convert_alpha())  # set_icon() cambia la imagen del sistema, en la ventana, por la imagen que le asignemos

# ----------------------------------------- Creacion de imagenes estaticas ----------------------------------------- 

img_cursor = scale(load(join(menu_subfolder,'Cursor.png')).convert_alpha(),(50,47))  # scale() nos ayuda a trasformar las dimensiones de una imagen, ingresamos el archivo y el nuevo tamaño en (x,y)
background_go = load(join(f_backgrounds,'Game_Over.png')).convert_alpha()            # load() crear un objeto tipo Surface() con las mismas caracteristicas del archivo que indicamos como entrada
background_menu = load(join(f_backgrounds,'Menu.png')).convert_alpha()               # nos pide ingresar la ruta y el nombre de la imagen, junto al tipo de formato ( en este caso .PNG )
background_car = load(join(f_backgrounds,'Vehicle_Select.png')).convert_alpha()      # el metodo convert() y conver_alpha() convierte la imagen a un formato interno adecuado para blitting
background_load = load(join(f_backgrounds,'Loading.png')).convert_alpha()            # usamos conver_alpha() para que la superficie respete la trasnparencia, ya que si usamos unicamente el metodo convert
background_h_s = load(join(f_backgrounds,'High_Score.png')).convert_alpha()          # los pixeles alpha seran trasnformados en color negro, lo cual en este caso no nos coviene
background_ht_play = load(join(f_backgrounds,'How_To_Play.png')).convert_alpha()     # podemos expresar la ruta mediante un string, en este caso las variables que usamos para los directorios         
game_map1_1 = load(join(f_backgrounds,'Game_Map1_1.png')).convert_alpha()            # lo que contienen es un string con la ruta, asi que para no tener que escribirla manualmente cada vez que
game_map1_2 = load(join(f_backgrounds,'Game_Map1_2.png')).convert_alpha()            # deseemos cargar una imagen, gracias a la funcion join() le indicamos que agrege la ruta de la carpeta indicada
arcade_menu = load(join(f_backgrounds,'Arcade_Menu.png')).convert_alpha()            # antes del nombre de la imagen, para que el metodo load() reciba como imagen, la ubicacion del archivo, con su
arcade_game = load(join(f_backgrounds,'Arcade_In_Game.png')).convert_alpha()         # ruta - nombre - formato y adicional la instruccion de convertir ese archivo asi que finalmente la variable lo que
arcade_pause = load(join(f_backgrounds,'Arcade_pause.png')).convert_alpha()          # nos guarda es un objeto de tipo Surface, optimizado para blitting lo cual nos ayuda a ganar rendimiento
arcade_game_over = load(join(f_backgrounds,'Arcade_Game_Over.png')).convert_alpha()  # ya que si dejamos las imagenes tal cual, seran mas complicadas de procesar ya que se tendria que hacer, pixel a pixel
arcade_lose = load(join(f_backgrounds,'Arcade_Lose.png')).convert_alpha()            # lo que repercutiria negativamente en la ejecicion, causando que si son muchas imagenes, el juego se ponga lento      
img_pause = load(join(f_pause,'Image_pause.png')).convert_alpha()
img_load = load(join(f_load,'loading.png')).convert_alpha()           
img_crash = load(join(f_gameover,'Crash.png')).convert_alpha()                       
img_busted = load(join(f_gameover,'Busted.png')).convert_alpha()                     
img_go_1 = load(join(f_gameover,'Your_Busted.png')).convert_alpha()                  
img_go_0 = load(join(f_gameover,'Your_Crash.png')).convert_alpha()                   
img_low_fuel = load(join(f_items,'Low_Fuel.png')).convert_alpha()   
img_cars = load(join(f_vselect,'Select_Car.png')).convert_alpha()
img_credits = load(join(f_credits,'Credits_Image.png')).convert_alpha()
img_htp = load(join(f_htp,'How_To_Play.png')).convert_alpha()     
img_hs = load(join(f_hs,'Best_Scores.png')).convert_alpha() 

# ----------------------------------------- Creacion de efectos de sonidos ----------------------------------------- 

init()                                                   # inicializa el modulo mezclador de pygame, para cargar y reproducir sonidos
sfx_crash = Sound(join(f_sfx,'Crash.ogg'))               # la clase Sound() crear un nuevo objeto Sound a partir de un archivo u objeto de búfer
sfx_busted = Sound(join(f_sfx,'Busted.ogg'))             # la clase internamente realiza un remuestreo para hacer que el sonido coincidir con los argumentos inciiales del mixer()
sfx_low_fuel = Sound(join(f_sfx,'Low_Gasoline.ogg'))     # El sonido se puede cargar desde un archivo de audio o desde un archivo sin comprimir ( .OGG / . WAV )
sfx_button_click = Sound(join(f_sfx,'Button_Click.ogg')) # es importante que indiquemos el formato ( .MP3 / etc. ) de lo contrario la clase podria conunfir la entrada
sfx_blood_porky = Sound(join(f_sfx,'Duque.ogg'))         # y tomarla no como un archivo de sonido, sino como otros parametros de entrada que soporta la clase
sfx_blood_oldwoman = Sound(join(f_sfx,'Gloria.ogg'))     # como otro objeto de python o un objeto de bufer, que al no corresponder con los datos esperados 
sfx_blood_tombos = Sound(join(f_sfx,'Tombos.ogg'))       # nos genera un error
sfx_perseo = Sound(join(f_sfx,'Perseo.ogg'))   
sfx_powerup = Sound(join(f_sfx,'Fuel_PowerUp.ogg'))
# ----------------------------------------- Verificacion Variables ------------------------------------------------- 

# PODEMOS VERIFICAR LO QUE ALMACENA CADA VARIABLE ( borrar el # del print ) PODEMOS CAMBIAR LA VARIABLE DENTRO DEL PRINT PARA VER QUE CONTIENE
#print(game_folder)    # en este caso nos retorna un string con la ruta que tiene guardada
#print(f_backgrounds)  # en este caso nos retorna un string con la ruta que creamos con join(), al sumar a la carpeta raiz la nueva direccion y nombre de la carpeta
#print(background_go)  # en este caso nos retorna un objeto de tipo surface y su tamaño ( que corresponde a las dimensiones del archivo que se le cargo )
#print(sfx_crash)      # en este caso nos retorna un objeto de tipo Sound y nos dice la posicion de memoria donde se almaceno