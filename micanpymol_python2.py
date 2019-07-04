import subprocess
import tempfile
import os
import shutil

class TemporaryDirectory(object):
    # For Python2: taken from https://qiita.com/everylittle/items/aa7c6f612ff0a9db7f01 
    def __init__(self, suffix="", prefix="tmp", dir=None):
        self.__name = tempfile.mkdtemp(suffix, prefix, dir)
    def __enter__(self):
        return self.__name
    def __exit__(self, exc, value, tb):
        self.cleanup()

    @property
    def name(self):
        return self.__name
    def cleanup(self):
        shutil.rmtree(self.__name)
                                                                                
def mican(mobile, target, option=""):

#make temporary dir and do everything there
    with TemporaryDirectory() as dname:
        # print tmp dir name
        print("Temporary directory =" + dname)
        # print(os.path.exists(dname))
        # make sure you have mican in PATH
        # directly giving 'execute' full path below is good alternative
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
                
#       proc=subprocess.Popen(mican,stdout = subprocess.PIPE)
        proc=subprocess.check_call(mican)
        #proc=subprocess.Popen(mican)
        #print(proc.stdout.decode("utf8")) # print result to pymol console
        
        pymol.cmd.load(outfile, "aligned")
        pymol.cmd.split_states("aligned")
        pymol.cmd.select("mobileback",mobile + " and backbone")
        pymol.cmd.pair_fit("mobileback", "aligned_0001 and backbone")
        pymol.cmd.delete("mobileback")
        pymol.cmd.delete("aligned")
        pymol.cmd.delete("aligned_0001")
        pymol.cmd.delete("aligned_0002")
        # pymol.cmd.quit()

pymol.cmd.extend("mican", mican)
cmd.auto_arg[0]['mican'] = cmd.auto_arg[0]['align']
cmd.auto_arg[1]['mican'] = cmd.auto_arg[1]['align']

