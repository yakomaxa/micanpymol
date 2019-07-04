# micanpymol
This is a wrapper to run mican from pymol.

* micanpymol.py / for python3-based pymol
* micanpymol_python2.py / for python2-based pymol

## Requirements

You need mican binary in your PATH.

If you launch pymol from GUI, PATH variable may differ from ones launched from CUI.

So it's better to give the full-path for mican inside the script.


## Usage
First, load this script:
 ```run micanpymol.py```

Then run mican on pymol:
 ```mican protein1, protein2, -R -i 3 -m matrix.txt -a align.txt```

Something around temporary directories differs between python3 and python2.

For older pymol running on python2, use micanpymol_python2.py instead.

## What's inside

* Selections are output into two temp files.
* Mican superposes them.
* Script load mican-output pdb as dummy.
* Script aligns the original object to the dummy pdb.
* Dummies are deleted.

## About MICAN
Mican is a protein structure alignment program by Shintaro Minami et.al.

http://www.tbp.cse.nagoya-u.ac.jp/MICAN/

Reference

* MICAN: a protein structure alignment algorithm that can handle Multiple-chains, Inverse alignments, Cα only models, Alternative alignments, and Non-sequential alignments
* http://www.biomedcentral.com/1471-2105/14/24/abstract

* MICAN-SQ: a sequential protein structure alignment program that is applicable to monomers and all types of oligomers
* https://academic.oup.com/bioinformatics/article-abstract/34/19/3324/4992143?redirectedFrom=fulltext
