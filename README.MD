# fullMonty

all of the file operations I commonly use in one place

* copy files from a directory/tree to another directory, tree, spread tree, or archive
* move files from a directory/tree to another directory, tree, spread tree, or archive
* test media files
* ID media files
* randomly rename files in the destination
* operate on any filetype, or combination of filetypes
* command line parameters to set all options
* overwrite files in place, or in the destination
* spread destination files across several numbered directories such that sorting and management of media (the most commonly spread files I have) is easier
* trial run


help entry for -arc:
destination is a single or spread directory-root (SPREADFILES; not currently implemented)

help entry for -ARC:
destination is an archive file (not currently implemented)

help entry for -dd=:
set DESTDIR and pattern (defaults to **)
set OUTPUTDIR and pattern (defaults to **)

help entry for -docode:
don't process code filetypes
select DOALLKNOWNFILES True first, then set this False to ignore code filetypes

help entry for -DOCODE:
process code filetypes

help entry for -dodocs:
don't process docs filetypes
select DOALLKNOWNFILES True first, then set this False to ignore docs filetypes

help entry for -DODOCS:
process docs filetypes

help entry for -doknown:
don't process known filetypes
select DOALLKNOWNFILES True first, then set this False to ignore known filetypes

help entry for -DOKNOWN:
process known filetypes
set this first, then deselect individual types to remove filetypes from the list of processed filetypes

help entry for -domedia:
don't process media filetypes
set DOALLKNOWNFILES True first, then set this False to ignore media filetypes
select this True first, then set a media False type to ignore that filetype
select this True first, then set a media False type to ignore that filetype

help entry for -DOMEDIA:
process medial filetypes

help entry for -dopics:
don't process pics filetypes

help entry for -DOPICS:
process pics files

help entry for -dotext:
don't process test filetypes

help entry for -DOTEXT:
process text filetypes

help entry for -dounk:
don't process unknown filetypes

help entry for -DOUNK:
process unknown filetypes

help entry for -dovids:
don't process vids filetypes

help entry for -DOVIDS:
process vids filetypes

help entry for -h=:
set the hasher to be used for random file renaming

help entry for -i:
don't ID media files

help entry for -I:
ID media files

help entry for -m:
copy files

help entry for -M:
move files; cross volume safe

help entry for -o=:
set OUTPUTDIR and pattern (defaults to **)
set DESTDIR and pattern (defaults to **)

help entry for -o:
don't overwrite files of the same name, simple rename as needed

help entry for -O:
overwrite files of the same name

help entry for -rnd:
use the pattern specified in DESTDIR parameter, defaults to '*' which uses the same filename, if RENAMEFILES is True

help entry for -RND:
use specified hasher to create a random filename to write/archive if RENAMEFILES is True

help entry for -rn:
don't rename files in DESTDIR

help entry for -RN:
rename files in DESTDIR

help entry for --help:
show help for selected options, defaults to all, and exit without doing anything

help entry for -h:
show help for selected options, defaults to all, and exit without doing anything

help entry for -help:
show help for selected options, defaults to all, and exit without doing anything

help entry for -sd=:
set SOURCEDIR and file pattern (defaults to **)

help entry for -sf:
spread files among a numbered

help entry for -SF:
spread files among a numbered directory structure at DESTDIR

help entry for -sm:
don't strip media files of metadata

help entry for -SM:
strip media files of metadata

help entry for -tm:
don't test media files

help entry for -TM:
test media files

help entry for -t:
don't output to STDOUT the things that would happen to any files, DO THEM

help entry for -T:
output to STDOUT the things that would happen to any files, without doing them

