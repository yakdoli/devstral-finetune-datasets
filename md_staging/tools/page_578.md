```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_578.jpeg
document_name: tools
page_number: 578
page_id: tools#page_578
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:21:53Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates how to set different border styles in ComboBoxAdv controls.
- Details the use of the Style property to apply various visual styles such as Default, OfficeXP, Office2003, VS2005, and Office2007.
- Provides examples in both C# and VB for configuring visual styles.

## Content

### Border Settings

#### Figure 356: Border Settings

![Figure 356: Border Settings](image)

**3.5.5.2.3.4.2 Visual Styles**

ComboBoxAdv supports visual styles such as Default, OfficeXP, Office2003, VS2005, and Office2007 with all three color schemes. The style can be set using the `Style` property.

#### C#

```csharp
// To set Default Visual Style
this.comboBoxAdv1.Style = Syncfusion.Windows.Forms.VisualStudio.Default;

// To set Office2003 Visual Style
this.comboBoxAdv1.Style = Syncfusion.Windows.Forms.VisualStudio.Office2003;

// To set OfficeXP Visual Style
this.comboBoxAdv1.Style = Syncfusion.Windows.Forms.VisualStudio.OfficeXP;

// To set VS2005 Visual Style
this.comboBoxAdv1.Style = Syncfusion.Windows.Forms.VisualStudio.VS2005;

// To set Office2007 Visual Style
this.comboBoxAdv1.Style = Syncfusion.Windows.Forms.VisualStudio.Office2007;
```

#### VB

```vb
' To set Default Visual Style
Me.comboBoxAdv1.Style = Syncfusion.Windows.Forms.VisualStudio.Default

' To set Office2003 Visual Style
Me.comboBoxAdv1.Style = Syncfusion.Windows.Forms.VisualStudio.Office2003

' To set OfficeXP Visual Style
Me.comboBoxAdv1.Style = Syncfusion.Windows.Forms.VisualStudio.OfficeXP

' To set VS2005 Visual Style
Me.comboBoxAdv1.Style = Syncfusion.Windows.Forms.VisualStudio.VS2005

' To set Office2007 Visual Style
Me.comboBoxAdv1.Style = Syncfusion.Windows.Forms.VisualStudio.Office2007
```

## RAG Annotations
<!-- tags: Visual Styles, Border Settings, ComboBoxAdv, Style Property, Syncfusion, WinForms, vs2005, office2003, officexp, default, vs2005, office2007 keywords: visual styles, border settings, comboboxadv, style property, syncfusion windows forms -->
```