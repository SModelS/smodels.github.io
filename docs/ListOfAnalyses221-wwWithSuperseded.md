# List Of Analyses 2.2.1-ww (including superseded and fastlim results)
List of analyses and topologies in the SMS results database, comprising 91 individual maps from 45 distinct signal regions, 5 different SMS topologies, from a total of 2 analyses.
The list has been created from the database version `2.2.1-ww.`
Results from FastLim are included. There is also an  [sms dictionary](SmsDictionary221-ww) and a [validation page](Validation221-ww).
Link to list of results [without superseded and fastlim results](ListOfAnalyses221-ww).

## Individual tables

### Run 2 - 13 TeV
In total, we have results from 0 ATLAS and 2 CMS 13 TeV searches.
 * [CMS upper limits](#CMSupperlimits13): 1 analyses, 3 results
 * [CMS efficiency maps](#CMSefficiencymaps13): 1 analyses, 2 results, 88 individual maps

### Run 1 - 8 TeV
In total, we have results from 0 ATLAS and 0 CMS 8 TeV searches.

<a name="CMSupperlimits13"></a>
## CMS, upper limits, 13 TeV (1 analyses)

| **ID** | **short description** | **L [1/fb]** | **Tx names** | **superseded by** | **exp. ULs [(3)](#A3)** |
|--------|-----------------------|--------------|--------------|-------------------|-------------------------|
| **Publications** | | | | | |
| [CMS-SUS-20-004](http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-20-004/index.html)<a name="CMS-SUS-20-004-eff"></a> | Higgsino search | 137.0 | [T5HH](SmsDictionary221-ww+superseded#T5HH), [TChiHH](SmsDictionary221-ww+superseded#TChiHH), [TChiHHG](SmsDictionary221-ww+superseded#TChiHHG) | | &#10004; |

<a name="CMSefficiencymaps13"></a>
## CMS, efficiency maps, 13 TeV (1 analyses)

| **ID** | **short description** | **L [1/fb]** | **Tx names** | **superseded by** | **SR comb. [(4)](#A4)** |
|--------|-----------------------|--------------|--------------|-------------------|-------------------------|
| **PAS** | | | | | |
| [CMS-PAS-SUS-16-052](http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-052/index.html)<a name="CMS-PAS-SUS-16-052-eff"></a> | soft lepton, <= 2 jets | 35.9 | [T2bbWWoff](SmsDictionary221-ww+superseded#T2bbWWoff) [(1)](#A1), [T6bbWWoff](SmsDictionary221-ww+superseded#T6bbWWoff) [(1)](#A1) | | cov. |


<a name='A1'>(1)</a> ''Home-grown'' result, i.e. produced by SModelS collaboration, using recasting tools like MadAnalysis5 or CheckMATE.

<a name='A2'>(2)</a> Aggregated result; the results are the public ones, but aggregation is done by the SModelS collaboration.

<a name='A3'>(3)</a> Expected upper limits ('exp. ULs'): Can be used to compute a crude approximation of a likelihood, modelled as a truncated Gaussian.

<a name='A4'>(4)</a> Likelihood information for combination of signal regions ('SR comb.'): 'cov' = a covariance matrix for a simplified likelihood. 'json' = full likelihoods as pyhf json files.
<a name='A5'>(5)</a> Please note that by default we discard zeroes-only results from FastLim. To remain firmly conservative, we consider efficiencies with relative statistical uncertainties > 25% to be zero.


This page was created Tue Apr 19 18:55:47 2022.
