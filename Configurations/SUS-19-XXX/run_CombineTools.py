#!/usr/bin/env python
import timeit
import optparse
import LatinoAnalysis.Gardener.hwwtools as hwwtools

# functions used in everyday life ...
from LatinoAnalysis.Tools.commonTools import *

COMBINE = os.getenv('COMBINE')
PWD = os.getenv('PWD')
if(type(COMBINE) is None): COMBINE = " "
if(type(PWD) is None): PWD = " "

if __name__ == '__main__':

    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)
    
    parser.add_option('--outputDirDatacard' , dest='outputDirDatacard' , help='output directory'                          , default='./')   
    parser.add_option('--combineLocation'   , dest='combineLocation'   , help='Combine CMSSW Directory'                   , default=COMBINE)   
    parser.add_option('--combcfg'           , dest='combcfg'           , help='Combination dictionnary'                  , default='combineCards.py') 
    parser.add_option('--tag'               , dest='tag'               , help='Tag used for the tag file name'           , default='Test')
    parser.add_option('--sigset'            , dest='sigset'            , help='Tag used for the sigset file name'           , default="")
    parser.add_option('--years'             , dest='years'             , help='Year to be processed. \
Default: all'           , default="all")
    parser.add_option('--merge'            , dest='merge'             , help='Merge Datacards. Default=True'            , default=True)
    parser.add_option('--limits'            , dest='limits'            , help='Use higgs combine to calculate limits. Default=True'           , default=True)
    parser.add_option('--limrun'            , dest='limrun'            , help='Type of limit to be calculated. Default=blind'           , default='blind')
    parser.add_option('--test'              , dest='test'              , help='Run on test mode'           , default=False)
    parser.add_option('--sigmp'             , dest='signalMPcfg'      , help='Signal Mass Point cfg file'               , default='signalMassPoints.py')
    # read default parsing options as well
    hwwtools.addOptions(parser)
    hwwtools.loadOptDefaults(parser)
    (opt, args) = parser.parse_args()



    years=[]
    if opt.years =='2016':
        years=["2016"]
    elif opt.years == '2017':
        years=["2017"]
    else:
        years=["2016","2017","2018"]


    doTest = opt.test
    doMerge = opt.merge
    doLimits = opt.limits

    print "\n\t Optional arguments"
    print " tag                = ", opt.tag
    print " sigset             = ", opt.sigset
    print " Years              = ", years
    print " outputDirDatacard  = ", opt.outputDirDatacard
    print " combineLocation    = ", opt.combineLocation  
    print " Combination Cfg    = ", opt.combcfg
    print " Run on test mode   = ", doTest
    print " Merge Datacards    = ", doMerge
    print " Calculate limits   = ", doLimits
    print "\n"

    if(doTest):
        print "On Test mode"
        opt.sigset="T2tt_mS-450_mX-350"

    # Check whether any of the input config files exist
    isVarsF = os.path.exists(opt.variablesFile)
    isCutsF = os.path.exists(opt.cutsFile)
    isSignF = os.path.exists(opt.signalMPcfg)
    cfgsF={}
    fMiss=''
    fIsMiss= False
    vals = [isVarsF, isCutsF, isSignF]
    keys = ["Variables", "Cuts", "Signal"]
    for i in range(0, len(keys)):
        cfgsF[keys[i]]=vals[i]
        if vals[i] is False:
            fMiss+= keys[i] +" "
            fIsMiss=True
    #Stop the program if some file is missing
    if(fIsMiss is True):
        error=fMiss+"file Missing, check the input"
        raise NameError(error)

    #Generate dictionaries with variables and cuts
    variables = {}
    cuts = {}
    if (isVarsF):  exec(open(opt.variablesFile).read())
    if (isCutsF):  exec(open(opt.cutsFile).read())
    if (isSignF):  exec(open(opt.signalMPcfg).read())
    
    #Loop over Signal mass points year cuts and variables, to get all Datacards
    cmsenv=' eval `scramv1 runtime -sh` '
    dirDC=''
    tagDC=''
    combCommand=opt.combcfg+' '
    thereIsDC=False
    for model in signalMassPoints:
        print "Model:", model,"\tSignal set", opt.sigset
        if model not in opt.sigset:  continue
        for massPoint in signalMassPoints[model]:
            #print opt.sigset, "<-sigset, masspoint->", massPoint
            if not massPointInSignalSet(massPoint, opt.sigset):  continue
            print "Mass Point:", massPoint
            for year in years:
                for cut in cuts:
                    mpLoc='./Datacards/'+year+'/'+massPoint
                    cutLoc=mpLoc+'/'+cut
                    #print os.path.exists(mpLoc), mpLoc, "cuts", cuts, variables
                    if(os.path.exists(mpLoc) is not True):
                        print "Folder for MassPoint", massPoint," does not exist:"
                        continue
                    elif(os.path.exists(cutLoc) is not True):
                        print "Folder for Cut", cut, "Does not exist"
                        continue
                    for variable in variables:
                        thisDC=cutLoc+'/'+variable+"/datacard.txt"
                        tagDC =cut #Could be changed to more complex in the future
                        dirDC+=tagDC+'='+thisDC+' '
                        if(os.path.exists(thisDC) is True):
                            thereIsDC=True
                            print "Datacard: ", thisDC
                        else:
                            if(doTest):print "DC", thisDC, "does not exist"
    #Do not combine DC nor calculate limits if no DC is found
    if(thereIsDC is False):
        print "there are no Datacards in the folder under the input parameters"
    else:
    
        #Actually combine the DC
        finalDC='allDC_'+opt.sigset+'.txt'
        doCombcmsenv='cd '+opt.combineLocation+ ';'+cmsenv+'; cd -; '
        if(doMerge is True and thereIsDC is True):
            combCommand+=dirDC+">"+finalDC
            combPrint=''
            if(doTest): combPrint=combCommand
            print "Combining Datacards:", combPrint
            print doCombcmsenv+combCommand
            os.system(doCombcmsenv+combCommand)
            print "Final Datacard:", finalDC
        else:
            print "\n Data card merging option set to false: no DC combination is done"
            
        #Calculate the limits
        #Note that currently it would only calculate the last MP
        if(doLimits is True and thereIsDC is True):
            combCommand='combine -M AsymptoticLimits --run '+opt.limrun +' ' +finalDC+' -n allDC'+opt.limrun+'_'+opt.sigset
            print "Sending combination", combCommand
            os.system(doCombcmsenv+combCommand)
        else:
            print "Limit option set to false: no limits were calculated"

    
    os.system('mv allDC*.txt Datacards/')
    os.system('mv higgs*.root Datacards/')

