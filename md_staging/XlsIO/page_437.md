```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_437.jpeg
document_name: XlsIO
page_number: 437
page_id: XlsIO#page_437
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:18:25Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- This page demonstrates the use of marker syntax to bind data in Excel files.
- It shows an example where data is bound to a marker that retains the formula for calculating product prices.

## Content

### Excel Data Binding Example

The following image (Figure 166) illustrates a screenshot of an Excel file after the data has been bound to a marker that retains the formula:

**Figure 166: Marker Syntax**

Here is a screen shot after binding the data with the marker that retains the formula.

| **Product ID** | **Quantity** | **Unit Price** | **Price** |
|-----------------|--------------|----------------|-----------|
| 4               | 8            | 6              | 48        |
| 5               | 9            | 8              | 72        |
| 3               | 4            | 2              | 8         |
| 3               | 2            | 5              | 10        |
| 8               | 2            | 2              | 4         |
| 1               | 9            | 7              | 63        |
| 5               | 6            | 3              | 18        |
| 7               | 9            | 9              | 81        |
| 0               | 2            | 1              | 2         |
| 9               | 8            | 7              | 56        |

The data shown above is structured as follows:
- **Product ID**: Identifies each product.
- **Quantity**: The number of units purchased.
- **Unit Price**: The price per unit for each product.
- **Price**: The total price for each product, calculated using the formula.

This example demonstrates how the marker in the Excel file retains the formula for calculating the total price to display accurate and dynamic results.

## RAG Annotations
<!-- tags: [Essential XlsIO, Excel, Marker Syntax, Data Binding, Formula Retention] keywords: [Product ID, Quantity, Unit Price, Price, Marker, Formula, Excel, Data Binding, Product Details, Path: /Report/Product Details] -->
```