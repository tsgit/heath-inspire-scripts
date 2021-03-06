#!/usr/bin/python
# -*- coding: utf-8 -*-

SEARCH_A = " not r fermilab not af fermilab"
SEARCH_A += " and (primarch astro-ph or astro-ph.he \
or astro-ph.co or astro-ph.GA \
or astro-ph.EP or astro-ph.IM \
or astro-ph.sr)"


search = "find a Annis, J \
or Bauer, D \
or Benson, B \
or Buckley-Geer, E \
or Chou, Aaron \
or Crisler, M \
or Diehl, T \
or Drlica-Wagner, A"
search += SEARCH_A
print search
print '\n'

search = "find a Estrada, J \
or Finley, D \
or Flaugher, B \
or Frieman, J \
or Glass, H \
or Gnedin, N \
or Gottschalk, E \
or Gutierrez, G \
or Hojvat, C \
or Hsu, L \
or Kent, S \
or Kron, R \
or Kubik, D \
or Krnjaic, G \
or Kuropatkin, N \
or Lebrun, P \
or Lin, H \
or Lippincott, H \
or Loer, B \
or Lukens, P "
search += SEARCH_A
print search
print '\n'


search = "find a Mantsch, P \
or Marriner, J \
or Mazur, P \
or Merritt, W \
or Neilsen, E \
or Nguyen, Hogan \
or Nord, B \
or Peoples, J \
or Pordes, S \
or Ramberg, E \
or Soares-Santos, M \
or Scarpine, V \
or Sonnenschein, A \
or Stebbins, A \
or Stoughton, C \
or Tiffenberg, J \
or Tucker, D \
or Wester, W \
or Yanny, B \
or Yoo, J \
or Gnedin, Nick \
or Hooper, Dan \
or Stebbins, Albert \
or Kent, Steve \
or Benson, Bradford \
or Frieman, Josh \
or Kron, Rich \
or Guardincerri, Yann \
or Hogan, Craig"
search += SEARCH_A
print search

print '\n'

SEARCH_T = " not r fermilab not af fermilab"
SEARCH_T += " and (primarch hep-ph or primarch hep-th or primarch hep-lat)"

search = "find a Campbell, J \
or Carena, M \
or Dobrescu, B \
or Eichten, E \
or Fox, P \
or Giele, W \
or Harnik, R \
or Hill, C \
or Kronfeld, A \
or Lykken, J \
or Machado, P \
or Mackenzie, P \
or Parke, S \
or Prestel, S \
or Quigg, C \
or Van de Water, R \
or Coloma, P \
or Blinov, N \
or Gao, Christina \
or Howe, K \
or Huges, C \
or Isaacson, J \
or Jay, W \
or Kelly, K \
or Krause, C \
or Low, Matthew \
or Martinez Soler, I \
or Neumann, T \
or Perez, Y \
or Turner, J \
or Rocco, N \
or Veernala, A \
or Zhang, Yue "

search += SEARCH_T
print search
print "\n"

search = "find a Meyer, A \
or Mohlabeng, G \
or Tenneti, A \
or Albright, C \
or Bardeen, w \
or de Gouvea, A \
or Freeland, E \
or Hill, R \
or Kayser, B \
or Keung, W \
or Martin, S \
or Mrenna, S \
or Simone, J "

search += SEARCH_T
print search
print "\n"

SEARCH_ACC = " not r fermilab not af fermilab"
SEARCH_ACC += " and (fc b or fc i)"

search = "find a Adey, D \
or Alexahin, Y \
or Balbekov, V \
or Barletta, W \
or Bowring, D \
or Broemmelsiek, D \
or Bross, A \
or Bruce, M \
or Burov, A \
or Carlson, K \
or Chou, W \
or Crawford, D \
or Dey, J \
or Duel, K \
or Edstrom, D \
or Gallo, P \
or Gianfelice-Wendt, E \
or Johnson, W \
or Johnstone, J \
or Kriss, M \
or Kufer, M \
or Lebedev, V \
or Leonova, M \
or Madrak, R \
or Mokhov, N \
or Moretti, A \
or Nagaitsev, S \
or Neuffer, D \
or Ng, K \
or Novitski, I \
or Pasquinelli, R \
or Peterson, D \
or Piekarz, H \
or Piot, P \
or Popovic, M \
or Prebys, E \
or Pronskikh, V \
or Rakhno, I \
or Ruan, J \
or Santucci, J \
or Sen, T \
or Shin, Y Min \
or Shiltsev, V \
or Snopok, P \
or Stancari, G \
or Stratakis, D \
or Striganov, S \
or Thangaraj, C \
or Tropin, I \
or Valishev, A \
or Warner, A \
or Winchester, S \
or Yonehara, K \
or Zwaska, R "

search += SEARCH_ACC
print search
print "\n"

print("""find a Alberto Accardi
or Ian Balitsky
or Raul Briceno
or Jozef Dudek
or Robert Edwards
or José Goity
or Franz Gross
or Wally Melnitchouk
or Kostas Orginos
or Jianwei Qiu
or or Anatoly Radyushkin
or David Richards
or or Ted Rogers
or or Rocco Schiavilla
or Adam Szczepaniak
or or Wally Van Orden
or Christian Weiss
and (primarch hep-lat or hep-ph or nucl-th)""")

print("""find a Miguel Albaladejo
or Carlota Andres
or Felippo Delcarro
or Ishara Fernando
or Luka Leskovec
or Tianbo Liu
or Vincent Mathieu
or Nobuo Sato
or Raza Sabbir Sufian
or Kazuhiro Watanabe
or Colin Egerer
or Juan Vicente Guerrero
or Christopher Johnson
or Joseph Karpie
or Tanjib Khan
or Eric Moffat
or Wayne Morris
or Felipe Ortega Gama
or Dimitra Pefkou
or Archana Radhakrishnan
or Yiyu Zhou
and (primarch hep-lat or hep-ph or nucl-th)
""")

print('refersto:affiliation:"jefferson lab" and (037:hep-ph or 037:hep-lat or 037:nucl-th)')

