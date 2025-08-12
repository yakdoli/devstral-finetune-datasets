```html
<!--  
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_679.jpeg
document_name: tools
page_number: 679
page_id: tools#page_679
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:28:48Z
fidelity: lossless
--> 

# Essential Tools for Windows Forms

## Overview
This page provides guidance on integrating and customizing the `SplitContainerAdv` control in Windows Forms applications, along with steps to create it programmatically.

## Content

### SplitContainerAdv with Child Controls

![Figure: SplitContainerAdv with Child Controls](attachment://Figure_421.png)

*Figure 421: SplitContainerAdv with Child Controls*

#### See Also

- **Concepts and Features**
- **3.5.6.4.2.2 Through Code**

#### Creating a SplitContainerAdv Control Programmatically

To programmatically create a `SplitContainerAdv` control in a Visual Studio application:

1. **Open a New Application**:
   - Start a new Visual C# or VB.NET application in Visual Studio.

2. **Add Required Assemblies**:
   - Include the Syncfusion assemblies `Shared.Base` and `Tool.Windows` in your project.

3. **Declare the SplitContainerAdv Control**:

   - **C#**
     ```csharp
     private Syncfusion.Windows.Forms.Tools.SplitContainerAdv
     splitContainerAdv1;
     ```

   - **VB.NET**
     ```vb
     Private splitContainerAdv1 As Syncfusion.Windows.Forms.Tools.SplitContainerAdv
     ```

4. **Initialize and Add the Control**:
   - Initialize the `SplitContainerAdv` and add it to your form.

   - **C#**
     ```csharp
     this.splitContainerAdv1 = new Syncfusion.Windows.Forms.Tools.SplitContainerAdv();
     this.Controls.Add(this.splitContainerAdv1);
     ```

## API Reference

The `SplitContainerAdv` control provides a programmable interface for advanced split container functionality. Below is a brief reference for some of its key properties and methods.

### Properties
- `Panel1`
- `Panel2`
- `Splitters`

### Methods
- `SplitterMoved`
- `SplitterMoving`

For a complete API reference, refer to the Syncfusion documentation.

## Code Examples

### Example: Creating a SplitContainerAdv in C#

```csharp
private void CreateSplitContainer()
{
    Syncfusion.Windows.Forms.Tools.SplitContainerAdv splitContainerAdv1 = new Syncfusion.Windows.Forms.Tools.SplitContainerAdv();
    this.Controls.Add(splitContainerAdv1);
    splitContainerAdv1.SplitterDistance = 300;
}
```

### Example: Creating a SplitContainerAdv in VB.NET

```vb
Private Sub CreateSplitContainer()
    Dim splitContainerAdv1 As Syncfusion.Windows.Forms.Tools.SplitContainerAdv = New Syncfusion.Windows.Forms.Tools.SplitContainerAdv()
    Me.Controls.Add(splitContainerAdv1)
    splitContainerAdv1.SplitterDistance = 300
End Sub
```

## Page-level Navigation/TOC (if applicable)

- [SplitContainerAdv Overview](#splitcontaineradv-overview)
- [Creating a SplitContainerAdv Programmatically](#creating-a-splitcontaineradv-programmatically)
- [API Reference](#api-reference)
- [Code Examples](#code-examples)

## Cross References

- **See also:**
  - Concepts and Features
  - 3.5.6.4.2.2 Through Code

<!-- tags: [SplitContainerAdv, Windows Forms, UI Controls, Syncfusion, C#, VB.NET, programmatically, customization] keywords: [splitcontaineradv, windows forms, controls, split container, advanced, syncfusion, vb.net, c#, programming, integration, child controls] -->
```