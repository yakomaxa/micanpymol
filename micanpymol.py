import subprocess
import tempfile
import os

def mican(mobile, target, option=""):


#make temporary dir and do everything there
    with tempfile.TemporaryDirectory() as dname:
        #turn off zooming when loading: set auto_zoom, off    
        old_auto_zoom=cmd.get("auto_zoom")
        cmd.set("auto_zoom","off")
        
        # print tmp dir name
        print("Temporary directory =" + dname)
        # make sure you have mican in PATH
        # directly giving 'execute' full path below is good alternative
        # For example : execute = "/usr/bin/mican"
        execute = "mican"
        tmptarget = dname + "/target.pdb"
        tmpmobile = dname + "/mobile.pdb"
        tmpout = dname + "/aligned.pdb"

        # save pdb for mican
        pymol.cmd.save(tmptarget, target)
        pymol.cmd.save(tmpmobile, mobile)

        modeoption = "-" + option
        option2 = "-o"
        outfile = tmpout
        

        mican = [execute, tmpmobile, tmptarget, option2, outfile]
        for op in option.split():
            if(op == "-o"):
                print("option -o is reserved")
                raise CmdException
            mican.append(op)
                
        proc=subprocess.run(mican,stdout = subprocess.PIPE)
        print(proc.stdout.decode("utf8")) # print result to pymol console
        
        pymol.cmd.load(outfile, "aligned")
        pymol.cmd.split_states("aligned")
        pymol.cmd.select("mobileback",mobile + " and backbone")
        pymol.cmd.align("mobileback", "aligned_0001 and backbone")
        # use cmd pair_fit if you think align is not good
        # print("Using cmd.align instead of cmd.pair_fit")
        # pymol.cmd.pair_fit("mobileback", "aligned_0001 and backbone")
        pymol.cmd.delete("mobileback")
        pymol.cmd.delete("aligned")
        pymol.cmd.delete("aligned_0001")
        pymol.cmd.delete("aligned_0002")
        # pymol.cmd.quit()

        # reset auto_zoom as you had set
        cmd.set("auto_zoom",old_auto_zoom)

pymol.cmd.extend("mican", mican)
cmd.auto_arg[0]['mican'] = cmd.auto_arg[0]['align']
cmd.auto_arg[1]['mican'] = cmd.auto_arg[1]['align']

