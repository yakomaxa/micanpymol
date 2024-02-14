import subprocess
import tempfile
import numpy as np
import pymol.cmd
from pymol import stored

def output2lists(mican_output:str):
    iaa1 = []
    aa1 = []
    ch1 = []
    iaa2 = []
    aa2 = []
    ch2 = []
    close = []
    dist = []
    for l in mican_output.split('\n'):
        if l.startswith('ALIGN'):
            _, _iaa1, _aa1, _ch1, _iaa2, _aa2, _ch2, _close, _dist = l.split()
            if _iaa2 != '.':
                iaa1.append(_iaa1)
                iaa2.append(_iaa2)
                ch1.append(_ch1)
                ch2.append(_ch2)
                aa1.append(_aa1)
                aa2.append(_aa2)
                close.append(_close)
                dist.append(_dist)

    return iaa1, iaa2, aa1, aa2, ch1, ch2, close, dist

def get_selection(output_str: str, chain_indexes, mode="target"):
    iaa1, iaa2, _, _, ch1, ch2, _, _ = output2lists(output_str)
    iaa1 = np.array(iaa1,dtype=object)
    iaa2 = np.array(iaa2,dtype=object)
    ch1 = np.array(ch1,dtype=object)
    ch2 = np.array(ch2,dtype=object)
    resis1 = []
    resis2 = []
    chains1 = []
    chains2 = []
    if mode == "mobile":
        for c, i in chain_indexes:
            i1 = iaa1 == i
            i2 = ch1 == c
            ind = i1 & i2
            if ind.sum() != 0:
                resis1.append(iaa1[ind][0])
                chains1.append(ch1[ind][0])
                resis2.append(iaa2[ind][0])
                chains2.append(ch2[ind][0])
    elif mode == "target":
        for c, i in chain_indexes:
            i1 = iaa2 == i
            i2 = ch2 == c
            ind = i1 & i2
            if ind.sum() != 0:
                resis1.append(iaa1[ind][0])
                chains1.append(ch1[ind][0])
                resis2.append(iaa2[ind][0])
                chains2.append(ch2[ind][0])

    sele1  = []
    sele2  = []
    for i in range(len(resis1)):
        if resis1[i] != "" and chains1[i] != "":
            sele1.append("resi " + str(resis1[i]) + " and chain " + str(chains1[i]))
        if resis2[i] != "" and chains2[i] != "":
            sele2.append("resi " + str(resis2[i]) + " and chain " + str(chains2[i]))

    sele1 = " or ".join(sele1)
    sele2 = " or ".join(sele2)
    return sele1, sele2

def mican_select(mobile, target, selection, mode="mobile", option=""):
    # make temporary dir and do everything there
    with tempfile.TemporaryDirectory() as dname:
        execute = "/Users/sakuma/mybin/mican"
        tmptarget = dname + "/target.pdb"
        tmpmobile = dname + "/mobile.pdb"
        tmpout = dname + "/aligned.pdb"

        # save pdb for mican
        pymol.cmd.save(tmptarget, target)
        pymol.cmd.save(tmpmobile, mobile)

        modeoption = "-" + option
        option2 = "-z -o"
        outfile = tmpout

        mican = [execute, tmpmobile, tmptarget, option2, outfile]
        for op in option.split():
            if (op == "-o"):
                print("option -o is reserved")
                raise CmdException
            mican.append(op)

        proc = subprocess.run(mican, stdout=subprocess.PIPE)
        print(proc.stdout.decode("utf8"))  # print result to pymol console
        lines = proc.stdout.decode("utf8")
        stored.ca_cr = []
        if mode == "mobile":
            tmpsel = mobile + " and " + selection
            pymol.cmd.iterate(tmpsel + " and name ca", "stored.ca_cr.append([chain,resi])")
            sele_m, sele_t = get_selection(output_str=lines, chain_indexes=stored.ca_cr, mode="mobile")
        elif mode == "target":
            tmpsel = target + " and " + selection
            pymol.cmd.iterate(tmpsel + " and name ca", "stored.ca_cr.append([chain,resi])")
            sele_m, sele_t = get_selection(output_str=lines, chain_indexes=stored.ca_cr, mode="target")
        if len(sele_m) == 0 or len(sele_t) == 0:
            print("No selection found")
            return
            
        pymol.cmd.load(outfile, "aligned")
        pymol.cmd.split_states("aligned")
        pymol.cmd.select("mobileback", mobile + " and backbone")
        pymol.cmd.align("mobileback", "aligned_0001 and backbone")
        pymol.cmd.delete("mobileback")
        pymol.cmd.delete("aligned")
        pymol.cmd.delete("aligned_0001")
        pymol.cmd.delete("aligned_0002")
        name1 = pymol.cmd.get_unused_name("aligned")
        pymol.cmd.select(name1, mobile + " and " + sele_m)
        name2 = pymol.cmd.get_unused_name("aligned")
        pymol.cmd.select(name2, target + " and " + sele_t)
        # pymol.cmd.quit()

pymol.cmd.extend("select_mican", mican_select)
cmd.auto_arg[0]['select_mican'] = cmd.auto_arg[0]['align']
cmd.auto_arg[1]['select_mican'] = cmd.auto_arg[1]['align']
cmd.auto_arg[2]['select_mican'] = cmd.auto_arg[1]['select']
