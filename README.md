# micanpymol
Wrapper to run mican from pymol (currently only for pymol with python3.x)

You need mican binary in your PATH. If you launch pymol from GUI, PATH variable may differ from ones launched from CUI. So it's better to give the full-path for mican inside the script.

First, load this script:
 run micanpymol.py

Then run mican on pymol:
 mican protein1, protein2, -R -i 3 -m matrix.txt -a align.txt

For older pymol running on python2, use micanpymol_python2.py instead.

## About Mican
Mican is a protein structure alignment program by Shintaro Minami et.al.

http://www.tbp.cse.nagoya-u.ac.jp/MICAN/

Reference

* MICAN: a protein structure alignment algorithm that can handle Multiple-chains, Inverse alignments, C α only models, Alternative alignments, and Non-sequential alignments
* http://www.biomedcentral.com/1471-2105/14/24/abstract

* MICAN-SQ: a sequential protein structure alignment program that is applicable to monomers and all types of oligomers
* https://academic.oup.com/bioinformatics/article-abstract/34/19/3324/4992143?redirectedFrom=fulltext
