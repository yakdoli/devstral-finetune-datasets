```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_237.jpeg
document_name: calculate
page_number: 237
page_id: calculate#page_237
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:12:44Z
fidelity: lossless
-->

## Overview

- This page explains the functionality and syntax of the VARPA and VDB functions used in calculations within the Syncfusion Winforms domain.
- VARPA calculates variance based on the entire population, including logical values and text. 
- VDB returns the depreciation of an asset for any specified period using the double-declining balance method or others.

## Content

### VARPA

**Description**  
Calculates variance based on the entire population. In addition to numbers and text, logical values such as True and False are also included in the calculation.

**Syntax**  
VARPA(value1, value2, ...)

**Arguments**  
value1, value2, ... are arguments corresponding to a population.

**Remarks**  
- VARPA assumes that its arguments are the entire population. If your data represents a sample of the population, you must compute the variance using VARA.
- Arguments that contain True evaluate as 1; arguments that contain text or False evaluate as 0 (zero). If the calculation does not include text or logical values, use the VARP worksheet function instead.
- The equation for VARPA is:

\[
\frac{\sum{(x - \bar{x})^2}}{n}
\]

where:  
- \( x \) is the sample mean AVERAGE(value1, value2, ...).  
- \( n \) is the sample size.

### VDB

#### Overview
Returns the depreciation of an asset for any period you specify, including partial periods, using the double-declining balance method or some other method you specify. VDB stands for variable declining balance.

**Syntax**  
VDB(cost, salvage, life, start_period, end_period, factor, no_switch)

**Arguments**  
- **cost** is the initial cost of the asset.
- **salvage** is the value at the end of the depreciation (sometimes called the salvage value of the asset).

## API Reference (if applicable)

None explicitly provided in the text.

## Code Examples (multi-language supported)

None explicitly provided in the text.

## Page-level Navigation/TOC (if applicable)

None explicitly provided in the text.

## Cross References

None explicitly provided in the text.

## RAG Annotations

<!-- tags: variance, depreciation, VARPA, VDB, logical values, sample mean, double-declining balance, Syncfusion Winforms, Excel functions, mathematical calculations keywords: VARPA, VDB, depreciation, variance, population, sample, logical values, cost, salvage, double-declining balance, partial periods, mathematical calculations -->
```