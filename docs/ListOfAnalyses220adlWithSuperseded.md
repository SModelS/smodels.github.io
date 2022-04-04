# List Of Analyses 2.2.0adl (including superseded and fastlim results)
List of analyses and topologies in the SMS results database, comprising 223 individual maps from 66 distinct signal regions, 10 different SMS topologies, from a total of 5 analyses.
The list has been created from the database version `2.2.0adl.`
Results from FastLim are included. There is also an  [sms dictionary](SmsDictionary220adl) and a [validation page](Validation220adl).
Link to list of results [without superseded and fastlim results](ListOfAnalyses220adl).

## Individual tables

### Run 2 - 13 TeV
In total, we have results from 0 ATLAS and 5 CMS 13 TeV searches.
 * [CMS upper limits](#CMSupperlimits13): 1 analyses, 3 results
 * [CMS efficiency maps](#CMSefficiencymaps13): 4 analyses, 11 results, 220 individual maps

### Run 1 - 8 TeV
In total, we have results from 0 ATLAS and 0 CMS 8 TeV searches.

<a name="CMSupperlimits13"></a>
## CMS, upper limits, 13 TeV (1 analyses)

| **ID** | **short description** | **L [1/fb]** | **Tx names** | **superseded by** | **exp. ULs [(3)](#A3)** |
|--------|-----------------------|--------------|--------------|-------------------|-------------------------|
| **Publications** | | | | | |
| [CMS-SUS-17-001](http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-17-001/index.html)<a name="CMS-SUS-17-001-eff"></a> | Stop search in dilepton + jets + Etmiss final state | 35.9 | [T2tt](SmsDictionary220adl+superseded#T2tt), [T2ttoff](SmsDictionary220adl+superseded#T2ttoff), [T6bbWW](SmsDictionary220adl+superseded#T6bbWW) | |  |

<a name="CMSefficiencymaps13"></a>
## CMS, efficiency maps, 13 TeV (4 analyses)

| **ID** | **short description** | **L [1/fb]** | **Tx names** | **superseded by** | **SR comb. [(4)](#A4)** |
|--------|-----------------------|--------------|--------------|-------------------|-------------------------|
| **Publications** | | | | | |
| [CMS-SUS-16-039-scalar](http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-039/index.html)<a name="CMS-SUS-16-039-scalar-eff"></a> | Multilepton EWK searches | 35.9 | [THigWZ](SmsDictionary220adl+superseded#THigWZ), [THigWZoff](SmsDictionary220adl+superseded#THigWZoff), [THigZZ](SmsDictionary220adl+superseded#THigZZ), [THigZZoff](SmsDictionary220adl+superseded#THigZZoff) | | cov. |
| [CMS-SUS-16-048](http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-048/index.html)<a name="CMS-SUS-16-048-agg"></a> | two soft OS leptons | 35.9 | [TChiWZoff](SmsDictionary220adl+superseded#TChiWZoff) | | cov. |
| [CMS-SUS-17-001-ma5](http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-17-001/index.html)<a name="CMS-SUS-17-001-ma5"></a> | Stop search in dilepton + jets + Etmiss final state | 35.9 | [T2tt](SmsDictionary220adl+superseded#T2tt), [T2ttoff](SmsDictionary220adl+superseded#T2ttoff), [T6bbWW](SmsDictionary220adl+superseded#T6bbWW) | | cov. |
| [CMS-SUS-19-005-adl](http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-19-005/index.html)<a name="CMS-SUS-19-005-adl-eff"></a> | 0L + jets, M<sub>T2</sub> | 137.0 | [T1bbbb](SmsDictionary220adl+superseded#T1bbbb), [T2bb](SmsDictionary220adl+superseded#T2bb), [T2tt](SmsDictionary220adl+superseded#T2tt) | |  |


<a name='A1'>(1)</a> ''Home-grown'' result, i.e. produced by SModelS collaboration, using recasting tools like MadAnalysis5 or CheckMATE.

<a name='A2'>(2)</a> Aggregated result; the results are the public ones, but aggregation is done by the SModelS collaboration.

<a name='A3'>(3)</a> Expected upper limits ('exp. ULs'): Can be used to compute a crude approximation of a likelihood, modelled as a truncated Gaussian.

<a name='A4'>(4)</a> Likelihood information for combination of signal regions ('SR comb.'): 'cov' = a covariance matrix for a simplified likelihood. 'json' = full likelihoods as pyhf json files.
<a name='A5'>(5)</a> Please note that by default we discard zeroes-only results from FastLim. To remain firmly conservative, we consider efficiencies with relative statistical uncertainties > 25% to be zero.


This page was created Mon Apr  4 12:36:04 2022.
