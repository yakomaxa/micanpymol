# micanpymol
Wrapper to run mican from pymol

You need mican binary in your PATH. 

First, load this script:
 run micanpymol.py

Then run mican on pymol:
 mican protein1, protein2, -R -i 3 -m matrix.txt -a align.txt

## About Mican
Mican is a protein structure alignment program by Shintaro Minami et.al.

http://www.tbp.cse.nagoya-u.ac.jp/MICAN/

Reference

* MICAN: a protein structure alignment algorithm that can handle Multiple-chains, Inverse alignments, C α only models, Alternative alignments, and Non-sequential alignments
* http://www.biomedcentral.com/1471-2105/14/24/abstract

* MICAN-SQ: a sequential protein structure alignment program that is applicable to monomers and all types of oligomers
* https://academic.oup.com/bioinformatics/article-abstract/34/19/3324/4992143?redirectedFrom=fulltext
