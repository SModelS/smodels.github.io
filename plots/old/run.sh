#!/bin/sh

../../smodels-utils/validation/combineValidation.py -a CMS-SUS-13-012-eff -v "T6bbWW_2EqMassAx_EqMassB0.5x+0.5y_EqMassCy.py,T6bbWWoff_2EqMassAx_EqMassB0.5x+0.5y_EqMassCy.py"
../../smodels-utils/validation/combineValidation.py -a CMS-SUS-13-012-eff -v "T5WW_2EqMassAx_EqMassB0.5x+0.5y_EqMassCy.py,T5WWoff_2EqMassAx_EqMassB0.5x+0.5y_EqMassCy.py"
../../smodels-utils/validation/combineValidation.py -a ATLAS-SUSY-2013-09-eff -v "T6ttWW_2EqMassAx_EqMassB2y_EqMassCy.py,T6ttWWoff_2EqMassAx_EqMassB2y_EqMassCy.py"
../../smodels-utils/validation/combineValidation.py -a ATLAS-SUSY-2013-04-eff -v "T5WW_2EqMassAx_EqMassB0.5x+0.5y_EqMassCy.py,T5WWoff_2EqMassAx_EqMassB0.5x+0.5y_EqMassCy.py"
../../smodels-utils/validation/combineValidation.py -a ATLAS-SUSY-2013-11-eff -v "TChiWW_2EqMassAx_EqMassBy.py,TChiWWoff_2EqMassAx_EqMassBy.py" --yrange "[0,190]" --xrange "[0,320]"

../../smodels-utils/covariances/plotBestSRs.py -a ATLAS-SUSY-2013-11-eff -v "TChiWW_2EqMassAx_EqMassBy.py,TChiWWoff_2EqMassAx_EqMassBy.py" --max_y 190. --max_x 350.

../../smodels-utils/covariances/plotBestSRs.py -a CMS-SUS-13-012-eff -v "T5WW_2EqMassAx_EqMassB0.5x+0.5y_EqMassCy.py,T5WWoff_2EqMassAx_EqMassB0.5x+0.5y_EqMassCy.py"
../../smodels-utils/covariances/plotBestSRs.py -a CMS-SUS-13-012-eff -v "T6bbWW_2EqMassAx_EqMassB0.5x+0.5y_EqMassCy.py,T6bbWWoff_2EqMassAx_EqMassB0.5x+0.5y_EqMassCy.py"

../../smodels-utils/covariances/plotBestSRs.py -a ATLAS-SUSY-2013-09-eff -v "T6ttWW_2EqMassAx_EqMassB2y_EqMassCy.py,T6ttWWoff_2EqMassAx_EqMassB2y_EqMassCy.py"

../../smodels-utils/covariances/plotRatio.py -a1 ATLAS-SUSY-2013-09 -a2 ATLAS-SUSY-2013-09-eff -v1 "T6ttWW_2EqMassAx_EqMassB2y_EqMassCy.py,T6ttWWoff_2EqMassAx_EqMassB2y_EqMassCy.py" -v2 "T6ttWW_2EqMassAx_EqMassB2y_EqMassCy.py,T6ttWWoff_2EqMassAx_EqMassB2y_EqMassCy.py" -Z 1.5 -z .1 -l1 'UL' -l2 'eff' -s

../../smodels-utils/covariances/plotBestSRs.py -a ATLAS-SUSY-2013-04-eff -v "T5WW_2EqMassAx_EqMassB0.5x+0.5y_EqMassCy.py,T5WWoff_2EqMassAx_EqMassB0.5x+0.5y_EqMassCy.py"

#../../smodels-utils/covariances/plotBestSRs.py -a ATLAS-SUSY-2018-06-eff -v "TChiWZ_2EqMassAx_EqMassBy.py,TChiWZoff_2EqMassAx_EqMassBy.py"
#../../smodels-utils/validation/combineValidation.py -a ATLAS-SUSY-2018-06-eff -v "TChiWZ_2EqMassAx_EqMassBy.py,TChiWZoff_2EqMassAx_EqMassBy.py"
#../../smodels-utils/covariances/plotRatio.py -a1 ATLAS-SUSY-2018-06 -a2 ATLAS-SUSY-2018-06-eff -v1 "TChiWZ_2EqMassAx_EqMassBy.py,TChiWZoff_2EqMassAx_EqMassBy.py" -v2 "TChiWZ_2EqMassAx_EqMassBy.py,TChiWZoff_2EqMassAx_EqMassBy.py" -Z 4. -l1 'UL' -l2 'eff' -s

./mkPage.py

mdcat README.md
