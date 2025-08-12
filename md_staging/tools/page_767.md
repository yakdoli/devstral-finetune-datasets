```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_767.jpeg
document_name: tools
page_number: 767
page_id: tools#page_767
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:34:22Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Overview
- This page describes how to initialize, set properties, and add the PercentTextBox control to a Windows Forms application using C# and VB.NET.
- The PercentTextBox control allows users to input percentage values in a user-friendly manner, enhancing usability in applications that require percentage handling.

### Content

1. **Declarations**
   ```csharp
   Private percentTextBox1 As Syncfusion.Windows.Forms.Tools.PercentTextBox
   ```

2. **Initialize the control.**

   #### C#
   ```csharp
   this.percentTextBox1 = new Syncfusion.Windows.Forms.Tools.PercentTextBox();
   ```

   #### VB.NET
   ```vb.net
   Me.percentTextBox1 = New Syncfusion.Windows.Forms.Tools.PercentTextBox()
   ```

3. **Set the properties of the PercentTextBox control.**

   #### C#
   ```csharp
   this.percentTextBox1.Location = new System.Drawing.Point(65, 29);
   this.percentTextBox1.Name = "percentTextBox1";
   this.percentTextBox1.Size = new System.Drawing.Size(84, 20);
   this.percentTextBox1.PercentValue = 5;
   ```

   #### VB.NET
   ```vb.net
   Me.percentTextBox1.Location = New System.Drawing.Point(65, 29)
   Me.percentTextBox1.Name = "numericUpDownExt1"
   Me.percentTextBox1.Size = New System.Drawing.Size(84, 20)
   Me.percentTextBox1.PercentValue = 5
   ```

4. **Add the control to the form.**

   #### C#
   ```csharp
   this.Controls.Add(this.percentTextBox1);
   ```

   #### VB.NET
   ```vb.net
   Me.Controls.Add(Me.percentTextBox1)
   ```

5. **Run the application.**

### API Reference

- **Namespace:** Syncfusion.Windows.Forms.Tools
- **Class:** PercentTextBox
- **Properties:**
  - **PercentValue:** Gets or sets the percentage value displayed by the control.

### Code Examples

#### C# Example
```csharp
using System;
using System.Drawing;
using Syncfusion.Windows.Forms.Tools;

public class MainForm : Form
{
    private PercentTextBox percentTextBox1;

    public MainForm()
    {
        percentTextBox1 = new PercentTextBox();
        percentTextBox1.Location = new Point(65, 29);
        percentTextBox1.Name = "percentTextBox1";
        percentTextBox1.Size = new Size(84, 20);
        percentTextBox1.PercentValue = 5;
        this.Controls.Add(percentTextBox1);
    }
}
```

#### VB.NET Example
```vb.net
Imports System
Imports System.Drawing
Imports Syncfusion.Windows.Forms.Tools

Public Class MainForm
    Inherits Form

    Private percentTextBox1 As PercentTextBox

    Public Sub New()
        percentTextBox1 = New PercentTextBox()
        percentTextBox1.Location = New Point(65, 29)
        percentTextBox1.Name = "percentTextBox1"
        percentTextBox1.Size = New Size(84, 20)
        percentTextBox1.PercentValue = 5
        Me.Controls.Add(percentTextBox1)
    End Sub
End Class
```

### Page-level Navigation/TOC
- [Top](#page_767)
- [Initialization](#init-control)
- [Setting Properties](#set-properties)
- [Adding to Form](#add-to-form)
- [Running the Application](#run-app)

### RAG Annotations
<!-- tags: [Syncfusion Winforms, PercentTextBox, Windows Forms, C#, VB.NET, control initialization, properties, design-time, runtime, user guide] keywords: [PercentTextBox, Windows Forms, C#, VB.NET, synchronization, control initialization, properties, design-time, runtime, essential tools] -->
```