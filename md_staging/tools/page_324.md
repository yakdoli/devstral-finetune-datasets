```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_324.jpeg
document_name: tools
page_number: 324
page_id: tools#page_324
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:05:36Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- This page explains how to configure the AutoComplete control in Syncfusion WinForms, specifically setting the AutoCompleteSource to "CustomSource" and viewing the resulting autocompletion behavior.
- It includes steps for configuring properties in the property grid, along with a visual representation of the runtime result.

## Content

not be none in this case. SeeSee [Source for AutoComplete Control](https://source-for-autocomplete-control) to know the different AutoCompleteModes.

1. 2. Set AutoCompleteSource to CustomSource as shown below. SeeSee [Source for AutoComplete Control](https://source-for-autocomplete-control) to know the different AutoComplete sources.

![Figure 137: Setting CustomSource](figure_137.png)

### Figure 137: Setting CustomSource

### Output

At runtime, type 'C' in the display area of ComboBoxAutoComplete, you will see the autocompletion behavior as shown below.

![Autocompletion behavior](autocompletion.png)

## API Reference

### AutoCompleteSource Enumeration

- **CustomSource**: The source of the autocompletion is specified through custom data.

### AutoCompleteModes Enumeration

- **Suggest**: Displays a drop-down list of suggestions that the user can select from.

## Code Examples

```csharp
// Setting AutoCompleteSource property
comboBoxAutoComplete1.AutoCompleteSource = AutoCompleteSource.CustomSource;

// Setting AutoCompleteMode property
comboBoxAutoComplete1.AutoCompleteMode = AutoCompleteMode.Suggest;
```

## Cross References

- SeeSee [Source for AutoComplete Control](https://source-for-autocomplete-control) for more information on different AutoCompleteModes and AutoComplete sources.

<!-- tags: [Syncfusion, WinForms, AutoComplete, AutoCompleteSource, AutoCompleteModes, ComboBox] keywords: [CustomSource, Suggest, AutoComplete control, property grid, runtime, autocompletion behavior] -->
```