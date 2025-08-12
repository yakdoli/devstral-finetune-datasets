```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_752.jpeg
document_name: tools
page_number: 752
page_id: tools#page_752
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:32:25Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Describes methods and properties related to Text Box controls.
- Explains the behavior and appearance settings of IntegerTextBox controls.
- Highlights the ability to set or reset color properties dynamically.
  
## Content

### Foreground Settings of IntegerTextBox

The following table describes the methods and properties related to the foreground settings of the IntegerTextBox control:

| Method/Property                  | Description                                                             |
|-----------------------------------|-------------------------------------------------------------------------|
| ResetNegativeColor                | Resets the NegativeColor property to its default value.           |
| ResetZeroColor                    | Resets the ZeroColor property to its default value.               |
| SetControlColor                   | Sets the foreground color of the control depending on whether the current value is negative. |
| ShouldSerializePositiveColor      | Serializes the PositiveColor property.                               |
| ShouldSerializeNegativeColor      | Serializes the NegativeColor property.                               |
| ShouldSerializeZeroColor          | Serializes the ZeroColor property.                                   |

A sample demonstrating the Foreground Settings of the IntegerTextBox control is available in the following sample installation path:

```
..My Documents\Syncfusion\EssentialStudio\VersionNumber\Windows\Tools.Windows\Samples\2.0\Editors Package\EditorControls
```

### Behavior Settings

#### Negative Key Settings

The integer value of the IntegerTextBox can be reset or changed to a negative value using the properties listed below:

| IntegerTextBox Properties     | Description                                                                 |
|-------------------------------|-----------------------------------------------------------------------------|
| DeleteSelectionOnNegative     | Defines the behavior when the contents of the IntegerTextBox is fully selected, and the negative key is pressed by the user. <br> When set to 'True', the current value is replaced by the default value. |

## API Reference (if applicable)

Not explicitly provided in this section. For comprehensive API details, please refer to the Syncfusion documentation or the official SDK reference.

## Code Examples (multi-language supported)

Not applicable in this section. Code examples for behavior or implementation are absent in the provided content.

## Page-level Navigation/TOC (if applicable)

Not explicitly provided. This section appears to be a part of a larger document, so a full table of contents is not present here.

## Cross References

See also:
- Syncfusion documentation for additional controls and properties.
- Behavior settings and implementation details in the IntegerTextBox control.

## RAG Annotations

<!-- tags: [Syncfusion, Winforms, IntegerTextBox, NegativeColor, ZeroColor, PositiveColor, BehaviorSettings, ForegroundSettings] keywords: [ResetNegativeColor, ResetZeroColor, SetControlColor, ShouldSerializePositiveColor, ShouldSerializeNegativeColor, ShouldSerializeZeroColor, DeleteSelectionOnNegative, NegativeKey] -->
```