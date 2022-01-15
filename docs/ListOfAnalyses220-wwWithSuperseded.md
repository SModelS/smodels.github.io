# List Of Analyses 2.2.0-ww (including superseded and fastlim results)
List of analyses and topologies in the SMS results database, comprising 667 individual maps from 162 distinct signal regions, 11 different SMS topologies, from a total of 4 analyses.
The list has been created from the database version `2.2.0-ww.`
Results from FastLim are included. There is also an  [sms dictionary](SmsDictionary220-ww) and a [validation page](Validation220-ww).
Link to list of results [without superseded and fastlim results](ListOfAnalyses220-ww).

## Individual tables

### Run 2 - 13 TeV
In total, we have results from 1 ATLAS and 4 CMS 13 TeV searches.
 * [ATLAS upper limits](#ATLASupperlimits13): 1  analyses, 2 results
 * [ATLAS efficiency maps](#ATLASefficiencymaps13): 1  analyses, 2 results, 4 individual maps
 * [CMS upper limits](#CMSupperlimits13): 1  analyses, 3 results
 * [CMS efficiency maps](#CMSefficiencymaps13): 3  analyses, 12 results, 658 individual maps

### Run 1 - 8 TeV
In total, we have results from 0 ATLAS and 0 CMS 8 TeV searches.

<a name="CMSupperlimits13"></a>
## CMS, upper limits, 13 TeV (1 analyses)

| **ID** | **short description** | **L [1/fb]** | **Tx names** | **superseded by** | **exp. ULs [(3)](#A3)** |
|--------|-----------------------|--------------|--------------|-------------------|-------------------------|
| **Publications** | | | | | |
| [CMS-SUS-18-007](http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-18-007/index.html)<a name="CMS-SUS-18-007"></a> | H(diphoton) | 77.5 | [T6bbHH](SmsDictionary220-ww+superseded#T6bbHH), [TChiHH](SmsDictionary220-ww+superseded#TChiHH), [TChiWH](SmsDictionary220-ww+superseded#TChiWH) | | &#10004; |

<a name="CMSefficiencymaps13"></a>
## CMS, efficiency maps, 13 TeV (3 analyses)

| **ID** | **short description** | **L [1/fb]** | **Tx names** | **superseded by** | **SR comb. [(4)](#A4)** |
|--------|-----------------------|--------------|--------------|-------------------|-------------------------|
| **PAS** | | | | | |
| [CMS-PAS-SUS-16-052](http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-052/index.html)<a name="CMS-PAS-SUS-16-052-eff"></a> | soft lepton, <= 2 jets | 35.9 | [T2bbWWoff](SmsDictionary220-ww+superseded#T2bbWWoff) [(1)](#A1), [T6bbWWoff](SmsDictionary220-ww+superseded#T6bbWWoff) [(1)](#A1) | | cov. |
| **Publications** | | | | | |
| [CMS-SUS-16-050](http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-050/index.html)<a name="CMS-SUS-16-050-eff"></a> | 0L + top tag | 35.9 | [T1tttt](SmsDictionary220-ww+superseded#T1tttt), [T1ttttoff](SmsDictionary220-ww+superseded#T1ttttoff), [T2tt](SmsDictionary220-ww+superseded#T2tt), [T2ttoff](SmsDictionary220-ww+superseded#T2ttoff), [T5tctc](SmsDictionary220-ww+superseded#T5tctc) | | cov. |
| [CMS-SUS-16-050-agg](http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-050/index.html)<a name="CMS-SUS-16-050-agg-eff"></a> | 0L + top tag | 35.9 | [T1tttt](SmsDictionary220-ww+superseded#T1tttt), [T1ttttoff](SmsDictionary220-ww+superseded#T1ttttoff), [T2tt](SmsDictionary220-ww+superseded#T2tt), [T2ttoff](SmsDictionary220-ww+superseded#T2ttoff), [T5tctc](SmsDictionary220-ww+superseded#T5tctc) | | cov. |

<a name="ATLASupperlimits13"></a>
## ATLAS, upper limits, 13 TeV (1 analyses)

| **ID** | **short description** | **L [1/fb]** | **Tx names** | **superseded by** | **exp. ULs [(3)](#A3)** |
|--------|-----------------------|--------------|--------------|-------------------|-------------------------|
| **Publications** | | | | | |
| [ATLAS-SUSY-2019-09](https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2019-09/)<a name="ATLAS-SUSY-2019-09"></a> | three leptons | 139.0 | [TChiWH](SmsDictionary220-ww+superseded#TChiWH), [TChiWZ](SmsDictionary220-ww+superseded#TChiWZ) | | &#10004; |

<a name="ATLASefficiencymaps13"></a>
## ATLAS, efficiency maps, 13 TeV (1 analyses)

| **ID** | **short description** | **L [1/fb]** | **Tx names** | **superseded by** | **SR comb. [(4)](#A4)** |
|--------|-----------------------|--------------|--------------|-------------------|-------------------------|
| **Publications** | | | | | |
| [ATLAS-SUSY-2019-09](https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2019-09/)<a name="ATLAS-SUSY-2019-09-eff"></a> | three leptons | 139.0 | [TChiWH](SmsDictionary220-ww+superseded#TChiWH), [TChiWZ](SmsDictionary220-ww+superseded#TChiWZ) | |  |


<a name='A1'>(1)</a> ''Home-grown'' result, i.e. produced by SModelS collaboration, using recasting tools like MadAnalysis5 or CheckMATE.

<a name='A2'>(2)</a> Aggregated result; the results are the public ones, but aggregation is done by the SModelS collaboration.

<a name='A3'>(3)</a> Expected upper limits ('exp. ULs'): Can be used to compute a crude approximation of a likelihood, modelled as a truncated Gaussian.

<a name='A4'>(4)</a> Likelihood information for combination of signal regions ('SR comb.'): 'cov' = a covariance matrix for a simplified likelihood. 'json' = full likelihoods as pyhf json files.
<a name='A5'>(5)</a> Please note that by default we discard zeroes-only results from FastLim. To remain firmly conservative, we consider efficiencies with relative statistical uncertainties > 25% to be zero.


This page was created Sat Jan 15 22:37:56 2022.
