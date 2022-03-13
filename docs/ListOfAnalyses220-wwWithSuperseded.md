# List Of Analyses 2.2.0-ww (including superseded and fastlim results)
List of analyses and topologies in the SMS results database, comprising 95 individual maps from 49 distinct signal regions, 5 different SMS topologies, from a total of 3 analyses.
The list has been created from the database version `2.2.0-ww.`
Results from FastLim are included. There is also an  [sms dictionary](SmsDictionary220-ww) and a [validation page](Validation220-ww).
Link to list of results [without superseded and fastlim results](ListOfAnalyses220-ww).

## Individual tables

### Run 2 - 13 TeV
In total, we have results from 2 ATLAS and 1 CMS 13 TeV searches.
 * [ATLAS upper limits](#ATLASupperlimits13): 1  analyses, 3 results
 * [ATLAS efficiency maps](#ATLASefficiencymaps13): 1  analyses, 3 results, 4 individual maps
 * [CMS efficiency maps](#CMSefficiencymaps13): 1  analyses, 2 results, 88 individual maps

### Run 1 - 8 TeV
In total, we have results from 0 ATLAS and 0 CMS 8 TeV searches.

<a name="CMSefficiencymaps13"></a>
## CMS, efficiency maps, 13 TeV (1 analyses)

| **ID** | **short description** | **L [1/fb]** | **Tx names** | **superseded by** | **SR comb. [(4)](#A4)** |
|--------|-----------------------|--------------|--------------|-------------------|-------------------------|
| **PAS** | | | | | |
| [CMS-PAS-SUS-16-052](http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-052/index.html)<a name="CMS-PAS-SUS-16-052-eff"></a> | soft lepton, <= 2 jets | 35.9 | [T2bbWWoff](SmsDictionary220-ww+superseded#T2bbWWoff) [(1)](#A1), [T6bbWWoff](SmsDictionary220-ww+superseded#T6bbWWoff) [(1)](#A1) | | cov. |

<a name="ATLASupperlimits13"></a>
## ATLAS, upper limits, 13 TeV (1 analyses)

| **ID** | **short description** | **L [1/fb]** | **Tx names** | **superseded by** | **exp. ULs [(3)](#A3)** |
|--------|-----------------------|--------------|--------------|-------------------|-------------------------|
| **Publications** | | | | | |
| [ATLAS-SUSY-2018-41](https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2018-41/)<a name="ATLAS-SUSY-2018-41"></a> | ewkinos to boosted hadronic bosons | 139.0 | [TChiWH](SmsDictionary220-ww+superseded#TChiWH), [TChiWW](SmsDictionary220-ww+superseded#TChiWW), [TChiWZ](SmsDictionary220-ww+superseded#TChiWZ) | | &#10004; |

<a name="ATLASefficiencymaps13"></a>
## ATLAS, efficiency maps, 13 TeV (1 analyses)

| **ID** | **short description** | **L [1/fb]** | **Tx names** | **superseded by** | **SR comb. [(4)](#A4)** |
|--------|-----------------------|--------------|--------------|-------------------|-------------------------|
| **Publications** | | | | | |
| [ATLAS-SUSY-2018-41-eff](https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2018-41/)<a name="ATLAS-SUSY-2018-41-eff-eff"></a> | ewkinos to boosted hadronic bosons | 139.0 | [TChiWH](SmsDictionary220-ww+superseded#TChiWH), [TChiWW](SmsDictionary220-ww+superseded#TChiWW), [TChiWZ](SmsDictionary220-ww+superseded#TChiWZ) | |  |


<a name='A1'>(1)</a> ''Home-grown'' result, i.e. produced by SModelS collaboration, using recasting tools like MadAnalysis5 or CheckMATE.

<a name='A2'>(2)</a> Aggregated result; the results are the public ones, but aggregation is done by the SModelS collaboration.

<a name='A3'>(3)</a> Expected upper limits ('exp. ULs'): Can be used to compute a crude approximation of a likelihood, modelled as a truncated Gaussian.

<a name='A4'>(4)</a> Likelihood information for combination of signal regions ('SR comb.'): 'cov' = a covariance matrix for a simplified likelihood. 'json' = full likelihoods as pyhf json files.
<a name='A5'>(5)</a> Please note that by default we discard zeroes-only results from FastLim. To remain firmly conservative, we consider efficiencies with relative statistical uncertainties > 25% to be zero.


This page was created Sun Mar 13 21:55:49 2022.
