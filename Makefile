# assignment 2 make file
# Celimpilo manqele
# 19 April 2021

JAVAC=/usr/bin/javac
.SUFFIXES: .java .class
SRCDIR=src
BINDIR=bin
FILESDIR=files
PYTHON=/usr/bin/python3

$(BINDIR)/%.class:$(SRCDIR)/%.java
	$(JAVAC) -d $(BINDIR)/ -cp $(BINDIR) $<

CLASSES=HashTableFunctions.class HashTable.class TestHashTable.class

CLASS_FILES=$(CLASSES:%.class=$(BINDIR)/%.class)

default: $(CLASS_FILES)

run:
	java -cp bin TestHashTable 0 4 2 1 4 2 0 2 2 4

test:
	$(PYTHON) src/test.py 3 >> smallcollisions.txt
#>> smallcollisions.txt
