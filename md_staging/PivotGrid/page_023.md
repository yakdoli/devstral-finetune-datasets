```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_023.jpeg
document_name: PivotGrid
page_number: 023
page_id: PivotGrid#page_023
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:54:04Z
fidelity: lossless
-->

# Essential PivotGrid WindowsForms

The following table lists the different types of format settings.

## Overview
- Lists various format settings for data presentation.
- Explains SummaryType, which determines field summary calculations.
- Includes descriptions of summary operations such as SUM, AVERAGE, and other statistical computations.

## Content

### Table 7: Types of format settings
| Format          | Description         |
|------------------|---------------------|
| 0.00            | Decimal             |
| C               | Currency            |
| #,##0           | Thousand Separator   |
| #' degrees'     | Literal String Specifier |
| D               | Long Date           |

### 4.3 SummaryType
**SummaryType** determines the type of field summary such as count, sum, average, etc. It is an enumerator that should be defined in the PivotComputationInfo class. It contains the following types for performing calculations.

#### Table 8: Summary Type
| Summary Type          | Description                               |
|------------------------|-------------------------------------------|
| DoubleTotalSum        | Computes the sum of double or integer values. |
| DoubleAverage         | Computes the simple average of double or integer values. |
| DoubleMaximum         | Computes the maximum of double or integer values. |
| DoubleMinimum         | Computes the minimum of double or integer values. |
| DoubleStandardDeviation | Computes the standard deviation of double or integer values. |
| DoubleVariance        | Computes the variance of double or integer values. |
| Count                 | Computes the count of double or integer values. |
| DecimalTotalSum       | Computes the sum of decimal values. |

## API Reference (if applicable)
Not explicitly defined in this section. This content focuses on format settings and summary calculations without referencing specific APIs.

## Code Examples (multi-language supported)
Not explicitly provided in the current content.

## Page-level Navigation/TOC (if applicable)
Not explicitly included in this section.

## Cross References
Not explicitly mentioned in this content.

## RAG Annotations
<!-- tags: PivotGrid, FormatSettings, SummaryType, WindowsForms, Syncfusion, ComputationInfo keywords: format, decimal, currency, thousand separator, literal string specifier, long date, summary type, double total sum, double average, double maximum, double minimum, double standard deviation, double variance, count, decimal total sum -->
```