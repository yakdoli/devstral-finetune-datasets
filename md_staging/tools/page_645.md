```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_645.jpeg
document_name: tools
page_number: 645
page_id: tools#page_645
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:25:09Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Code Examples

```csharp
this.gradientPanel1 = new Syncfusion.Windows.Forms.Tools.GradientPanel();
((System.ComponentModel.ISupportInitialize)(this.gradientPanel1)).BeginInit();
```

```vb.net
Me.GradientPanel1 = New Syncfusion.Windows.Forms.Tools.GradientPanel(CType(Me.GradientPanel1, System.ComponentModel.ISupportInitialize)).BeginInit()
```

### Setting Properties for the Gradient Panel and Form

1. **Set the properties as follows for the gradient panel and the form.**

   **C#**

   ```csharp
   // gradientPanel
   this.gradientPanel1.BackColor = new Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.PatternStyle.DiagonalC
   old, System.Drawing.Color.LightBlue, System.Drawing.SystemColors.InactiveCaption);
   this.gradientPanel1.BorderColor = System.Drawing.Color.White;
   this.gradientPanel1.Location = new System.Drawing.Point(37, 32);
   this.gradientPanel1.Name = "gradientPanel1";
   this.gradientPanel1.Size = new System.Drawing.Size(350, 202);
   this.gradientPanel1.TabIndex = 0;
   this.Controls.Add(this.gradientPanel1);
   ```

   **VB.NET**

   ```vb.net
   'GradientPanel
   Me.GradientPanel1.BackColor = New Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.PatternStyle.DiagonalC
   old, System.Drawing.Color.LightSkyBlue, System.Drawing.SystemColors.Window)
   Me.GradientPanel1.BorderColor = System.Drawing.Color.Black
   Me.GradientPanel1.Location = New System.Drawing.Point(64, 48)
   Me.GradientPanel1.Name = "GradientPanel1"
   Me.GradientPanel1.Size = New System.Drawing.Size(296, 208)
   Me.GradientPanel1.TabIndex = 0
   Me.Controls.Add(Me.GradientPanel1)
   ```

2. **Run the application.**

<!-- tags: [product, module, control, api, version?] keywords: [k1, k2, ...] -->
```