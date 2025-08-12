```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_168.jpeg
document_name: XlsIO
page_number: 168
page_id: XlsIO#page_168
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:00:16Z
fidelity: lossless
-->

# XlsIO

## Overview

- Describes the common `Find` and `Replace` methods and properties in `XlsIO`.
- Outlines how to utilize various find and replace functionalities in `XlsIO`.
- Lists relevant methods and properties, including `FindFirst`, `FindAll`, etc.

## Content

### Find and Replace Dialog Box

**Figure 57: Find and Replace Dialog Box**

![Find and Replace Dialog Box](dialog_box_image_location)

**XlsIO** has the following common find and replace methods and properties, and their usage. This section describes all the methods listed below.

- **FindFirst**
- **FindAll**
- **FindStringStartswith**
- **FindStringEndswith**
- **Replace**

### ExcelFindType Enumerator in FindFirst and FindAll Methods

The following are the possible types of `params` of the `ExcelFindType` enumerator in the `FindFirst` and `FindAll` methods:

| **Member Name**            | **Description**                                         |
|-----------------------------|---------------------------------------------------------|
| Text                       | Represents the Text Finding type.                     |
| Formula                    | Represents the Formula Finding type.                  |
| FormulaStringValue         | Represents the FormulaStringValue Finding type.      |
| Error                      | Represents the Error Finding type.                    |
| Number                     | Represents the Number Finding type.                  |
| FormulaValue               | Represents the FormulaValue Finding type.            |

### ExcelFindOptions Enumerator in FindFirst and FindAll Methods

The following are the possible types of `params` of the `ExcelFindOptions` enumerator in the `FindFirst` and `FindAll` methods.

### Summary and References

#### See also:
- [Find and Replace Dialog Box](#figure-57)
- [ExcelFindType Enumerator](#excelfindtype)
- [ExcelFindOptions Enumerator](#excelfindoptions)

<!-- tags: [xlsio, find, replace, dialog, method, property, enum, type, enumeration, details] keywords: [xslrio, findfirst, finall, findstringstartswith, findstringendswith, replace, text finding, formula finding, error finding, number finding, formulastringvalue finding, formulavalue finding, excelfindtype, excelfindoptions] -->
```