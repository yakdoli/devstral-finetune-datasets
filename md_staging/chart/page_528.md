```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_528.jpeg
document_name: chart
page_number: 528
page_id: chart#page_528
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:47:26Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Explains the computation of Between and Within Variation in a statistical context.
- Focuses on calculating Sum of Squares, Degrees of Freedom, and Mean Squares for these variations.

## Content

### Between Variation

The formula for calculating the Sum of Squares among series is given by:

\[
SS_{\text{among}} = \left[ \frac{\left( \sum {y}_1 \right)^2}{n_1} + \frac{\left( \sum {y}_2 \right)^2}{n_2} + \cdots \frac{\left( \sum {y}_r \right)^2}{n_r} \right] - \frac{\left( \sum {y}_1 + \sum {y}_2 + \cdots \sum {y}_r \right)}{N}
\]

Where:
- \( y \) is the individual \( y \) points of the series,
- \( r \) is the number of series present,
- \( N \) is the total number of \( y \) points for all the series,
- \( n \) is the number of \( y \) points in each series.

### Within Variation

The formula for calculating the Sum of Squares within series is:

\[
SS_{\text{within}} = SS_{\text{total}} - SS_{\text{among}}
\]

### Degrees of Freedom

Using the above quantities, calculate the degrees of freedom (\( df \)) for these variations.

#### Between Variation

\[
df_{\text{among}} = r - 1
\]

#### Within Variation

\[
df_{\text{within}} = N - r
\]

Where:
- \( r \) is the number of series present,
- \( N \) is the total number of \( Y \) points for all the series.

### Mean Squares

As the next step, calculate the Mean Squares of these variations. The mean square for a variation can be calculated simply by dividing its sum of squares by its degrees of freedom.

#### Between Variation

\[
MS_{\text{among}} = \frac{SS_{\text{among}}}{df_{\text{among}}}
\]

#### Within Variation

<!-- tags: [chart, windows forms, mean squares, degrees of freedom, sum of squares, between variation, within variation] keywords: [variation, series, degrees of freedom, mean squares, total points, individual points] -->
```