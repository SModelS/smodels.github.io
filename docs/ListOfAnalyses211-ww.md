# List Of Analyses 2.1.1-ww 
List of analyses and topologies in the SMS results database,comprising 716 individual maps from 182 distinct signal regions, 9 different SMS topologies, from a total of 5 analyses.
The list has been created from the database version `2.1.1-ww.`
There is also an  [sms dictionary](SmsDictionary211-ww) and a [validation page](Validation211-ww).
Link to list of results [including superseded and fastlim results](ListOfAnalyses211-wwWithSuperseded).

## Individual tables

### Run 2 - 13 TeV
In total, we have results from 2 ATLAS and 3 CMS 13 TeV searches.
 * [ATLAS upper limits](#ATLASupperlimits13): 2  analyses, 4 results
 * [ATLAS efficiency maps](#ATLASefficiencymaps13): 2  analyses, 4 results, 54 individual maps
 * [CMS efficiency maps](#CMSefficiencymaps13): 3  analyses, 12 results, 658 individual maps

### Run 1 - 8 TeV
In total, we have results from 0 ATLAS and 0 CMS 8 TeV searches.

<a name="CMSefficiencymaps13"></a>
## CMS, efficiency maps, 13 TeV (3 analyses)

| **ID** | **short description** | **L [1/fb]** | **Tx names** | **SR comb. [(4)](#A4)** |
|--------|-----------------------|--------------|--------------|-------------------------|
| **PAS** | | | | |
| [CMS-PAS-SUS-16-052](http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-052/index.html)<a name="CMS-PAS-SUS-16-052"></a> | soft lepton, <= 2 jets | 35.9 | [T2bbWWoff](SmsDictionary211-ww#T2bbWWoff) [(1)](#A1), [T6bbWWoff](SmsDictionary211-ww#T6bbWWoff) [(1)](#A1) | cov. |
| **Publications** | | | | |
| [CMS-SUS-16-050](http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-050/index.html)<a name="CMS-SUS-16-050"></a> | 0L + top tag | 35.9 | [T1tttt](SmsDictionary211-ww#T1tttt), [T1ttttoff](SmsDictionary211-ww#T1ttttoff), [T2tt](SmsDictionary211-ww#T2tt), [T2ttoff](SmsDictionary211-ww#T2ttoff), [T5tctc](SmsDictionary211-ww#T5tctc) | cov. |
| [CMS-SUS-16-050-agg](http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-050/index.html)<a name="CMS-SUS-16-050-agg"></a> | 0L + top tag | 35.9 | [T1tttt](SmsDictionary211-ww#T1tttt), [T1ttttoff](SmsDictionary211-ww#T1ttttoff), [T2tt](SmsDictionary211-ww#T2tt), [T2ttoff](SmsDictionary211-ww#T2ttoff), [T5tctc](SmsDictionary211-ww#T5tctc) | cov. |

<a name="ATLASupperlimits13"></a>
## ATLAS, upper limits, 13 TeV (2 analyses)

| **ID** | **short description** | **L [1/fb]** | **Tx names** | **exp. ULs [(3)](#A3)** |
|--------|-----------------------|--------------|--------------|-------------------------|
| **Publications** | | | | |
| [ATLAS-SUSY-2018-08](https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2018-08/)<a name="ATLAS-SUSY-2018-08"></a> | OS leptons | 139.0 | [T2bbffff](SmsDictionary211-ww#T2bbffff), [T2tt](SmsDictionary211-ww#T2tt), [T2ttoff](SmsDictionary211-ww#T2ttoff) |  |
| [ATLAS-SUSY-2018-40](https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2018-40/)<a name="ATLAS-SUSY-2018-40"></a> | sbottoms with hadronic taus | 139.0 | [T6bbHH](SmsDictionary211-ww#T6bbHH) | &#10004; |

<a name="ATLASefficiencymaps13"></a>
## ATLAS, efficiency maps, 13 TeV (2 analyses)

| **ID** | **short description** | **L [1/fb]** | **Tx names** | **SR comb. [(4)](#A4)** |
|--------|-----------------------|--------------|--------------|-------------------------|
| **Publications** | | | | |
| [ATLAS-SUSY-2018-08](https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2018-08/)<a name="ATLAS-SUSY-2018-08"></a> | OS leptons | 139.0 | [T2bbffff](SmsDictionary211-ww#T2bbffff), [T2tt](SmsDictionary211-ww#T2tt), [T2ttoff](SmsDictionary211-ww#T2ttoff) |  |
| [ATLAS-SUSY-2018-40](https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2018-40/)<a name="ATLAS-SUSY-2018-40"></a> | sbottoms with hadronic taus | 139.0 | [T6bbHH](SmsDictionary211-ww#T6bbHH) |  |


<a name='A1'>(1)</a> ''Home-grown'' result, i.e. produced by SModelS collaboration, using recasting tools like MadAnalysis5 or CheckMATE.

<a name='A2'>(2)</a> Aggregated result; the results are the public ones, but aggregation is done by the SModelS collaboration.

<a name='A3'>(3)</a> Expected upper limits ('exp. ULs'): Can be used to compute a crude approximation of a likelihood, modelled as a truncated Gaussian.

<a name='A4'>(4)</a> Likelihood information for combination of signal regions ('SR comb.'): 'cov' = a covariance matrix for a simplified likelihood. 'json' = full likelihoods as pyhf json files.

This page was created Mon Aug  9 17:39:49 2021.
