# -*- coding: utf-8 -*-
from random import *   #  Made by SuSE jeb @AijaSuse ražojums :)   p.s  Nezagt kodu bez paprasīšanas:)  #variants ar izslēgto kodu-vieglais
from graphics import *
win=GraphWin("Desas",500,500)
win.setBackground("white")

#def priekš grafikas
def aplitis(o):      #zīmējums
	aplis=Circle(o,30)
	aplis.setWidth(2)
	aplis.draw(win)
def krustins(p1,p2): #zīmējums
	pk1=Point(p1+30,p2+30) 
	pk2=Point(p1+30,p2-30)
	pk3=Point(p1-30,p2-30)
	pk4=Point(p1-30,p2+30)
	k1=Line(pk1,pk3)
	k2=Line(pk2,pk4)
	k1.setWidth(2)
	k2.setWidth(2)
	k2.draw(win)
	k1.draw(win)
def laukums():       #režģis
	p1a=Point(200,100) # katrs laukumiņš ir 100X100 px a b c d režģa līnijas
	p2a=Point(200,400)
	a=Line(p1a,p2a)
	a.setWidth(2)
	a.draw(win)
	p1b=Point(300,100)
	p2b=Point(300,400)
	b=Line(p1b,p2b)
	b.setWidth(2)
	b.draw(win)
	p1c=Point(100,200)
	p2c=Point(400,200)
	c=Line(p1c,p2c)
	c.setWidth(2)
	c.draw(win)
	p1d=Point(100,300)
	p2d=Point(400,300)
	d=Line(p1d,p2d)
	d.setWidth(2)
	d.draw(win)
	# uzzīmets spiežamais lauciņš:
	POINT=[130,170,230,270,320,370,]
	for i in range(0,6,2):
		A=Rectangle(  Point (130,POINT[i])  ,Point (170,POINT[i+1])  )
		A.setOutline("#E5E5E5")
		A.draw(win)
	for i in range(0,6,2):
		A=Rectangle(  Point (230,POINT[i])  ,Point (270,POINT[i+1])  )
		A.setOutline("#E5E5E5")
		A.draw(win)
	for i in range(0,6,2):
		A=Rectangle(  Point (330,POINT[i])  ,Point (370,POINT[i+1])  )
		A.setOutline("#E5E5E5")
		A.draw(win)
def speles_sakums(): #sākumiņš
	sak1=Text(Point(250,50),"Esiet sveicināti ''Desas'' vers.2.4!")
	sak2=Text(Point(250,100),"Lai sāktu spēli, nokliksķiniet ar peli jebkur laukumā")
	sak1.setFace("helvetica")
	sak1.setSize(16)
	sak1.draw(win)
	sak2.setFace("helvetica")
	sak2.setSize(16)
	sak2.draw(win)
	Sak=win.getMouse()
	sak1.undraw()
	sak2.undraw()
def pieprasijums():	 #jā un nē lauciņi					 
	sak4=Text(Point(250,420),"Vai turpināsiet?")
	sak4.draw(win)
	sak5=Text(Point(210,435),"Jā")
	sak5.draw(win)
	sak6=Text(Point(310,435),"Nē")
	sak6.draw(win)
	keksis1=Rectangle(  Point (200,450), Point(220,470) )
	keksis1.setOutline("#202020")
	keksis1.draw(win)
	keksis2=Rectangle(Point(300,450), Point(320,470) )
	keksis2.setOutline("#202020")
	keksis2.draw(win)	
def iziesana():
	win=GraphWin("Desas",500,500)
	win.setBackground("white")
	tnx=Text(Point(250,150),"Paldies, ka spēlējāt!")
	tnx.setSize(16)
	tnx.setFace("helvetica")
	tnx2=Text(Point(250,330),"Autore-Rīgas 6. vidusskolas 11.a skolniece ")
	tnx2.setFace("helvetica")
	tnx2.setSize(16)
	tnx3=Text(Point(250,350)," Aija Trimdale")
	tnx3.setFace("helvetica")
	tnx3.setSize(16)
	tnx4=Text(Point(250,450),"Lai izietu, nospiediet ar peli jebkur laukumā")
	tnx4.setFace("helvetica")
	tnx4.setSize(10)
	tnx.draw(win)
	tnx2.draw(win)
	tnx3.draw(win)
	tnx4.draw(win)
	iziet=win.getMouse()
	
#def priekš spēlēs
def parbauda_laukumu(rezultati, diognale):	#rezultātu masīvs, diog
	S1,S2=0,0
	for i in range(0,3): 				 															
		for j in range(0,3):
			#print(desa[i][j], end="")
			if desa[i][j]==0:
				desa[i][j]=10											
		print()	
	print()									
	for i in range(0,3):
		for j in range(0,3):
			S1=S1+desa[i][j]
			S2=S2+desa[j][i]	
		rezultati.append(S1)
		rezultati.append(S2)
		S1,S2=0,0	
	diognale1=desa[0][0]+desa[1][1]+desa[2][2]
	diognale2=desa[0][2]+desa[1][1]+desa[2][0]
	diognale.append(diognale1)
	diognale.append(diognale2)	
	if diognale1<10:						
		rezultati.append(diognale1)
	if diognale2<10:						
		rezultati.append(diognale2)
	for i in range(0,3): 				 															
		for j in range(0,3):											
			if desa[i][j]==10:
				desa[i][j]=0

# def spelei un grafikai				
def speletaja_gajiens():                 #ar aplīša ielikšanu
	Jap=0
	while Jap!=1: #aplitis
		o=win.getMouse()
		p11=o.getX()
		p22=o.getY()
		if p11>=130 and p11<=170 or p11>=230 and p11<=270 or p11>=330 and p11<=370:
			if p22>=130 and p22<=170 or p22>=230 and p22<=270 or p22>=330 and p22<=370:
				y=int(p11//100)
				x=int(p22//100)
				if desa[int(x-1)][int(y-1)]==0:
					desa[int(x-1)][int(y-1)]=2
					aplitis(o)
					Jap=1											
def random():                            #ar krustiņa ieliksanu	random dators			
	X=randint(1,3) 															
	Y=randint(1,3) 										
	desa[int(X-1)][int(Y-1)]=1
	p2=X*100 +50
	p1=Y*100 +50
	krustins(p1,p2)
def datora_gajiens(rezultati, diognale): #liek krustiņus dators
	gajiens=0

	if 12 in rezultati:
		I=rezultati.index(12) +1
		if I%2!=0: #rindas
			rinda=I//2
			for kk in range(0,3):
				if desa[rinda][kk]==0:
					desa[rinda][kk]=1
					p1=(kk+1)*100 +50
					p2=(rinda+1)*100 +50
					krustins(p1,p2)
					gajiens=10
					Rin=(rinda+1) *100 +50
					Sarkans=Line(Point(100,Rin),Point(400,Rin))
					Sarkans.setOutline("#B40737")
					Sarkans.setWidth(3)
					Sarkans.draw(win)
					break
		elif I%2==0: #kolonas
			kolona=I//3
			for kk in range(0,3):
				if desa[kk][kolona]==0:
					desa[kk][kolona]=1
					p1=(kolona+1)*100 +50
					p2=(kk+1)*100 +50
					krustins(p1,p2)
					gajiens=10
					Rin=(kolona+1) *100 +50
					Sarkans=Line(Point(Rin,100),Point(Rin,400))
					Sarkans.setOutline("#B40737")
					Sarkans.setWidth(3)
					Sarkans.draw(win)
					break			
	elif 12 in diognale: 
		I=diognale.index(12)
		if I==1:
			for dd in range(0,3): 
				dio=[2,1,0]
				ddd=dio[dd]
				if desa[dd][ddd]==0:
					desa[dd][ddd]=1
					p1=(ddd+1)*100 +50
					p2=(dd+1)*100 +50
					krustins(p1,p2)
					gajiens=10
					Sarkans=Line(Point(400,100),Point(100,400))
					Sarkans.setOutline("#B40737")
					Sarkans.setWidth(3)
					Sarkans.draw(win)
					break
		elif I==0: 
			for dd in range(0,3):
				if desa[dd][dd]==0:
					desa[dd][dd]=1
					p1=(dd+1)*100 +50
					p2=(dd+1)*100 +50
					krustins(p1,p2)
					gajiens=10
					Sarkans=Line(Point(100,100),Point(400,400))
					Sarkans.setOutline("#B40737")
					Sarkans.setWidth(3)
					Sarkans.draw(win)
					break
	elif 14 in rezultati:
		I=rezultati.index(14) +1	
		if I%2!=0: #rindas
			rinda=I//2
			for kk in range(0,3):
				if desa[rinda][kk]==0:
					desa[rinda][kk]=1
					p1=(kk+1)*100 +50
					p2=(rinda+1)*100 +50
					krustins(p1,p2)
					gajiens=10
					break
		elif I%2==0: #kolonas
			kolona=I//3
			for kk in range(0,3):
				if desa[kk][kolona]==0:
					desa[kk][kolona]=1
					p1=(kolona+1)*100 +50
					p2=(kk+1)*100 +50
					krustins(p1,p2)
					gajiens=10
					break
	elif 14 in diognale:
		I=diognale.index(14)
		if I==1: #diognāle
			for dd in range(0,3):
				dio=[2,1,0]
				ddd=dio[dd]
				if desa[dd][ddd]==0:
					desa[dd][ddd]=1					
					p1=(ddd+1)*100 +50
					p2=(dd+1)*100 +50
					krustins(p1,p2)
					gajiens=10
					break
		elif I==0: 
			for dd in range(0,3):
				if desa[dd][dd]==0:
					desa[dd][dd]=1					
					p1=(dd+1)*100 +50
					p2=(dd+1)*100 +50
					krustins(p1,p2)
					gajiens=10
					break		
	elif gajiens==0:
		if desa[1][1]==0:
			desa[1][1]=1
			p1=(2)*100 +50
			p2=(2)*100 +50
			krustins(p1,p2)
			#print("centrs")
			gajiens=10
			'''
		if gajiens==0:
			cisins=[0,0,2,2,0]
			for DEDE in range(0,4):
				A=cisins[DEDE]
				B=cisins[DEDE+1]
				print("malaA",A)
				print("malaB",B)
				if desa[A][B]==0:
					desa[A][B]=1
					p2=(A+1)*100 +50
					p1=(B+1)*100 +50
					krustins(p1,p2)
					gajiens=1
					break
					'''
		if gajiens==0:
			AA=1
			while AA!=0:						   #dators, random, while, mainīt kodu
				#print("rando")
				X=randint(1,3)
				Y=randint(1,3)
				if desa[int(X-1)][int(Y-1)]==0:
					desa[int(X-1)][int(Y-1)]=1
					p2=X*100 +50
					p1=Y*100 +50
					krustins(p1,p2)
					AA=0
				else:
					AA=1
def pieprasijums_dara(Spele,sudo):                 # Vai turpināt spēli
	Spele=2
	Jap=0
	while Jap==0:
		keksis_spelei=win.getMouse()
		jax=keksis_spelei.getX()
		jay=keksis_spelei.getY()
		if  jay<=470 and jay>=450:	
			if  jax>=200 and jax<=220:
				sudo.append(0)
				Jap=1
				win.close()
			elif jax<=320 and jax>=300:
				sudo.append(10)
				win.close()
				Jap=1
	
#sākas kods, beidzas def jūra
#1-dators, krustiņš (pagaidām, varbūt vēlāk uz izveli)
#2-spēlētājs,  aplītis
Spele=0
Spele_karta=1
speles_sakums()
dators=0
speletajs=0
while Spele==0:
	if Spele_karta==1:
		sak3=Text(Point(250,50),"1. gājiens ir datoram") 
		sak3.draw(win)
	elif Spele_karta%2!=0:
		win=GraphWin("Desas",500,500)
		win.setBackground("white")
		sak3=Text(Point(250,50),"1. gājiens ir datoram") 
		sak3.draw(win)
		kopa=   Text(Point(100,430),"Speles kopā      - ")
		sardele=Text(Point(100,450),"Datora    uzvaras- ")
		desina= Text(Point(100,470),"Spēlētāja uzvaras- ")
		kopa1=Text(Point(170, 430),Spele_karta -1)
		sardele1 =Text(Point(170,450),dators)
		desina1= Text(Point(170,470),speletajs)
		sardele.draw(win)
		desina.draw(win)
		sardele1.draw(win)
		desina1.draw(win)
		kopa.draw(win)
		kopa1.draw(win)
	elif Spele_karta%2==0:
		win=GraphWin("Desas",500,500)
		win.setBackground("white")
		sak3=Text(Point(250,50),"1. gājiens ir spēlētājam") 
		sak3.draw(win)
		kopa=   Text(Point(100,430),"Speles kopā      - ")
		sardele=Text(Point(100,450),"Datora    uzvaras- ")
		desina= Text(Point(100,470),"Spēlētāja uzvaras- ")
		kopa1=Text(Point(170, 430),Spele_karta -1)
		sardele1 =Text(Point(170,450),dators)
		desina1= Text(Point(170,470),speletajs)
		sardele.draw(win)
		desina.draw(win)
		sardele1.draw(win)
		desina1.draw(win)
		kopa.draw(win)
		kopa1.draw(win)
	
	laukums()
	desa=[[ 0 for col in range (3)] for row in range (3)] 
	if Spele_karta%2!=0: #datora gājiens pirmais
		karta=1 
	elif Spele_karta%2==0:#spēlētāja gājiens pirmais
		karta=2  
		
	for SG in range(0,9):
		if karta==1:  
			random()
		elif karta %2!=0 and karta!=1:
			datora_gajiens(rezultati, diognale)	
		elif karta %2==0:
			speletaja_gajiens()
			sak3.undraw()
	
		karta=karta+1	
		rezultati=[]
		diognale=[]
		parbauda_laukumu(rezultati, diognale)
		if 3 in rezultati:
			break
		elif 6 in rezultati:
			break
	
	beigas=Text(Point(250,25),"Spēle beigusies-")
	beigas.setFace("helvetica")
	beigas.setSize(16)
	beigas.draw(win)
	
	if 3 in rezultati:
		beigas=Text(Point(250,50),"Uzvarēja dators")
		beigas.setFace("helvetica")
		beigas.setSize(16)
		beigas.draw(win)
		dators=dators+1
	elif 6 in rezultati:
		beigas=Text(Point(250,50),"Uzvarēja spēlētājs")
		beigas.setFace("helvetica")
		beigas.setSize(16)
		beigas.draw(win)
		I=rezultati.index(6)
		if I<=5:
			I=I+1
			if I%2!=0:#rindas
				I=I//2
				Rin=(I+1)*100 +50
				Sarkans=Line(Point(100,Rin),Point(400,Rin))
				Sarkans.setOutline("#B40737")
				Sarkans.setWidth(3)
				Sarkans.draw(win)
				speletajs=speletajs+1
			elif I%2==0:
				I=I//3
				Rin=(I+1)*100 +50
				Sarkans=Line(Point(Rin,100),Point(Rin,400))
				Sarkans.setOutline("#B40737")
				Sarkans.setWidth(3)
				Sarkans.draw(win)
				speletajs=speletajs+1
		else:
			I=diognale.index(6)
			if I==0:
				Sarkans=Line(Point(100,100),Point(400,400))
				Sarkans.setOutline("#B40737")
				Sarkans.setWidth(3)
				Sarkans.draw(win)
				speletajs=speletajs+1
			elif I==1:
				Sarkans=Line(Point(100,400),Point(400,100))
				Sarkans.setOutline("#B40737")
				Sarkans.setWidth(3)
				Sarkans.draw(win)
				speletajs=speletajs+1
	else:
		beigas=Text(Point(250,50),"Neizšķirts")
		beigas.setFace("helvetica")
		beigas.setSize(16)
		beigas.draw(win)
	sudo=[]
	pieprasijums()
	pieprasijums_dara(Spele,sudo)
	Spele=sudo[0]
	Spele_karta=Spele_karta+1
iziesana()

