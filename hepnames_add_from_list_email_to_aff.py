import re


EMAIL_TO_AFF = {"acnet.ge":"Tbilisi, Inst. Phys.",
"adelaide.edu.au":"Adelaide U.",
"agh.edu.pl":"AGH-UST, Cracow",
"aip.de":"Potsdam, Astrophys. Inst.",
"albany.edu":"SUNY, Albany",
"ameslab.gov":"Ames Lab",
"anl.gov":"Argonne",
"anu.edu.au":"Australian Natl. U., Canberra",
"apsu.edu":"Austin Peay State U.",
"arizona.edu":"Arizona U.",
"asu.edu":"Arizona State U.",
"au.dk":"Aarhus U.",
"auth.gr":"Thessaloniki U.",
"bao.ac.cn":"Beijing Observ.",
"bas.bg":"Sofiya, Inst. Nucl. Res.",
"berkeley.edu":"UC, Berkeley",
"bgu.ac.il":"Ben Gurion U. of Negev",
"bham.ac.uk":"Birmingham U.",
"bnl.gov":"Brookhaven",
"brandeis.edu":"Brandeis U.",
"bris.ac.uk":"Bristol U.",
"brown.edu":"Brown U.",
"brunel.ac.uk":"Brunel U.",
"bu.edu":"Boston U.",
"buffalo.edu":"SUNY, Buffalo",
"caltech.edu":"Caltech",
"cam.ac.uk":"Cambridge U.",
"camk.edu.pl":"Warsaw, Copernicus Astron. Ctr.",
"carleton.ca":"Carleton U.",
"carleton.edu":"Carleton Coll.",
"carnegiescience.edu":"Carnegie Inst. Observ.",
"cas.cn":"Beijing, Inst. Theor. Phys.",
"cas.cz":"Rez, Nucl. Phys. Inst.",
"cbpf.br":"Rio de Janeiro, CBPF",
"ccast.ac.cn":"CCAST World Lab, Beijing",
"ccnu.edu.cn":"Hua-Zhong Normal U.",
"cea.fr":"Saclay",
"cern.ch":"CERN",
"chalmers.se":"Goteborg, ITP",
"chiba-u.ac.jp":"Chiba U.",
"ciemat.es":"Madrid, CIEMAT",
"cinvestav.mx":"CINVESTAV, IPN",
"cmu.edu":"Carnegie Mellon U.",
"college-de-france.fr":"College de France",
"colorado.edu":"Colorado U.",
"colostate.edu":"Colorado State U.",
"columbia.edu":"Columbia U.",
"cornell.edu":"Cornell U., LNS",
"creighton.edu":"Creighton U.",
"csic.es":"Madrid, Inst. Estructura Materia",
"cuni.cz":"Charles U.",
"cuny.edu":"City Coll., N.Y.",
"cvut.cz":"Prague, Tech. U.",
"cwru.edu":"Case Western Reserve U.",
"demokritos.gr":"Democritos Nucl. Res. Ctr.",
"desy.de":"DESY",
"dias.ie":"Dublin Inst.",
"dl.ac.uk":"Daresbury",
"du.ac.in":"Delhi U.",
"duke.edu":"Duke U.",
"dur.ac.uk":"Durham U.",
"ed.ac.uk":"Edinburgh U.",
"elte.hu":"Eotvos U.",
"energy.gov":"Dept. of Energy, Wash., D.C.",
"ens.fr":"Ecole Normale Superieure",
"prl.ernet.in":"Ahmedabad, Phys. Res. Lab",
"barc.ernet.in":"Bhabha Atomic Res. Ctr.",
"veccal.ernet.in":"Calcutta, VECC",
"iucaa.ernet.in":"IUCAA, Pune",
"saha.ernet.in":"Saha Inst.",
"eso.cl":"European Southern Obs., Chile",
"eso.org":"European Southern Observ.",
"ethz.ch":"Zurich, ETH",
"fnal.gov":"Fermilab",
"fsu.edu":"Florida State U., SCRI",
"fsu.edu":"Florida State U.",
"fu-berlin.de":"Freie U., Berlin",
"fuw.edu.pl":"Warsaw U.",
"fz-juelich.de":"Julich, Forschungszentrum",
"fzu.cz":"Prague, Inst. Phys.",
"ganil.fr":"GANIL",
"gla.ac.uk":"Glasgow U.",
"gsi.de":"Darmstadt, GSI",
"gwu.edu":"George Washington U.",
"harvard.edu":"Harvard U.",
"hawaii.edu":"Hawaii U.",
"helsinki.fi":"Helsinki U.",
"hep.net":"SSCL",
"hip.fi":"Helsinki Inst. of Phys.",
"hiroshima-u.ac.jp":"Hiroshima U.",
"hokudai.ac.jp":"Hokkaido U.",
"hu-berlin.de":"Humboldt U., Berlin",
"huji.ac.il":"Hebrew U.",
"iap.fr":"Paris, Inst. Astrophys.",
"ias.edu":"Princeton, Inst. Advanced Study",
"iastate.edu":"Iowa State U.",
"ictp.it":"ICTP, Trieste",
"ifae.es":"Barcelona, IFAE",
"ifj.edu.pl":"Cracow, INP",
"ihep.ac.cn":"Beijing, Inst. High Energy Phys.",
"ihep.su":"Serpukhov, IHEP",
"ihep.su":"Serpukhov, IHEP",
"ihes.fr":"IHES, Bures-sur-Yvette",
"iihe.ac.be":"Brussels U., IIHE",
"iit.edu":"IIT, Chicago",
"ijs.si":"Stefan Inst., Ljubljana",
"imperial.ac.uk":"Imperial Coll., London",
"illinois.edu":"Illinois U., Urbana",
"inaf.it":"Brera Observ.",
"inaf.it":"Rome Observ.",
"indiana.edu":"Indiana U.",
"fe.infn.it":"Ferrara U.",
"lnf.infn.it":"Frascati",
"lngs.infn.it":"Gran Sasso",
"ba.infn.it":"INFN, Bari",
"bo.infn.it":"INFN, Bologna",
"ca.infn.it":"INFN, Cagliari",
"ct.infn.it":"INFN, Catania",
"fe.infn.it":"INFN, Ferrara",
"fi.infn.it":"INFN, Florence",
"ge.infn.it":"INFN, Genoa",
"le.infn.it":"INFN, Lecce",
"lnl.infn.it":"INFN, Legnaro",
"mi.infn.it":"INFN, Milan",
"na.infn.it":"INFN, Naples",
"pd.infn.it":"INFN, Padua",
"pv.infn.it":"INFN, Pavia",
"pg.infn.it":"INFN, Perugia",
"pi.infn.it":"INFN, Pisa",
"roma1.infn.it":"INFN, Rome",
"sa.infn.it":"INFN, Salerno",
"ts.infn.it":"INFN, Trieste",
"to.infn.it":"INFN, Turin",
"iss.infn.it":"Rome, ISS",
"inr.ac.ru":"Moscow, INR",
"lapp.in2p3.fr":"Annecy, LAPP",
"clr.in2p3.fr":"Clermont-Ferrand U.",
"llr.in2p3.fr":"Ecole Polytechnique",
"lpsc.in2p3.fr":"LPSC, Grenoble",
"mar.in2p3.fr":"Marseille, CPPM",
"ipn.in2p3.fr":"Orsay, IPN",
"lal.in2p3.fr":"Orsay, LAL",
"lpnhe.in2p3.fr":"Paris U., VI-VII",
"crn.in2p3.fr":"Strasbourg, CRN",
"ires.in2p3.fr":"Strasbourg, IReS",
"in2p3.fr":"SUBATECH, Nantes",
"ipj.gov.pl":"Warsaw, Inst. Nucl. Studies",
"ipm.ac.ir":"IPM, Tehran",
"irb.hr":"Boskovic Inst., Zagreb",
"isas.ac.jp":"JAXA, Sagamihara",
"itep.ru":"Moscow, ITEP",
"itp.ac.ru":"Landau Inst.",
"jadavpur.edu":"Jadavpur U.",
"jhu.edu":"Johns Hopkins U.",
"jinr.ru":"Dubna, JINR",
"jlab.org":"Jefferson Lab",
"jyu.fi":"Jyvaskyla U.",
"kanazawa-u.ac.jp":"Kanazawa U.",
"kek.jp":"INS, Tokyo",
"kek.jp":"KEK, Tsukuba",
"kent.edu":"Kent State U.",
"kfki.hu":"Budapest, RMKI",
"kharkov.ua":"Kharkov, KIPT",
"kiae.ru":"Kurchatov Inst., Moscow",
"kiev.ua":"BITP, Kiev",
"knu.ac.kr":"Kyungpook Natl. U.",
"kobe-u.ac.jp":"Kobe U.",
"korea.edu":"Korea U.",
"kth.se":"Royal Inst. Tech., Stockholm",
"ku.edu":"Kansas U.",
"kuleuven.ac.be":"Leuven U.",
"kvi.nl":"Groningen, KVI",
"kyoto-u.ac.jp":"Kyoto U.",
"kyushu-u.ac.jp":"Kyushu U.",
"lancs.ac.uk":"Lancaster U.",
"lanl.gov":"Los Alamos",
"lbl.gov":"LBL, Berkeley",
"le.ac.uk":"Leicester U.",
"leeds.ac.uk":"Leeds U.",
"leidenuniv.nl":"Leiden Observ.",
"leidenuniv.nl":"Leiden U.",
"linea.gov.br":"LIneA, Rio de Janeiro",
"lip.pt":"Lisbon, LIFEP",
"liv.ac.uk":"Liverpool U.",
"llnl.gov":"LLNL, Livermore",
"lmu.de":"Munich U.",
"lodz.pl":"Lodz U.",
"lpi.ru":"Lebedev Inst.",
"lsu.edu":"Louisiana State U.",
"lu.se":"Lund U.",
"manchester.ac.uk":"Manchester U.",
"mcgill.ca":"McGill U.",
"mcmaster.ca":"McMaster U.",
"mephi.ru":"Moscow Phys. Eng. Inst.",
"metu.edu.tr":"Middle East Tech. U., Ankara",
"lns.mit.edu":"MIT, LNS",
"mki.mit.edu":"MIT, MKI",
"mit.edu":"MIT",
"mpifr-bonn.mpg.de":"Bonn, Max Planck Inst., Radioastron.",
"mpa-garching.mpg.de":"Garching, Max Planck Inst.",
"mpe-garching.mpg.de":"Garching, Max Planck Inst.",
"mpia-hd.mpg.de":"Heidelberg, Max Planck Inst. Astron.",
"mpi-hd.mpg.de":"Heidelberg, Max Planck Inst.",
"mpp.mpg.de":"Munich, Max Planck Inst.",
"aei-potsdam.mpg.de":"Potsdam, Max Planck Inst.",
"msu.edu":"Michigan State U.",
"msu.ru":"Moscow State U.",
"mtholyoke.edu":"Mt. Holyoke Coll.",
"nagoya-u.ac.jp":"Nagoya U.",
"nao.ac.jp":"Natl. Astron. Observ. of Japan",
"navy.mil":"Naval Research Lab, Wash., D.C.",
"nbi.dk":"Bohr Inst.",
"nbia.dk":"Bohr Inst.",
"ncsu.edu":"North Carolina State U.",
"ncu.edu.tw":"Taiwan, Natl. Central U.",
"nd.edu":"Notre Dame U.",
"neu.edu":"Northeastern U.",
"nihon-u.ac.jp":"Nihon U., Tokyo",
"niigata-u.ac.jp":"Niigata U.",
"nikhef.nl":"NIKHEF, Amsterdam",
"nipne.ro":"Bucharest, IFIN-HH",
"niu.edu":"Northern Illinois U.",
"nmsu.edu":"New Mexico State U.",
"nordita.org":"Nordita",
"northwestern.edu":"Northwestern U.",
"nottingham.ac.uk":"Nottingham U.",
"nrao.edu":"NRAO, Socorro",
"nsf.gov":"NSF, Wash., D.C.",
"nsk.su":"Novosibirsk, IYF",
"nthu.edu.tw":"Taiwan, Natl. Tsing Hua U.",
"ntu.edu.tw":"Taiwan, Natl. Taiwan U.",
"ntua.gr":"Natl. Tech. U., Athens",
"nyu.edu":"New York U.",
"obspm.fr":"Meudon Observ.",
"obspm.fr":"Paris Observ.",
"oeaw.ac.at":"Vienna, OAW",
"ohio-state.edu":"Ohio State U.",
"ohiou.edu":"Ohio U.",
"olemiss.edu":"Mississippi U.",
"on.br":"Rio de Janeiro Observ.",
"ornl.gov":"Oak Ridge",
"osaka-cu.ac.jp":"Osaka City U.",
"osaka-u.ac.jp":"Osaka U.",
"osu.edu":"Ohio State U.",
"ou.edu":"Oklahoma U.",
"ox.ac.uk":"Oxford U.",
"perimeterinstitute.ca":"Perimeter Inst. Theor. Phys.",
"physto.se":"Stockholm U.",
"pitt.edu":"Pittsburgh U.",
"pku.edu.cn":"Peking U.",
"polito.it":"Turin Polytechnic",
"princeton.edu":"Princeton U. Observ.",
"princeton.edu":"Princeton U.",
"psi.ch":"PSI, Villigen",
"psu.edu":"Penn State U.",
"puchd.ac.in":"Panjab U.",
"purdue.edu":"Purdue U.",
"qmul.ac.uk":"Queen Mary, U. of London",
"ras.ru":"Steklov Math. Inst., Moscow",
"iopb.res.in":"Bhubaneswar, Inst. Phys.",
"rri.res.in":"Harish-Chandra Res. Inst.",
"imsc.res.in":"IMSc, Chennai",
"tifr.res.in":"Tata Inst.",
"rhul.ac.uk":"Royal Holloway, U. of London",
"rice.edu":"Rice U.",
"rochester.edu":"Rochester U.",
"rockefeller.edu":"Rockefeller U.",
"rpi.edu":"Rensselaer Poly.",
"rssi.ru":"Ioffe Phys. Tech. Inst.",
"ru.nl":"Nijmegen U.",
"ruhr-uni-bochum.de":"Ruhr U., Bochum",
"rutgers.edu":"Rutgers U., Piscataway",
"rwth-aachen.de":"Aachen, Tech. Hochsch.",
"saga-u.ac.jp":"Saga U., Japan",
"saitama-u.ac.jp":"Saitama U.",
"sc.edu":"South Carolina U.",
"sfu.ca":"Simon Fraser U.",
"shef.ac.uk":"Sheffield U.",
"sinap.ac.cn":"SINAP, Shanghai",
"sinica.edu.tw":"Taiwan, Inst. Phys.",
"sissa.it":"SISSA, Trieste",
"skku.ac.kr":"Sungkyunkwan U.",
"smu.edu":"Southern Methodist U.",
"sns.it":"Pisa, Scuola Normale Superiore",
"snue.ac.kr":"Seoul Natl. U.",
"soton.ac.uk":"Southampton U.",
"spb.ru":"St. Petersburg, INP",
"spbu.ru":"St. Petersburg State U.",
"slac.stanford.edu":"SLAC",
"stanford.edu":"Stanford U., Phys. Dept.",
"stfc.ac.uk":"Rutherford",
"stonybrook.edu":"Stony Brook U.",
"stsci.edu":"Baltimore, Space Telescope Sci.",
"sunysb.edu":"SUNY, Stony Brook",
"sussex.ac.uk":"Sussex U.",
"susx.ac.uk":"Sussex U.",
"swan.ac.uk":"Swansea U.",
"swin.edu.au":"Swinburne U. Tech., Hawthorn",
"sydney.edu.au":"Sydney U.",
"syr.edu":"Syracuse U.",
"tamu.edu":"Texas A-M",
"tau.ac.il":"Tel Aviv U.",
"technion.ac.il":"Technion",
"temple.edu":"Temple U.",
"titech.ac.jp":"Tokyo Inst. Tech.",
"tmu.ac.jp":"Tokyo Metropolitan U.",
"toho-u.ac.jp":"Toho U.",
"tohoku.ac.jp":"Tohoku U.",
"trieste.it":"Trieste U.",
"triumf.ca":"TRIUMF",
"tsinghua.edu.cn":"Tsinghua U., Beijing",
"tsu.ge":"Tbilisi State U.",
"tsukuba.ac.jp":"Tsukuba U.",
"tu-darmstadt.de":"Darmstadt, Tech. Hochsch.",
"tu-dresden.de":"Dresden, Tech. U.",
"tu-muenchen.de":"Munich, Tech. U.",
"tuat.ac.jp":"Tokyo U. of Agric. Tech.",
"tufts.edu":"Tufts U.",
"tum.de":"Munich, Tech. U.",
"tuwien.ac.at":"Vienna, Tech. U.",
"u-psud.fr":"Orsay",
"u-tokyo.ac.jp":"Tokyo U.",
"ua.ac.be":"Antwerp U.",
"ua.edu":"Alabama U.",
"uab.es":"Barcelona, Autonoma U.",
"ualberta.ca":"Alberta U.",
"uam.es":"Madrid, Autonoma U.",
"ub.es":"Barcelona U.",
"uba.ar":"Buenos Aires U.",
"ubc.ca":"British Columbia U.",
"uc.edu":"Cincinnati U.",
"uc.pt":"Coimbra U.",
"ucdavis.edu":"UC, Davis",
"uchicago.edu":"Chicago U.",
"uci.edu":"UC, Irvine",
"ucl.ac.be":"Louvain U.",
"ucl.ac.uk":"University Coll. London",
"ucla.edu":"UCLA",
"ucm.es":"Madrid U.",
"ucolick.org":"Lick Observ.",
"uconn.edu":"Connecticut U.",
"ucr.edu":"UC, Riverside",
"ucsb.edu":"Santa Barbara, KITP",
"ucsb.edu":"UC, Santa Barbara",
"ucsc.edu":"UC, Santa Cruz",
"ucsd.edu":"UC, San Diego",
"uct.ac.za":"Cape Town U.",
"udel.edu":"Delaware U., Bartol Inst.",
"uerj.br":"Rio de Janeiro State U.",
"ufl.edu":"Florida U.",
"ufrj.br":"Rio de Janeiro Federal U.",
"ugent.be":"Gent U.",
"uh.edu":"Houston U.",
"uib.no":"Bergen U.",
"uic.edu":"Illinois U., Chicago",
"uio.no":"Oslo U.",
"uiowa.edu":"Iowa U.",
"uiuc.edu":"Illinois U., Urbana",
"uj.edu.pl":"Jagiellonian U.",
"uky.edu":"Kentucky U.",
"ulb.ac.be":"Brussels U.",
"ulg.ac.be":"Liege U.",
"ull.es":"Laguna U., Tenerife",
"umass.edu":"Massachusetts U., Amherst",
"umd.edu":"Maryland U.",
"umich.edu":"Michigan U.",
"umn.edu":"Minnesota U.",
"umons.ac.be":"UMH, Mons",
"umontreal.ca":"Montreal U.",
"unam.mx":"Mexico U., ICN",
"unam.mx":"Mexico U.",
"unc.edu":"North Carolina U.",
"unesp.br":"Sao Paulo, IFT",
"uni-bielefeld.de":"Bielefeld U.",
"uni-bonn.de":"Bonn U.",
"uni-dortmund.de":"Dortmund U.",
"uni-erlangen.de":"Erlangen - Nuremberg U.",
"uni-frankfurt.de":"Frankfurt U.",
"uni-freiburg.de":"Freiburg U.",
"uni-giessen.de":"Giessen U.",
"uni-goettingen.de":"Gottingen U.",
"uni-graz.at":"Graz U.",
"uni-hamburg.de":"Hamburg U.",
"uni-hannover.de":"Hannover U.",
"uni-heidelberg.de":"Heidelberg U.",
"uni-karlsruhe.de":"Karlsruhe U.",
"uni-kiel.de":"Kiel U.",
"uni-kl.de":"Kaiserslautern U.",
"uni-koeln.de":"Cologne U.",
"uni-leipzig.de":"Leipzig U.",
"uni-lj.si":"Ljubljana U.",
"kph.uni-mainz.de":"Mainz U., Inst. Kernphys.",
"physik.uni-mainz.de":"Mainz U., Inst. Phys.",
"uni-marburg.de":"Philipps U. Marburg",
"uni-muenchen.de":"Munich U.",
"uni-regensburg.de":"Regensburg U.",
"uni-rostock.de":"Rostock U.",
"uni-siegen.de":"Siegen U.",
"uni-tuebingen.de":"Tubingen U.",
"uni-wuerzburg.de":"Wurzburg U.",
"uni-wuppertal.de":"Wuppertal U.",
"uniba.it":"Bari U.",
"uniba.sk":"Comenius U.",
"unibas.ch":"Basel U.",
"unibe.ch":"Bern U.",
"unibo.it":"Bologna U.",
"unibuc.ro":"Bucharest U.",
"unica.it":"Cagliari U.",
"unicamp.br":"Campinas State U.",
"unict.it":"Catania U.",
"unifi.it":"Florence U.",
"unige.ch":"Geneva U.",
"unige.it":"Genoa U.",
"unil.ch":"Lausanne U.",
"unimelb.edu.au":"Melbourne U.",
"unimi.it":"Milan U.",
"unimib.it":"Milan Bicocca U.",
"unina.it":"Naples U.",
"unipd.it":"Padua U.",
"unipg.it":"Perugia U.",
"unipi.it":"Pisa U.",
"unipr.it":"Parma U.",
"unipv.it":"Pavia U.",
"uniroma1.it":"Rome U.",
"uniroma2.it":"Rome U.,Tor Vergata",
"uniroma3.it":"Rome III U.",
"unisa.it":"Salerno U.",
"unitn.it":"Trento U.",
"unito.it":"Turin U.",
"uniud.it":"Udine U.",
"univ-montp2.fr":"Montpellier U.",
"univ-mrs.fr":"Marseille, CPT",
"univie.ac.at":"Vienna U.",
"unizar.es":"Zaragoza U.",
"unizh.ch":"Zurich U.",
"unlp.edu.ar":"La Plata U.",
"unm.edu":"New Mexico U.",
"uoa.gr":"Athens U.",
"uoi.gr":"Ioannina U.",
"uoregon.edu":"Oregon U.",
"upenn.edu":"Pennsylvania U.",
"uqconnect.edu.au":"Queensland U.",
"usc.edu":"Southern California U.",
"usc.es":"Santiago de Compostela U.",
"usp.br":"Sao Paulo U.",
"ustc.edu.cn":"Hefei, CUST",
"usyd.edu.au":"Sydney U.",
"utah.edu":"Utah U.",
"utdallas.edu":"Texas U., Dallas",
"utexas.edu":"Texas U.",
"utk.edu":"Tennessee U.",
"utl.pt":"Lisbon, IST",
"utoronto.ca":"Canadian Inst. Theor. Astrophys.",
"utoronto.ca":"Toronto U.",
"uu.nl":"Utrecht U.",
"uu.se":"Uppsala U.",
"uv.es":"Valencia U.",
"uva.nl":"Amsterdam U.",
"uvic.ca":"Victoria U.",
"uwaterloo.ca":"Waterloo U.",
"uwo.ca":"Western Ontario U.",
"vanderbilt.edu":"Vanderbilt U.",
"virginia.edu":"Virginia U.",
"vt.edu":"Virginia Tech.",
"vu.nl":"Vrije U., Amsterdam",
"warwick.ac.uk":"Warwick U.",
"waseda.ac.jp":"Waseda U.",
"washington.edu":"Washington U., Seattle",
"wayne.edu":"Wayne State U.",
"weizmann.ac.il":"Weizmann Inst.",
"wisc.edu":"Wisconsin U., Madison",
"wm.edu":"William-Mary Coll.",
"wroc.pl":"Wroclaw U.",
"wustl.edu":"Washington U., St. Louis",
"yale.edu":"Yale U.",
"yerphi.am":"Yerevan Phys. Inst.",
"yonsei.ac.kr":"Yonsei U.",
"yorku.ca":"York U., Canada"}


def aff_from_email(email):
    domain = re.sub(r'.*\@(.*)', r'\1', email)
    for key in EMAIL_TO_AFF:
        search_string = r'.*\W' + key
        #print search_string, domain
        if re.search(search_string, domain) or domain == key:
            return EMAIL_TO_AFF[key]
    return None



