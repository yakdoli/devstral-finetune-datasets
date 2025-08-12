```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_210.jpeg
document_name: edit
page_number: 210
page_id: edit#page_210
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:06:56Z
fidelity: lossless
-->

## Overview

- Describes the features of the Selection Margin in the Syncfusion Windows Forms Editor.
- Focuses on marking changed lines and saved lines with distinct colors for differentiation.
- Explains the process of enabling the changed lines marking feature using the `MarkChangedLines` property.

## Content

### Differentiating the Lines based on Actions

Edit Control supports marking the changed lines and the saved lines with different colors.

#### Key Features

- **Marking Changed Lines:**
  - Lines modified after the file load or after the last file save operations are marked as changed lines.
  - Changed lines are highlighted in yellow by default.
  - Once saved, they are marked in green by default.

#### Enabling Changed Lines Marking

The changed lines marking feature can be enabled by setting the `MarkChangedLines` property to `True`. For this property to be visible in the Edit Control, the `SelectionMargin` property should also be enabled.

##### Code Examples

**C#**
```csharp
this.editControl1.MarkChangedLines = true;
```

**VB.NET**
```vb
this.editControl1.MarkChangedLines = True
```

### Figure 65: Selection Margin Set

The image shows a demonstration of the `Selection Margin Demo` where the margin highlights changes in red.

---

## API Reference

### Properties

- **MarkChangedLines**: A boolean property that enables marking changed lines in the editor.
- **SelectionMargin**: A boolean property that enables the visibility of the selection margin.

## Code Examples

### C#

```csharp
using System;
using System.Drawing;
using System.Collections;
using System.ComponentModel;
using System.Windows.Forms;
using System.Data;

namespace SelectionMarginDemo
{
    public class Form1 : System.Windows.Forms.Form
    {
        private Syncfusion.Windows.Forms.Edit.EditControl editControl;
        private System.Windows.Forms.MainMenu mainMenu;

        public Form1()
        {
            // Constructor implementation
            this.editControl1.MarkChangedLines = true;
        }
    }
}
```

### VB.NET

```vb
Imports System
Imports System.Drawing
Imports System.Collections
Imports System.ComponentModel
Imports System.Windows.Forms
Imports System.Data

Namespace SelectionMarginDemo
    Public Class Form1
        Inherits System.Windows.Forms.Form
        Private editControl As Syncfusion.Windows.Forms.Edit.EditControl
        Private mainMenu As System.Windows.Forms.MainMenu

        Public Sub New()
            ' Constructor implementation
            Me.editControl1.MarkChangedLines = True
        End Sub
    End Class
End Namespace
```

---

<!-- tags: [syncfusion windows forms, selection margin, changed lines marking, editor control] keywords: [MarkChangedLines, SelectionMargin, Windows Forms, editor, changed lines, saved lines, highlighting] -->
```