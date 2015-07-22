#!/usr/bin/python
# coding=utf-8

import os
import sys
import time
import re
from grip.command import main


def byNote(nFile):
    x = []
    arch = open(".index.md", "a")
    arch.write("## " + mdLink("Notas", "notas") + "\n")
    arch.close()
    y = open(".notas.md", "w")
    y.write("# Notas de Bitácora \n")
    pattern = re.compile("Nota:")
    for i in nFile:
        # TODO: Revisar si quedan procesos abiertos
        if 'Nota:' in open(i[1]).read():
            x.append(i[1])
    for i in x:
        w = open(i, "r")
        for j, line in enumerate(w):
            if re.search(pattern, line):
                y.write("### Archivo: " + mdLink(w.name) + "\n Linea: "
                        + str(j) + "\n" + line + "\n" + next(w) + "\n")
    y.close()


def mdLink(name, link=None):
    nname = name.split("/")[-1][:-3]
    if link is None:
        x = "[" + nname + "]" + "(" + name + ")"
    else:
        link = "." + link + ".md"
        x = "[" + name + "]" + "(" + link + ")"
    return x


def manageFile():
    # No recursivo
    # x = next(os.walk("."))[1:]
    # x = [f for f in x if not f.startswith('.')]
    # Recursivo
    x = []
    for root, dirs, files in os.walk("."):
        for f in files:
            if not f.startswith('.') and not f.startswith('notas.'):
                x.append(os.path.join(root, f))

    y = []
    for val in x:
        y.append(os.path.getmtime(val))
    z = zip(y, x)
    z.sort(reverse=True)
    return z


def lastChanges(nFile):
    arch = open(".index.md", "w")
    arch.write("# Indice de Bitácora \n")
    arch.write("\n")
    arch.write("## Ultimos archivos editados \n")
    arch.write("\n")
    arch.write("### Fecha &nbsp;&nbsp;&nbsp; \
               Archivo &nbsp;&nbsp;&nbsp;&nbsp; Título\n")
    arch.write("\n")
    for i in nFile[0:10]:
        try:
            first_line = " **" + next(open(i[1])).rstrip().lstrip('# ') + "**"
        except StopIteration:
            first_line = ""
        arch.write("* " + "**" + time.strftime('%d/%m/%Y',
                   time.localtime(i[0])) + "** &nbsp;&nbsp;&nbsp;"
                   + mdLink(i[1]) + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
                   + first_line + "\n")
    arch.write("\n")
    arch.write("\n")
    arch.close()


def monthYear(nFile):
    x = [[time.strftime('%b-%Y', time.localtime(x[0])), x[1]] for x in nFile]
    y = list(set([x[i][0] for i in range(len(x))]))
    arch = open(".index.md", "a")
    arch.write("## Editadas por mes \n")
    arch.write("\n")
    arch.write("\n")
    for i in y:
        arch.write("* " + mdLink(i, i) + "\n")
        arch2 = open("." + i + ".md", "w")
        arch2.write("# Archivos " + i + "\n")
        for j in x:
            if j[0] == i:
                try:
                        first_line = " **" \
                                     + next(open(j[1])).rstrip().lstrip('# ') \
                                     + "**"
                except StopIteration:
                        first_line = ""
                arch2.write("* " + mdLink(j[1]) + "&nbsp;&nbsp;&nbsp;&nbsp;"
                            + first_line + "\n")
        arch2.close()
    arch.write("\n")
    arch.close()


def createIndex():
    try:
        os.remove(".index.md")
    except OSError:
        pass
    nFile = manageFile()
    lastChanges(nFile)
    monthYear(nFile)
    byNote(nFile)
    main("--gfm .index.md")

sys.path.append(os.path.dirname(__file__))
createIndex()
