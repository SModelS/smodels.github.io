#!/usr/bin/env python3

#import os, sys
#sys.path.insert(0,'/scratch-cbe/users/wolfgan.waltenberger/git')
#sys.path.insert(0,'/scratch-cbe/users/wolfgan.waltenberger/git/protomodels')
#sys.path.insert(0,'/scratch-cbe/users/wolfgan.waltenberger/git/protomodels/ptools')
from ptools import updateHiscores
from base.runEnviron import RunEnviron
#batchjob="SLURM_JOBID" in os.environ
batchjob = False
environ = RunEnviron()
updateHiscores.loop ( maxruns=1, createPlots=not batchjob,
    uploadTo='rundir8_310', environ=environ, walkerid='uphi' )
