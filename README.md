<p align="center"><img src="https://smodels.github.io/pics/banner.png" alt="banner"></p>
  
# A tool for interpreting simplified-model results from the LHC 
Federico Ambrogi, Juhi Dutta, Jan Heisig, Sabine Kraml, Suchita Kulkarni, Ursula Laa, Andre Lessa, Veronika Magerl, Wolfgang Magerl, Doris Proschofsky, Humberto Reyes-Gonzalez, Jory Sonneveld, Michael Traub, Wolfgang Waltenberger, Matthias Wolf, Alicia Wongel

------------------------------------------------------------------------   
                                                                           
## 24 Oct 2019: Our old smodels.hephy.at server is down! 
Using e.g. **official** as your database path will currently not work (sorry!).
Please use instead full database path names, e.g.
*http://smodels.github.io/database/official122* for the official 1.2.2
database. We apologize for the inconvenience.

## 28 Nov 2018: [SModelS version 1.2.2](https://github.com/SModelS/smodels/releases) is now available [(what's new)](http://smodels.readthedocs.io/en/latest/ReleaseUpdate.html)

------------------------------------------------------------------------

* A detailed documentation is available in the [online manual](http://smodels.readthedocs.io/)
* You may also want to check the [release notes](https://smodels.readthedocs.io/en/stable/ReleaseUpdate.html)
and [known issues](https://github.com/SModelS/smodels/blob/master/KnownIssues)
* For questions and comments, send an e-mail to: <smodels-users@lists.oeaw.ac.at> 
* To receive updates and announcements, subscribe to [smodels-info](https://lists.oeaw.ac.at/mailman/listinfo/smodels-info).

------------------------------------------------------------------------

# If you use SModelS, please cite the following papers:

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

# Introduction                                            
                                                          
SModelS is based on a general procedure to decompose Beyond the Standard Model (BSM) collider signatures presenting a Z<sub>2</sub> symmetry into Simplified Model Spectrum (SMS) topologies. Our method provides a way to cast BSM predictions for the LHC in a model independent framework,  which can be directly confronted with the relevant experimental constraints.  The main SModelS ingredients are

 * the decomposition of the BSM spectrum into SMS topologies
 * a database of experimental SMS results
 * the interface between decomposition and results database to compute limits
 
 <p align="center"><img src="https://smodels.github.io/pics/smodelsScheme.png" width="680"></p>

-------------------------------------------------------------------------

# Code and Database updates
* For code and database releases, see [Download](docs/CodeReleases)

# Installation
* For instructions on how to install SModelS, check the [installation section in the manual](http://smodels.readthedocs.io/en/latest/Installation.html).

# Experimental results in the database
* Here is the [list of analyses contained in the latest database version](docs/ListOfAnalyses)
* Same as above but [including superseded analyses](docs/ListOfAnalysesWithSuperseded)
* Pretty [validation plots](docs/Validation) for all analyses
* We also provide an [SMS dictionary](https://smodels.github.io/docs/SmsDictionary) explaining the Tx names used by SModelS

# Publications and Talks
See the [publications and talks](docs/SModelSTalks) page

# Recommendations about the presentation of results
A wishlist regarding the presentation of results was compiled by the LHC
reinterpretation forum, see [arXiv:2003.07868](https://arxiv.org/abs/2003.07868).

<img src="http://micheldesvignes38.free.fr/ITSarchitep/logos/logoLPSC.jpg" width="250pt" align="top"> &nbsp;
<img src="https://smodels.github.io/logos/hephy-logo.png" width="300pt" align="top"> &nbsp;
<img src="logos/CCNH-logo.jpg" width="250pt" align="top"> &nbsp;
<img src="https://smodels.github.io/logos/unihh.jpg" width="300pt" align="top"> &nbsp;
<img src="https://smodels.github.io/logos/monash_university_logo.png" width="230pt" align="top"> &nbsp;
<img src="https://smodels.github.io/logos/logo_UCLouvain.jpeg" width="280pt" align="top">
