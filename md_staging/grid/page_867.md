```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_867.jpeg
document_name: grid
page_number: 867
page_id: grid#page_867
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:46:07Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- This page demonstrates how to apply conditional formatting to the grouping grid using both the UI designer and programming.
- It includes steps for defining a Conditional Format Descriptor, specifying filter criteria, and applying styles.

## Content

### GridConditionalFormatDescriptor Collection Editor
The conditional formatting can be managed through the UI designer as shown in **Figure 337**.

![GridConditionalFormatDescriptor Collection Editor](#)

**Figure 337: GridConditionalFormatDescriptor Collection Editor**

#### Programatically

The following code example illustrates how to apply conditional formatting to the grouping grid.

1. **Define a Conditional Format Descriptor and specify a filter criteria and style to be applied.**

```csharp
// Apply the following style to the records whose CustomerID starts
// with 'A'.
```

## API Reference
- **GridConditionalFormatDescriptor**: Represents a descriptor for conditional formatting.

## Code Examples
- The example demonstrates how to apply conditional formatting based on the `CustomerID` attribute in a grid.

## Cross References
- See related sections for more information on grid formatting and conditional expressions.

<!-- tags: [conditional formatting, gridConditionalFormatDescriptor, grid forms, syncfusion winforms] keywords: [conditional formatting, gridConditionalFormatDescriptor, Grid forms] -->
```