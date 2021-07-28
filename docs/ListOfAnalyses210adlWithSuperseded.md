# List Of Analyses 2.1.0adl (including superseded and fastlim results)
List of analyses and topologies in the SMS results database,comprising 42 individual maps from 21 distinct signal regions, 2 different SMS topologies, from a total of 2 analyses.
The list has been created from the database version `2.1.0adl.`
Results from FastLim are included. There is also an  [sms dictionary](SmsDictionary210adl) and a [validation page](Validation210adl).
Link to list of results [without superseded and fastlim results](ListOfAnalyses210adl).

## Individual tables

### Run 2 - 13 TeV
In total, we have results from 0 ATLAS and 2 CMS 13 TeV searches.
 * [CMS efficiency maps](#CMSefficiencymaps13): 2  analyses, 4 results, 42 individual maps

### Run 1 - 8 TeV
In total, we have results from 0 ATLAS and 0 CMS 8 TeV searches.

<a name="CMSefficiencymaps13"></a>
## CMS, efficiency maps, 13 TeV (2 analyses)

| **ID** | **short description** | **L [1/fb]** | **Tx names** | **superseded by** | **SR comb. [(4)](#A4)** |
|--------|-----------------------|--------------|--------------|-------------------|-------------------------|
| **Publications** | | | | | |
| [CMS-SUS-19-005](http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-19-005/index.html)<a name="CMS-SUS-19-005"></a> | 0L + jets, M<sub>T2</sub> | 137.0 | [T1](SmsDictionary210adl+superseded#T1), [T2](SmsDictionary210adl+superseded#T2) | |  |
| [CMS-SUS-19-006](http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-19-006/index.html)<a name="CMS-SUS-19-006"></a> | 0L + jets, MHT | 137.0 | [T1](SmsDictionary210adl+superseded#T1), [T2](SmsDictionary210adl+superseded#T2) | |  |


<a name='A1'>(1)</a> ''Home-grown'' result, i.e. produced by SModelS collaboration, using recasting tools like MadAnalysis5 or CheckMATE.

<a name='A2'>(2)</a> Aggregated result; the results are the public ones, but aggregation is done by the SModelS collaboration.

<a name='A3'>(3)</a> Expected upper limits ('exp. ULs'): Can be used to compute a crude approximation of a likelihood, modelled as a truncated Gaussian.

<a name='A4'>(4)</a> Likelihood information for combination of signal regions ('SR comb.'): 'cov' = a covariance matrix for a simplified likelihood. 'json' = full likelihoods as pyhf json files.
<a name='A5'>(5)</a> Please note that by default we discard zeroes-only results from FastLim. To remain firmly conservative, we consider efficiencies with relative statistical uncertainties > 25% to be zero.


This page was created Wed Jul 28 15:39:07 2021.
