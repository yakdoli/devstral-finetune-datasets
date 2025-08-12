```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_548.jpeg
document_name: chart
page_number: 548
page_id: chart#page_548
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:48:50Z
fidelity: lossless
--> 

# Essential Chart for Windows Forms

1. Calculate the standard error (SE) of the mean:
   \[
   \text{SE} = \frac{\sigma}{\sqrt{n}}
   \]

2. Then compute the z-score for the Z-test as below.
   \[
   z = \frac{x - \mu}{\text{SE}}
   \]

3. Finally, the z score is compared to a Z table which contains the percent of area under the normal curve between the mean and the z score. Using this table will indicate whether the calculated z score is within the realm of chance or it is so different from the mean that the sample mean is unlikely to have happened by chance.

## Using the Formula

The Z-test can be carried out on any two series values by using the `ZTest` method of `BasicStatisticalFormulas` class. Below table gives the detailed description of this method. The method returns an instance of `ZTestResult` object that saves the intermediate results and also the final z score of the test.

| **Method Name** | **Parameters** | **Return Value** |
|------------------|----------------|-----------------|
| ZTest            | 1. HypothesizedMeanDifference: the difference between the population means. <br> 2. VarianceOfFirstSeries: the variance within the first series population. <br> 3. VarianceOfSecondSeries: the variance within the second series population. <br> 4. Probability: the probability that gives the confidence level. <br> 5. FirstSeries: A `ChartSeries` object that stores the first group of data. <br> 6. SecondSeries: A `ChartSeries` object that stores the second group of data. | An `ZTestResult` object that has the following members: <br> • FirstSeriesMean <br> • SecondSeriesMean <br> • FirstSeriesVariance <br> • SecondSeriesVariance <br> • ZValue <br> • ProbabilityZOneTail <br> • ZCriticalValueOneTail <br> • ProbabilityZTwoTail <br> • ZCriticalValueTwoTail |

## Example
``` 
© 2013 Syncfusion. All rights reserved.
```

<!-- tags: [chart, windows forms, syncfusion, z-test, statistical formulas, standard error, z-score, probability, chartseries] keywords: [basicstatisticalformulas, ztest, ztestresult, firstseries, secondseries, hypotdifferencedifference, varianceofirstseries, variancesecondseries, probabilityz, two-tail] -->
``` 
