

# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# start of FO.py file operations
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#


import os
import re
import shutil
import pathlib as PL


import CF


OSPATH = os.path

ABSPATH = os.path.abspath
CHMOD = os.chmod
HOME = f"{OSPATH.expanduser('~')}"
MKDIR = os.mkdir
MOVE = shutil.move
RENAME = os.rename
STAT = os.stat
SUB = re.sub


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# modules included in this file
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#
# * def checkSetMode(pathToCheck, modeIn, modeToSet):
# * def deFuxDir(toDeFux):
# * def deFuxFile(toDeFux):
# * def fxDir(dirToCk):
# * def getIndexes(destDir):
# * def incIndex(indexType):
# * def PLmkdir(fullPath):
# * def putIndexes(destDir):
# * def returnPathPiecesChmod(entryPath_):
# * def scanADir(rootPath_, recurse_):
#
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# other useful defines in this file
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#
# * ABSPATH = os.path.abspath
# * CHMOD = os.chmod
# * HOME = f"{PATH.expanduser('~')}"
# * MKDIR = os.mkdir
# * MOVE = shutil.move
# * PATH = os.path
# * STAT = os.stat
# * SUB = re.sub


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN300 FO defines
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
BLACKTAIL = "BLACKTAIL"  #
CODE = "CODE"  #
CODEFILES = "CODEFILES"  #
DIRBLACKLIST = "[a-zA-Z0-9./]+"  #
DIRWHITELIST = "[^a-zA-Z0-9./]+"  #
DOCS = "DOCS"  #
ENTRYMODE = "ENTRYMODE"  #
EXTHEAD = "EXTHEAD"  #
EXTTAIL = "EXTTAIL"  #
FILEWHITELIST = "[^a-zA-Z0-9.]+"  #
ISADIR = "ISADIR"  #
ISAFILE = "ISAFILE"  #
ISASYMLINK = "ISASYMLINK"  #
ISMEDIAFILETYPE = "ISMEDIAFILETYPE"  #
ISUNKNOWNFILETYPE = "ISUNKNOWNFILETYPE"  #
KNOWNFILES = "KNOWNFILES"  #
KNOWNFILETYPE = "KNOWNFILETYPE"  #
MEDIAFILES = "MEDIAFILES"  #
NOTKNOWNFILES = "NOTKNOWNFILES"  #
NOTMEDIAFILES = "NOTMEDIAFILES"  #
NOTUNKNOWNFILES = "NOTUNKNOWNFILES"  #
PATH = "PATH"  #
PATHHEAD = "PATHHEAD"  #
PATHTAIL = "PATHTAIL"  #
PICS = "PICS"  #
RECURSE = "RECURSE"  #
ROOTDIR = "ROOTDIR"  #
TEXT = "TEXT"  #
UNKNOWNFILES = "UNKNOWNFILES"  #
VIDS = "VIDS"  #
WHITEFILENAME = "WHITEFILENAME"  #
WHITEFULLPATH = "WHITEFULLPATH"  #


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN301 FO dicts
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN302 FO lists
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
ILLEGALPATHS = [  # list of absolute paths to be completely ignored if used
	"/",  # do not operate on / ever
]


ILLEGALWILDCARDS = [  # list all of the portions of a filename which will result in an error [0:] based
	"/bin/",  # illegal wildcards, these are most often /path/ and will be [0:] based
	"/boot/",  # illegal wildcards, these are most often /path/ and will be [0:] based
	"/dev/",  # illegal wildcards, these are most often /path/ and will be [0:] based
	"/efi/",  # illegal wildcards, these are most often /path/ and will be [0:] based
	"/etc/",  # illegal wildcards, these are most often /path/ and will be [0:] based
	"/home/",  # illegal wildcards, these are most often /path/ and will be [0:] based
	"/lib/",  # illegal wildcards, these are most often /path/ and will be [0:] based
	"/lib64/",  # illegal wildcards, these are most often /path/ and will be [0:] based
	"/media/",  # illegal wildcards, these are most often /path/ and will be [0:] based
	"/opt/",  # illegal wildcards, these are most often /path/ and will be [0:] based
	"/proc/",  # illegal wildcards, these are most often /path/ and will be [0:] based
	"/root/",  # illegal wildcards, these are most often /path/ and will be [0:] based
	"/run/",  # illegal wildcards, these are most often /path/ and will be [0:] based
	"/sbin/",  # illegal wildcards, these are most often /path/ and will be [0:] based
	"/srv/",  # illegal wildcards, these are most often /path/ and will be [0:] based
	"/sys/",  # illegal wildcards, these are most often /path/ and will be [0:] based
	"/tmp/",  # illegal wildcards, these are most often /path/ and will be [0:] based
	"/usr/",  # illegal wildcards, these are most often /path/ and will be [0:] based
	"/var/",  # illegal wildcards, these are most often /path/ and will be [0:] based
]


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN303 FO tupdicts
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of EMPTYENTRY structures
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

EMPTYENTRYTUP = (
	(BLACKTAIL, ""),  #
	(EXTHEAD, ""),  #
	(EXTTAIL, ""),  #
	(PATH, ""),  #
	(PATHHEAD, ""),  #
	(PATHTAIL, ""),  #
	(WHITEFILENAME, ""),  #
	(WHITEFULLPATH, ""),  #
	(ENTRYMODE, 0),  #
	(ISADIR, False),  #
	(ISAFILE, False),  #
	(ISAKNOWNFILETYPE, False),  #
	(ISAMEDIAFILETYPE, False),  #
	(ISASYMLINK, False),  #
	(ISUNKNOWNFILETYPE, False),  #
)

def EMPTYENTRYDICT():
	return dict((x, y) for x, y in EMPTYENTRYTUP)


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN304 FO file extension management structures
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
EXTENSIONSTYPES = {
	CODE: [  # define CODE file extension
		".c",  #
		".C",
		".php",  #
		".PHP",
		".py",  #
		".PY",
	],

	PICS: [  # define PICS file extension
		".bmp",  #
		".BMP",
		".gif",  #
		".GIF",
		".jpeg",  #
		".JPEG",
		".jpg",  #
		".JPG",
		".png",  #
		".PNG",
		".webp",  #
		".WEBP",
	],

	TEXT: [  # define TEXT file extension
		".lst",  #
		".LST",
		".lst.txt",  #
		".LST.TXT",
	],

	VIDS: [  # define VIDS file extension
		".avi",  #
		".AVI",
		".divx",  #
		".DIVX",
		".flv",  #
		".FLV",
		".gifv",  #
		".GIFV",
		".m2ts",  #
		".M2TS",
		".m4a",  #
		".M4A",
		".m4v",  #
		".M4V",
		".mkv",  #
		".MKV",
		".mov",  #
		".MOV",
		".mp4",  #
		".MP4",
		".mpeg",  #
		".MPEG",
		".mpg",  #
		".MPG",
		".webm",  #
		".WEBM",
		".wmv",  #
		".WMV",
	],

	DOCS: [  # define DOCS file extension
	],

}

MEDIAEXTENSIONTYPES = [
	PICS,  # define PICS file extension
	VIDS,  # define VIDS file extension
]


#
#
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * end of managed sections of FO.py
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
#


#
#
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# start of unmanaged sections of FO.py
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#
#


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * deFuxFile
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def deFuxFile(toDeFux):
	thisWhiteTail = SUB(C.FILEWHITELIST, "", toDeFux)
	thisBlackTail = SUB(C.FILEBLACKLIST, "", toDeFux)
	return thisWhiteTail, thisBlackTail


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * deFuxDir
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def deFuxDir(toDeFux):
	thisWhiteTail = SUB(C.DIRWHITELIST, "", toDeFux)
	thisBlackTail = SUB(C.DIRBLACKLIST, "", toDeFux)
	return thisWhiteTail, thisBlackTail


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * incIndex
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def incIndex(indexType):
	if indexType == C.PICSTAIL:
		currentIndex = int(C.PICSINDEX) + 1
		C.PICSINDEX = currentIndex
	elif indexType == C.VIDSTAIL:
		currentIndex = int(C.VIDSINDEX) + 1
	if currentIndex >= C.MAXDIR:
		currentIndex = C.MINDIR
	if indexType == C.PICSTAIL:
		C.PICSINDEX = currentIndex
	elif indexType == C.VIDSTAIL:
		C.VIDSINDEX = currentIndex
		currentIndex += C.MAXDIR
	return currentIndex


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * fxDir
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def fxDir(dirToCk):
	dirToCk = ABSPATH(dirToCk)
	TIsADir = OSPATH.isdir(dirToCk)
	if not TIsADir:
		return None
	if dirToCk in C.ILLEGALPATHS:
		return None

	for thisStub in C.ILLEGALWILDCARDS:
		isFound = dirToCk.find(thisStub)
		if isFound == 0:
			return None

	return dirToCk + "/"


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * use pathlib to recursively create directories
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def PLmkdir(fullPath):
	PL.Path(fullPath).mkdir(parents=True, exist_ok=True)


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * make directories if not present
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def checkDest(destRoot):
	print(f"""
checking destination dir {destRoot}
""")
	if C.DEBUGME == 44:
		return
	destRoot = FO.fxDir(destRoot)
	if destRoot is not None:
		for suffix in C.DIRLIST:
			dirToChk = f"{destRoot}{suffix}"
			if not FO.OSPATH.isdir(dirToChk):
				FO.PLmkdir(dirToChk)


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# *
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def returnPathPieces(osDirEntry):
	thisPath = osDirEntry.path
	thisPathHead, thisPathTail = FO.PATH.split(thisPath)
	thisIsASymlink = osDirEntry.is_symlink()
	thisIsADir = osDirEntry.is_dir(follow_symlinks=False)
	thisIsAFile = osDirEntry.is_file(follow_symlinks=False)
	thisExtHead, thisExtTail = FO.PATH.splitext(thisPath)
	thisMode = osDirEntry.stat()[0] & 0o777
	if thisIsADir:
		thisWhiteTail, thisBlackTail = FO.deFuxDir(thisPathTail)
		thisWhiteFullPath = thisPathHead + "/" + thisWhiteTail
		# print(f"thismode {thisMode} octal {thisMode:o} 0o777 {0o777}")
	if thisIsAFile:
		thisWhiteTail, thisBlackTail = FO.deFuxFile(thisPathTail)
		thisWhiteFullPath = thisPathHead + "/" + thisWhiteTail.lower()
	return {
		PATH: thisPath,
		PATHHEAD: thisPathHead,
		PATHTAIL: thisPathTail,
		ISASYMLINK: thisIsASymlink,
		ISADIR: thisIsADir,
		ISAFILE: thisIsAFile,
		EXTHEAD: thisExtHead,
		EXTTAIL: thisExtTail,
		BLACKTAIL: thisBlackTail,
		WHITEFULLPATH: thisWhiteFullPath,
		ENTRYMODE: thisMode,
		WHITEFILENAME: thisWhiteTail.lower(),
	}

# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * get the indexes from ~/.cache
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#**#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def getIndexes(destDir):
	destDir = fxDir(destDir)
	if destDir is None:
		return False
	if not OSPATH.isdir(destDir):
		return False
	whiteDir, blackDir = deFuxFile(destDir)
	indexNamePICS = f"{C.DIRINDEXPATH}{whiteDir}.{C.PICSTAIL}INDEX.txt"
	if OSPATH.isfile(indexNamePICS):
		FDIn = open(indexNamePICS, "r")
		C.PICSINDEX = int(FDIn.readline())
		FDIn.close()
	else:
		C.PICSINDEX = C.MINDIR
	indexNameVIDS = f"{C.DIRINDEXPATH}{whiteDir}.{C.VIDSTAIL}INDEX.txt"
	if OSPATH.isfile(indexNameVIDS):
		FDIn = open(indexNameVIDS, "r")
		C.VIDSINDEX = int(FDIn.readline())
		FDIn.close()
	else:
		C.VIDSINDEX = C.MINDIR
	return True


def putIndexes(destDir):
	destDir = fxDir(destDir)
	if destDir is None:
		return False
	whiteStr, blackStr = deFuxFile(destDir)
	indexNamePICS = f"{C.DIRINDEXPATH}{whiteStr}.{C.PICSTAIL}INDEX.txt"
	FDOut = open(indexNamePICS, "w")
	FDOut.write(f"{C.PICSINDEX}\n")
	FDOut.flush()
	FDOut.close()
	indexNameVIDS = f"{C.DIRINDEXPATH}{whiteStr}.{C.VIDSTAIL}INDEX.txt"
	FDOut = open(indexNameVIDS, "w")
	FDOut.write(f"{C.VIDSINDEX}\n")
	FDOut.flush()
	FDOut.close()
	return True
	# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * checkSetMode
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def checkSetMode(pathToCheck, modeIn, modeToSet):
	# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
	return
	if modeIn != modeToSet:
		# print(f"dir chmod {pathToCheck} {modeIn:03o}  ==>  {modeToSet:03o}")
		CHMOD(pathToCheck, modeToSet)
	# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# returnPathPiecesChmod
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def returnPathPiecesChmod(entryPath_):
	# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
	thisPath_ = entryPath_.path
	thisPathHead_, thisPathTail_ = OSPATH.split(thisPath_)
	thisIsSymlink_ = entryPath_.is_symlink()
	thisIsDir_ = entryPath_.is_dir(follow_symlinks=False)
	thisIsFile_ = entryPath_.is_file(follow_symlinks=False)
	thisExtHead_, thisExtTail_ = OSPATH.splitext(thisPath_)
	thisMode_ = entryPath_.stat()[0] & 0o777
	if thisIsDir_:
		thisWhiteTail_, thisBlackTail_ = deFuxDir(thisPathTail_)
		thisWhiteFullPath_ = thisPathHead_ + "/" + thisWhiteTail_
		checkSetMode(thisPath_, thisMode_, 0o777)
	if thisIsFile_:
		thisWhiteTail_, thisBlackTail_ = deFuxFile(thisPathTail_)
		thisWhiteFullPath_ = thisPathHead_ + "/" + thisWhiteTail_.lower()
		checkSetMode(thisPath_, thisMode_, 0o666)
	if thisExtTail_ in EXTENSIONLOOKUP and thisIsFile_ is True:
		thisIsKnownFileType_ = True
		thisIsUnknownFiletype = False
	else:
		thisIsKnownFileType_ = False
		thisIsUnknownFiletype = True
	thisIsMediaFiletype_ = False
	for thisFileType_ in MEDIAEXTENSIONTYPES:
		if thisExtTail_ in EXTENSIONSTYPES[thisFileType_] and thisIsFile_ is True:
			thisIsMediaFiletype_ = True
	return {
		BLACKTAIL: thisBlackTail_,
		EXTHEAD: thisExtHead_,
		EXTTAIL: thisExtTail_,
		ISDIR: thisIsDir_,
		ISFILE: thisIsFile_,
		ISKNOWNFILETYPE: thisIsKnownFileType_,
		ISMEDIAFILETYPE: thisIsMediaFiletype_,
		ISSYMLINK: thisIsSymlink_,
		ISUNKNOWNFILETYPE: thisIsUnknownFiletype,
		PATH: thisPath_,
		PATHHEAD: thisPathHead_,
		PATHTAIL: thisPathTail_,
		WHITEFULLPATH:  thisWhiteFullPath_,
	}
	# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# scanADir
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def scanADir(rootPath_, recurse_):
	# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
	listToRtn_ = []
	with os.scandir(rootPath_) as dirEntries_:
		for entry_ in dirEntries_:
			thisEntryData_ = returnPathPiecesChmod(entry_)
			listToRtn_.append(thisEntryData_)
			if thisEntryData_[ISDIR] is True and recurse_ is True:
				addToListToRtn = scanADir(thisEntryData_[PATH], recurse_)
				for thisEntry_ in addToListToRtn:
					listToRtn_.append(thisEntry_)
	return listToRtn_
	# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰

#
#
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# end of FO.py
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
