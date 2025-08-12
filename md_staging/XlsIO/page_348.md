```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_348.jpeg
document_name: XlsIO
page_number: 348
page_id: XlsIO#page_348
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:12:50Z
fidelity: lossless
-->

# Error Checking

## Overview
- Excel offers error-checking rules that can be enabled or disabled to display green indicators for warnings.

## Content

In this section, we will discuss the various error-checking rules available in Excel that can help identify and flag potential issues within your worksheet. Below are the detailed descriptions and scenarios for each rule:

### Key Rules for Error Checking

#### 1. Evaluates to Error Value
- This rule treats cells containing formulas that result in an error.
- It displays a warning in such cases.

#### 2. Text Date
- This rule treats formulas that contain text-formatted cells with years represented as 2-digits as an error.
- It displays a warning while checking for errors.

#### 3. Number Stored as Text
- This rule treats numbers formatted as text or preceded by an apostrophe as an error.
- It displays a warning in these scenarios.

#### 4. Inconsistent Formula in Region
- This rule treats a formula in a region of your worksheet that differs from the other formulas in the same region as an error.
- It displays a warning to indicate inconsistency.

#### 5. Formula Omits Cells in Region
- This rule treats formulas that omit certain cells in a region as an error.
- It displays a warning when such formulas are encountered.

#### 6. Unlocked Cells Containing Formulas
- This rule treats an unlocked cell containing a formula as an error.
- It displays a warning when checking for errors.

#### 7. Formulas Referring to Empty Cells
- This rule treats formulas that refer to empty cells as an error.
- It displays a warning when such occurrences are identified.

### Visual Representation

![](Figure 126: Error Checking)
**Figure 126:** Error Checking

The above figure shows an example of error-checking options in Excel, where the user has the option to convert a number stored as text into a numerical format or explore further options such as error handling and formula auditing.

### Summary

These error-checking rules in Excel are vital for maintaining data integrity and identifying potential issues within your spreadsheets. By enabling or disabling these rules as needed, you can tailor the error-checking experience to suit your specific needs and ensure accurate and reliable data handling.

## Cross References
See also:
- Advanced Error Handling in Excel
- Formula Auditing Tools in XlsIO

## RAG Annotations
<!-- tags: [syncfusion, xlsio, error checking, formulas, data integrity, winforms, version: 11.4.0.26] keywords: [error-checking rules, green indicators, formulas, warning, data consistency, number as text] -->
```