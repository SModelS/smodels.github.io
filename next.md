<p align="center"><img src="https://smodels.github.io/pics/banner.png" alt="banner"></p>

# A tool for interpreting simplified-model results from the LHC
Gael Alguero, Jan Heisig, Charanjit K. Khosa, Sabine Kraml, Suchita Kulkarni, Andre Lessa, Philipp Neuhuber, Humberto Reyes-Gonzalez, Wolfgang Waltenberger, Alicia Wongel

 <font color='grey'>Previously involved in SModelS: Federico Ambrogi, Juhi Dutta, Ursula Laa, Veronika Magerl, Wolfgang Magerl, Doris Proschofsky, Jory Sonneveld, Michael Traub, Matthias Wolf</font>

------------------------------------------------------------------------

|GitHub Project|
[![PyPI version](https://badge.fury.io/py/smodels.svg)](https://badge.fury.io/py/smodels)
[![CodeFactor](https://www.codefactor.io/repository/github/smodels/smodels/badge/master)](https://www.codefactor.io/repository/github/smodels/smodels/overview/master)

------------------------------------------------------------------------
### 03 Sep 2020: [SModelS version 1.2.4](https://github.com/SModelS/smodels/releases) is now available [(what's new)](http://smodels.readthedocs.io/en/stable/ReleaseUpdate.html)

### [arXiv:2009.01809](https://arxiv.org/abs/2009.01809): preprint describing v1.2.4 with its support for [pyhf](https://github.com/scikit-hep/pyhf)
------------------------------------------------------------------------

* A detailed documentation is available in the [online manual](http://smodels.readthedocs.io/)
* For instructions on how to install SModelS, check the [installation section in the manual](http://smodels.readthedocs.io/en/latest/Installation.html).
* You may also want to check the [release notes](https://smodels.readthedocs.io/en/stable/ReleaseUpdate.html)
and [known issues](https://github.com/SModelS/smodels/blob/master/KnownIssues)
* Here are the [list of analyses](docs/ListOfAnalyses) in the latest database version, the respective [validation plots](docs/Validation) and an [SMS dictionary](https://smodels.github.io/docs/SmsDictionary) explaining the Tx names used by SModelS.
* A discussion of re-interpretation methods and tools, and recommendations about the presentation of results can be found in this [report](https://arxiv.org/abs/2003.07868) by the [LHC Reinterpretation Forum](https://twiki.cern.ch/twiki/bin/view/LHCPhysics/InterpretingLHCresults), [arXiv:2003.07868](https://arxiv.org/abs/2003.07868).

### Mailing lists:

* For questions and comments, send an e-mail to: <smodels-users@lists.oeaw.ac.at>.
* To receive updates and announcements, subscribe to [smodels-info](https://lists.oeaw.ac.at/mailman/listinfo/smodels-info).

------------------------------------------------------------------------

## If you use SModelS, please cite the following papers:

* *SModelS database update v1.2.3*, Charanjit K. Khosa, Sabine Kraml, Andre Lessa, Philipp Neuhuber, Wolfgang Waltenberger, [arXiv:2005.00555](https://arxiv.org/abs/2005.00555), [LHEP 158 2020](https://doi.org/10.31526/lhep.2020.158)
* *SModelS v1.2: long-lived particles, combination of signal regions, and other novelties*, Federico Ambrogi et al., [arXiv:1811.10624](https://arxiv.org/abs/1811.10624), [CPC 251, June 2020, 106848](https://www.sciencedirect.com/science/article/pii/S0010465519302255?via%3Dihub)
* *Constraining new physics with searches for long-lived
particles: Implementation into SModelS*, Jan Heisig, Sabine Kraml, Andre Lessa, [arXiv:1808.05229](https://arxiv.org/abs/1808.05229), [Phys.Lett. B788 (2019) 87-95](https://doi.org/10.1016/j.physletb.2018.10.049).
* *SModelS extension with the CMS supersymmetry search results from Run 2*, Juhi Dutta, Sabine Kraml, Andre Lessa, Wolfgang Waltenberger, [arXiv:1803.02204](http://arxiv.org/abs/1803.02204), [LHEP 1 (2018) no.1,5-12](http://journals.andromedapublisher.com/index.php/LHEP/article/view/28)
* *SModelS v1.1 user manual: improving simplified model constraints with efficiency maps*, Federico Ambrogi, Sabine Kraml, Suchita Kulkarni, Ursula Laa, Andre Lessa, Veronika Magerl, Jory Sonneveld, Michael Traub, Wolfgang Waltenberger [arXiv:1701.06586](http://arxiv.org/abs/1701.06586), [CPC 227 (2018) 72-98](https://www.sciencedirect.com/science/article/pii/S0010465518300353?via%3Dihub)
 * *SModelS: a tool for interpreting simplified-model results from the LHC and its application to supersymmetry*, Sabine Kraml, Suchita Kulkarni, Ursula Laa, Andre Lessa,  Wolfgang Magerl, Doris Proschofsky, Wolfgang Waltenberger, [arXiv:1312.4175](http://arxiv.org/abs/arXiv:1312.4175), [EPJC (2014) 74:2868](http://link.springer.com/article/10.1140/epjc/s10052-014-2868-5)

Moreover

* If you use the *cross section calculator* please cite *Pythia and NLLfast*
* If you use the Fastlim results in the database, please cite *Fastlim 1.0* [arXiv:1402.40492](http://arxiv.org/abs/1402.40492), [EPJC74 (2014) 11](https://link.springer.com/article/10.1140%2Fepjc%2Fs10052-014-3163-1).

For convenience a .bib file is provided with the code containing all relevant references.
Likewise, a .bib file is provided in the database folder with references to all the ATLAS and CMS analyses used.

------------------------------------------------------------------------

## Working principle

SModelS is based on a general procedure to decompose Beyond the Standard Model (BSM) collider signatures presenting a Z<sub>2</sub> symmetry into Simplified Model Spectrum (SMS) topologies. Our method provides a way to cast BSM predictions for the LHC in a model independent framework,  which can be directly confronted with the relevant experimental constraints.  The main SModelS ingredients are

 * the decomposition of the BSM spectrum into SMS topologies
 * a database of experimental SMS results
 * the interface between decomposition and results database to compute limits

 <p align="center"><img src="https://smodels.github.io/pics/smodelsScheme.png" width="640" height="500"></p>


## Code and Database updates
* For code and database releases, see [Download](docs/CodeReleases)

## Experimental results in the database
* Here is the [list of analyses contained in the latest database version](docs/ListOfAnalyses)
* Same as above but [including superseded analyses](docs/ListOfAnalysesWithSuperseded)
* Pretty [validation plots](docs/Validation) for all analyses
* We also provide an [SMS dictionary](https://smodels.github.io/docs/SmsDictionary) explaining the Tx names used by SModelS

## Publications and Talks
See the [publications and talks](docs/SModelSTalks) page

<br><br>

<img src="logos/CCNH-logo.jpg" height="140pt" align="bottom"> &nbsp; &nbsp;
<img src="logos/hephy-logo.png" height="140pt" align="bottom"> &nbsp; &nbsp;
<img src="logos/LPSC_Grenoble_Modane.jpg" height="140pt" align="bottom"> <br>
<img src="logos/unihh.jpg" width="300pt" align="middle"> &nbsp;
<img src="logos/monash_university_logo.png" width="230pt" align="middle"> &nbsp; &nbsp;
<img src="logos/logo_UCLouvain.jpeg" width="280pt" align="middle">
