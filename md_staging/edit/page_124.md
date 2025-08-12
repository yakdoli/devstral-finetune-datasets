```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_124.jpeg
document_name: edit
page_number: 124
page_id: edit#page_124
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:01:08Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- Specifies the behavior for selecting text after drag/drop operations.
- Explains how to get/set selected text using properties.
- Describes the transparent selection feature.

## Content

### SelectTextAfterDragDrop
| SelectTextAfterDragDrop | Specifies whether text should be selected after drag/drop operations. |
|--------------------------|---------------------------------------------------------------|

#### C#
```csharp
this.editControl1.SelectTextAfterDragDrop = true;
```

#### VB.NET
```vb
Me.editControl1.SelectTextAfterDragDrop = True
```

### Selected Text
#### The following properties can be used to get/set selected text.

| Edit Control Property | Description |
|-----------------------|-------------|
| SelectedText         | Gets/sets selected text. |
| Selection            | Gets selected text range. |

#### C#
```csharp
// Returns the currently selected text in the Edit Control.
string editText = this.editControl1.SelectedText;
```

#### VB.NET
```vb
' Returns the currently selected text in the Edit Control.
Dim editText as String = Me.editControl1.SelectedText
```

### Transparent Selection
Setting the `TransparentSelection` property to `True` will highlight the selected text range with a transparent blue background (which will let you view the syntax highlighting in the text within the selected region), as shown in the following screenshot.
```