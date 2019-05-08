import subprocess
import tempfile
import os

def mican(mobile, target, option=""):
    
#make temporary dir and do everything there
    with tempfile.TemporaryDirectory() as dname:
        # print tmp dir name
        print("Temporary directory =" + dname)        
        # make sure you have mican in PATH
        # directly giving the full path below is a good alternative
        execute = "mican"
        tmptarget = dname + "/target.pdb"
        tmpmobile = dname + "/mobile.pdb"
        tmpout = dname + "/aligned.pdb"

        # save pdb for mican to read
        pymol.cmd.save(tmptarget, target)
        pymol.cmd.save(tmpmobile, mobile)

        option1 = "-" + option
        option2 = "-o"
        outfile = tmpout

        mican = [execute, option1, tmpmobile, tmptarget, option2, outfile]
        subprocess.run(mican)
        
        pymol.cmd.load(outfile, "aligned")
        pymol.cmd.split_states("aligned")
        pymol.cmd.select("mobileback",mobile + " and backbone")
        pymol.cmd.align("mobileback", "aligned_0001 and backbone")
        #pymol.cmd.save("mobile_test.pdb", "mobileback")
        pymol.cmd.delete("mobileback")
        pymol.cmd.delete("aligned")
        pymol.cmd.delete("aligned_0001")
        pymol.cmd.delete("aligned_0002")
        # pymol.cmd.quit()

pymol.cmd.extend("mican", mican)
cmd.auto_arg[0]['mican'] = cmd.auto_arg[0]['align']
cmd.auto_arg[1]['mican'] = cmd.auto_arg[1]['align']

