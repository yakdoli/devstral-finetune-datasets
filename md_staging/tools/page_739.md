```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_739.jpeg
document_name: tools
page_number: 739
page_id: tools#page_739
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:32:28Z
fidelity: lossless
-->

## Overview
- This page demonstrates how to create and configure an `IntegerTextBox` control in a Windows Forms application using Syncfusion's tools library in VB.NET and C#.
- It outlines the steps to instantiate an `IntegerTextBox`, set its value and size, and add it to the form.
- The focus is on integrating and utilizing the `IntegerTextBox` control effectively.

## Content

### Setting Up the `IntegerTextBox` Control

#### 1. Import the Necessary Namespace

In both VB.NET and C#, start by importing the Syncfusion namespace that contains the `IntegerTextBox` control:

```vb
Imports Syncfusion.Windows.Forms.Tools
```

```csharp
using Syncfusion.Windows.Forms.Tools;
```

#### 2. Create an Instance of the `IntegerTextBox` Control

##### [C#]

```csharp
// Create IntegerTextBox control.
private Syncfusion.Windows.Forms.Tools.IntegerTextBox integerTextBox1;
this.integerTextBox1 = new Syncfusion.Windows.Forms.Tools.IntegerTextBox();
```

##### [VB.NET]

```vb
' Create IntegerTextBox control.
Private integerTextBox1 As Syncfusion.Windows.Forms.Tools.IntegerTextBox
Me.integerTextBox1 = New Syncfusion.Windows.Forms.Tools.IntegerTextBox()
```

#### 3. Specify Its Value and Size

##### [C#]

```csharp
this.integerTextBox1.IntegerValue = ((long)(7));
this.integerTextBox1.Size = new System.Drawing.Size(144, 20);
```

##### [VB.NET]

```vb
Me.integerTextBox1.IntegerValue = (CLng(7))
Me.integerTextBox1.Size = New System.Drawing.Size(144, 20)
```

#### 4. Add the `IntegerTextBox` Control to the Form

##### [C#]

```csharp
this.Controls.Add(this.integerTextBox1);
```

##### [VB.NET]

```vb
Me.Controls.Add(Me.integerTextBox1)
```

## API Reference

### Classes and Properties

- **Syncfusion.Windows.Forms.Tools.IntegerTextBox**
  - **IntegerValue**: Represents the integer value of the control. Can be set or retrieved.
  - **Size**: Defines the dimensions of the control in pixels.

## Code Examples

### VB.NET Example

```vb
Imports Syncfusion.Windows.Forms.Tools

Public Class Form1
    Inherits System.Windows.Forms.Form

    Private integerTextBox1 As Syncfusion.Windows.Forms.Tools.IntegerTextBox

    Public Sub New()
        Me.integerTextBox1 = New Syncfusion.Windows.Forms.Tools.IntegerTextBox()
        Me.integerTextBox1.IntegerValue = (CLng(7))
        Me.integerTextBox1.Size = New System.Drawing.Size(144, 20)
        Me.Controls.Add(Me.integerTextBox1)
    End Sub
End Class
```

### C# Example

```csharp
using Syncfusion.Windows.Forms.Tools;

public class Form1 : System.Windows.Forms.Form
{
    private Syncfusion.Windows.Forms.Tools.IntegerTextBox integerTextBox1;

    public Form1()
    {
        this.integerTextBox1 = new Syncfusion.Windows.Forms.Tools.IntegerTextBox();
        this.integerTextBox1.IntegerValue = ((long)(7));
        this.integerTextBox1.Size = new System.Drawing.Size(144, 20);
        this.Controls.Add(this.integerTextBox1);
    }
}
```

## Cross References

- See also: Other controls and functionality in `Syncfusion.Windows.Forms.Tools` namespace for advanced configurations and additional features.

<!-- tags: [Syncfusion Winforms, IntegerTextBox, Control, Namespace, C#, VB.NET] keywords: [IntegerTextBox, Syncfusion.Windows.Forms.Tools, ControlSetup, ValueSetting, Size, C#, VB.NET, Windows Forms] -->
```