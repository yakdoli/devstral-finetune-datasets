```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_372.jpeg
document_name: XlsIO
page_number: 372
page_id: XlsIO#page_372
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:14:14Z
fidelity: lossless
-->

## Overview
- Manually inserted page breaks in Excel documents are included when converting to PDF.
- Print order and print area settings from Excel are preserved in the generated PDF document.
- Unicode support is maintained in headers and footers.
- Features for binding data objects to template markers are explained.

## Content

### Print Order Support
The Print order enabled in the Excel document will be considered while laying out the PDF page. The following are the page order options that are supported:

- Down Then Over
- Over Then Down

**Note:** It considers the Print Area and Page breaks while laying out, based on Print Order.

### Print Area Support
Print Area available in the Excel document will be considered while laying out the PDF document. Both, Row Index Only[1: 20] and Column Index Only[A:D] support have also been included in Unicode in Headers and Footers.

### Unicode in Headers and Footers
The other language and unicode present in the headers and footers will be preserved in the generated PDF document.

### For More Information Refer:
- AutoFilters
- Validating Data
- Template Markers
- Grouping and Ungrouping
- Print Settings

### 4.5.4.1 Binding Data Objects to Template Markers
Support is provided for binding business objects to template markers by binding the list of custom class objects to template markers. It also supports header names, images, and enumeration type in business objects.

#### Sub-features
- Representing the HeaderName using C# Attributes
- Representing the NumberFormat using C# Attributes
- Template Marker with the Class name

##### 4.5.4.1.1 Use Case Scenario
This feature helps users to bind business objects to template markers.

##### 4.5.4.1.2 Feature Summary
The following are the key features:
- Representing the HeaderName using C# Attributes – The Template Marker can apply the header name of the property (to be displayed) as the column name.
```

<!-- tags: [XlsIO, Print Order, Print Area, Unicode, Headers, Footers, Template Markers, Data Binding, WinForms, C# Attributes] keywords: [print breaks, PDF layout, business objects, custom class objects, header names, images, enumeration type, C# Attributes, use case scenario, feature summary] -->