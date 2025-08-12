```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_944.jpeg
document_name: tools
page_number: 944
page_id: tools#page_944
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:43:58Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Creating and Configuring the GradientLabel Control

### Step-by-Step Guide

1. **Create a C# or VB.NET application through Visual Studio.**
2. **Add the required assembly references.**
3. **Include the required namespace.**

#### Namespace Usage

- **[C#]**
  ```csharp
  using Syncfusion.Windows.Forms.Tools;
  ```

- **[VB.NET]**
  ```vbnet
  Imports Syncfusion.Windows.Forms.Tools
  ```

### Declaring the GradientLabel Control

- **[C#]**
  ```csharp
  private Syncfusion.Windows.Forms.Tools.GradientLabel gradientLabel1;
  ```

- **[VB.NET]**
  ```vbnet
  Private gradientLabel1 As Syncfusion.Windows.Forms.Tools.GradientLabel
  ```

### Initializing the Control

- **[C#]**
  ```csharp
  this.gradientLabel1 = new Syncfusion.Windows.Forms.Tools.GradientLabel();
  ```

- **[VB.NET]**
  ```vbnet
  Me.gradientLabel1 = New Syncfusion.Windows.Forms.Tools.GradientLabel()
  ```

### Setting Properties and Adding to the Form

- **[C#]**
  ```csharp
  this.gradientLabel1.BorderStyle = System.Windows.Forms.BorderStyle.Sunken;
  this.gradientLabel1.ForeColor = System.Drawing.SystemColors.Info;
  this.gradientLabel1.Text = "Syncfusion Control";
  ```

## Summary

This section outlines the process of creating and configuring a GradientLabel control in a Windows Forms application using Syncfusion tools. It covers setting up the necessary namespaces, declaring, initializing, and adjusting the properties of the GradientLabel control.
```