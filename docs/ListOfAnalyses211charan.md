# List Of Analyses 2.1.1charan 
List of analyses and topologies in the SMS results database,comprising 12 individual maps from 5 distinct signal regions, 12 different SMS topologies, from a total of 5 analyses.
The list has been created from the database version `2.1.1charan.`
Results from FastLim are included. There is also an  [sms dictionary](SmsDictionary211charan) and a [validation page](Validation211charan).
Link to list of results [including superseded results](ListOfAnalyses211charanWithSuperseded).

## Individual tables

### Run 2 - 13 TeV
In total, we have results from 0 ATLAS and 5 CMS 13 TeV searches.
 * [CMS upper limits](#CMSupperlimits13): 5  analyses, 12 results

### Run 1 - 8 TeV
In total, we have results from 0 ATLAS and 0 CMS 8 TeV searches.

<a name="CMSupperlimits13"></a>
## CMS, upper limits, 13 TeV (5 analyses)

| **ID** | **short description** | **L [1/fb]** | **Tx names** | **exp. ULs [(3)](#A3)** |
|--------|-----------------------|--------------|--------------|-------------------------|
| **Publications** | | | | |
| [CMS-SUS-17-003](https://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-17-003/)<a name="CMS-SUS-17-003"></a> | a tau lepton pair + Etmiss | 35.9 | [TChiChipmStauStau](SmsDictionary211charan#TChiChipmStauStau) |  |
| [CMS-SUS-17-004](http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-17-004/index.html)<a name="CMS-SUS-17-004"></a> | Chargino-neutralino production with WZ topology | 35.9 | [TChiWH](SmsDictionary211charan#TChiWH), [TChiWZ](SmsDictionary211charan#TChiWZ), [TChiWZoff](SmsDictionary211charan#TChiWZoff) |  |
| [CMS-SUS-17-005](https://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-17-005/)<a name="CMS-SUS-17-005"></a> | multijets + Etmiss, top tagging | 35.9 | [T2bbffff](SmsDictionary211charan#T2bbffff), [T6bbWWoff](SmsDictionary211charan#T6bbWWoff) | &#10004; |
| [CMS-SUS-17-006](https://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-17-006/)<a name="CMS-SUS-17-006"></a> | High momentum Higgs Boson+ Etmiss | 35.9 | [T5HH](SmsDictionary211charan#T5HH), [T5HZ](SmsDictionary211charan#T5HZ) | &#10004; |
| [CMS-SUS-18-002](https://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-18-002/)<a name="CMS-SUS-18-002"></a> | photon, jets, b-jets+ Etmiss, top tagging | 35.9 | [T5Hg](SmsDictionary211charan#T5Hg), [T5bbbbZg](SmsDictionary211charan#T5bbbbZg), [T5ttttZg](SmsDictionary211charan#T5ttttZg), [T6ttZg](SmsDictionary211charan#T6ttZg) | &#10004; |


<a name='A1'>(1)</a> ''Home-grown'' result, i.e. produced by SModelS collaboration, using recasting tools like MadAnalysis5 or CheckMATE.

<a name='A2'>(2)</a> Aggregated result; the results are the public ones, but aggregation is done by the SModelS collaboration.

<a name='A3'>(3)</a> Expected upper limits ('exp. ULs'): Can be used to compute a crude approximation of a likelihood, modelled as a truncated Gaussian.

<a name='A4'>(4)</a> Likelihood information for combination of signal regions ('SR comb.'): 'cov' = a covariance matrix for a simplified likelihood. 'json' = full likelihoods as pyhf json files.
<a name='A5'>(5)</a> Please note that by default we discard zeroes-only results from FastLim. To remain firmly conservative, we consider efficiencies with relative statistical uncertainties > 25% to be zero.


This page was created Mon Jun 28 10:47:27 2021.