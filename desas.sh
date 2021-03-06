#!/bin/bash

cels=/opt/desas
ver="v2.4"

if [[ -f /usr/bin/apt-get ]]; then
	os="Debian"
elif [[ -f /usr/bin/yum ]]; then
	os="Red Hat"
else
	if [[ -f /usr/bin/pacman ]]; then
		os="Arch Linux"
	else
		os="nezināma"
	fi
fi

if [[ "$os" == "nezināma" ]]; then
	echo "Atvainojiet, jūsu izmantotā sitēma pašlaik netiek atbalstīta, sazinieties ar skripta izstrādātāju!"
	zenity --error --title="Neatbalstīta sistēma" --text="<b><span color=\"red\">Atvainojiet, jūsu izmantotā sitēma pašlaik netiek atbalstīta, sazinieties ar skripta izstrādātāju!</span></b>"
	exit 1
fi

case $1 in
	"")
		if [[ $UID -eq 0 ]]; then
			if [[ -f /usr/bin/desas ]]; then
				darbiba=$(zenity --list --title="Izvēlieties darbību" --text="Spēle <b>Desas $ver</b> jau ir instalēta jūsu sistēmā." --column="Veicamā darbība" "Palaist spēli" "Atjaunināt spēles datnes" "Atinstalēt spēli" "Palīdzība" "Par...")
				
				case $darbiba in
					"Palaist spēli")
						desas --start
						exit 1;;
					"Atjaunināt spēles datnes")
						if [[ "$0" == "/usr/bin/desas" ]]; then
							zenity --error --title="Nevar atjaunināt" --text="<b><span color=\"red\">Spēles datņu atjaunināšana iespējama tikai no instalācijas skripta (desas.sh).</span></b>"
							exit 1
						fi;;
					"Atinstalēt spēli")
						desas --remove
						exit 1;;
					"Palīdzība")
						desas --help
						exit 1;;
					"Par...")
						desas --about
						exit 1;;
				esac
			fi
			
			if [[ ! -f /usr/bin/zenity ]]; then
				(case $os in
					"Debian")
						apt-get install zenity;;
					"Red Hat")
						yum install zenity;;
					"Arch Linux")
						pacman -S zenity;;
				esac) | zenity --progress --title="Zenity pakotnes instalēšana" --text="Uzgaidiet, notiek <b>Zenity</b> pakotnes instalēšana." --auto-close --pulsate
			fi
			
			zenity --info --title="Desas instalēšanas rīks v0.8.0" --text="Esiet sveicināti spēles <b>Desas $ver</b> instalēšanas rīkā.\n\nNospiediet <b>OK</b>, lai turpinātu instalēšanas procesu."
			
			if [[ ! -f /usr/bin/python ]]; then
				(case $os in
					"Debian")
						apt-get install python;;
					"Red Hat")
						yum install python;;
					"Arch Linux")
						pacman -S python2;;
				esac) | zenity --progress --title="Python pakotnes instalēšana" --text="Uzgaidiet, notiek <b>Python</b> pakotnes instalēšana." --auto-close --pulsate
			fi
			
			if [[ ! (( -f /usr/lib/python2.7/lib-dynload/_tkinter.so ) || ( -d /usr/lib/python2.7/lib-dynload/_tkinter.so )) ]]; then
				(case $os in
					"Debian")
						apt-get install python-tk;;
					"Red Hat")
						yum install tkinter;;
					"Arch Linux")
						pacman -S tk;;
				esac) | zenity --progress --title="Tkinter pakotnes instalēšana" --text="Uzgaidiet, notiek <b>Tkinter</b> (tk) pakotnes instalēšana." --auto-close --pulsate
			fi
			
			(mkdir -p $cels
			cp -fu ./desas/desas.pyw $cels
			cp -fu ./desas/graphics.py $cels
			cp -rfu ./desas/images $cels
			cp -fu ./desas/desas /usr/bin
			cp -fu ./desas/desas.desktop /usr/share/applications) | zenity --progress --title="Datņu kopēšana" --text="Uzgaidiet, notiek <b>Desas $ver</b> datņu kopēšana." --auto-close --pulsate
			
			if [[ -f /usr/bin/desas ]]; then
				zenity --question --title="Instalēšana pabeigta" --text="<b>Desas $ver</b> instalēšana veiksmīgi pabeigta!\nVai vēlaties tagad palaist spēli?"
				case $? in
					0)
						python /opt/desas/desas.pyw;;
					1)
						exit 1;;
				esac
			else
				zenity --error --title="Kļūda instalēšanā" --text="<b><span color=\"red\">Atvainojiet, instalēšanas procesā radās kļūda. Mēģiniet palaist instalēšanas skriptu vēlreiz vai arī sazinieties ar skripta izstrādātāju.</span></b>"
			fi
		else
			if [[ "$0" == "/usr/bin/desas" ]]; then
				desas --start
				exit 1
			fi
			
			if [[ ! -f /usr/bin/gksu ]]; then
				echo "Lai instalētu Desas $ver, nepieciešamas sudo piekļuves tiesības."
				echo "Terminālī izpildiet sekojošu komandu: desas ./desas.sh."
				echo
				echo "Ja izmantojiet Debian (Ubuntu, Linux Mint...) vai Arch Linux bāzētu sistēmu,"
				echo "varat instalēt pakotni gksu un pēc tam atkārtoti palaidiet šo skriptu."
				zenity --error --title="Nepieciešamas sudo piekļuves tiesības" --text="<span color=\"red\">Lai instalētu spēli, nepieciešamas sudo piekļuves tiesības.\nTerminālī izpildiet sekojošu komandu: <b>sudo ./desas.sh</b>.\n\nJa izmantojiet Debian (Ubuntu, Linux Mint...) vai Arch Linux bāzētu sistēmu, varat instalēt pakotni <b>gksu</b> un pēc tam atkārtoti palaidiet šo skriptu.</span>"
				exit 1
			fi
			
			gksu "bash" $0 $@ --message="Desas $ver instalēšanai ir nepieciešamas sudo piekļuves tiesības, lai ierakstītu datus /opt, /usr/bin un /usr/share/applications direktorijās. Lūdzu, zemāk esošajā laukā ievadiet sudo piekļuves paroli un nospiediet pogu OK, lai turpinātu instalēšanu."
		fi;;
		
	--run|--start|--palaist|--sakt)
		python /opt/desas/desas.pyw;;
		
	-a|--about|--par)
		zenity --info --title="Desas $ver" --text="<b>(CC) Aija Trimdale</b>\nE-pasts: aija.trimdale@r6vsk.lv";;
		
	-h|--help|--palidziba)
		zenity --info --title="Desas $ver palīdzība" --text="Terminālī iespējams izmantot šādas komandas:\n<b>desas --about</b>\t- vispārīgās informācijas parādīšana\n<b>desas --help</b>\t- šī palīdzības loga parādīšana\n<b>desas --start</b>\t- spēles palaišana\n\nAr sudo piekļuves tiesībām papildus iespējams izpildīt šādu komandu:\n<b>desas --remove</b>\t- spēles atinstalēšana";;
		
	-r|--remove|--uninstall|--atinstalet|--nonemt)
		if [[ $UID -eq 0 ]]; then
			(rm -rf /opt/desas
			rm -f /usr/bin/desas
			rm -f /usr/share/applications/desas.desktop) |  zenity --progress --title="Datņu dzēšana" --text="Uzgaidiet, notiek <b>Desas $ver</b> datņu dzēšana." --auto-close --pulsate
			zenity --info --title="Atinstalēšana pabeigta" --text="<b>Desas $ver</b> atinstalēšana veiksmīgi pabeigta!"
		else
			zenity --error --title="Nepieciešamas sudo piekļuves tiesības" --text="<span color=\"red\">Lai atinstalētu spēli, nepieciešamas sudo piekļuves tiesības.\nTerminālī izpildiet sekojošu komandu: <b>sudo desas --remove</b>.</span>"
		fi;;
esac