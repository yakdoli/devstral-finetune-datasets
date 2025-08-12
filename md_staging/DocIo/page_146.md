```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_146.jpeg
document_name: DocIo
page_number: 146
page_id: DocIo#page_146
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:37:09Z
fidelity: lossless
-->

# CheckBoxSize Property

## Overview
- The `CheckBoxSize` property defines the size of the check box.
- The `SizeType` property controls whether the size is automatic (`Auto`) or custom (`Exactly`).
- Default and checked values can be set for checkboxes.

## Content

### CheckBoxSize Property Definition
The `CheckBoxSize` property defines the size of the check box. When the `SizeType` property is set to `Auto`, the size of the check box will be set automatically. You can also set a custom size for the check box. This is achieved by setting the `SizeType` property to `Exactly`.

#### DefaultCheckBoxValue Property
`DefaultCheckBoxValue` defines the default value of the check box. You can use the `Checked` property to set the value of the check box.

#### Adding Check Boxes to Paragraphs
You can use the `AppendCheckBox` function of `WParagraph` to append a check box to the end of the paragraph.

### Class Hierarchy
```
WTextRange
|
├── WField
|
├── WFormField
|
└── WCheckBox
```

### Public Methods
<table>
    <tr>
        <th>Name</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>`WCheckBox.WCheckBox (IWordDocument)`</td>
        <td>Initializes a new instance of the `WCheckBox` class.</td>
    </tr>
</table>

### Public Properties
<table>
    <tr>
        <th>Name</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>`CheckBoxSize`</td>
        <td>Gets or sets size of checkbox (in integer).</td>
    </tr>
    <tr>
        <td>`Checked`</td>
        <td>Gets or sets Checked property.</td>
    </tr>
    <tr>
        <td>`DefaultCheckBoxValue`</td>
        <td>Gets or sets default checkbox value.</td>
    </tr>
</table>

<!-- tags: [checkbox, checkboxsize, winforms, wcheckbox, sizecontrol] keywords: [checkboxsize, checked, defaultcheckboxvalue] -->
```