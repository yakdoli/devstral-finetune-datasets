```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_595.jpeg
document_name: tools
page_number: 595
page_id: tools#page_595
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:23:24Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates how to create and configure ComboBoxBase and ListBox controls using external data sources.
- Covers setting up data sources for controls and adding them to a Windows Form.
- Explains ListControl-Derived controls with external data sources.

## Content

### Setting up DataSources for Controls

#### VB.NET
```vb
' Sets the datasource.
Dim USStates As ArrayList = New ArrayList()

USStates.Add(New USState("Washington", "WA"))
USStates.Add(New USState("West Virginia", "WV"))
USStates.Add(New USState("Wisconsin", "WI"))
USStates.Add(New USState("Wyoming", "WY"))

ListBox1.DataSource = USStates
```

#### Adding Controls to the Form

5. Finally, add ComboBoxBase and ListBox to the Form.

##### C#
```csharp
this.Controls.Add(this.listBox1);
this.Controls.Add(this.comboBoxBase1);
```

##### VB.NET
```vb
Me.Controls.Add(Me.listBox1)
Me.Controls.Add(Me.comboBoxBase1)
```

### Visual Representation

![Figure 368: ComboBoxBase with External DataSource](image.png)

### Detailed Reference

Refer [Creating ListControl-Derived Controls](#creating-listcontrol-derived-controls) about ListControl-Derived controls in detail.

### Concepts and Features

#### 3.5.5.3.3 Concepts and Features

## Page-level Navigation/TOC (if applicable)
- [1] Setting up DataSources for Controls
- [2] Adding Controls to the Form
- [3] Visual Representation
- [4] Detailed Reference
- [5] Concepts and Features

<!-- tags: [ComboBoxBase, ListBox, DataSources, Windows Forms, Syncfusion Winforms, Essential Tools] keywords: [ComboBoxBase, ListBox, DataSources, Windows Forms, Controls, Form, ListControl-Derived, External Data Source] -->
```