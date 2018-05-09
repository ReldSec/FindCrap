 /$$$$$$$$ /$$                 /$$  /$$$$$$                              
| $$_____/|__/                | $$ /$$__  $$                             
| $$       /$$ /$$$$$$$   /$$$$$$$| $$  \__/  /$$$$$$  /$$$$$$   /$$$$$$ 
| $$$$$   | $$| $$__  $$ /$$__  $$| $$       /$$__  $$|____  $$ /$$__  $$
| $$__/   | $$| $$  \ $$| $$  | $$| $$      | $$  \__/ /$$$$$$$| $$  \ $$
| $$      | $$| $$  | $$| $$  | $$| $$    $$| $$      /$$__  $$| $$  | $$
| $$      | $$| $$  | $$|  $$$$$$$|  $$$$$$/| $$     |  $$$$$$$| $$$$$$$/
|__/      |__/|__/  |__/ \_______/ \______/ |__/      \_______/| $$____/ 
                                                               | $$      
                                                               | $$      
                                                               |__/      

==========================================================================
La herramienta fue creada para el descubrimiento de directorios sensibles en aplicaciones web así como la localización de paneles de administración
Es multiplataforma por lo que puede ejecutarse en Windows, Android y desde luego, Linux
==========================================================================
The tool was created for the discovery of sensitive directories in web applications as well as the location of administration panels
It is cross-platform so it can run on Windows, Android and of course, Linux
==========================================================================

			    Instalación

==========================================================================

Android, Termux:
		apt install git
		git clone https://github.com/ReldSec/FindCrap
		cd FindCrap
		pkg update
		apt install python2 python-dev
		pip2 install -r requirements.txt
		pip2 install colorama random
		
		python2 FindCrap.py -h

Linux, Windows:
	       git clone https://github.com/ReldSec/FindCrap
	       cd FindCrap
	       pip install -r requirements.txt
	       python FindCrap.py -h
