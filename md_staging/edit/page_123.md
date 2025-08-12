```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_123.jpeg
document_name: edit
page_number: 123
page_id: edit#page_123
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:01:31Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- Explains how to select lines or all text in the Edit control.
- Discusses using the `ExtendSelectionToFarRight` property to extend line selection.
- Provides examples in C# and VB.NET for specifying text selection positions and selecting lines.

## Content

### Text Selection Methods

| Method          | Description                         |
|-----------------|-------------------------------------|
| SelectLine      | Selects line with specified index. |
| SelectAll       | Selects all text.                  |

Line selection in Edit Control is extended by using the `ExtendSelectionToFarRight` property.

### Edit Control Property

| Edit Control Property         | Description                                                                 |
|------------------------------|-----------------------------------------------------------------------------|
| ExtendSelectionToFarRight    | Gets / sets value indicating whether line selection should be extended to the far right. |

### Example Usage

#### C#

```csharp
// Specifies start position for selecting text.
this.editControl1.StartSelection(1, 1);

// Specifies end position for selecting text.
this.editControl1.StopSelection(10, 1);

// Selects line with specified index.
this.editControl1.SelectLine(5);

// Extend line selection to far right.
this.editControl1.ExtendSelectionToFarRight = true;
```

#### VB.NET

```vbnet
' Specifies start position for selecting text.
Me.editControl1.StartSelection(1, 1)

' Specifies end position for selecting text.
Me.editControl1.StopSelection(5, 1)

' Selects line with specified index.
Me.editControl1.SelectLine(5)

' Extend line selection to far right.
Me.editControl1.ExtendSelectionToFarRight = True
```

Text can also be selected after drag / drop operations by using the below given property.

### Edit Control Property

| Edit Control Property | Description |
|----------------------|-------------|
| (Property Name)      | (Description) |

## Code Examples

The provided code examples demonstrate how to use `StartSelection`, `StopSelection`, `SelectLine`, and `ExtendSelectionToFarRight` in both C# and VB.NET.

<!-- tags: [Syncfusion Winforms, Edit Control, Text Selection, Line Selection, ExtendSelectionToFarRight] keywords: [EditControl, Text, Selection, Line, FarRight, Example, C#, VB.NET] -->
```