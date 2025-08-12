```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_140.jpeg
document_name: chart
page_number: 140
page_id: chart#page_140
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:24:31Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Explains the Three Line Break Chart, a chart type designed for visualizing price changes in financial data.
- Highlights the methodology and structure of the chart, including how it differs from point and figure charts.
- Describes the role of PriceUpColor and PriceDownColor in indicating bullish and bearish trends.
- Discusses the importance of the ReversalAmount in determining when a new vertical box is rendered.

## Content

### 4.4.7.7 Three Line Break Chart
The Three Line Break Chart is similar in concept to point and figure charts. The Three Line Break charting method is so-named because of the number of lines typically used. It displays a series of vertical boxes ("lines") that are based on changes in prices. It ignores the passage of time.

The three-line break chart looks like a series of rising and falling lines of varying heights. Each new line, like the X's and O's of a point and figure chart, occupies a new column. Based on closing prices (or highs and lows), a new rising line is drawn if the previous high is exceeded, and a new falling line is drawn if the price hits a new low. Change in price trends are highlighted by changing colors. Use the PriceUpColor to indicate a bullish trend and PriceDownColor to indicate a bearish trend.

The ReversalAmount specifies the threshold amount by which the price should change to begin rendering a new vertical box in the appropriate direction.

![Three Line Break Series](https://image.png)
**Figure 79: Chart displaying Three Line Break Series**

### Chart Details
Details

## Page-level Navigation/TOC
- Essential Chart for Windows Forms
  - 4.4.7.7 Three Line Break Chart

## Cross References
- Refer to point and figure charts for comparison.
- Refer to PriceUpColor and PriceDownColor for color coding details.

<!-- tags: [chart, financial data, windows forms, line break chart, price trend, syncfusion, point figure chart] keywords: [three line break chart, priceupcolor, pricedowncolor, reversalamount, vertical boxes, financial visualization] -->
```