import gc
import os
import subprocess as SP
from sys import argv


from dataStuff import dataStuff as DS
from dataStuff import constants as C


gc.enable()


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# *
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def checkSetMode(pathToCheck, modeIn, modeToSet):

	if modeIn != modeToSet:
		# print(f"dir chmod {pathToCheck} {modeIn:03o}  ==>  {modeToSet:03o}")

		if not C.DRYRUN:
			DS.CHMOD(pathToCheck, modeToSet)


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# *
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def returnPathPiecesChmod(entryPath):
	thisPath = entryPath.path
	thisPathHead, thisPathTail = DS.PATH.split(thisPath)
	thisIsASymlink = entryPath.is_symlink()
	thisIsADir = entryPath.is_dir(follow_symlinks=False)
	thisIsAFile = entryPath.is_file(follow_symlinks=False)
	thisExtHead, thisExtTail = DS.PATH.splitext(thisPath)
	thisMode = entryPath.stat()[0] & 0o777

	if thisIsADir:
		thisWhiteTail, thisBlackTail = DS.deFuxDir(thisPathTail)
		thisWhiteFullPath = thisPathHead + "/" + thisWhiteTail
		# print(f"thismode {thisMode} octal {thisMode:o} 0o777 {0o777}")
		checkSetMode(thisPath, thisMode, 0o777)

	if thisIsAFile:
		thisWhiteTail, thisBlackTail = DS.deFuxFile(thisPathTail)
		thisWhiteFullPath = thisPathHead + "/" + thisWhiteTail.lower()
		checkSetMode(thisPath, thisMode, 0o666)

	return \
		{
			C.THISPATH: thisPath,
			C.THISPATHHEAD: thisPathHead,
			C.THISPATHTAIL: thisPathTail,
			C.THISISASYMLINK: thisIsASymlink,
			C.THISISADIR: thisIsADir,
			C.THISISAFILE: thisIsAFile,
			C.THISEXTHEAD: thisExtHead,
			C.THISEXTTAIL: thisExtTail,
			C.THISBLACKTAIL: thisBlackTail,
			C.THISWHITEFULLPATH:  thisWhiteFullPath,
		}


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# *
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def doDirsInADir(rootPath2ck):
	if DS.fxDir(rootPath2ck) == None:
		print(f"I won't work on paths in the C.ILLEGALPATHS or C.ILLEGALWILDCARDS lists\n{rootPath2ck}\n is in one of "
					f"those lists")

	with os.scandir(rootPath2ck) as dirEntries:

		for entry in dirEntries:
			thisEntryData = returnPathPiecesChmod(entry)

			if not thisEntryData[C.THISISADIR]:
				continue

			if thisEntryData[C.THISBLACKTAIL] != "":
				# we need to rename the directory to deFux the dir names
				DS.MOVE(thisEntryData[C.THISPATH], thisEntryData[C.THISWHITEFULLPATH])
				thisEntryData = returnPathPiecesChmod(thisEntryData[C.THISWHITEFULLPATH])

			doDirsInADir(thisEntryData[C.THISPATH])


def doFilesInADir(rootPath2ck, destPath):

	with os.scandir(rootPath2ck) as dirEntries:

		for entry in dirEntries:
			thisPathPieces = returnPathPiecesChmod(entry)

			if thisPathPieces[C.THISISAFILE]:

				if thisPathPieces[C.THISBLACKTAIL] != "":
					# rename files with out of code-page characters eventually
					# currently only works with characters represented in utf-8
					DS.MOVE(thisPathPieces[C.THISPATH], thisPathPieces[C.THISWHITEFULLPATH])
					entry.path = thisPathPieces[C.THISWHITEFULLPATH]
					thisPathPieces = returnPathPiecesChmod(entry)

				thisLowerExtTail = thisPathPieces[C.THISEXTTAIL].lower()

				if thisPathPieces[C.THISEXTTAIL] != thisLowerExtTail:
					# rename to lowercase extension for old time sake
					newName = f"{thisPathPieces[C.THISPATHHEAD]}{thisLowerExtTail}"
					DS.MOVE(thisPathPieces[C.THISPATH], newName)
					entry.path = newName
					thisPathPieces = returnPathPiecesChmod(entry)

				if thisLowerExtTail in C.PICSEXTS:
					execSet = ["/wbin-extras/exiftool/exiftool", "-all=", "--icc_profile:all", thisPathPieces[C.THISPATH],
											"-overwrite_original_in_place"]
					result = SP.run(execSet, capture_output=True)

					if result.returncode == 0:
						thisIsAGoodFile = True
						destSorter = "picSource"
						thisDest = "PICSEXTS"

					else:
						thisIsAGoodFile = False
						destSorter = "errors"
						thisDest = ""

				elif thisLowerExtTail in C.VIDSEXTS:
					execSet = ["ffmpeg", "-y", "-i", thisPathPieces[C.THISPATH], "-c", "copy", "-dn", "-sn", "s-$file"]
					result = SP.run(execSet, capture_output=True)

					if result.returncode == 0:
						thisIsAGoodFile = True
						destSorter = "vidSource"
						thisDest = "VIDSEXTS"

					else:
						thisIsAGoodFile = False
						destSorter = "errors"
						thisDest = ""

				else:
					thisIsAGoodFile = False
					destSorter = "errors"
					thisDest = ""
				# end of it thisLowerExtTail in PICSEXTS ; else thisLowerExtTail in vids

				if thisIsAGoodFile:

					if thisDest != "" and destPath != "":
						thisIndexStr = f"{DS.getIndex(thisDest, destPath):03d}"
						theHasher = DS.theHasherBlake2b
						destSorter = f"/{destSorter}/d{thisIndexStr}/"
						myHash = DS.doAHash(theHasher, thisPathPieces[C.THISPATH])
						thisNewName = f"{destPath}/{destSorter}/{myHash}{thisPathPieces[C.THISEXTTAIL].casefold()}"
						DS.incIndex(thisDest, destPath, thisIndexStr)

					else:
						thisNewName = f"{destPath}{destSorter}{thisPathPieces[C.THISEXTHEAD]}{thisPathPieces[C.THISEXTTAIL].lower()}"

			elif thisPathPieces[C.THISISADIR]:
				doFilesInADir(thisPathPieces[C.THISPATH], destPath)

			else:
				continue

			if not C.DRYRUN:
				thisNewName = f"{destPath}/errors/{thisPathPieces[C.THISEXTHEAD]}{thisPathPieces[C.THISEXTTAIL].lower()}"
				DS.MOVE(thisPathPieces[C.THISPATH], thisNewName)


bigSourceDir = argv.pop(1)
bigDestDir = argv.pop(1)

bigSourceDir = DS.fxDir(bigSourceDir)
bigDestDir = DS.fxDir(bigDestDir)

if bigSourceDir == None or bigDestDir == None:
	print(f"{bigSourceDir}\nor\n{bigDestDir}\nis an invalid directory for my use")
	exit(1)

doDirsInADir(bigSourceDir)
doFilesInADir(bigSourceDir, bigDestDir)


