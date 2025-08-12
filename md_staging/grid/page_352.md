```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_352.jpeg
document_name: grid
page_number: 352
page_id: grid#page_352
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:11:56Z
fidelity: lossless
-->

## Overview

- This section explains the SLN function, SALVAGE value, and deprecation of assets.
- It discusses the SLOPE function, which calculates the slope of a linear regression line.
- It explains the SMALL function, which retrieves the k-th smallest value from a dataset.

## Content

### SLN Depreciation Function

**SLN(cost, salvage, life)**, where:

- **cost** is the initial cost of the asset.
- **salvage** is the value at the end of the depreciation (sometimes called the salvage value of the asset).
- **life** is the number of periods over which the asset is depreciated (the useful life of the asset).

### 4.1.4.6.6.218 SLOPE

**SLOPE(known_y's, known_x's)**, where:

- Returns the slope of the linear regression line through data points in known_y's and known_x's.
- The slope is the rate of change along the regression line.

#### Syntax

**SLOPE(known_y's, known_x's)**, where:

- **known_y's** is an array or cell range of numeric dependent data points.
- **known_x's** is the set of independent data points.

#### Remarks

- The equation for the slope of the regression line is:

```
b = Σ(x - x̄)(y - ȳ) / Σ(x - x̄)²
```

  where x-bar and y-bar are the sample means AVERAGE(known_x's) and AVERAGE(known_y's).

### 4.1.4.6.6.219 SMALL

**SMALL(array, k)**, where:

- Returns the k-th smallest value in a data set.

#### Syntax

**SMALL(array, k)**, where:

  <!-- tags: [SLN, salvage, life, SLOPE, regression, slope, SMALL, k-th smallest] -->
```