#!/usr/bin/python


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# modules defined in FM.py
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# FM.py is copied, along with the appropriate FMxxxxxx.py file from CONFIGDIR to local by pythonUnitsLink.py
# make sure if you change the modules, you also update the stored copy FMxxxxxx.py TBGLST file when you update FM.py
# CF.py is always linked, make sure to update CFTOP.py and SCTN0102 when FM.py or CF.py are changed
# all other units are loaded dynamically by pythonUnitsLink.py using the SCTN16 structure, FMSCTNENABLED.py file locally, etc.
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * def doErrorItem(message_, itemToError_):
# * def explodeItem(itemToExplode_):
# * def makeAComment(comment_):
# * def makeADict(dictName_, dictComment_, dictItems_):
# * def makeAList(listName_, listComment_, listItems_):
# * def makeATupDict(tupDictName_, tupDictItems_, tupDictSidecar_):
# * def makeAWideComment(comment_):
# * def makeCF():
# * def makeDBSQLT()
# * def makeDO():
# * def makeDOHBI():
# * def makeFM():
# * def makeFO():
# * def makeSP():
# * def parseTBGLST(FDTBGLST):
# * def readFileToStr(FILENAME_):
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * def __main__():


#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN001 _CHR_ _CONST_
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
BKQT = "`"  # BACK TICK
BKSLSH = "\\"  # BACKSLASH
CBRCE = "}"  # CLOSEBRACE
CBRKT = "]"  # CLOSEBRACKET
CPAREN = ")"  # CLOSE PARENTHESIS
DBLQT = "\""  # DOUBLE QUOTE
ESC = "\x1b"
NEWLINE = "\n"  # NEWLINE
OBRCE = "{"  # OPENBRACE
OBRKT = "["  # OPENBRACKET
OPAREN = "("  # OPENPAREN
SGLQT = "'"  # simple ' character
SPCSTR = " "  # SPACE character"
TABSTR = "\t"  # TAB

CMNTLEN = 200
CONFIGDIR = "/rcr/0-units/python/"
FOLDLEN = 200
TRIQT = f"""{DBLQT}{DBLQT}{DBLQT}"""


#
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN002 value_ constants
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
#


BIN04 = lambda X: f"""{X:04b}"""
BIN08 = lambda X: f"""{X:08b}"""
BIN16 = lambda X: f"""{X:016b}"""
BIN32 = lambda X: f"""{X:032b}"""
BIN64 = lambda X: f"""{X:064b}"""
CF_NAME = "newCF.py"
CFTOP_NAME = f"""{CONFIGDIR}CFTOP.py"""
CLRALL = f"""{ESC}[2J"""
CLRDOWN = f"""{ESC}[J"""
CLREOL = f"""{ESC}[K"""
CMNTLINE = f"""# * {"#*" * (CMNTLEN // 2)}"""
DBSQLT_NAME = "newDBSQLT.py"
DICTMODE_KEYSTR = "DICTMODE_KEYSTR"  # define dictmode 'key':val
DICTMODE_KEYVAL = "DICTMODE_KEYVAL"  # define dictmode key:val
DOHBIBTM_NAME = f"""{CONFIGDIR}HBIBTM.py"""
DOHBI_NAME = "newHBI.py"
DOHBITOP_NAME = f"""{CONFIGDIR}HBITOP.py"""
DO_NAME = "newDO.py"
DOTOP_NAME = f"""{CONFIGDIR}DOTOP.py"""
EEOL = f"""{ESC}[K"""
EMPTY_DICT = {}
EMPTY_LIST = []
EMPTY_STR = ""
EMPTYSTRLST = [None, "", DBLQT, f"""{DBLQT}{DBLQT}""", SGLQT, f"""{SGLQT}{SGLQT}""", BKQT, "None", "\r", NEWLINE, "\r\n", "\n\r", ]
EMPTY_TUPLE = ()
FM_NAME = "newFM.py"
FMTOP_NAME = f"""{CONFIGDIR}FMTOP.py"""
FOLD1ENDHERE = f"""# fold here {"⥣1" * (FOLDLEN // 2)}"""
FOLD1ENDHERELN = f"""# fold here {"⥣1" * (FOLDLEN // 2)}{NEWLINE}"""
FOLD1STARTHERE = f"""# fold here {"⥥1" * (FOLDLEN // 2)}"""
FOLD1STARTHERELN = f"""# fold here {"⥥1" * (FOLDLEN // 2)}{NEWLINE}"""
FOLD2ENDHERE = f"""# fold here {"⥣2" * (FOLDLEN // 2)}"""
FOLD2ENDHERELN = f"""# fold here {"⥣2" * (FOLDLEN // 2)}{NEWLINE}"""
FOLD2STARTHERE = f"""# fold here {"⥥2" * (FOLDLEN // 2)}"""
FOLD2STARTHERELN = f"""# fold here {"⥥2" * (FOLDLEN // 2)}{NEWLINE}"""
FOLD3ENDHERE = f"""# fold here {"⥣3" * (FOLDLEN // 2)}"""
FOLD3ENDHERELN = f"""# fold here {"⥣3" * (FOLDLEN // 2)}{NEWLINE}"""
FOLD3STARTHERE = f"""# fold here {"⥥3" * (FOLDLEN // 2)}"""
FOLD3STARTHERELN = f"""# fold here {"⥥3" * (FOLDLEN // 2)}{NEWLINE}"""
FO_NAME = "newFO.py"
FOTOP_NAME = f"""{CONFIGDIR}FOTOP.py"""
HEX08 = lambda X_: f"""{X_:02H}"""  # {thisComment_}
HEX16 = lambda X_: f"""{X_:04H}"""  # {thisComment_}
HEX32 = lambda X_: f"""{X_:08H}"""  # {thisComment_}
HEX64 = lambda X_: f"""{X_:016H}"""  # {thisComment_}
IMPORTANTSTR = f"""# * {"!-" * (CMNTLEN // 2)}"""  # important line marker
INDENTIN = " -=> "  # display arrow RIGHT
INDENTOUT = " <=- "  # display arrow LEFT
INFOSTR = f"""# * {"%_" * (CMNTLEN // 2)}"""  # INFO _STR_ line\
LINESUP = lambda NUM_: f"""{ESC}[{NUM_}A"""
MARK1END = lambda TAG_: f"""# {"⥣1 " * (CMNTLEN // 3)} {TAG_}"""
MARK1ENDLN = lambda TAG_: f"""# {"⥣1 " * (CMNTLEN // 3)} {TAG_}{NEWLINE}"""
MARK1MID = lambda TAG_: f"""# {"⥣1⥥ " * (CMNTLEN // 4)} {TAG_}"""
MARK1MIDLN = lambda TAG_: f"""# {"⥣1⥥ " * (CMNTLEN // 4)} {TAG_}{NEWLINE}"""
MARK1START = lambda TAG_: f"""# {"1⥥ " * (CMNTLEN // 3)} {TAG_}"""
MARK1STARTLN = lambda TAG_: f"""# {"1⥥ " * (CMNTLEN // 3)} {TAG_}{NEWLINE}"""
MARK2END = lambda TAG_: f"""# {"⥣2 " * (CMNTLEN // 3)} {TAG_}"""
MARK2ENDLN = lambda TAG_: f"""# {"⥣2 " * (CMNTLEN // 3)} {TAG_}{NEWLINE}"""
MARK2MID = lambda TAG_: f"""# {"⥣2⥥ " * (CMNTLEN // 4)} {TAG_}"""
MARK2MIDLN = lambda TAG_: f"""# {"⥣2⥥ " * (CMNTLEN // 4)} {TAG_}{NEWLINE}"""
MARK2START = lambda TAG_: f"""# {"2⥥ " * (CMNTLEN // 3)} {TAG_}"""
MARK2STARTLN = lambda TAG_: f"""# {"2⥥ " * (CMNTLEN // 3)} {TAG_}{NEWLINE}"""
MARK3END = lambda TAG_: f"""# {"⥣3 " * (CMNTLEN // 3)} {TAG_}"""
MARK3ENDLN = lambda TAG_: f"""# {"⥣3 " * (CMNTLEN // 3)} {TAG_}{NEWLINE}"""
MARK3MID = lambda TAG_: f"""# {"⥣3⥥ " * (CMNTLEN // 4)} {TAG_}"""
MARK3MIDLN = lambda TAG_: f"""# {"⥣3⥥ " * (CMNTLEN // 4)} {TAG_}{NEWLINE}"""
MARK3START = lambda TAG_: f"""# {"3⥥ " * (CMNTLEN // 3)} {TAG_}"""
MARK3STARTLN = lambda TAG_: f"""# {"3⥥ " * (CMNTLEN // 3)} {TAG_}{NEWLINE}"""
MARK4END = lambda TAG_: f"""# {"⥣4 " * (CMNTLEN // 3)} {TAG_}"""
MARK4ENDLN = lambda TAG_: f"""# {"⥣4 " * (CMNTLEN // 3)} {TAG_}{NEWLINE}"""
MARK4MID = lambda TAG_: f"""# {"⥣4⥥ " * (CMNTLEN // 4)} {TAG_}"""
MARK4MIDLN = lambda TAG_: f"""# {"⥣4⥥ " * (CMNTLEN // 4)} {TAG_}{NEWLINE}"""
MARK4START = lambda TAG_: f"""# {"4⥥ " * (CMNTLEN // 3)} {TAG_}"""
MARK4STARTLN = lambda TAG_: f"""# {"4⥥ " * (CMNTLEN // 3)} {TAG_}{NEWLINE}"""
MARK5END = lambda TAG_: f"""# {"⥣5 " * (CMNTLEN // 3)} {TAG_}"""
MARK5ENDLN = lambda TAG_: f"""# {"⥣5 " * (CMNTLEN // 3)} {TAG_}{NEWLINE}"""
MARK5MID = lambda TAG_: f"""# {"⥣5⥥ " * (CMNTLEN // 4)} {TAG_}"""
MARK5MIDLN = lambda TAG_: f"""# {"⥣5⥥ " * (CMNTLEN // 4)} {TAG_}{NEWLINE}"""
MARK5START = lambda TAG_: f"""# {"5⥥ " * (CMNTLEN // 3)} {TAG_}"""
MARK5STARTLN = lambda TAG_: f"""# {"5⥥ " * (CMNTLEN // 3)} {TAG_}{NEWLINE}"""
MARK6END = lambda TAG_: f"""# {"⥣6 " * (CMNTLEN // 3)} {TAG_}"""
MARK6ENDLN = lambda TAG_: f"""# {"⥣6 " * (CMNTLEN // 3)} {TAG_}{NEWLINE}"""
MARK6MID = lambda TAG_: f"""# {"⥣6⥥ " * (CMNTLEN // 4)} {TAG_}"""
MARK6MIDLN = lambda TAG_: f"""# {"⥣6⥥ " * (CMNTLEN // 4)} {TAG_}{NEWLINE}"""
MARK6START = lambda TAG_: f"""# {"6⥥ " * (CMNTLEN // 3)} {TAG_}"""
MARK6STARTLN = lambda TAG_: f"""# {"6⥥ " * (CMNTLEN // 3)} {TAG_}{NEWLINE}"""
MARK7END = lambda TAG_: f"""# {"⥣7 " * (CMNTLEN // 3)} {TAG_}"""
MARK7ENDLN = lambda TAG_: f"""# {"⥣7 " * (CMNTLEN // 3)} {TAG_}{NEWLINE}"""
MARK7MID = lambda TAG_: f"""# {"⥣7⥥ " * (CMNTLEN // 4)} {TAG_}"""
MARK7MIDLN = lambda TAG_: f"""# {"⥣7⥥ " * (CMNTLEN // 4)} {TAG_}{NEWLINE}"""
MARK7START = lambda TAG_: f"""# {"7⥥ " * (CMNTLEN // 3)} {TAG_}"""
MARK7STARTLN = lambda TAG_: f"""# {"7⥥ " * (CMNTLEN // 3)} {TAG_}{NEWLINE}"""
MARK8END = lambda TAG_: f"""# {"⥣8 " * (CMNTLEN // 3)} {TAG_}"""
MARK8ENDLN = lambda TAG_: f"""# {"⥣8 " * (CMNTLEN // 3)} {TAG_}{NEWLINE}"""
MARK8MID = lambda TAG_: f"""# {"⥣8⥥ " * (CMNTLEN // 4)} {TAG_}"""
MARK8MIDLN = lambda TAG_: f"""# {"⥣8⥥ " * (CMNTLEN // 4)} {TAG_}{NEWLINE}"""
MARK8START = lambda TAG_: f"""# {"8⥥ " * (CMNTLEN // 3)} {TAG_}"""
MARK8STARTLN = lambda TAG_: f"""# {"8⥥ " * (CMNTLEN // 3)} {TAG_}{NEWLINE}"""
MARK9END = lambda TAG_: f"""# {"⥣9 " * (CMNTLEN // 3)} {TAG_}"""
MARK9ENDLN = lambda TAG_: f"""# {"⥣9 " * (CMNTLEN // 3)} {TAG_}{NEWLINE}"""
MARK9MID = lambda TAG_: f"""# {"⥣9⥥ " * (CMNTLEN // 4)} {TAG_}"""
MARK9MIDLN = lambda TAG_: f"""# {"⥣9⥥ " * (CMNTLEN // 4)} {TAG_}{NEWLINE}"""
MARK9START = lambda TAG_: f"""# {"9⥥ " * (CMNTLEN // 3)} {TAG_}"""
MARK9STARTLN = lambda TAG_: f"""# {"9⥥ " * (CMNTLEN // 3)} {TAG_}{NEWLINE}"""
MARKLINES_NAME = f"""{CONFIGDIR}MARKLINES.py"""
MOVETO = lambda LN_, COL_: f"""{ESC}[{LN_};{COL_}H"""
NSPC = lambda NUM_: f"""{SPCSTR * NUM_}"""  # returns a string with NUM_ SPC
NTAB = lambda NUM_: f"""{TABSTR * NUM_}"""  # returns a string with NUM_ TAB
QTSET = [DBLQT, SGLQT, BKQT]  # set of all quote characters
SCTN0102NAME = f"""{CONFIGDIR}SCTN0102.py"""
SCTNSNAME = f"""{CONFIGDIR}SCTNS.py"""
SP_NAME = "newSP.py"
SPTOP_NAME = f"""{CONFIGDIR}SPTOP.py"""
TBGLST_NAME = "TBGLST.py"


CODES2STRIP = [  # {'CODES2STRIP': "dict holding all of the things to strip from 'text' strings like color codes"}
	f"{ESC}[0m",  # entry for ESC-[0m
	f"{ESC}[1m",  # entry for ESC-[1m
	f"{ESC}[32m",  # entry for ESC-[32m
	f"{ESC}[35m",  # entry for ESC-[35m
	f"{ESC}[36m",  # entry for ESC-[36m
]


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN003 TYPEs and lambda
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN101 FMAX _DEF_
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
FMAXCF_SCTN0003_LAMBDADEF = "FMAXCF_SCTN0003_LAMBDADEF"  # define a lambda function <NAC><NAME><lambda str>
FMAXCF_SCTN0003_TYPEDEF = "FMAXCF_SCTN0003_TYPEDEF"  # define a fake type used in the translation dict <NAC><NAME><TYPE>
FMAXCF_SCTN0201_STRDEF = "FMAXCF_SCTN0201_STRDEF"  # define a STR in SCTN21 <NAC><NAME><str>
FMAXCF_SCTN0201_VALDEF = "FMAXCF_SCTN0201_VALDEF"  # define a VAL in SCTN21 <NAC><NAME><VAL>
FMAXCF_SCTN0202_OPTIONSADDHELPLINE = "FMAXCF_SCTN0202_OPTIONSADDHELPLINE"  # add a line to the help for a PARM, after the comment is automatically added<NAC><PARM><ADDONHELPLINE>
FMAXCF_SCTN0202_OPTIONSDICTSTRADD = "FMAXCF_SCTN0202_OPTIONSDICTSTRADD"  # define a OPTNAME: 'str' in SCTN202 <NAC><KEY><PARM><STRDEFAULT>
FMAXCF_SCTN0202_OPTIONSDICTVALADD = "FMAXCF_SCTN0202_OPTIONSDICTVALADD"  # define a OPTNAME: VAL in SCTN202 <NAC><KEY><PARM><VALDEFAULT>
FMAXCF_SCTN0202_OPTIONSSTRADD = "FMAXCF_SCTN0202_OPTIONSSTRADD"  # define a '-a[=]' in SCTN22 <NAC><PARM><KEY><VAL>
FMAXCF_SCTN0202_OPTIONSVALADD = "FMAXCF_SCTN0202_OPTIONSVALADD"  # define a '-a[=]' in SCTN22 <NAC><PARM><KEY><VAL>
FMAXCF_SCTN0203_DICTDEF = "FMAXCF_SCTN0203_DICTDEF"  # define a dict in SCTN203 <NAC><DICTNAME><DICTMODE>
FMAXCF_SCTN0203_DICTSTRADD = "FMAXCF_SCTN0203_DICTSTRADD"  # define a dict STR in SCTN203 <NAC><DICTNAME><STR>
FMAXCF_SCTN0203_DICTVALADD = "FMAXCF_SCTN0203_DICTVALADD"  # define a dict VAL in SCTN203 <NAC><DICTNAME><VAL>
FMAXCF_SCTN0204_LISTDEF = "FMAXCF_SCTN0204_LISTDEF"  # define a list in SCTN204 <NAC><LISTNAME>
FMAXCF_SCTN0204_LISTSTRADD = "FMAXCF_SCTN0204_LISTSTRADD"  # define a list STR in SCTN204 <NAC><LISTNAME><STR>
FMAXCF_SCTN0204_LISTVALADD = "FMAXCF_SCTN0204_LISTVALADD"  # define a VAL in a list in SCTN204 <NAC><LISTNAME><VAL>
FMAXFM_SCTN0101_AXDEF = "FMAXFM_SCTN0101_AXDEF"  # define a new FM action <NAC>
FMAXFM_SCTN0102_STRDEF = "FMAXFM_SCTN0102_STRDEF"  # define a FM string <NAC><VALNAME><STR>
FMAXFM_SCTN0102_VALDEF = "FMAXFM_SCTN0102_VALDEF"  # define a FM value_ <NAC><VALNAME><VAL>
FMAXFM_SCTN0103_DICTDEF = "FMAXFM_SCTN0103_DICTDEF"  # define a dict for FM <NAC>
FMAXFM_SCTN0104_LISTDEF = "FMAXFM_SCTN0104_LISTDEF"  # define a list in FM <NAC>
FMAXFO_SCTN0300_STRDEF = "FMAXFO_SCTN0300_STRDEF"  # add a string <NAC><STRNAME><STR>
FMAXFO_SCTN0300_VALDEF = "FMAXFO_SCTN0300_VALDEF"  # add a value to a dict <NAC><VALNAME><VAL>
FMAXFO_SCTN0301_DICTDEF = "FMAXFO_SCTN0301_DICTDEF"  # define a dict in FO.py <NAC><DICTNAME>
FMAXFO_SCTN0301_DICTSTRADD = "FMAXFO_SCTN0301_DICTSTRADD"  # add a string to a dict <NAC><DICTNAME><STRNAME><STR>
FMAXFO_SCTN0301_DICTVALADD = "FMAXFO_SCTN0301_DICTVALADD"  # add a string to a dict <NAC><DICTNAME><VALNAME><VAL>
FMAXFO_SCTN0301_STRDICTSTRADD = "FMAXFO_SCTN0301_STRDICTSTRADD"  # add a STR string to a dict <NAC><DICTNAME><STR><STR>
FMAXFO_SCTN0301_STRDICTVALADD = "FMAXFO_SCTN0301_STRDICTVALADD"  # add a STR val to a dict <NAC><DICTNAME><STR><VAL>
FMAXFO_SCTN0302_LISTDEF = "FMAXFO_SCTN0302_LISTDEF"  # define a list in FO.py <NAC><LISTNAME>
FMAXFO_SCTN0302_LISTSTRADD = "FMAXFO_SCTN0302_LISTSTRADD"  # add a string to a list <NAC><LISTNAME><STR>
FMAXFO_SCTN0302_LISTVALADD = "FMAXFO_SCTN0302_LISTVALADD"  # add a string to a list <NAC><LISTNAME><VAL>
FMAXFO_SCTN0303_TUPDICTDEF = "FMAXFO_SCTN0303_TUPDICTDEF"  # define a TUPDICT <NAC><TUPDICTNAME>
FMAXFO_SCTN0303_TUPDICTSTRADD = "FMAXFO_SCTN0303_TUPDICTSTRADD"  # add a string to a dict <NAC><DICTNAME><STRNAME><STR>
FMAXFO_SCTN0303_TUPDICTSTRSTRADD = "FMAXFO_SCTN0303_TUPDICTSTRSTRADD"  # add a STR string to a dict <NAC><DICTNAME><STR><STR>
FMAXFO_SCTN0303_TUPDICTSTRVALADD = "FMAXFO_SCTN0303_TUPDICTSTRVALADD"  # add a STR val to a dict <NAC><DICTNAME><STR><VAL>
FMAXFO_SCTN0303_TUPDICTVALADD = "FMAXFO_SCTN0303_TUPDICTVALADD"  # add a string to a dict <NAC><DICTNAME><VALNAME><VAL>
FMAXFO_SCTN0304_EXTENSIONADD = "FMAXFO_SCTN0304_EXTENSIONADD"  # add an extension <NAC><TYPE><EXTENSION>
FMAXFO_SCTN0304_EXTENSIONTYPEDEF = "FMAXFO_SCTN0304_EXTENSIONTYPEDEF"  # add an extension type <NAC><TYPE><MEDIABOOL>
FMAXSP_SCTN0600_STRDEF = "FMAXSP_SCTN0600_STRDEF"  # define a SP str <NAC><STRNAME><STR>
FMAXSP_SCTN0600_VALDEF = "FMAXSP_SCTN0600_VALDEF"  # define a SP val <NAC><VAL>
FMAXSP_SCTN0601_DICTDEF = "FMAXSP_SCTN0601_DICTDEF"  # define a dict for SP <NAC><DICTNAME>
FMAXSP_SCTN0601_DICTSTRADD = "FMAXSP_SCTN0601_DICTSTRADD"  # define a dict str entry SP <NAC><DICTNAME><KEY><STR>
FMAXSP_SCTN0601_DICTVALADD = "FMAXSP_SCTN0601_DICTVALADD"  # define a dict val entry SP <NAC><DICTNAME><KEY><VAL>
FMAXSP_SCTN0602_LISTDEF = "FMAXSP_SCTN0602_LISTDEF"  # define a list in SP <NAC><LISTNAME>
FMAXSP_SCTN0602_LISTSTRADD = "FMAXSP_SCTN0602_LISTSTRADD"  # define a list str in SP <NAC><LISTNAME><KEY><STR>
FMAXSP_SCTN0602_LISTVALADD = "FMAXSP_SCTN0602_LISTVALADD"  # define a list str in SP <NAC><LISTNAME><KEY><VAL>
FMAXSP_SCTN0603_TUPDICTDEF = "FMAXSP_SCTN0603_TUPDICTDEF"  # define a (tuple dict function) set <NAC><TUPDICTNAME>
FMAXSP_SCTN0603_TUPDICTLISTDEF = "FMAXSP_SCTN0603_TUPDICTLISTDEF"  # define a list entry in a tupdict <NAC><TUPDICTNAME><KEY>
FMAXSP_SCTN0603_TUPDICTLISTSTRADD = "FMAXSP_SCTN0603_TUPDICTLISTSTRADD"  # define a list STR entry in a tupdict <NAC><TUPDICTNAME><KEY><STR>
FMAXSP_SCTN0603_TUPDICTLISTVALADD = "FMAXSP_SCTN0603_TUPDICTLISTVALADD"  # define a list VAL entry in a tupdict <NAC><TUPDICTNAME><KEY><VAL>
FMAXSP_SCTN0603_TUPDICTSTRADD = "FMAXSP_SCTN0603_TUPDICTSTRADD"  # define a tuple dict str <NAC><TUPDICTNAME><KEY><VAL>
FMAXSP_SCTN0603_TUPDICTVALADD = "FMAXSP_SCTN0603_TUPDICTVALADD"  # define a tuple dict str <NAC><TUPDICTNAME><KEY><VAL>
FMAX_NOP = "FMAX_NOP"  # skip this entry


FMAXFM_AXLST = [
	FMAXCF_SCTN0003_LAMBDADEF,  # define a lambda function <NAC><NAME><lambda str>
	FMAXCF_SCTN0003_TYPEDEF,  # define a fake type used in the translation dict <NAC><NAME><TYPE>
	FMAXCF_SCTN0201_STRDEF,  # define a STR in SCTN21 <NAC><NAME><str>
	FMAXCF_SCTN0201_VALDEF,  # define a VAL in SCTN21 <NAC><NAME><VAL>
	FMAXCF_SCTN0202_OPTIONSADDHELPLINE,  # add a line to the help for a PARM, after the comment is automatically added<NAC><PARM><ADDONHELPLINE>
	FMAXCF_SCTN0202_OPTIONSDICTSTRADD,  # define a OPTNAME: 'str' in SCTN202 <NAC><KEY><PARM><STRDEFAULT>
	FMAXCF_SCTN0202_OPTIONSDICTVALADD,  # define a OPTNAME: VAL in SCTN202 <NAC><KEY><PARM><VALDEFAULT>
	FMAXCF_SCTN0202_OPTIONSSTRADD,  # define a '-a[=]' in SCTN22 <NAC><PARM><KEY><VAL>
	FMAXCF_SCTN0202_OPTIONSVALADD,  # define a '-a[=]' in SCTN22 <NAC><PARM><KEY><VAL>
	FMAXCF_SCTN0203_DICTDEF,  # define a dict in SCTN203 <NAC><DICTNAME><DICTMODE>
	FMAXCF_SCTN0203_DICTSTRADD,  # define a dict STR in SCTN203 <NAC><DICTNAME><STR>
	FMAXCF_SCTN0203_DICTVALADD,  # define a dict VAL in SCTN203 <NAC><DICTNAME><VAL>
	FMAXCF_SCTN0204_LISTDEF,  # define a list in SCTN204 <NAC><LISTNAME>
	FMAXCF_SCTN0204_LISTSTRADD,  # define a list STR in SCTN204 <NAC><LISTNAME><STR>
	FMAXCF_SCTN0204_LISTVALADD,  # define a VAL in a list in SCTN204 <NAC><LISTNAME><VAL>
	FMAXFM_SCTN0101_AXDEF,  # define a new FM action <NAC>
	FMAXFM_SCTN0102_STRDEF,  # define a FM string <NAC><VALNAME><STR>
	FMAXFM_SCTN0102_VALDEF,  # define a FM value_ <NAC><VALNAME><VAL>
	FMAXFM_SCTN0103_DICTDEF,  # define a dict for FM <NAC>
	FMAXFM_SCTN0104_LISTDEF,  # define a list in FM <NAC>
	FMAXFO_SCTN0300_STRDEF,  # add a string <NAC><STRNAME><STR>
	FMAXFO_SCTN0300_VALDEF,  # add a value to a dict <NAC><VALNAME><VAL>
	FMAXFO_SCTN0301_DICTDEF,  # define a dict in FO.py <NAC><DICTNAME>
	FMAXFO_SCTN0301_DICTSTRADD,  # add a string to a dict <NAC><DICTNAME><STRNAME><STR>
	FMAXFO_SCTN0301_DICTVALADD,  # add a string to a dict <NAC><DICTNAME><VALNAME><VAL>
	FMAXFO_SCTN0301_STRDICTSTRADD,  # add a STR string to a dict <NAC><DICTNAME><STR><STR>
	FMAXFO_SCTN0301_STRDICTVALADD,  # add a STR val to a dict <NAC><DICTNAME><STR><VAL>
	FMAXFO_SCTN0302_LISTDEF,  # define a list in FO.py <NAC><LISTNAME>
	FMAXFO_SCTN0302_LISTSTRADD,  # add a string to a list <NAC><LISTNAME><STR>
	FMAXFO_SCTN0302_LISTVALADD,  # add a string to a list <NAC><LISTNAME><VAL>
	FMAXFO_SCTN0303_TUPDICTDEF,  # define a TUPDICT <NAC><TUPDICTNAME>
	FMAXFO_SCTN0303_TUPDICTSTRADD,  # add a string to a dict <NAC><DICTNAME><STRNAME><STR>
	FMAXFO_SCTN0303_TUPDICTSTRSTRADD,  # add a STR string to a dict <NAC><DICTNAME><STR><STR>
	FMAXFO_SCTN0303_TUPDICTSTRVALADD,  # add a STR val to a dict <NAC><DICTNAME><STR><VAL>
	FMAXFO_SCTN0303_TUPDICTVALADD,  # add a string to a dict <NAC><DICTNAME><VALNAME><VAL>
	FMAXFO_SCTN0304_EXTENSIONADD,  # add an extension <NAC><TYPE><EXTENSION>
	FMAXFO_SCTN0304_EXTENSIONTYPEDEF,  # add an extension type <NAC><TYPE><MEDIABOOL>
	FMAXSP_SCTN0600_STRDEF,  # define a SP str <NAC><STRNAME><STR>
	FMAXSP_SCTN0600_VALDEF,  # define a SP val <NAC><VAL>
	FMAXSP_SCTN0601_DICTDEF,  # define a dict for SP <NAC><DICTNAME>
	FMAXSP_SCTN0601_DICTSTRADD,  # define a dict str entry SP <NAC><DICTNAME><KEY><STR>
	FMAXSP_SCTN0601_DICTVALADD,  # define a dict val entry SP <NAC><DICTNAME><KEY><VAL>
	FMAXSP_SCTN0602_LISTDEF,  # define a list in SP <NAC><LISTNAME>
	FMAXSP_SCTN0602_LISTSTRADD,  # define a list str in SP <NAC><LISTNAME><KEY><STR>
	FMAXSP_SCTN0602_LISTVALADD,  # define a list str in SP <NAC><LISTNAME><KEY><VAL>
	FMAXSP_SCTN0603_TUPDICTDEF,  # define a (tuple dict function) set <NAC><TUPDICTNAME>
	FMAXSP_SCTN0603_TUPDICTLISTDEF,  # define a list entry in a tupdict <NAC><TUPDICTNAME><KEY>
	FMAXSP_SCTN0603_TUPDICTLISTSTRADD,  # define a list STR entry in a tupdict <NAC><TUPDICTNAME><KEY><STR>
	FMAXSP_SCTN0603_TUPDICTLISTVALADD,  # define a list VAL entry in a tupdict <NAC><TUPDICTNAME><KEY><VAL>
	FMAXSP_SCTN0603_TUPDICTSTRADD,  # define a tuple dict str <NAC><TUPDICTNAME><KEY><VAL>
	FMAXSP_SCTN0603_TUPDICTVALADD,  # define a tuple dict str <NAC><TUPDICTNAME><KEY><VAL>
	FMAX_NOP,  # skip this entry
]


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN102 VAL _DEF_
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
FMFO_SCTN0304_MEDIAFILELSTSTR = ""  # SCTN304 FO.py EXTENSIONS media filetypes list in FM.py while parsing


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN103 _DICT_ _DEF_
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
FMCF_SCTN0003_TYPECMNTDICT = {}  # SCTN009 types comments
FMCF_SCTN0003_TYPEDICT = {}  # SCTN003 types
FMCF_SCTN0201_DEFCMNTDICT = {}  # SCTN201 defines comments dict
FMCF_SCTN0201_DEFDICT = {}  # SCTN201 defines dict
FMCF_SCTN0202_OPTIONSCMNTDICT = {}  # SCTN202 OPTIONS comments dict
FMCF_SCTN0202_OPTIONSDICT = {}  # SCTN202 OPTIONS dict
FMCF_SCTN0202_OPTIONSDICTCMNTDICT = {}  # SCTN202 OPTIONSDICT comments dict
FMCF_SCTN0202_OPTIONSDICTDICT = {}  # SCTN202 OPTIONSDICT
FMCF_SCTN0202_OPTIONSHELPDICT = {}  # SCTN202 OPTIONS HELPDICT
FMCF_SCTN0203_DICTCMNTDICT = {}  # SCTN203 dict comments dict
FMCF_SCTN0203_DICTDICT = {}  # SCTN203 dict dict
FMCF_SCTN0204_LISTCMNTDICT = {}  # SCTN204 list comments dict
FMCF_SCTN0204_LISTDICT = {}  # SCTN204 list dict
FMFM_SCTN0101_AXCMNTDICT = {}  # SCTN101 FMAX defined
FMFM_SCTN0101_AXDICT = {}  # SCTN101 FMAX defined
FMFM_SCTN0102_VALCMNTDICT = {}  # SCTN102 val
FMFM_SCTN0102_VALDICT = {}  # SCTN102 val
FMFM_SCTN0103_DICTCMNTDICT = {}  # SCTN103 dict defined
FMFM_SCTN0103_DICTDICT = {}  # SCTN103 dict defined
FMFM_SCTN0104_LISTCMNTDICT = {}  # SCTN201 device defines
FMFM_SCTN0104_LISTDICT = {}  # SCTN201 device defines
FMFO_SCTN0300_VALCMNTDICT = {}  # SCTN300 FO.py comment
FMFO_SCTN0300_VALDICT = {}  # SCTN300 FO.py values
FMFO_SCTN0301_DICTCMNTDICT = {}  # SCTN301 FO.py comment
FMFO_SCTN0301_DICTDICT = {}  # SCTN301 FO.py dict values
FMFO_SCTN0302_LISTCMNTDICT = {}  # SCTN302 FO.py comment
FMFO_SCTN0302_LISTDICT = {}  # SCTN302 FO.py list values
FMFO_SCTN0303_TUPDICTCMNTDICT = {}  # SCTN303 FO.py TUPDICT comment
FMFO_SCTN0303_TUPDICTDICT = {}  # SCTN303 FO.py TUPDICT values
FMFO_SCTN0304_EXTENSIONLOOKUPDICT = {}  # SCTN304 FO.py EXTENSIONLOOKUP values
FMFO_SCTN0304_EXTENSIONSCMNTDICT = {}  # SCTN304 FO.py EXTENSIONS comment
FMFO_SCTN0304_EXTENSIONSTYPESDICT = {}  # SCTN304 FO.py EXTENSIONSTYPES values
FMSP_SCTN0600_DEFCMNTDICT = {}  # SCTN600 defines
FMSP_SCTN0600_DEFDICT = {}  # SCTN600 defines
FMSP_SCTN0601_DICTCMNTDICT = {}  # SCTN601 defines
FMSP_SCTN0601_DICTDICT = {}  # SCTN601 defines
FMSP_SCTN0602_LISTCMNTDICT = {}  # SCTN602 defines
FMSP_SCTN0602_LISTDICT = {}  # SCTN602 defines
FMSP_SCTN0603_TUPDICTCMNTDICT = {}  # SCTN603 defines
FMSP_SCTN0603_TUPDICTDICT = {}  # SCTN603 defines
FMSP_SCTN0603_TUPDICTLISTCMNTDICT = {}  # SCTN600 defines
FMSP_SCTN0603_TUPDICTLISTDICT = {}  # SCTN603 defines


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN104 _LIST_ _DEF_
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
FMFO_SCTN0303_TUPDICTLIST = []  # SCTN303 FO.py TUPDICT list values


#
#
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * end of managed portions of FM.py
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
#


#
#
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of not managed portions of FM.py
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
#


# !_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!
# !_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!
# !_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# START OF TBGLST SCTN0105
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# !_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!
# !_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!
# !_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!


TBGLST = [
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	("CFVAL_ARCHIVEFILES", FMAXCF_SCTN0201_STRDEF, "ARCHIVEFILES", "ARCHIVEFILES", "archive files bool",),
	("CFVAL_DESTDIR", FMAXCF_SCTN0201_STRDEF, "DESTDIR", "OUTPUTDIR", "alias for OUTPUTDIR",),
	("CFVAL_DOALLCODEFILES", FMAXCF_SCTN0201_STRDEF, "DOALLCODEFILES", "DOALLCODEFILES", "do all code files bool",),
	("CFVAL_DOALLDOCSFILES", FMAXCF_SCTN0201_STRDEF, "DOALLDOCSFILES", "DOALLDOCSFILES", "do all docs files bool",),
	("CFVAL_DOALLKNOWNFILES", FMAXCF_SCTN0201_STRDEF, "DOALLKNOWNFILES", "DOALLKNOWNFILES", "do all known files bool",),
	("CFVAL_DOALLMEDIAFILES", FMAXCF_SCTN0201_STRDEF, "DOALLMEDIAFILES", "DOALLMEDIAFILES", "do all media files bool",),
	("CFVAL_DOALLPICSFILES", FMAXCF_SCTN0201_STRDEF, "DOALLPICSFILES", "DOALLPICSFILES", "do all pics files bool",),
	("CFVAL_DOALLTEXTFILES", FMAXCF_SCTN0201_STRDEF, "DOALLTEXTFILES", "DOALLTEXTFILES", "do all text files bool",),
	("CFVAL_DOALLUNKNOWNFILES", FMAXCF_SCTN0201_STRDEF, "DOALLUNKNOWNFILES", "DOALLUNKNOWNFILES", "do all unknown files bool",),
	("CFVAL_DOALLVIDSFILES", FMAXCF_SCTN0201_STRDEF, "DOALLVIDSFILES", "DOALLVIDSFILES", "do all video files bool",),
	("CFVAL_HASHER", FMAXCF_SCTN0201_STRDEF, "HASHER", "HASHER", "the hasher to use for random file names",),
	("CFVAL_IDMEDIAFILES", FMAXCF_SCTN0201_STRDEF, "IDMEDIAFILES", "IDMEDIAFILES", "ID media files bool",),
	("CFVAL_MOVEFILES", FMAXCF_SCTN0201_STRDEF, "MOVEFILES", "MOVEFILES", "MOVE/copy files bool",),
	("CFVAL_OUTPUTDIR", FMAXCF_SCTN0201_STRDEF, "OUTPUTDIR", "OUTPUTDIR", "output root",),
	("CFVAL_OVERWRITEFILES", FMAXCF_SCTN0201_STRDEF, "OVERWRITEFILES", "OVERWRITEFILES", "overwrite in place bool",),
	("CFVAL_RANDOM", FMAXCF_SCTN0201_STRDEF, "RANDOM", "RANDOM", "RANDOM/pattern file names bool",),
	("CFVAL_RENAMEFILES", FMAXCF_SCTN0201_STRDEF, "RENAMEFILES", "RENAMEFILES", "RENAME/copy file names bool",),
	("CFVAL_SHOWHELP", FMAXCF_SCTN0201_STRDEF, "SHOWHELP", "SHOWHELP", "show help for selected options, defaults to all",),
	("CFVAL_SOURCEDIR", FMAXCF_SCTN0201_STRDEF, "SOURCEDIR", "SOURCEDIR", "source directory default '.'",),
	("CFVAL_SPREADFILES", FMAXCF_SCTN0201_STRDEF, "SPREADFILES", "SPREADFILES", "SPREAD/one-destDir for files bool",),
	("CFVAL_STRIPMEDIAFILES", FMAXCF_SCTN0201_STRDEF, "STRIPMEDIAFILES", "STRIPMEDIAFILES", "strip media files bool",),
	("CFVAL_TESTMEDIAFILES", FMAXCF_SCTN0201_STRDEF, "TESTMEDIAFILES", "TESTMEDIAFILES", "test media files bool",),
	("CFVAL_TRIALRUN", FMAXCF_SCTN0201_STRDEF, "TRIALRUN", "TRIALRUN", "trial run bool",),
	("CFVAL__OPT_ARCHIVEFILES", FMAXCF_SCTN0202_OPTIONSDICTVALADD, "ARCHIVEFILES", "False", "archive files bool False default",),
	("CFVAL__OPT_DESTDIR", FMAXCF_SCTN0202_OPTIONSDICTSTRADD, "DESTDIR", "/storage/media/source/**", "default output directory '/storage/media/source/**'",),
	("CFVAL__OPT_DOALLCODEFILES", FMAXCF_SCTN0202_OPTIONSDICTVALADD, "DOALLCODEFILES", "False", "do all code files bool False default",),
	("CFVAL__OPT_DOALLDOCSFILES", FMAXCF_SCTN0202_OPTIONSDICTVALADD, "DOALLDOCSFILES", "False", "do all docs files bool False default",),
	("CFVAL__OPT_DOALLKNOWNFILES", FMAXCF_SCTN0202_OPTIONSDICTVALADD, "DOALLKNOWNFILES", "False", "do all known files bool False default",),
	("CFVAL__OPT_DOALLMEDIAFILES", FMAXCF_SCTN0202_OPTIONSDICTVALADD, "DOALLMEDIAFILES", "True", "do all media files (defined in SCTN0304) bool True default",),
	("CFVAL__OPT_DOALLPICSFILES", FMAXCF_SCTN0202_OPTIONSDICTVALADD, "DOALLPICSFILES", "False", "do all pics files bool True default (because DOALLMEDIAFILES defaults to True)",),
	("CFVAL__OPT_DOALLTEXTFILES", FMAXCF_SCTN0202_OPTIONSDICTVALADD, "DOALLTEXTFILES", "False", "do all text files bool False default",),
	("CFVAL__OPT_DOALLUNKNOWNFILES", FMAXCF_SCTN0202_OPTIONSDICTVALADD, "DOALLUNKNOWNFILES", "False", "do all unknown files False default",),
	("CFVAL__OPT_DOALLVIDSFILES", FMAXCF_SCTN0202_OPTIONSDICTVALADD, "DOALLVIDSFILES", "False", "do all known vids files True default (because DOALLMEDIAFILES defaults to True)",),
	("CFVAL__OPT_HASHER", FMAXCF_SCTN0202_OPTIONSDICTVALADD, "HASHER", "HASH_blake2b", "hash used to make random file names RANDOM=True + RENAMEFILES=True",),
	("CFVAL__OPT_IDMEDIAFILES", FMAXCF_SCTN0202_OPTIONSDICTVALADD, "IDMEDIAFILES", "True", "ID or not media filetypes bool default True",),
	("CFVAL__OPT_MOVEFILES", FMAXCF_SCTN0202_OPTIONSDICTVALADD, "MOVEFILES", "True", "Move/copy files bool",),
	("CFVAL__OPT_OUTPUTDIR", FMAXCF_SCTN0202_OPTIONSDICTSTRADD, "OUTPUTDIR", "/storage/media/Source/**", "default output directory '/storage/media/source/**'",),
	("CFVAL__OPT_OVERWRITEFILES", FMAXCF_SCTN0202_OPTIONSDICTVALADD, "OVERWRITEFILES", "False", "OVERWRITE/simple-rename files, either in place, or in DESTDIR",),
	("CFVAL__OPT_RANDOM", FMAXCF_SCTN0202_OPTIONSDICTVALADD, "RANDOM", "False", "RANDOM/pattern renam bool",),
	("CFVAL__OPT_RENAMEFILES", FMAXCF_SCTN0202_OPTIONSDICTVALADD, "RENAMEFILES", "False", "RENAME/as-is file naming bool",),
	("CFVAL__OPT_SHOWHELP", FMAXCF_SCTN0202_OPTIONSDICTVALADD, "SHOWHELP", "False", "print help (defaults to all) for all selected options and exit without processing any files",),
	("CFVAL__OPT_SOURCEDIR", FMAXCF_SCTN0202_OPTIONSDICTSTRADD, "SOURCEDIR", ".", "source directory, defaults to '.' or the current directory when invoked",),
	("CFVAL__OPT_SPREADFILES", FMAXCF_SCTN0202_OPTIONSDICTVALADD, "SPREADFILES", "False", "SPREAD/allInOne files bool",),
	("CFVAL__OPT_STRIPMEDIAFILES", FMAXCF_SCTN0202_OPTIONSDICTVALADD, "STRIPMEDIAFILES", "True", "STRIP/dont media filetypes",),
	("CFVAL__OPT_TESTMEDIAFILES", FMAXCF_SCTN0202_OPTIONSDICTVALADD, "TESTMEDIAFILES", "True", "test media filetypes bool default True",),
	("CFVAL__OPT_TRIALRUN", FMAXCF_SCTN0202_OPTIONSDICTVALADD, "TRIALRUN", "False", "OUTPUT what would be done/execute as configured",),
	("CFVAL__PARM_ARCHIVEFILESF", FMAXCF_SCTN0202_OPTIONSVALADD, "-arc", "ARCHIVEFILES", "False", "destination is a single or spread directory-root (SPREADFILES; not currently implemented)",),
	("CFVAL__PARM_ARCHIVEFILEST", FMAXCF_SCTN0202_OPTIONSVALADD, "-ARC", "ARCHIVEFILES", "True", "destination is an archive file (not currently implemented)",),
	("CFVAL__PARM_DESTDIR00", FMAXCF_SCTN0202_OPTIONSSTRADD, "-dd=", "DESTDIR", "/storage/media/picDest//**", "set DESTDIR and pattern (defaults to **)",),
	("CFVAL__PARM_DESTDIR01", FMAXCF_SCTN0202_OPTIONSSTRADD, "-dd=", "OUTPUTDIR", "/storage/media/picDest//**", "set OUTPUTDIR and pattern (defaults to **)",),
	("CFVAL__PARM_DOALLCODEFILESF", FMAXCF_SCTN0202_OPTIONSVALADD, "-docode", "DOALLCODEFILES", "False", "don't process code filetypes",),
	("CFVAL__PARM_DOALLCODEFILESF01", FMAXCF_SCTN0202_OPTIONSADDHELPLINE, "-docode", "select DOALLKNOWNFILES True first, then set this False to ignore code filetypes",),
	("CFVAL__PARM_DOALLCODEFILEST", FMAXCF_SCTN0202_OPTIONSVALADD, "-DOCODE", "DOALLCODEFILES", "True", "process code filetypes",),
	("CFVAL__PARM_DOALLDOCSFILESF", FMAXCF_SCTN0202_OPTIONSVALADD, "-dodocs", "DOALLDOCSFILES", "False", "don't process docs filetypes",),
	("CFVAL__PARM_DOALLDOCSFILESF01", FMAXCF_SCTN0202_OPTIONSADDHELPLINE, "-dodocs", "select DOALLKNOWNFILES True first, then set this False to ignore docs filetypes",),
	("CFVAL__PARM_DOALLDOCSFILEST", FMAXCF_SCTN0202_OPTIONSVALADD, "-DODOCS", "DOALLDOCSFILES", "True", "process docs filetypes",),
	("CFVAL__PARM_DOALLKNOWNFILESF", FMAXCF_SCTN0202_OPTIONSVALADD, "-doknown", "DOALLKNOWNFILES", "False", "don't process known filetypes",),
	("CFVAL__PARM_DOALLKNOWNFILESF01", FMAXCF_SCTN0202_OPTIONSADDHELPLINE, "-doknown", "select DOALLKNOWNFILES True first, then set this False to ignore known filetypes",),
	("CFVAL__PARM_DOALLKNOWNFILEST", FMAXCF_SCTN0202_OPTIONSVALADD, "-DOKNOWN", "DOALLKNOWNFILES", "True", "process known filetypes",),
	("CFVAL__PARM_DOALLKNOWNFILEST01", FMAXCF_SCTN0202_OPTIONSADDHELPLINE, "-DOKNOWN", "set this first, then deselect individual types to remove filetypes from the list of processed filetypes",),
	("CFVAL__PARM_DOALLMEDIAFILESF", FMAXCF_SCTN0202_OPTIONSVALADD, "-domedia", "DOALLMEDIAFILES", "False", "don't process media filetypes",),
	("CFVAL__PARM_DOALLMEDIAFILESF01", FMAXCF_SCTN0202_OPTIONSADDHELPLINE, "-domedia", "set DOALLKNOWNFILES True first, then set this False to ignore media filetypes",),
	("CFVAL__PARM_DOALLMEDIAFILESF02", FMAXCF_SCTN0202_OPTIONSADDHELPLINE, "-domedia", "select this True first, then set a media False type to ignore that filetype",),
	("CFVAL__PARM_DOALLMEDIAFILEST", FMAXCF_SCTN0202_OPTIONSVALADD, "-DOMEDIA", "DOALLMEDIAFILES", "True", "process medial filetypes",),
	("CFVAL__PARM_DOALLMEDIAFILEST01", FMAXCF_SCTN0202_OPTIONSADDHELPLINE, "-domedia", "select this True first, then set a media False type to ignore that filetype",),
	("CFVAL__PARM_DOALLPICSFILESF", FMAXCF_SCTN0202_OPTIONSVALADD, "-dopics", "DOALLPICSFILES", "False", "don't process pics filetypes",),
	("CFVAL__PARM_DOALLPICSFILEST", FMAXCF_SCTN0202_OPTIONSVALADD, "-DOPICS", "DOALLPICSFILES", "True", "process pics files",),
	("CFVAL__PARM_DOALLTEXTFILESF", FMAXCF_SCTN0202_OPTIONSVALADD, "-dotext", "DOALLTEXTFILES", "False", "don't process test filetypes",),
	("CFVAL__PARM_DOALLTEXTFILEST", FMAXCF_SCTN0202_OPTIONSVALADD, "-DOTEXT", "DOALLTEXTFILES", "True", "process text filetypes",),
	("CFVAL__PARM_DOALLUNKNOWNFILESF", FMAXCF_SCTN0202_OPTIONSVALADD, "-dounk", "DOALLUNKNOWNFILES", "False", "don't process unknown filetypes",),
	("CFVAL__PARM_DOALLUNKNOWNFILEST", FMAXCF_SCTN0202_OPTIONSVALADD, "-DOUNK", "DOALLUNKNOWNFILES", "True", "process unknown filetypes",),
	("CFVAL__PARM_DOALLVIDSFILESF", FMAXCF_SCTN0202_OPTIONSVALADD, "-dovids", "DOALLVIDSFILES", "False", "don't process vids filetypes",),
	("CFVAL__PARM_DOALLVIDSFILEST", FMAXCF_SCTN0202_OPTIONSVALADD, "-DOVIDS", "DOALLVIDSFILES", "True", "process vids filetypes",),
	("CFVAL__PARM_HASHER", FMAXCF_SCTN0202_OPTIONSVALADD, "-h=", "HASHER", "HASH_blake2b", "set the hasher to be used for random file renaming",),
	("CFVAL__PARM_IDMEDIAFILESF", FMAXCF_SCTN0202_OPTIONSVALADD, "-i", "IDMEDIAFILES", "False", "don't ID media files",),
	("CFVAL__PARM_IDMEDIAFILEST", FMAXCF_SCTN0202_OPTIONSVALADD, "-I", "IDMEDIAFILES", "True", "ID media files",),
	("CFVAL__PARM_MOVEFILESF", FMAXCF_SCTN0202_OPTIONSVALADD, "-m", "MOVEFILES", "False", "copy files",),
	("CFVAL__PARM_MOVEFILEST", FMAXCF_SCTN0202_OPTIONSVALADD, "-M", "MOVEFILES", "True", "move files; cross volume safe",),
	("CFVAL__PARM_OUTPUTDIR00", FMAXCF_SCTN0202_OPTIONSSTRADD, "-o=", "OUTPUTDIR", "/storage/media/picDest/**", "set OUTPUTDIR and pattern (defaults to **)",),
	("CFVAL__PARM_OUTPUTDIR01", FMAXCF_SCTN0202_OPTIONSSTRADD, "-o=", "DESTDIR", "/storage/media/picDest/**", "set DESTDIR and pattern (defaults to **)",),
	("CFVAL__PARM_OVERWRITEFILESF", FMAXCF_SCTN0202_OPTIONSVALADD, "-o", "OVERWRITEFILES", "False", "don't overwrite files of the same name, simple rename as needed",),
	("CFVAL__PARM_OVERWRITEFILEST", FMAXCF_SCTN0202_OPTIONSVALADD, "-O", "OVERWRITEFILES", "True", "overwrite files of the same name",),
	("CFVAL__PARM_RANDOMF", FMAXCF_SCTN0202_OPTIONSVALADD, "-rnd", "RANDOM", "False", "use the pattern specified in DESTDIR parameter, defaults to '*' which uses the same filename, if RENAMEFILES is True",),
	("CFVAL__PARM_RANDOMT", FMAXCF_SCTN0202_OPTIONSVALADD, "-RND", "RANDOM", "True", "use specified hasher to create a random filename to write/archive if RENAMEFILES is True",),
	("CFVAL__PARM_RENAMEFILESF", FMAXCF_SCTN0202_OPTIONSVALADD, "-rn", "RENAMEFILES", "False", "don't rename files in DESTDIR",),
	("CFVAL__PARM_RENAMEFILEST", FMAXCF_SCTN0202_OPTIONSVALADD, "-RN", "RENAMEFILES", "True", "rename files in DESTDIR",),
	("CFVAL__PARM_SHOWHELP", FMAXCF_SCTN0202_OPTIONSVALADD, "--help", "SHOWHELP", "False", "show help for selected options, defaults to all, and exit without doing anything",),
	("CFVAL__PARM_SHOWHELP", FMAXCF_SCTN0202_OPTIONSVALADD, "-h", "SHOWHELP", "False", "show help for selected options, defaults to all, and exit without doing anything",),
	("CFVAL__PARM_SHOWHELP", FMAXCF_SCTN0202_OPTIONSVALADD, "-help", "SHOWHELP", "False", "show help for selected options, defaults to all, and exit without doing anything",),
	("CFVAL__PARM_SOURCEDIR", FMAXCF_SCTN0202_OPTIONSSTRADD, "-sd=", "SOURCEDIR", ".", "set SOURCEDIR and file pattern (defaults to **)",),
	("CFVAL__PARM_SPREADFILESF", FMAXCF_SCTN0202_OPTIONSVALADD, "-sf", "SPREADFILES", "False", "spread files among a numbered",),
	("CFVAL__PARM_SPREADFILEST", FMAXCF_SCTN0202_OPTIONSVALADD, "-SF", "SPREADFILES", "True", "spread files among a numbered directory structure at DESTDIR",),
	("CFVAL__PARM_STRIPMEDIAFILESF", FMAXCF_SCTN0202_OPTIONSVALADD, "-sm", "STRIPMEDIAFILES", "False", "don't strip media files of metadata",),
	("CFVAL__PARM_STRIPMEDIAFILEST", FMAXCF_SCTN0202_OPTIONSVALADD, "-SM", "STRIPMEDIAFILES", "True", "strip media files of metadata",),
	("CFVAL__PARM_TESTMEDIAFILESF", FMAXCF_SCTN0202_OPTIONSVALADD, "-tm", "TESTMEDIAFILES", "False", "don't test media files",),
	("CFVAL__PARM_TESTMEDIAFILEST", FMAXCF_SCTN0202_OPTIONSVALADD, "-TM", "TESTMEDIAFILES", "True", "test media files",),
	("CFVAL__PARM_TRIALRUNF", FMAXCF_SCTN0202_OPTIONSVALADD, "-t", "TRIALRUN", "False", "don't output to STDOUT the things that would happen to any files, DO THEM",),
	("CFVAL__PARM_TRIALRUNT", FMAXCF_SCTN0202_OPTIONSVALADD, "-T", "TRIALRUN", "True", "output to STDOUT the things that would happen to any files, without doing them",),
	("FMAXCF", FMAX_NOP, "FMAX_TBGLST_CF_BEGINS",),
	("FMAXCF_SCTN0003_LAMBDADEF", FMAXFM_SCTN0101_AXDEF, "define a lambda function <NAC><NAME><lambda str>",),
	("FMAXCF_SCTN0003_TYPEDEF", FMAXFM_SCTN0101_AXDEF, "define a fake type used in the translation dict <NAC><NAME><TYPE>",),
	("FMAXCF_SCTN0201_STRDEF", FMAXFM_SCTN0101_AXDEF, "define a STR in SCTN21 <NAC><NAME><str>",),
	("FMAXCF_SCTN0201_VALDEF", FMAXFM_SCTN0101_AXDEF, "define a VAL in SCTN21 <NAC><NAME><VAL>",),
	("FMAXCF_SCTN0202_OPTIONSADDHELPLINE", FMAXFM_SCTN0101_AXDEF, "add a line to the help for a PARM, after the comment is automatically added<NAC><PARM><ADDONHELPLINE>",),
	("FMAXCF_SCTN0202_OPTIONSDICTSTRADD", FMAXFM_SCTN0101_AXDEF, "define a OPTNAME: 'str' in SCTN202 <NAC><KEY><PARM><STRDEFAULT>",),
	("FMAXCF_SCTN0202_OPTIONSDICTVALADD", FMAXFM_SCTN0101_AXDEF, "define a OPTNAME: VAL in SCTN202 <NAC><KEY><PARM><VALDEFAULT>",),
	("FMAXCF_SCTN0202_OPTIONSSTRADD", FMAXFM_SCTN0101_AXDEF, "define a '-a[=]' in SCTN22 <NAC><PARM><KEY><VAL>",),
	("FMAXCF_SCTN0202_OPTIONSVALADD", FMAXFM_SCTN0101_AXDEF, "define a '-a[=]' in SCTN22 <NAC><PARM><KEY><VAL>",),
	("FMAXCF_SCTN0203_DICTDEF", FMAXFM_SCTN0101_AXDEF, "define a dict in SCTN203 <NAC><DICTNAME><DICTMODE>",),
	("FMAXCF_SCTN0203_DICTSTRADD", FMAXFM_SCTN0101_AXDEF, "define a dict STR in SCTN203 <NAC><DICTNAME><STR>",),
	("FMAXCF_SCTN0203_DICTVALADD", FMAXFM_SCTN0101_AXDEF, "define a dict VAL in SCTN203 <NAC><DICTNAME><VAL>",),
	("FMAXCF_SCTN0204_LISTDEF", FMAXFM_SCTN0101_AXDEF, "define a list in SCTN204 <NAC><LISTNAME>",),
	("FMAXCF_SCTN0204_LISTSTRADD", FMAXFM_SCTN0101_AXDEF, "define a list STR in SCTN204 <NAC><LISTNAME><STR>",),
	("FMAXCF_SCTN0204_LISTVALADD", FMAXFM_SCTN0101_AXDEF, "define a VAL in a list in SCTN204 <NAC><LISTNAME><VAL>",),
	("FMAXCF_____", FMAX_NOP, "FMAX_TBGLST_CF_ENDS",),
	("FMAXFM", FMAX_NOP, "FMAX_TBGLST_FM_BEGINS",),
	("FMAXFM_SCTN0101_AXDEF", FMAXFM_SCTN0101_AXDEF, "define a new FM action <NAC>",),
	("FMAXFM_SCTN0102_STRDEF", FMAXFM_SCTN0101_AXDEF, "define a FM string <NAC><VALNAME><STR>",),
	("FMAXFM_SCTN0102_VALDEF", FMAXFM_SCTN0101_AXDEF, "define a FM value_ <NAC><VALNAME><VAL>",),
	("FMAXFM_SCTN0103_DICTDEF", FMAXFM_SCTN0101_AXDEF, "define a dict for FM <NAC>",),
	("FMAXFM_SCTN0104_LISTDEF", FMAXFM_SCTN0101_AXDEF, "define a list in FM <NAC>",),
	("FMAXFM_____", FMAX_NOP, "FMAX_TBGLST_FM_ENDS",),
	("FMAXFO", FMAX_NOP, "FMAX_TBGLST_FO_BEGINS",),
	("FMAXFO_SCTN0300_STRDEF", FMAXFM_SCTN0101_AXDEF, "add a string <NAC><STRNAME><STR>",),
	("FMAXFO_SCTN0300_VALDEF", FMAXFM_SCTN0101_AXDEF, "add a value to a dict <NAC><VALNAME><VAL>",),
	("FMAXFO_SCTN0301_DICTDEF", FMAXFM_SCTN0101_AXDEF, "define a dict in FO.py <NAC>",),
	("FMAXFO_SCTN0301_DICTDEF", FMAXFM_SCTN0101_AXDEF, "define a dict in FO.py <NAC><DICTNAME>",),
	("FMAXFO_SCTN0301_DICTSTRADD", FMAXFM_SCTN0101_AXDEF, "add a string to a dict <NAC><DICTNAME><STRNAME><STR>",),
	("FMAXFO_SCTN0301_DICTVALADD", FMAXFM_SCTN0101_AXDEF, "add a string to a dict <NAC><DICTNAME><VALNAME><VAL>",),
	("FMAXFO_SCTN0301_STRDICTSTRADD", FMAXFM_SCTN0101_AXDEF, "add a STR string to a dict <NAC><DICTNAME><STR><STR>",),
	("FMAXFO_SCTN0301_STRDICTVALADD", FMAXFM_SCTN0101_AXDEF, "add a STR val to a dict <NAC><DICTNAME><STR><VAL>",),
	("FMAXFO_SCTN0302_LISTDEF", FMAXFM_SCTN0101_AXDEF, "define a list in FO.py <NAC><LISTNAME>",),
	("FMAXFO_SCTN0302_LISTSTRADD", FMAXFM_SCTN0101_AXDEF, "add a string to a list <NAC><LISTNAME><STR>",),
	("FMAXFO_SCTN0302_LISTVALADD", FMAXFM_SCTN0101_AXDEF, "add a string to a list <NAC><LISTNAME><VAL>",),
	("FMAXFO_SCTN0303_TUPDICTDEF", FMAXFM_SCTN0101_AXDEF, "define a TUPDICT <NAC><TUPDICTNAME>",),
	("FMAXFO_SCTN0303_TUPDICTSTRADD", FMAXFM_SCTN0101_AXDEF, "add a string to a dict <NAC><DICTNAME><STRNAME><STR>",),
	("FMAXFO_SCTN0303_TUPDICTSTRSTRADD", FMAXFM_SCTN0101_AXDEF, "add a STR string to a dict <NAC><DICTNAME><STR><STR>",),
	("FMAXFO_SCTN0303_TUPDICTSTRVALADD", FMAXFM_SCTN0101_AXDEF, "add a STR val to a dict <NAC><DICTNAME><STR><VAL>",),
	("FMAXFO_SCTN0303_TUPDICTVALADD", FMAXFM_SCTN0101_AXDEF, "add a string to a dict <NAC><DICTNAME><VALNAME><VAL>",),
	("FMAXFO_SCTN0304_EXTENSIONADD", FMAXFM_SCTN0101_AXDEF, "add an extension <NAC><TYPE><EXTENSION>",),
	("FMAXFO_SCTN0304_EXTENSIONTYPEDEF", FMAXFM_SCTN0101_AXDEF, "add an extension type <NAC><TYPE><MEDIABOOL>",),
	("FMAXFO_____", FMAX_NOP, "FMAX_TBGLST_FO_ENDS",),
	("FMAXSP", FMAX_NOP, "FMAX_TBGLST_SP_BEGINS",),
	("FMAXSP_SCTN0600_STRDEF", FMAXFM_SCTN0101_AXDEF, "define a SP str <NAC><STRNAME><STR>",),
	("FMAXSP_SCTN0600_VALDEF", FMAXFM_SCTN0101_AXDEF, "define a SP val <NAC><VAL>",),
	("FMAXSP_SCTN0601_DICTDEF", FMAXFM_SCTN0101_AXDEF, "define a dict for SP <NAC><DICTNAME>",),
	("FMAXSP_SCTN0601_DICTSTRADD", FMAXFM_SCTN0101_AXDEF, "define a dict str entry SP <NAC><DICTNAME><KEY><STR>",),
	("FMAXSP_SCTN0601_DICTVALADD", FMAXFM_SCTN0101_AXDEF, "define a dict val entry SP <NAC><DICTNAME><KEY><VAL>",),
	("FMAXSP_SCTN0602_LISTDEF", FMAXFM_SCTN0101_AXDEF, "define a list in SP <NAC><LISTNAME>",),
	("FMAXSP_SCTN0602_LISTSTRADD", FMAXFM_SCTN0101_AXDEF, "define a list str in SP <NAC><LISTNAME><KEY><STR>",),
	("FMAXSP_SCTN0602_LISTVALADD", FMAXFM_SCTN0101_AXDEF, "define a list str in SP <NAC><LISTNAME><KEY><VAL>",),
	("FMAXSP_SCTN0603_TUPDICTDEF", FMAXFM_SCTN0101_AXDEF, "define a (tuple dict function) set <NAC><TUPDICTNAME>",),
	("FMAXSP_SCTN0603_TUPDICTLISTDEF", FMAXFM_SCTN0101_AXDEF, "define a list entry in a tupdict <NAC><TUPDICTNAME><KEY>",),
	("FMAXSP_SCTN0603_TUPDICTLISTSTRADD", FMAXFM_SCTN0101_AXDEF, "define a list STR entry in a tupdict <NAC><TUPDICTNAME><KEY><STR>",),
	("FMAXSP_SCTN0603_TUPDICTLISTVALADD", FMAXFM_SCTN0101_AXDEF, "define a list VAL entry in a tupdict <NAC><TUPDICTNAME><KEY><VAL>",),
	("FMAXSP_SCTN0603_TUPDICTSTRADD", FMAXFM_SCTN0101_AXDEF, "define a tuple dict str <NAC><TUPDICTNAME><KEY><VAL>",),
	("FMAXSP_SCTN0603_TUPDICTVALADD", FMAXFM_SCTN0101_AXDEF, "define a tuple dict str <NAC><TUPDICTNAME><KEY><VAL>",),
	("FMAXSP_____", FMAX_NOP, "FMAX_TBGLST_SP_ENDS",),
	("FMAX_NOP", FMAXFM_SCTN0101_AXDEF, "skip this entry",),
	("FMCF", FMAX_NOP, "FMCF_TBGLST_BEGINS",),
	("FMCF_SCTN0003_TYPECMNTDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN009 types comments",),
	("FMCF_SCTN0003_TYPEDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN003 types",),
	("FMCF_SCTN0201_DEFCMNTDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN201 defines comments dict",),
	("FMCF_SCTN0201_DEFDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN201 defines dict",),
	("FMCF_SCTN0202_OPTIONSCMNTDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN202 OPTIONS comments dict",),
	("FMCF_SCTN0202_OPTIONSDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN202 OPTIONS dict",),
	("FMCF_SCTN0202_OPTIONSDICTCMNTDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN202 OPTIONSDICT comments dict",),
	("FMCF_SCTN0202_OPTIONSDICTDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN202 OPTIONSDICT",),
	("FMCF_SCTN0202_OPTIONSHELPDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN202 OPTIONS HELPDICT",),
	("FMCF_SCTN0203_DICTCMNTDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN203 dict comments dict",),
	("FMCF_SCTN0203_DICTDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN203 dict dict",),
	("FMCF_SCTN0204_LISTCMNTDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN204 list comments dict",),
	("FMCF_SCTN0204_LISTDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN204 list dict",),
	("FMCF_____", FMAX_NOP, "FMCF_TBGLST_ENDS",),
	("FMFM", FMAX_NOP, "FMFM_TBGLST_BEGINS",),
	("FMFM_SCTN0101_AXCMNTDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN003 types",),
	("FMFM_SCTN0101_AXCMNTDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN101 FMAX defined",),
	("FMFM_SCTN0101_AXDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN101 FMAX defined",),
	("FMFM_SCTN0102_VALCMNTDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN102 val",),
	("FMFM_SCTN0102_VALDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN102 val",),
	("FMFM_SCTN0103_DICTCMNTDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN103 dict defined",),
	("FMFM_SCTN0103_DICTDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN103 dict defined",),
	("FMFM_SCTN0104_LISTCMNTDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN201 device defines",),
	("FMFM_SCTN0104_LISTDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN201 device defines",),
	("FMFM_____", FMAX_NOP, "FMFM_TBGLST_ENDS",),
	("FMFO", FMAX_NOP, "FMFO_TBGLST_BEGINS",),
	("FMFO_SCTN0300_VALCMNTDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN300 FO.py comment",),
	("FMFO_SCTN0300_VALDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN300 FO.py values",),
	("FMFO_SCTN0301_DICTCMNTDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN301 FO.py comment",),
	("FMFO_SCTN0301_DICTDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN301 FO.py dict values",),
	("FMFO_SCTN0302_LISTCMNTDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN302 FO.py comment",),
	("FMFO_SCTN0302_LISTDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN302 FO.py list values",),
	("FMFO_SCTN0303_TUPDICTCMNTDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN303 FO.py TUPDICT comment",),
	("FMFO_SCTN0303_TUPDICTDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN303 FO.py TUPDICT values",),
	("FMFO_SCTN0303_TUPDICTLIST", FMAXFM_SCTN0104_LISTDEF, "SCTN303 FO.py TUPDICT list values",),
	("FMFO_SCTN0304_EXTENSIONLOOKUPDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN304 FO.py EXTENSIONLOOKUP values",),
	("FMFO_SCTN0304_EXTENSIONSCMNTDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN304 FO.py EXTENSIONS comment",),
	("FMFO_SCTN0304_EXTENSIONSTYPESDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN304 FO.py EXTENSIONSTYPES values",),
	("FMFO_SCTN0304_MEDIAFILELSTSTR", FMAXFM_SCTN0102_STRDEF, "FMFO_SCTN0304_MEDIAFILELSTSTR", "", "SCTN304 FO.py EXTENSIONS media filetypes list in FM.py while parsing",),
	("FMFO_____", FMAX_NOP, "FMFO_TBGLST_ENDS",),
	("FMSP", FMAX_NOP, "FMSP_TBGLST_BEGINS",),
	("FMSP_SCTN0600_DEFCMNTDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN600 defines",),
	("FMSP_SCTN0600_DEFCMNTDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN600 defines",),
	("FMSP_SCTN0600_DEFCMNTDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN600 defines",),
	("FMSP_SCTN0600_DEFDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN600 defines",),
	("FMSP_SCTN0600_DEFDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN600 defines",),
	("FMSP_SCTN0600_DEFDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN600 defines",),
	("FMSP_SCTN0601_DICTCMNTDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN600 defines",),
	("FMSP_SCTN0601_DICTCMNTDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN601 defines",),
	("FMSP_SCTN0601_DICTCMNTDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN601 defines",),
	("FMSP_SCTN0601_DICTDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN600 defines",),
	("FMSP_SCTN0601_DICTDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN601 defines",),
	("FMSP_SCTN0601_DICTDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN601 defines",),
	("FMSP_SCTN0602_LISTCMNTDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN600 defines",),
	("FMSP_SCTN0602_LISTCMNTDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN602 defines",),
	("FMSP_SCTN0602_LISTCMNTDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN602 defines",),
	("FMSP_SCTN0602_LISTDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN600 defines",),
	("FMSP_SCTN0602_LISTDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN602 defines",),
	("FMSP_SCTN0602_LISTDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN602 defines",),
	("FMSP_SCTN0603_TUPDICTCMNTDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN600 defines",),
	("FMSP_SCTN0603_TUPDICTCMNTDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN603 defines",),
	("FMSP_SCTN0603_TUPDICTCMNTDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN603 defines",),
	("FMSP_SCTN0603_TUPDICTDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN600 defines",),
	("FMSP_SCTN0603_TUPDICTDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN603 defines",),
	("FMSP_SCTN0603_TUPDICTDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN603 defines",),
	("FMSP_SCTN0603_TUPDICTLISTCMNTDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN600 defines",),
	("FMSP_SCTN0603_TUPDICTLISTDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN600 defines",),
	("FMSP_SCTN0603_TUPDICTLISTDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN603 defines",),
	("FMSP_SCTN0603_TUPDICTLISTDICT", FMAXFM_SCTN0103_DICTDEF, "SCTN603 defines",),
	("FMSP_____", FMAX_NOP, "FMSP_TBGLST_ENDS",),
	("FOVAL_BLACKTAIL", FMAXFO_SCTN0300_STRDEF, "BLACKTAIL", "BLACKTAIL", "",),
	("FOVAL_CODE", FMAXFO_SCTN0300_STRDEF, "CODE", "CODE", "",),
	("FOVAL_CODEFILES", FMAXFO_SCTN0300_STRDEF, "CODEFILES", "CODEFILES", "",),
	("FOVAL_DIRBLACKLIST", FMAXFO_SCTN0300_STRDEF, "DIRBLACKLIST", "[a-zA-Z0-9./]+", "",),
	("FOVAL_DIRWHITELIST", FMAXFO_SCTN0300_STRDEF, "DIRWHITELIST", "[^a-zA-Z0-9./]+", "",),
	("FOVAL_DOCS", FMAXFO_SCTN0300_STRDEF, "DOCS", "DOCS", "",),
	("FOVAL_EMPTYENTRY", FMAXFO_SCTN0303_TUPDICTDEF, "EMPTYENTRY", "an empty entry tupdict+function for each file/directory",),
	("FOVAL_EMPTYENTRY", FMAXFO_SCTN0303_TUPDICTSTRADD, "EMPTYENTRY", "BLACKTAIL", "", "",),
	("FOVAL_EMPTYENTRY", FMAXFO_SCTN0303_TUPDICTSTRADD, "EMPTYENTRY", "EXTHEAD", "", "",),
	("FOVAL_EMPTYENTRY", FMAXFO_SCTN0303_TUPDICTSTRADD, "EMPTYENTRY", "EXTTAIL", "", "",),
	("FOVAL_EMPTYENTRY", FMAXFO_SCTN0303_TUPDICTSTRADD, "EMPTYENTRY", "PATH", "", "",),
	("FOVAL_EMPTYENTRY", FMAXFO_SCTN0303_TUPDICTSTRADD, "EMPTYENTRY", "PATHHEAD", "", "",),
	("FOVAL_EMPTYENTRY", FMAXFO_SCTN0303_TUPDICTSTRADD, "EMPTYENTRY", "PATHTAIL", "", "",),
	("FOVAL_EMPTYENTRY", FMAXFO_SCTN0303_TUPDICTSTRADD, "EMPTYENTRY", "WHITEFILENAME", "", "",),
	("FOVAL_EMPTYENTRY", FMAXFO_SCTN0303_TUPDICTSTRADD, "EMPTYENTRY", "WHITEFULLPATH", "", "",),
	("FOVAL_EMPTYENTRY", FMAXFO_SCTN0303_TUPDICTVALADD, "EMPTYENTRY", "ENTRYMODE", "0", "",),
	("FOVAL_EMPTYENTRY", FMAXFO_SCTN0303_TUPDICTVALADD, "EMPTYENTRY", "ISADIR", "False", "",),
	("FOVAL_EMPTYENTRY", FMAXFO_SCTN0303_TUPDICTVALADD, "EMPTYENTRY", "ISAFILE", "False", "",),
	("FOVAL_EMPTYENTRY", FMAXFO_SCTN0303_TUPDICTVALADD, "EMPTYENTRY", "ISAKNOWNFILETYPE", "False", "",),
	("FOVAL_EMPTYENTRY", FMAXFO_SCTN0303_TUPDICTVALADD, "EMPTYENTRY", "ISAMEDIAFILETYPE", "False", "",),
	("FOVAL_EMPTYENTRY", FMAXFO_SCTN0303_TUPDICTVALADD, "EMPTYENTRY", "ISASYMLINK", "False", "",),
	("FOVAL_EMPTYENTRY", FMAXFO_SCTN0303_TUPDICTVALADD, "EMPTYENTRY", "ISUNKNOWNFILETYPE", "False", "",),
	("FOVAL_ENTRYMODE", FMAXFO_SCTN0300_STRDEF, "ENTRYMODE", "ENTRYMODE", "",),
	("FOVAL_EXTENSIONS", FMAXFO_SCTN0304_EXTENSIONADD, "CODE", ".c", "",),
	("FOVAL_EXTENSIONS", FMAXFO_SCTN0304_EXTENSIONADD, "CODE", ".php", "",),
	("FOVAL_EXTENSIONS", FMAXFO_SCTN0304_EXTENSIONADD, "CODE", ".py", "",),
	("FOVAL_EXTENSIONS", FMAXFO_SCTN0304_EXTENSIONADD, "PICS", ".bmp", "",),
	("FOVAL_EXTENSIONS", FMAXFO_SCTN0304_EXTENSIONADD, "PICS", ".gif", "",),
	("FOVAL_EXTENSIONS", FMAXFO_SCTN0304_EXTENSIONADD, "PICS", ".jpeg", "",),
	("FOVAL_EXTENSIONS", FMAXFO_SCTN0304_EXTENSIONADD, "PICS", ".jpg", "",),
	("FOVAL_EXTENSIONS", FMAXFO_SCTN0304_EXTENSIONADD, "PICS", ".png", "",),
	("FOVAL_EXTENSIONS", FMAXFO_SCTN0304_EXTENSIONADD, "PICS", ".webp", "",),
	("FOVAL_EXTENSIONS", FMAXFO_SCTN0304_EXTENSIONADD, "TEXT", ".lst", "",),
	("FOVAL_EXTENSIONS", FMAXFO_SCTN0304_EXTENSIONADD, "TEXT", ".lst.txt", "",),
	("FOVAL_EXTENSIONS", FMAXFO_SCTN0304_EXTENSIONADD, "VIDS", ".avi", "",),
	("FOVAL_EXTENSIONS", FMAXFO_SCTN0304_EXTENSIONADD, "VIDS", ".divx", "",),
	("FOVAL_EXTENSIONS", FMAXFO_SCTN0304_EXTENSIONADD, "VIDS", ".flv", "",),
	("FOVAL_EXTENSIONS", FMAXFO_SCTN0304_EXTENSIONADD, "VIDS", ".gifv", "",),
	("FOVAL_EXTENSIONS", FMAXFO_SCTN0304_EXTENSIONADD, "VIDS", ".m2ts", "",),
	("FOVAL_EXTENSIONS", FMAXFO_SCTN0304_EXTENSIONADD, "VIDS", ".m4a", "",),
	("FOVAL_EXTENSIONS", FMAXFO_SCTN0304_EXTENSIONADD, "VIDS", ".m4v", "",),
	("FOVAL_EXTENSIONS", FMAXFO_SCTN0304_EXTENSIONADD, "VIDS", ".mkv", "",),
	("FOVAL_EXTENSIONS", FMAXFO_SCTN0304_EXTENSIONADD, "VIDS", ".mov", "",),
	("FOVAL_EXTENSIONS", FMAXFO_SCTN0304_EXTENSIONADD, "VIDS", ".mp4", "",),
	("FOVAL_EXTENSIONS", FMAXFO_SCTN0304_EXTENSIONADD, "VIDS", ".mpeg", "",),
	("FOVAL_EXTENSIONS", FMAXFO_SCTN0304_EXTENSIONADD, "VIDS", ".mpg", "",),
	("FOVAL_EXTENSIONS", FMAXFO_SCTN0304_EXTENSIONADD, "VIDS", ".webm", "",),
	("FOVAL_EXTENSIONS", FMAXFO_SCTN0304_EXTENSIONADD, "VIDS", ".wmv", "",),
	("FOVAL_EXTENSIONTYPES", FMAXFO_SCTN0304_EXTENSIONTYPEDEF, "CODE", "False", "define CODE file extension",),
	("FOVAL_EXTENSIONTYPES", FMAXFO_SCTN0304_EXTENSIONTYPEDEF, "DOCS", "False", "define DOCS file extension",),
	("FOVAL_EXTENSIONTYPES", FMAXFO_SCTN0304_EXTENSIONTYPEDEF, "PICS", "True", "define PICS file extension",),
	("FOVAL_EXTENSIONTYPES", FMAXFO_SCTN0304_EXTENSIONTYPEDEF, "TEXT", "False", "define TEXT file extension",),
	("FOVAL_EXTENSIONTYPES", FMAXFO_SCTN0304_EXTENSIONTYPEDEF, "VIDS", "True", "define VIDS file extension",),
	("FOVAL_EXTHEAD", FMAXFO_SCTN0300_STRDEF, "EXTHEAD", "EXTHEAD", "",),
	("FOVAL_EXTTAIL", FMAXFO_SCTN0300_STRDEF, "EXTTAIL", "EXTTAIL", "",),
	("FOVAL_FILEWHITELIST", FMAXFO_SCTN0300_STRDEF, "FILEWHITELIST", "[^a-zA-Z0-9.]+", "",),
	("FOVAL_ILLEGALPATHS", FMAXFO_SCTN0302_LISTDEF, "ILLEGALPATHS", "list of absolute paths to be completely ignored if used",),
	("FOVAL_ILLEGALPATHS01", FMAXFO_SCTN0302_LISTSTRADD, "ILLEGALPATHS", "/", "do not operate on / ever",),
	("FOVAL_ILLEGALWILDCARDS", FMAXFO_SCTN0302_LISTDEF, "ILLEGALWILDCARDS", "list all of the portions of a filename which will result in an error [0:] based",),
	("FOVAL_ILLEGALWILDCARDS", FMAXFO_SCTN0302_LISTSTRADD, "ILLEGALWILDCARDS", "/bin/", "illegal wildcards, these are most often /path/ and will be [0:] based",),
	("FOVAL_ILLEGALWILDCARDS", FMAXFO_SCTN0302_LISTSTRADD, "ILLEGALWILDCARDS", "/boot/", "illegal wildcards, these are most often /path/ and will be [0:] based",),
	("FOVAL_ILLEGALWILDCARDS", FMAXFO_SCTN0302_LISTSTRADD, "ILLEGALWILDCARDS", "/dev/", "illegal wildcards, these are most often /path/ and will be [0:] based",),
	("FOVAL_ILLEGALWILDCARDS", FMAXFO_SCTN0302_LISTSTRADD, "ILLEGALWILDCARDS", "/efi/", "illegal wildcards, these are most often /path/ and will be [0:] based",),
	("FOVAL_ILLEGALWILDCARDS", FMAXFO_SCTN0302_LISTSTRADD, "ILLEGALWILDCARDS", "/etc/", "illegal wildcards, these are most often /path/ and will be [0:] based",),
	("FOVAL_ILLEGALWILDCARDS", FMAXFO_SCTN0302_LISTSTRADD, "ILLEGALWILDCARDS", "/home/", "illegal wildcards, these are most often /path/ and will be [0:] based",),
	("FOVAL_ILLEGALWILDCARDS", FMAXFO_SCTN0302_LISTSTRADD, "ILLEGALWILDCARDS", "/lib/", "illegal wildcards, these are most often /path/ and will be [0:] based",),
	("FOVAL_ILLEGALWILDCARDS", FMAXFO_SCTN0302_LISTSTRADD, "ILLEGALWILDCARDS", "/lib64/", "illegal wildcards, these are most often /path/ and will be [0:] based",),
	("FOVAL_ILLEGALWILDCARDS", FMAXFO_SCTN0302_LISTSTRADD, "ILLEGALWILDCARDS", "/media/", "illegal wildcards, these are most often /path/ and will be [0:] based",),
	("FOVAL_ILLEGALWILDCARDS", FMAXFO_SCTN0302_LISTSTRADD, "ILLEGALWILDCARDS", "/opt/", "illegal wildcards, these are most often /path/ and will be [0:] based",),
	("FOVAL_ILLEGALWILDCARDS", FMAXFO_SCTN0302_LISTSTRADD, "ILLEGALWILDCARDS", "/proc/", "illegal wildcards, these are most often /path/ and will be [0:] based",),
	("FOVAL_ILLEGALWILDCARDS", FMAXFO_SCTN0302_LISTSTRADD, "ILLEGALWILDCARDS", "/root/", "illegal wildcards, these are most often /path/ and will be [0:] based",),
	("FOVAL_ILLEGALWILDCARDS", FMAXFO_SCTN0302_LISTSTRADD, "ILLEGALWILDCARDS", "/run/", "illegal wildcards, these are most often /path/ and will be [0:] based",),
	("FOVAL_ILLEGALWILDCARDS", FMAXFO_SCTN0302_LISTSTRADD, "ILLEGALWILDCARDS", "/sbin/", "illegal wildcards, these are most often /path/ and will be [0:] based",),
	("FOVAL_ILLEGALWILDCARDS", FMAXFO_SCTN0302_LISTSTRADD, "ILLEGALWILDCARDS", "/srv/", "illegal wildcards, these are most often /path/ and will be [0:] based",),
	("FOVAL_ILLEGALWILDCARDS", FMAXFO_SCTN0302_LISTSTRADD, "ILLEGALWILDCARDS", "/sys/", "illegal wildcards, these are most often /path/ and will be [0:] based",),
	("FOVAL_ILLEGALWILDCARDS", FMAXFO_SCTN0302_LISTSTRADD, "ILLEGALWILDCARDS", "/tmp/", "illegal wildcards, these are most often /path/ and will be [0:] based",),
	("FOVAL_ILLEGALWILDCARDS", FMAXFO_SCTN0302_LISTSTRADD, "ILLEGALWILDCARDS", "/usr/", "illegal wildcards, these are most often /path/ and will be [0:] based",),
	("FOVAL_ILLEGALWILDCARDS", FMAXFO_SCTN0302_LISTSTRADD, "ILLEGALWILDCARDS", "/var/", "illegal wildcards, these are most often /path/ and will be [0:] based",),
	("FOVAL_ISADIR", FMAXFO_SCTN0300_STRDEF, "ISADIR", "ISADIR", "",),
	("FOVAL_ISAFILE", FMAXFO_SCTN0300_STRDEF, "ISAFILE", "ISAFILE", "",),
	("FOVAL_ISASYMLINK", FMAXFO_SCTN0300_STRDEF, "ISASYMLINK", "ISASYMLINK", "",),
	("FOVAL_ISMEDIAFILETYPE", FMAXFO_SCTN0300_STRDEF, "ISMEDIAFILETYPE", "ISMEDIAFILETYPE", "",),
	("FOVAL_ISUNKNOWNFILETYPE", FMAXFO_SCTN0300_STRDEF, "ISUNKNOWNFILETYPE", "ISUNKNOWNFILETYPE", "",),
	("FOVAL_KNOWNFILES", FMAXFO_SCTN0300_STRDEF, "KNOWNFILES", "KNOWNFILES", "",),
	("FOVAL_KNOWNFILETYPE", FMAXFO_SCTN0300_STRDEF, "KNOWNFILETYPE", "KNOWNFILETYPE", "",),
	("FOVAL_MEDIAFILES", FMAXFO_SCTN0300_STRDEF, "MEDIAFILES", "MEDIAFILES", "",),
	("FOVAL_NOTKNOWNFILES", FMAXFO_SCTN0300_STRDEF, "NOTKNOWNFILES", "NOTKNOWNFILES", "",),
	("FOVAL_NOTMEDIAFILES", FMAXFO_SCTN0300_STRDEF, "NOTMEDIAFILES", "NOTMEDIAFILES", "",),
	("FOVAL_NOTUNKNOWNFILES", FMAXFO_SCTN0300_STRDEF, "NOTUNKNOWNFILES", "NOTUNKNOWNFILES", "",),
	("FOVAL_PATH", FMAXFO_SCTN0300_STRDEF, "PATH", "PATH", "",),
	("FOVAL_PATHHEAD", FMAXFO_SCTN0300_STRDEF, "PATHHEAD", "PATHHEAD", "",),
	("FOVAL_PATHTAIL", FMAXFO_SCTN0300_STRDEF, "PATHTAIL", "PATHTAIL", "",),
	("FOVAL_PICS", FMAXFO_SCTN0300_STRDEF, "PICS", "PICS", "",),
	("FOVAL_RECURSE", FMAXFO_SCTN0300_STRDEF, "RECURSE", "RECURSE", "",),
	("FOVAL_SOURCEDIR", FMAXFO_SCTN0300_STRDEF, "SOURCEDIR", "SOURCEDIR", "",),
	("FOVAL_TEXT", FMAXFO_SCTN0300_STRDEF, "TEXT", "TEXT", "",),
	("FOVAL_UNKNOWNFILES", FMAXFO_SCTN0300_STRDEF, "UNKNOWNFILES", "UNKNOWNFILES", "",),
	("FOVAL_VIDS", FMAXFO_SCTN0300_STRDEF, "VIDS", "VIDS", "",),
	("FOVAL_WHITEFILENAME", FMAXFO_SCTN0300_STRDEF, "WHITEFILENAME", "WHITEFILENAME", "",),
	("FOVAL_WHITEFULLPATH", FMAXFO_SCTN0300_STRDEF, "WHITEFULLPATH", "WHITEFULLPATH", "",),

	("SPVAL_BUFSIZE", FMAXSP_SCTN0600_STRDEF, "BUFSIZE", "bufsize", "ARG keys",),
	("SPVAL_CAPOUT", FMAXSP_SCTN0600_STRDEF, "CAPOUT", "capture_output", "capture_output key",),
	("SPVAL_CHECK", FMAXSP_SCTN0600_STRDEF, "CHECK", "check", "check key",),
	("SPVAL_CLOSE_FDS", FMAXSP_SCTN0600_STRDEF, "CLOSE_FDS", "close_fds", "ARG key",),
	("SPVAL_CREATIONFLAGS", FMAXSP_SCTN0600_STRDEF, "CREATIONFLAGS", "creationflags", "ARG key",),
	("SPVAL_CWD", FMAXSP_SCTN0600_STRDEF, "CWD", "cwd", "cwd key",),
	("SPVAL_ENCODING", FMAXSP_SCTN0600_STRDEF, "ENCODING", "encoding", "encoding key",),
	("SPVAL_ENV", FMAXSP_SCTN0600_STRDEF, "ENV", "env", "env key",),
	("SPVAL_ERRORS", FMAXSP_SCTN0600_STRDEF, "ERRORS", "errors", "errors key",),
	("SPVAL_EXECUTABLE", FMAXSP_SCTN0600_STRDEF, "EXECUTABLE", "executable", "ARG key",),
	("SPVAL_EXTRA_GROUPS", FMAXSP_SCTN0600_STRDEF, "EXTRA_GROUPS", "extra_groups", "ARG key",),
	("SPVAL_GETDEPS", FMAXSP_SCTN0603_TUPDICTDEF, "ARGS_GETDEPS", "define empty ARGS_GETDEPS structures",),
	("SPVAL_GETDEPS_CAPOUT", FMAXSP_SCTN0603_TUPDICTVALADD, "ARGS_GETDEPS", "CAPOUT", "True", "default CAPOUT True",),
	("SPVAL_GETDEPS_POPENARGS_00", FMAXSP_SCTN0603_TUPDICTLISTDEF, "ARGS_GETDEPS", "POPENARGS", "default POPENARGS for getting deps",),
	("SPVAL_GETDEPS_POPENARGS_01", FMAXSP_SCTN0603_TUPDICTLISTSTRADD, "ARGS_GETDEPS", "POPENARGS", "trizen -Qi", "call trizen",),
	("SPVAL_GETDEPS_SHELL", FMAXSP_SCTN0603_TUPDICTVALADD, "ARGS_GETDEPS", "SHELL", "True", "default SHELL False",),
	("SPVAL_GETDEPS_TEXT", FMAXSP_SCTN0603_TUPDICTVALADD, "ARGS_GETDEPS", "TEXT", "True", "default SHELL False",),
	("SPVAL_GETFRGN", FMAXSP_SCTN0603_TUPDICTDEF, "ARGS_GETFRGN", "define empty ARGS_GETFRGN structures",),
	("SPVAL_GETFRGN_CAPOUT", FMAXSP_SCTN0603_TUPDICTVALADD, "ARGS_GETFRGN", "CAPOUT", "True", "default CAPOUT True",),
	("SPVAL_GETFRGN_POPENARGS_00", FMAXSP_SCTN0603_TUPDICTLISTDEF, "ARGS_GETFRGN", "POPENARGS", "define POPENARGS",),
	("SPVAL_GETFRGN_POPENARGS_01", FMAXSP_SCTN0603_TUPDICTLISTSTRADD, "ARGS_GETFRGN", "POPENARGS", "trizen -Qm", "call trizen",),
	("SPVAL_GETFRGN_SHELL", FMAXSP_SCTN0603_TUPDICTVALADD, "ARGS_GETFRGN", "SHELL", "True", "default SHELL False",),
	("SPVAL_GETFRGN_TEXT", FMAXSP_SCTN0603_TUPDICTVALADD, "ARGS_GETFRGN", "TEXT", "True", "default text True",),
	("SPVAL_GETQI", FMAXSP_SCTN0603_TUPDICTDEF, "ARGS_GETQI", "define empty ARGS_GETQI structures",),
	("SPVAL_GETQI_CAPOUT", FMAXSP_SCTN0603_TUPDICTVALADD, "ARGS_GETQI", "CAPOUT", "True", "default CAPOUT True",),
	("SPVAL_GETQI_POPENARGS_00", FMAXSP_SCTN0603_TUPDICTLISTDEF, "ARGS_GETQI", "POPENARGS", "default POPENARGS for getting deps",),
	("SPVAL_GETQI_POPENARGS_01", FMAXSP_SCTN0603_TUPDICTLISTSTRADD, "ARGS_GETQI", "POPENARGS", "trizen -Qi", "call trizen",),
	("SPVAL_GETQI_SHELL", FMAXSP_SCTN0603_TUPDICTVALADD, "ARGS_GETQI", "SHELL", "True", "default SHELL False",),
	("SPVAL_GETQI_TEXT", FMAXSP_SCTN0603_TUPDICTVALADD, "ARGS_GETQI", "TEXT", "True", "default SHELL False",),
	("SPVAL_GETSI", FMAXSP_SCTN0603_TUPDICTDEF, "ARGS_GETSI", "define empty ARGS_GETSI structures",),
	("SPVAL_GETSI_CAPOUT", FMAXSP_SCTN0603_TUPDICTVALADD, "ARGS_GETSI", "CAPOUT", "True", "default CAPOUT True",),
	("SPVAL_GETSI_POPENARGS_00", FMAXSP_SCTN0603_TUPDICTLISTDEF, "ARGS_GETSI", "POPENARGS", "default POPENARGS for getting deps",),
	("SPVAL_GETSI_POPENARGS_01", FMAXSP_SCTN0603_TUPDICTLISTSTRADD, "ARGS_GETSI", "POPENARGS", "trizen -Si", "call trizen",),
	("SPVAL_GETSI_SHELL", FMAXSP_SCTN0603_TUPDICTVALADD, "ARGS_GETSI", "SHELL", "True", "default SHELL False",),
	("SPVAL_GETSI_TEXT", FMAXSP_SCTN0603_TUPDICTVALADD, "ARGS_GETSI", "TEXT", "True", "default SHELL False",),
	("SPVAL_GROUP", FMAXSP_SCTN0600_STRDEF, "GROUP", "group", "ARG key",),
	("SPVAL_INPUT", FMAXSP_SCTN0600_STRDEF, "INPUT", "input", "input key",),
	("SPVAL_PASS_FDS", FMAXSP_SCTN0600_STRDEF, "PASS_FDS", "pass_fds", "ARG key",),
	("SPVAL_POPENARGS", FMAXSP_SCTN0600_STRDEF, "POPENARGS", "args", "popenargs key",),
	("SPVAL_PREEXEC_FN", FMAXSP_SCTN0600_STRDEF, "PREEXEC_FN", "preexec_fn", "ARG key",),
	("SPVAL_RESTORE_SIGNALS", FMAXSP_SCTN0600_STRDEF, "RESTORE_SIGNALS", "restore_signals", "ARG key",),
	("SPVAL_SHELL", FMAXSP_SCTN0600_STRDEF, "SHELL", "shell", "shell key",),
	("SPVAL_STARTUPINFO", FMAXSP_SCTN0600_STRDEF, "STARTUPINFO", "startupinfo", "ARG key",),
	("SPVAL_START_NEW_SESSION", FMAXSP_SCTN0600_STRDEF, "START_NEW_SESSION", "start_new_session", "ARG key",),
	("SPVAL_STDERR", FMAXSP_SCTN0600_STRDEF, "STDERR", "stderr", "stderr key",),
	("SPVAL_STDIN", FMAXSP_SCTN0600_STRDEF, "STDIN", "stdin", "stdin key",),
	("SPVAL_STDOUT", FMAXSP_SCTN0600_STRDEF, "STDOUT", "stdout", "stdout key",),
	("SPVAL_TEXT", FMAXSP_SCTN0600_STRDEF, "TEXT", "text", "ARG key",),
	("SPVAL_TIMEOUT", FMAXSP_SCTN0600_STRDEF, "TIMEOUT", "timeout", "timeout key",),
	("SPVAL_UMASK", FMAXSP_SCTN0600_STRDEF, "UMASK", "umask", "ARG key",),
	("SPVAL_UNIVERSAL_NEWLINES", FMAXSP_SCTN0600_STRDEF, "UNIVERSAL_NEWLINES", "universal_newlines", "ARG key",),
	("SPVAL_USER", FMAXSP_SCTN0600_STRDEF, "USER", "user", "ARG key",),

	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1
]
TBGLST.sort()


# !_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!
# !_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!
# !_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# END OF TBGLST SCTN0105
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# !_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!
# !_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!
# !_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# makeAComment
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def makeAComment(comment_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	strToRtn_ = ""
	strToRtn_ += f"""{CMNTLINE}{NEWLINE}# * {comment_}{NEWLINE}{CMNTLINE}{NEWLINE}"""
	return strToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# makeAComment
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def makeAWideComment(comment_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	strToRtn_ = ""
	strToRtn_ += f"""#{NEWLINE}#{NEWLINE}{CMNTLINE}{NEWLINE}# * {comment_}{NEWLINE}{CMNTLINE}{NEWLINE}#{NEWLINE}#{NEWLINE}"""
	return strToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# makeADict
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def makeADict(dictName_, dictComment_, dictItems_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	strToRtn_ = ""
	strToRtn_ += f"""{dictName_} = {OBRCE}  # {dictComment_}
{dictItems_}{CBRCE}{NEWLINE}{NEWLINE}{NEWLINE}"""
	return strToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# makeAList
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def makeAList(listName_, listComment_, listItems_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	strToRtn_ = ""
	strToRtn_ += f"""{listName_} = {OBRKT}  # {listComment_}
{listItems_}{CBRKT}{NEWLINE}{NEWLINE}{NEWLINE}"""
	return strToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# makeATupDict
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def makeATupDict(tupDictName_, tupDictItems_, tupDictSidecar_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	strToRtn_ = ""
	strToRtn1_ = ""

	# 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥
	if tupDictSidecar_ is None:
		strToRtn_ += f"""{makeAComment(f"start of {tupDictName_} structures")}
{tupDictName_}TUP = {OPAREN}
{tupDictItems_}{CPAREN}{NEWLINE}{NEWLINE}def {tupDictName_}DICT{OPAREN}{CPAREN}:
{NTAB(1)}return dict{OPAREN}{OPAREN}x, y{CPAREN} for x, y in {tupDictName_}TUP{CPAREN}{NEWLINE}{NEWLINE}{NEWLINE}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	else:
		strToRtn_ += f"""{makeAComment(f"start of {tupDictName_} structures")}{NEWLINE}"""
		for key_, items_ in tupDictSidecar_.items():
			strToRtn_ += f"""{tupDictName_}_{key_}TUP = {OPAREN}{NEWLINE}{items_}{CPAREN}{NEWLINE}{NEWLINE}"""
			strToRtn1_ += f"""{NTAB(1)}listToRtn_ = list((x) for x in {tupDictName_}_{key_}TUP){NEWLINE}"""
		strToRtn_ += f"""{tupDictName_}TUP = {OPAREN}
{tupDictItems_}{CPAREN}{NEWLINE}{NEWLINE}def {tupDictName_}DICT{OPAREN}{CPAREN}:
{NTAB(1)}dictToRtn_ = dict{OPAREN}{OPAREN}x, y{CPAREN} for x, y in {tupDictName_}TUP{CPAREN}{NEWLINE}{strToRtn1_}{NTAB(1)}return listToRtn_, dictToRtn_{NEWLINE}{NEWLINE}{NEWLINE}"""

	# ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1
	return strToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# readFileToStr
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def readFileToStr(FILENAME_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	strToRtn_ = ""
	with open(FILENAME_, "tr") as FDIN:
		strToRtn_ += FDIN.read()
	return strToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# doErrorItem
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def doErrorItem(message_, itemToError_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	print(f"""{NEWLINE}{message_}{NEWLINE}is a tuple {isinstance(itemToError_, tuple)}{NEWLINE}item as parsed{NEWLINE}{repr(itemToError_)}{NEWLINE}""")
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# explodeItem
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def explodeItem(itemToExplode_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	strToRtn_ = ""
	strToRtn_ += f"""{NTAB(1)}{OPAREN}{DBLQT}{itemToExplode_[0]}{DBLQT}, {itemToExplode_[1]}, """
	for TI1_ in range(2, len(itemToExplode_)):
		strToRtn_ += f"""{DBLQT}{itemToExplode_[TI1_]}{DBLQT}, """
	strToRtn_ = f"""{strToRtn_[:-1]}{CPAREN},{NEWLINE}"""
	return strToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# FM_MAKE_CF_BEGINS
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# makeCF
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def makeCF():
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	strToRtn_ = ""
	strToRtn_ += f"""{readFileToStr(CFTOP_NAME)}{readFileToStr(SCTN0102NAME)}"""

	# 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥
	strToRtn_ += f"""{makeAComment("SCTN0201 CF defines")}"""
	for name_, value_ in FMCF_SCTN0201_DEFDICT.items():
		strToRtn_ += f"""{name_} = {value_}  # {FMCF_SCTN0201_DEFCMNTDICT[name_]}{NEWLINE}"""
	strToRtn_ += f"""{NEWLINE}{NEWLINE}"""
	# ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1

	# 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥
	strToRtn_ += f"""{makeAComment("SCTN0202 options structures")}"""
	strToRtn1_ = ""
	strToRtn2_ = ""
	strToRtn1_ += f"""OPTIONS = {OBRCE}{NEWLINE}{FOLD1STARTHERELN}"""
	strToRtn2_ += f"""OPTIONSHELPDICT = {OBRCE}{NEWLINE}{FOLD1STARTHERELN}"""
	for name_, values_ in FMCF_SCTN0202_OPTIONSDICT.items():
		strToRtn1_ += f"""{NTAB(1)}{DBLQT}{name_}{DBLQT}: {OBRCE}{NEWLINE}{NTAB(1)}{FOLD2STARTHERELN}{values_}{NTAB(1)}{CBRCE},{NEWLINE}{NTAB(1)}{FOLD2ENDHERELN}"""
		strToRtn2_ += f"""{NTAB(1)}{DBLQT}{name_}{DBLQT}: \{NEWLINE}{NTAB(1)}{FOLD2STARTHERELN}{TRIQT}{FMCF_SCTN0202_OPTIONSHELPDICT[name_]}{NTAB(1)}{TRIQT},{NEWLINE}{NTAB(1)}{FOLD2ENDHERELN}"""
	strToRtn1_ += f"""{CBRCE}{NEWLINE}{FOLD1ENDHERELN}{NEWLINE}"""
	strToRtn2_ += f"""{CBRCE}{NEWLINE}{FOLD1ENDHERELN}{NEWLINE}"""
	strToRtn_ += f"""{strToRtn1_}{strToRtn2_}"""

	# ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥ ⥣1⥥
	strToRtn_ += f"""OPTIONSDICT = {OBRCE}{NEWLINE}"""
	for name_, value_ in FMCF_SCTN0202_OPTIONSDICTDICT.items():
		strToRtn_ += f"""{value_}"""
	strToRtn_ += f"""{CBRCE}{NEWLINE}{NEWLINE}{NEWLINE}"""
	# ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1

	strToRtn_ += f"""{makeAWideComment("end of managed sections of CF.py")}{NEWLINE}{NEWLINE}"""
	return strToRtn_

	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1
# FM_MAKE_CF_ENDS


# FM_MAKE_FM_BEGINS
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# makeFM
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def makeFM():
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	# 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥
	strToRtn_ = ""
	strToRtn_ += f"""{readFileToStr(FMTOP_NAME)}{readFileToStr(SCTN0102NAME)}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	strToRtn_ += f"""{makeAComment("SCTN003 TYPEs and lambda")}"""
	for thisName_, value_ in FMCF_SCTN0003_TYPEDICT.items():
		strToRtn_ += f"""{thisName_} = {value_}  # {FMCF_SCTN0003_TYPECMNTDICT[thisName_]}{NEWLINE}"""
	strToRtn_ += NEWLINE + NEWLINE

	## ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	strToRtn_ += f"""{makeAComment("SCTN101 FMAX _DEF_")}"""
	strToRtn01_ = ""
	for thisName_, value_ in FMFM_SCTN0101_AXDICT.items():
		strToRtn_ += f"""{thisName_} = {value_}  # {FMFM_SCTN0101_AXCMNTDICT[thisName_]}{NEWLINE}"""
		strToRtn01_ += f"""{NTAB(1)}{thisName_},  # {FMFM_SCTN0101_AXCMNTDICT[thisName_]}{NEWLINE}"""
	strToRtn_ += f"""{NEWLINE}{NEWLINE}FMAXFM_AXLST = {OBRKT}{NEWLINE}{strToRtn01_}{CBRKT}{NEWLINE}{NEWLINE}{NEWLINE}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	strToRtn_ += f"""{makeAComment("SCTN102 VAL _DEF_")}"""
	strToRtn01_ = ""
	for thisName_, value_ in FMFM_SCTN0102_VALDICT.items():
		strToRtn_ += f"""{thisName_} = {value_}  # {FMFM_SCTN0102_VALCMNTDICT[thisName_]}{NEWLINE}"""
	strToRtn_ += f"""{NEWLINE}{NEWLINE}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	strToRtn_ += f"""{makeAComment("SCTN103 _DICT_ _DEF_")}"""
	strToRtn01_ = ""
	for thisName_, value_ in FMFM_SCTN0103_DICTDICT.items():
		strToRtn_ += f"""{thisName_} = {OBRCE}{CBRCE}  # {FMFM_SCTN0103_DICTCMNTDICT[thisName_]}{NEWLINE}"""
	strToRtn_ += f"""{NEWLINE}{NEWLINE}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	strToRtn_ += f"""{makeAComment("SCTN104 _LIST_ _DEF_")}"""
	for thisName_, value_ in FMFM_SCTN0104_LISTDICT.items():
		strToRtn_ += f"""{thisName_} = {value_}  # {FMFM_SCTN0104_LISTCMNTDICT[thisName_]}{NEWLINE}"""
	strToRtn_ += f"""{NEWLINE}{NEWLINE}{makeAWideComment("end of managed portions of FM.py")}{NEWLINE}{NEWLINE}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	strToRtn_ += f"""{NTAB(1)}global {BKSLSH}{NEWLINE}"""
	for key_ in FMFM_SCTN0102_VALDICT:
		strToRtn_ += f"""{NTAB(2)}{key_}, {BKSLSH}{NEWLINE}"""
	for key_ in FMFM_SCTN0103_DICTDICT:
		strToRtn_ += f"""{NTAB(2)}{key_}, {BKSLSH}{NEWLINE}"""
	for key_ in FMFM_SCTN0104_LISTDICT:
		strToRtn_ += f"""{NTAB(2)}{key_}, {BKSLSH}{NEWLINE}"""
	strToRtn_ = f"""{strToRtn_[:-4]}{NEWLINE}"""

	return strToRtn_
	# ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1

	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1
# FM_MAKE_FM_ENDS


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# doErrorItem
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def doErrorItem(message_, itemToError_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	print(f"""{NEWLINE}{message_}{NEWLINE}is a tuple {isinstance(itemToError_, tuple)}{NEWLINE}item as parsed{NEWLINE}{repr(itemToError_)}{NEWLINE}""")
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# explodeItem
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def explodeItem(itemToExplode_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	strToRtn_ = ""
	strToRtn_ += f"""{NTAB(1)}{OPAREN}{DBLQT}{itemToExplode_[0]}{DBLQT}, {itemToExplode_[1]}, """
	for TI1_ in range(2, len(itemToExplode_)):
		strToRtn_ += f"""{DBLQT}{itemToExplode_[TI1_]}{DBLQT}, """
	strToRtn_ = f"""{strToRtn_[:-1]}{CPAREN},{NEWLINE}"""
	return strToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# FM_MAKE_FO_BEGINS
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# makeFM
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def makeFO():
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	# 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥
	strToRtn_ = ""
	strToRtn_ += f"""{readFileToStr(FOTOP_NAME)}{readFileToStr(SCTN0102NAME)}"""


	return strToRtn_
	# ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1

	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1
# FM_MAKE_FO_ENDS


# MAKESP BEGINS
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# makeSP
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def makeSP():
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	# 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥
	strToRtn_ = ""
	strToRtn_ += f"""{readFileToStr(SPTOP_NAME)}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	strToRtn_ += f"""{makeAComment("SCTN600 SP defs")}#{NEWLINE}"""
	for thisName_, item_ in FMSP_SCTN0600_DEFDICT.items():
		strToRtn_ += f"""{thisName_} = {item_}  # {FMSP_SCTN0600_DEFCMNTDICT[thisName_]}{NEWLINE}"""
	strToRtn_ += f"{NEWLINE}{NEWLINE}"

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	strToRtn_ += f"""{makeAComment("SCTN601 SP dicts")}#{NEWLINE}"""
	for thisName_, items_ in FMSP_SCTN0601_DICTDICT.items():
		strToRtn_ += f"""{makeADict(thisName_, FMSP_SCTN0601_DICTCMNTDICT[thisName_], items_)}"""
	strToRtn_ += f"{NEWLINE}{NEWLINE}"

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	strToRtn_ += f"""{makeAComment("SCTN062 SP lists")}#{NEWLINE}"""
	for thisName_, items_ in FMSP_SCTN0602_LISTDICT.items():
		strToRtn_ += f"""{makeAList(thisName_, FMSP_SCTN0602_LISTCMNTDICT[thisName_], items_)}"""
	strToRtn_ += f"{NEWLINE}{NEWLINE}"

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	strToRtn_ += f"""{makeAComment("SCTN603 SP tupdict")}#{NEWLINE}"""
	for thisName_, items_ in FMSP_SCTN0603_TUPDICTDICT.items():
		if thisName_ in FMSP_SCTN0603_TUPDICTLISTDICT:
			strToRtn_ += f"""{makeATupDict(thisName_, items_, FMSP_SCTN0603_TUPDICTLISTDICT[thisName_])}"""
		else:
			strToRtn_ += f"""{makeATupDict(thisName_, items_, None)}"""

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣
	strToRtn_ += f"""{makeAWideComment("end of managed sections of SP.py")}"""
	return strToRtn_

	# ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1
# MAKESP ENDS

# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# parseTBGLST
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def parseTBGLST(FDTBGLST):
	global \
		FMFO_SCTN0304_MEDIAFILELSTSTR, \
		FMCF_SCTN0003_TYPECMNTDICT, \
		FMCF_SCTN0003_TYPEDICT, \
		FMCF_SCTN0201_DEFCMNTDICT, \
		FMCF_SCTN0201_DEFDICT, \
		FMCF_SCTN0202_OPTIONSCMNTDICT, \
		FMCF_SCTN0202_OPTIONSDICT, \
		FMCF_SCTN0202_OPTIONSDICTCMNTDICT, \
		FMCF_SCTN0202_OPTIONSDICTDICT, \
		FMCF_SCTN0202_OPTIONSHELPDICT, \
		FMCF_SCTN0203_DICTCMNTDICT, \
		FMCF_SCTN0203_DICTDICT, \
		FMCF_SCTN0204_LISTCMNTDICT, \
		FMCF_SCTN0204_LISTDICT, \
		FMFM_SCTN0101_AXCMNTDICT, \
		FMFM_SCTN0101_AXDICT, \
		FMFM_SCTN0102_VALCMNTDICT, \
		FMFM_SCTN0102_VALDICT, \
		FMFM_SCTN0103_DICTCMNTDICT, \
		FMFM_SCTN0103_DICTDICT, \
		FMFM_SCTN0104_LISTCMNTDICT, \
		FMFM_SCTN0104_LISTDICT, \
		FMFO_SCTN0300_VALCMNTDICT, \
		FMFO_SCTN0300_VALDICT, \
		FMFO_SCTN0301_DICTCMNTDICT, \
		FMFO_SCTN0301_DICTDICT, \
		FMFO_SCTN0302_LISTCMNTDICT, \
		FMFO_SCTN0302_LISTDICT, \
		FMFO_SCTN0303_TUPDICTCMNTDICT, \
		FMFO_SCTN0303_TUPDICTDICT, \
		FMFO_SCTN0304_EXTENSIONLOOKUPDICT, \
		FMFO_SCTN0304_EXTENSIONSCMNTDICT, \
		FMFO_SCTN0304_EXTENSIONSTYPESDICT, \
		FMSP_SCTN0600_DEFCMNTDICT, \
		FMSP_SCTN0600_DEFDICT, \
		FMSP_SCTN0601_DICTCMNTDICT, \
		FMSP_SCTN0601_DICTDICT, \
		FMSP_SCTN0602_LISTCMNTDICT, \
		FMSP_SCTN0602_LISTDICT, \
		FMSP_SCTN0603_TUPDICTCMNTDICT, \
		FMSP_SCTN0603_TUPDICTDICT, \
		FMSP_SCTN0603_TUPDICTLISTCMNTDICT, \
		FMSP_SCTN0603_TUPDICTLISTDICT, \
		FMFO_SCTN0303_TUPDICTLIST
		# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1

	# 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥ 1⥥
	for thisItem_ in TBGLST:
		# 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ 2⥥ for thisItem_ in TBGLST:

		FDTBGLST.write(f"{explodeItem(thisItem_)}")
		thisItemLen_ = len(thisItem_)
		if thisItemLen_ < 3:
			doErrorItem("fewer than 3 elements", thisItem_)
			continue
		if not isinstance(thisItem_, tuple):
			doErrorItem("not a tuple", thisItem_)
			continue
		thisName_ = thisItem_[0]
		thisAX_ = thisItem_[1]
		thisComment_ = thisItem_[-1]
		if thisAX_ not in FMAXFM_AXLST:
			doErrorItem("not a supported action in FM", thisItem_)
			continue

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		if thisAX_ is None or thisAX_ == FMAX_NOP:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# FM_PARSE_CF_BEGINS
	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXCF_SCTN0003_LAMBDADEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisLambdaName_ = thisItem_[2]
			thisLambdaVal_ = thisItem_[3]
			FMCF_SCTN0003_TYPEDICT[thisLambdaName_] = f"lambda {thisLambdaVal_}"
			FMCF_SCTN0003_TYPECMNTDICT[thisLambdaName_] = "{thisComment_}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXCF_SCTN0003_TYPEDEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisTypeName_ = thisItem_[2]
			thisType_ = thisItem_[3]
			FMCF_SCTN0003_TYPEDICT[thisTypeName_] = f"{DBLQT}{thisType_}{DBLQT}"
			FMCF_SCTN0003_TYPECMNTDICT[thisTypeName_] = f"{thisComment_}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXCF_SCTN0201_STRDEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisValName_ = thisItem_[2]
			thisVal_ = thisItem_[3]
			FMCF_SCTN0201_DEFDICT[thisValName_] = f"{DBLQT}{thisVal_}{DBLQT}"
			FMCF_SCTN0201_DEFCMNTDICT[thisValName_] = f"{thisComment_}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXCF_SCTN0201_VALDEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisValName_ = thisItem_[2]
			thisVal_ = thisItem_[3]
			FMCF_SCTN0201_DEFDICT[thisValName_] = f"{thisVal_}"
			FMCF_SCTN0201_DEFCMNTDICT[thisValName_] = f"{thisComment_}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXCF_SCTN0202_OPTIONSADDHELPLINE:  # define a '-a[=]' in SCTN22 <NAC><KEY><PARM><VAL>
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 4:
				doErrorItem("not 4 items", thisItem_)
				continue
			thisParm_ = thisItem_[2]
			if thisParm_ not in FMCF_SCTN0202_OPTIONSHELPDICT:
				FMCF_SCTN0202_OPTIONSHELPDICT[thisParm_] = ""
			FMCF_SCTN0202_OPTIONSHELPDICT[thisParm_] += f"""{thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXCF_SCTN0202_OPTIONSSTRADD:  # define a '-a[=]' in SCTN22 <NAC><KEY><PARM><VAL>
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisParm_ = thisItem_[2]
			thisKey_ = thisItem_[3]
			thisVal_ = thisItem_[4]
			if thisParm_ not in FMCF_SCTN0202_OPTIONSDICT:
				FMCF_SCTN0202_OPTIONSDICT[thisParm_] = ""
			if thisParm_ not in FMCF_SCTN0202_OPTIONSHELPDICT:
				FMCF_SCTN0202_OPTIONSHELPDICT[thisParm_] = ""
			FMCF_SCTN0202_OPTIONSDICT[thisParm_] += f"""{NTAB(2)}{DBLQT}{thisKey_}{DBLQT}: {DBLQT}{thisVal_}{DBLQT},  # {thisComment_}{NEWLINE}"""
			FMCF_SCTN0202_OPTIONSHELPDICT[thisParm_] += f"""{thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXCF_SCTN0202_OPTIONSVALADD:  # define a '-a[=]' in SCTN22 <NAC><KEY><PARM><VAL>
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisParm_ = thisItem_[2]
			thisKey_ = thisItem_[3]
			thisVal_ = thisItem_[4]
			if thisParm_ not in FMCF_SCTN0202_OPTIONSDICT:
				FMCF_SCTN0202_OPTIONSDICT[thisParm_] = ""
			if thisParm_ not in FMCF_SCTN0202_OPTIONSHELPDICT:
				FMCF_SCTN0202_OPTIONSHELPDICT[thisParm_] = ""
			FMCF_SCTN0202_OPTIONSDICT[thisParm_] += f"""{NTAB(2)}{thisKey_}: {thisVal_},  # {thisComment_}{NEWLINE}"""
			FMCF_SCTN0202_OPTIONSHELPDICT[thisParm_] += f"""{thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXCF_SCTN0202_OPTIONSDICTSTRADD:  # define a OPTNAME: 'str' in SCTN202 <NAC><KEY><STRDEFAULT>
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisKey_ = thisItem_[2]
			thisVal_ = thisItem_[3]
			FMCF_SCTN0202_OPTIONSDICTDICT[thisName_] = f"{NTAB(1)}{thisKey_}: {DBLQT}{thisVal_}{DBLQT},  # {thisComment_}{NEWLINE}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXCF_SCTN0202_OPTIONSDICTVALADD:  # define a OPTNAME: VAL in SCTN202 <NAC><KEY><VALDEFAULT>
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisKey_ = thisItem_[2]
			thisVal_ = thisItem_[3]
			FMCF_SCTN0202_OPTIONSDICTDICT[thisName_] = f"{NTAB(1)}{thisKey_}: {thisVal_},  # {thisComment_}{NEWLINE}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXCF_SCTN0204_LISTDEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 4:
				doErrorItem("not 4 items", thisItem_)
				continue
			thisListName_ = thisItem_[2]
			FMCF_SCTN0204_LISTDICT[thisListName_] = ""
			FMCF_SCTN0204_LISTCMNTDICT[thisListName_] = f"{thisComment_}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXCF_SCTN0204_LISTSTRADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisListName_ = thisItem_[2]
			thisVal_ = thisItem_[3]
			FMCF_SCTN0204_LISTDICT[thisListName_] += f"{NTAB(1)}f{DBLQT}{thisVal_}{DBLQT},  # {thisComment_}{NEWLINE}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXCF_SCTN0204_LISTSTRADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisListName_ = thisItem_[2]
			thisVal_ = thisItem_[3]
			FMCF_SCTN0204_LISTDICT[thisListName_] += f"{NTAB(1)}{DBLQT}{thisVal_}{DBLQT},  # {thisComment_}{NEWLINE}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXCF_SCTN0204_LISTVALADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisListName_ = thisItem_[2]
			thisVal_ = thisItem_[3]
			FMCF_SCTN0204_LISTDICT[thisListName_] += f"{NTAB(1)}{thisVal_},  # {thisComment_}{NEWLINE}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2
	# FM_PARSE_CF_ENDS

	# FM_PARSE_FM_BEGINS
	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXFM_SCTN0101_AXDEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 3:
				doErrorItem("not 3 items", thisItem_)
				continue
			FMFM_SCTN0101_AXDICT[thisName_] = f"{DBLQT}{thisName_}{DBLQT}"
			FMFM_SCTN0101_AXCMNTDICT[thisName_] = f"{thisComment_}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXFM_SCTN0102_STRDEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisValName_ = thisItem_[2]
			thisVal_ = thisItem_[3]
			FMFM_SCTN0102_VALDICT[thisValName_] = f"""{DBLQT}{thisVal_}{DBLQT}"""
			FMFM_SCTN0102_VALCMNTDICT[thisValName_] = f"{thisComment_}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXFM_SCTN0102_VALDEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisValName_ = thisItem_[2]
			thisVal_ = thisItem_[3]
			FMFM_SCTN0102_VALDICT[thisValName_] = thisVal_
			FMFM_SCTN0102_VALCMNTDICT[thisValName_] = f"{thisComment_}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXFM_SCTN0103_DICTDEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 3:
				doErrorItem("not 3 items", thisItem_)
				continue
			FMFM_SCTN0103_DICTDICT[thisName_] = f"{OBRCE}{CBRCE}"
			FMFM_SCTN0103_DICTCMNTDICT[thisName_] = f"{thisComment_}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXFM_SCTN0104_LISTDEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 3:
				doErrorItem("not 3 items", thisItem_)
				continue
			FMFM_SCTN0104_LISTDICT[thisName_] = f"{OBRKT}{CBRKT}"
			FMFM_SCTN0104_LISTCMNTDICT[thisName_] = f"{thisComment_}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2
	# FM_PARSE_FM_ENDS

	# FM_PARSE_FO_BEGINS
	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXFO_SCTN0300_STRDEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisValName_ = thisItem_[2]
			thisVal_ = thisItem_[3]
			FMFO_SCTN0300_VALDICT[thisValName_] = f"""{DBLQT}{thisVal_}{DBLQT}"""
			FMFO_SCTN0300_VALCMNTDICT[thisValName_] = thisComment_
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXFO_SCTN0300_VALDEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisValName_ = thisItem_[2]
			thisVal_ = thisItem_[3]
			FMFO_SCTN0300_VALDICT[thisValName_] = f"""{thisVal_}"""
			FMFO_SCTN0300_VALCMNTDICT[thisValName_] = thisComment_
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXFO_SCTN0301_DICTDEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 4:
				doErrorItem("not 4 items", thisItem_)
				continue
			thisDictName_ = thisItem_[2]
			if thisDictName_ not in FMFO_SCTN0301_DICTDICT:
				FMFO_SCTN0301_DICTDICT[thisDictName_] = ""
			FMFO_SCTN0301_DICTCMNTDICT[thisValName_] = thisComment_
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXFO_SCTN0301_DICTSTRADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisDictName_ = thisItem_[2]
			thisKey_ = thisItem_[3]
			thisVal_ = thisItem_[4]
			if thisDictName_ not in FMFO_SCTN0301_DICTDICT:
				FMFO_SCTN0301_DICTDICT[thisDictName_] = ""
			FMFO_SCTN0301_DICTDICT[thisDictName_] += f"""{NTAB(1)}{thisKey_}: {DBLQT}{thisVal_}{DBLQT},  # {thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXFO_SCTN0301_DICTVALADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisDictName_ = thisItem_[2]
			thisKey_ = thisItem_[3]
			thisVal_ = thisItem_[4]
			if thisDictName_ not in FMFO_SCTN0301_DICTDICT:
				FMFO_SCTN0301_DICTDICT[thisDictName_] = ""
			FMFO_SCTN0301_DICTDICT[thisDictName_] += f"""{NTAB(1)}{thisKey_}: {thisVal_},  # {thisComment_}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXFO_SCTN0302_LISTDEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 4:
				doErrorItem("not 4 items", thisItem_)
				continue
			thisDictName_ = thisItem_[2]
			if thisDictName_ not in FMFO_SCTN0302_LISTDICT:
				FMFO_SCTN0302_LISTDICT[thisDictName_] = ""
			FMFO_SCTN0302_LISTCMNTDICT[thisDictName_] = thisComment_
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXFO_SCTN0302_LISTSTRADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisDictName_ = thisItem_[2]
			thisVal_ = thisItem_[3]
			if thisDictName_ not in FMFO_SCTN0302_LISTDICT:
				FMFO_SCTN0302_LISTDICT[thisDictName_] = ""
			FMFO_SCTN0302_LISTDICT[thisDictName_] += f"""{NTAB(1)}{DBLQT}{thisVal_}{DBLQT},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXFO_SCTN0302_LISTVALADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisDictName_ = thisItem_[2]
			thisKey_ = thisItem_[3]
			thisVal_ = thisItem_[4]
			if thisDictName_ not in FMFO_SCTN0302_LISTDICT:
				FMFO_SCTN0302_LISTDICT[thisDictName_] = ""
			FMFO_SCTN0302_LISTDICT[thisDictName_] += f"""{NTAB(1)}{thisVal_},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXFO_SCTN0303_TUPDICTDEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 4:
				doErrorItem("not 4 items", thisItem_)
				continue
			thisDictName_ = thisItem_[2]
			if thisDictName_ not in FMFO_SCTN0303_TUPDICTDICT:
				FMFO_SCTN0303_TUPDICTDICT[thisDictName_] = ""
			FMFO_SCTN0303_TUPDICTCMNTDICT[thisValName_] = thisComment_
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXFO_SCTN0303_TUPDICTSTRADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisDictName_ = thisItem_[2]
			thisKey_ = thisItem_[3]
			thisVal_ = thisItem_[4]
			if thisDictName_ not in FMFO_SCTN0303_TUPDICTDICT:
				FMFO_SCTN0303_TUPDICTDICT[thisDictName_] = ""
			FMFO_SCTN0303_TUPDICTDICT[thisDictName_] += f"""{NTAB(1)}{OPAREN}{thisKey_}, {DBLQT}{thisVal_}{DBLQT}{CPAREN},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXFO_SCTN0303_TUPDICTVALADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisDictName_ = thisItem_[2]
			thisKey_ = thisItem_[3]
			thisVal_ = thisItem_[4]
			if thisDictName_ not in FMFO_SCTN0303_TUPDICTDICT:
				FMFO_SCTN0303_TUPDICTDICT[thisDictName_] = ""
			FMFO_SCTN0303_TUPDICTDICT[thisDictName_] += f"""{NTAB(1)}{OPAREN}{thisKey_}, {thisVal_}{CPAREN},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXFO_SCTN0304_EXTENSIONADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisExtensionType_ = thisItem_[2]
			thisExtension_ = thisItem_[3]
			if thisExtensionType_ not in FMFO_SCTN0304_EXTENSIONSTYPESDICT:
				FMFO_SCTN0304_EXTENSIONSTYPESDICT[thisExtensionType_] = ""
			FMFO_SCTN0304_EXTENSIONSTYPESDICT[thisExtensionType_] += f"""{NTAB(2)}{DBLQT}{thisExtension_.lower()}{DBLQT},  # {thisComment_}{NEWLINE}{NTAB(2)}{DBLQT}{thisExtension_.upper()}{DBLQT},{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXFO_SCTN0304_EXTENSIONTYPEDEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisExtensionType_ = thisItem_[2]
			thisMediaBool_ = thisItem_[3]
			if thisExtensionType_ not in FMFO_SCTN0304_EXTENSIONSTYPESDICT:
				FMFO_SCTN0304_EXTENSIONSTYPESDICT[thisExtensionType_] = ""
			FMFO_SCTN0304_EXTENSIONSCMNTDICT[thisExtensionType_] = thisComment_
			if thisMediaBool_ == "True":
				FMFO_SCTN0304_MEDIAFILELSTSTR += f"""{NTAB(1)}{thisExtensionType_},  # {thisComment_}{NEWLINE}"""
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2
	# FM_PARSE_FO_ENDS

	# FM_PARSE_SP_BEGINS
	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXSP_SCTN0600_STRDEF:
			# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisStrName_ = thisItem_[2]
			thisStr_ = thisItem_[3]
			FMSP_SCTN0600_DEFDICT[thisStrName_] = f"{DBLQT}{thisStr_}{DBLQT}"
			FMSP_SCTN0600_DEFCMNTDICT[thisStrName_] = f"{thisComment_}"
			continue
			# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXSP_SCTN0600_VALDEF:
			# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
			if thisItemLen_ != 4:
				doErrorItem("not 4 items", thisItem_)
				continue
			thisVal_ = thisItem_[2]
			FMSP_SCTN0600_DEFDICT[thisName_] = f"{thisVal_}"
			FMSP_SCTN0600_DEFCMNTDICT[thisName_] = f"{thisComment_}"
			continue
			# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXSP_SCTN0601_DICTDEF:
			# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
			continue
			if thisItemLen_ != 4:
				doErrorItem("not 4 items", thisItem_)
				continue
			thisDictName_ = thisItem_[2]
			FMSP_SCTN0600_DEFDICT[thisDictName_] = ""
			FMSP_SCTN0600_DEFCMNTDICT[thisDictName_] = f"{thisComment_}"
			continue
			# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXSP_SCTN0601_DICTSTRADD:
			# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
			continue
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisDictName_ = thisItem_[2]
			thisKey_ = thisItem_[3]
			thisVal_ = thisItem_[4]
			FMSP_SCTN0601_DICTDICT[thisDictName_] += f"{NTAB(1)}{thisKey_}: {DBLQT}{thisVal_}{DBLQT},  # {thisComment_}{NEWLINE}"
			continue
			# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXSP_SCTN0601_DICTVALADD:
			# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
			continue
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisDictName_ = thisItem_[2]
			thisKey_ = thisItem_[3]
			thisVal_ = thisItem_[4]
			FMSP_SCTN0601_DICTDICT[thisDictName_] += f"{NTAB(1)}{thisKey_}: {thisVal_},  # {thisComment_}{NEWLINE}"
			continue
			# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXSP_SCTN0602_LISTDEF:
			# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
			continue
			if thisItemLen_ != 4:
				doErrorItem("not 4 items", thisItem_)
				continue
			thisListName_ = thisItem_[2]
			FMSP_SCTN600DEFLIST[thisListName_] = {}
			FMSP_SCTN600DEFCMNTLIST[thisListName_] = f"{thisComment_}"
			continue
			# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXSP_SCTN0602_LISTSTRADD:
			# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
			continue
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisListName_ = thisItem_[2]
			thisVal_ = thisItem_[3]
			FMSP_SCTN0602_LISTDICT[thisListName_] += f"{NTAB(1)}{DBLQT}{thisVal_}{DBLQT},  # {thisComment_}{NEWLINE}"
			continue
			# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXSP_SCTN0602_LISTVALADD:
			# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
			continue
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisListName_ = thisItem_[2]
			thisVal_ = thisItem_[3]
			FMSP_SCTN601LISTLIST[thisListName_] += f"{NTAB(1)}{thisVal_},  # {thisComment_}{NEWLINE}"
			continue
			# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXSP_SCTN0603_TUPDICTDEF:
			# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
			if thisItemLen_ != 4:
				doErrorItem("not 4 items", thisItem_)
				continue
			thisTupDictName_ = thisItem_[2]
			FMSP_SCTN0603_TUPDICTDICT[thisTupDictName_] = ""
			FMSP_SCTN0603_TUPDICTCMNTDICT[thisTupDictName_] = f"{thisComment_}"
			continue
			# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXSP_SCTN0603_TUPDICTLISTDEF:
			# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisTupDictName_ = thisItem_[2]
			thisKey_ = thisItem_[3]
			if thisTupDictName_ not in FMSP_SCTN0603_TUPDICTLISTDICT:
				FMSP_SCTN0603_TUPDICTLISTDICT[thisTupDictName_] = {}
			FMSP_SCTN0603_TUPDICTLISTDICT[thisTupDictName_][thisKey_] = ""
			# FMSP_SCTN0603_TUPDICTDICT[thisTupDictName_] += f"{NTAB(1)}{OPAREN}{thisKey_}, {OBRKT}{CBRKT}{CPAREN},  # {thisComment_}{NEWLINE}"
			continue
			# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXSP_SCTN0603_TUPDICTLISTSTRADD:
			# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisTupDictName_ = thisItem_[2]
			thisKey_ = thisItem_[3]
			thisVal_ = thisItem_[4]
			FMSP_SCTN0603_TUPDICTLISTDICT[thisTupDictName_][thisKey_] += f"{NTAB(1)}{DBLQT}{thisVal_}{DBLQT},  # {thisComment_}{NEWLINE}"
			continue
			# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXSP_SCTN0603_TUPDICTLISTVALADD:
			# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisTupDictName_ = thisItem_[2]
			thisKey_ = thisItem_[3]
			thisVal_ = thisItem_[4]
			FMSP_SCTN0603_TUPDICTLISTDICT[thisTupDictName_][thisKey_] += f"{NTAB(1)}{thisVal_},  # {thisComment_}{NEWLINE}"
			continue
			# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXSP_SCTN0603_TUPDICTSTRADD:
			# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisTupDictName_ = thisItem_[2]
			thisKey_ = thisItem_[3]
			thisVal_ = thisItem_[4]
			FMSP_SCTN0603_TUPDICTDICT[thisTupDictName_] += f"{NTAB(1)}{OPAREN}{thisKey_}, {DBLQT}{thisVal_}{DBLQT}{CPAREN},  # {thisComment_}{NEWLINE}"
			continue
			# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1

	# ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ ⥥1⥣ for thisItem_ in TBGLST:
		# ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ ⥥2⥣ if thisAX_ …
		elif thisAX_ == FMAXSP_SCTN0603_TUPDICTVALADD:
			# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisTupDictName_ = thisItem_[2]
			thisKey_ = thisItem_[3]
			thisVal_ = thisItem_[4]
			FMSP_SCTN0603_TUPDICTDICT[thisTupDictName_] += f"{NTAB(1)}{OPAREN}{thisKey_}, {thisVal_}{CPAREN},  # {thisComment_}{NEWLINE}"
			continue
			# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1
	# FM_PARSE_SP_ENDS

		# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2
	# ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1

	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# __main__
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def __main__():
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	with open(TBGLST_NAME, "tw") as FDOut:
		FDOut.write(f"TBGLST = {OBRKT}{NEWLINE}{NTAB(1)}{FOLD1STARTHERE}{NEWLINE}")
		parseTBGLST(FDOut)
		FDOut.write(f"{NTAB(1)}{FOLD1ENDHERE}{NEWLINE}{CBRKT}{NEWLINE}")

	with open(MARKLINES_NAME, "tw") as FDOut:
		FDOut.write(f"""CMNTLINE = {CMNTLINE}{NEWLINE}""")
		FDOut.write(f"""FOLD1ENDHERE = {FOLD1ENDHERE}{NEWLINE}""")
		FDOut.write(f"""FOLD1ENDHERELN = {FOLD1ENDHERELN}{NEWLINE}""")
		FDOut.write(f"""FOLD1STARTHERE = {FOLD1STARTHERE}{NEWLINE}""")
		FDOut.write(f"""FOLD1STARTHERELN = {FOLD1STARTHERELN}{NEWLINE}""")
		FDOut.write(f"""FOLD2ENDHERE = {FOLD2ENDHERE}{NEWLINE}""")
		FDOut.write(f"""FOLD2ENDHERELN = {FOLD2ENDHERELN}{NEWLINE}""")
		FDOut.write(f"""FOLD2STARTHERE = {FOLD2STARTHERE}{NEWLINE}""")
		FDOut.write(f"""FOLD2STARTHERELN = {FOLD2STARTHERELN}{NEWLINE}""")
		FDOut.write(f"""FOLD3ENDHERELN = {FOLD3ENDHERELN}{NEWLINE}""")
		FDOut.write(f"""FOLD3STARTHERE = {FOLD3STARTHERE}{NEWLINE}""")
		FDOut.write(f"""FOLD3STARTHERELN = {FOLD3STARTHERELN}{NEWLINE}""")
		FDOut.write(f"""IMPORTANTSTR = {IMPORTANTSTR}{NEWLINE}""")
		FDOut.write(f"""INFOSTR = {INFOSTR}{NEWLINE}""")
		FDOut.write(f"""MARK1END = {MARK1END("")}{NEWLINE}""")
		FDOut.write(f"""MARK1ENDLN = {MARK1ENDLN("")}{NEWLINE}""")
		FDOut.write(f"""MARK1MID = {MARK1MID("")}{NEWLINE}""")
		FDOut.write(f"""MARK1MIDLN = {MARK1MIDLN("")}{NEWLINE}""")
		FDOut.write(f"""MARK1START = {MARK1START("")}{NEWLINE}""")
		FDOut.write(f"""MARK1STARTLN = {MARK1STARTLN("")}{NEWLINE}""")
		FDOut.write(f"""MARK2END = {MARK2END("")}{NEWLINE}""")
		FDOut.write(f"""MARK2ENDLN = {MARK2ENDLN("")}{NEWLINE}""")
		FDOut.write(f"""MARK2MID = {MARK2MID("")}{NEWLINE}""")
		FDOut.write(f"""MARK2MIDLN = {MARK2MIDLN("")}{NEWLINE}""")
		FDOut.write(f"""MARK2START = {MARK2START("")}{NEWLINE}""")
		FDOut.write(f"""MARK2STARTLN = {MARK2STARTLN("")}{NEWLINE}""")
		FDOut.write(f"""MARK3END = {MARK3END("")}{NEWLINE}""")
		FDOut.write(f"""MARK3ENDLN = {MARK3ENDLN("")}{NEWLINE}""")
		FDOut.write(f"""MARK3MID = {MARK3MID("")}{NEWLINE}""")
		FDOut.write(f"""MARK3MIDLN = {MARK3MIDLN("")}{NEWLINE}""")
		FDOut.write(f"""MARK3START = {MARK3START("")}{NEWLINE}""")
		FDOut.write(f"""MARK3STARTLN = {MARK3STARTLN("")}{NEWLINE}""")
		FDOut.write(f"""MARK4END = {MARK4END("")}{NEWLINE}""")
		FDOut.write(f"""MARK4ENDLN = {MARK4ENDLN("")}{NEWLINE}""")
		FDOut.write(f"""MARK4MID = {MARK4MID("")}{NEWLINE}""")
		FDOut.write(f"""MARK4MIDLN = {MARK4MIDLN("")}{NEWLINE}""")
		FDOut.write(f"""MARK4START = {MARK4START("")}{NEWLINE}""")
		FDOut.write(f"""MARK4STARTLN = {MARK4STARTLN("")}{NEWLINE}""")
		FDOut.write(f"""MARK5END = {MARK5END("")}{NEWLINE}""")
		FDOut.write(f"""MARK5ENDLN = {MARK5ENDLN("")}{NEWLINE}""")
		FDOut.write(f"""MARK5MID = {MARK5MID("")}{NEWLINE}""")
		FDOut.write(f"""MARK5MIDLN = {MARK5MIDLN("")}{NEWLINE}""")
		FDOut.write(f"""MARK5START = {MARK5START("")}{NEWLINE}""")
		FDOut.write(f"""MARK5STARTLN = {MARK5STARTLN("")}{NEWLINE}""")
		FDOut.write(f"""MARK6END = {MARK6END("")}{NEWLINE}""")
		FDOut.write(f"""MARK6ENDLN = {MARK6ENDLN("")}{NEWLINE}""")
		FDOut.write(f"""MARK6MID = {MARK6MID("")}{NEWLINE}""")
		FDOut.write(f"""MARK6MIDLN = {MARK6MIDLN("")}{NEWLINE}""")
		FDOut.write(f"""MARK6START = {MARK6START("")}{NEWLINE}""")
		FDOut.write(f"""MARK6STARTLN = {MARK6STARTLN("")}{NEWLINE}""")
		FDOut.write(f"""MARK7END = {MARK7END("")}{NEWLINE}""")
		FDOut.write(f"""MARK7ENDLN = {MARK7ENDLN("")}{NEWLINE}""")
		FDOut.write(f"""MARK7MID = {MARK7MID("")}{NEWLINE}""")
		FDOut.write(f"""MARK7MIDLN = {MARK7MIDLN("")}{NEWLINE}""")
		FDOut.write(f"""MARK7START = {MARK7START("")}{NEWLINE}""")
		FDOut.write(f"""MARK7STARTLN = {MARK7STARTLN("")}{NEWLINE}""")
		FDOut.write(f"""MARK8END = {MARK8END("")}{NEWLINE}""")
		FDOut.write(f"""MARK8ENDLN = {MARK8ENDLN("")}{NEWLINE}""")
		FDOut.write(f"""MARK8MID = {MARK8MID("")}{NEWLINE}""")
		FDOut.write(f"""MARK8MIDLN = {MARK8MIDLN("")}{NEWLINE}""")
		FDOut.write(f"""MARK8START = {MARK8START("")}{NEWLINE}""")
		FDOut.write(f"""MARK8STARTLN = {MARK8STARTLN("")}{NEWLINE}""")
		FDOut.write(f"""MARK9END = {MARK9END("")}{NEWLINE}""")
		FDOut.write(f"""MARK9ENDLN = {MARK9ENDLN("")}{NEWLINE}""")
		FDOut.write(f"""MARK9MID = {MARK9MID("")}{NEWLINE}""")
		FDOut.write(f"""MARK9MIDLN = {MARK9MIDLN("")}{NEWLINE}""")
		FDOut.write(f"""MARK9START = {MARK9START("")}{NEWLINE}""")
		FDOut.write(f"""MARK9STARTLN = {MARK9STARTLN("")}{NEWLINE}""")


	with open(CF_NAME, "tw") as FDOut:
		strToWrt_ = makeCF()
		FDOut.writelines(strToWrt_)

	with open(FM_NAME, "tw") as FDOut:
		strToWrt_ = makeFM()
		FDOut.writelines(strToWrt_)

	with open(FO_NAME, "tw") as FDOut:
		strToWrt_ = makeFO()
		FDOut.writelines(strToWrt_)

	with open(SP_NAME, "tw") as FDOut:
		strToWrt_ = makeSP()
		FDOut.writelines(strToWrt_)

	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


if __name__ == "__main__":
	__main__()


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# end of FM.py
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#
#
