# VARIABLES
GPP = "./gpp.exe"
SOURCE = index.md
OUT_PREFIX = ./output/output

default: source

html:
	$(GPP) $(SOURCE) -x | pandoc -t html5 -s -o $(OUT_PREFIX).html

docx:
	$(GPP) $(SOURCE) -x | pandoc -t docx -o $(OUT_PREFIX).docx

source:
	$(GPP) $(SOURCE) -x > $(OUT_PREFIX).md
