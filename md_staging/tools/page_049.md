```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_049.jpeg
document_name: tools
page_number: 049
page_id: tools#page_049
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:18:19Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- This section outlines the essential tools for Windows Forms, focusing on the `BannerText` feature.
- Demonstrates how to style and configure the banner text for controls under different modes.

## Content

### BannerText Configuration
The `BannerText` feature is configurable through the `BannerTextMode` property, which determines when the banner text disappears based on the control's state. Here are the modes:

- **FocusMode** - The banner text disappears when the associated textbox is not in focus.
- **EditMode** - The banner text will only disappear when the control is in Edit Mode or the associated textbox is not empty.

#### Code Examples

[C#]
```csharp
this.bannerTextProvider1.SetBannerText(this.comboBoxBarItem1, new Syncfusion.Windows.Forms.BannerTextInfo("Enter Your Country", true, new System.Drawing.Font("Verdana", 8.25F, System.Drawing.FontStyle.Italic), System.Drawing.Color.RoyalBlue, Syncfusion.Windows.Forms.BannerTextMode.FocusMode));
```

[VB.NET]
```vb
Me.bannerTextProvider1.SetBannerText(Me.comboBoxBarItem1, New Syncfusion.Windows.Forms.BannerTextInfo("Enter Your Country", True, New System.Drawing.Font("Verdana", 8.25F, System.Drawing.FontStyle.Italic), System.Drawing.Color.RoyalBlue, Syncfusion.Windows.Forms.BannerTextMode.FocusMode))
```

#### Figure 7: Text = "Enter Your Country"; Font = "Verdana, 8, Italic"; Color = "Royal Blue";

![](attachment:Figure-7.png)

**Figure 7**: Text = "Enter Your Country"; Font = "Verdana, 8, Italic"; Color = "Royal Blue";

### Note: BannerText feature can be made available for the below controls only.

- TextBoxBarItem (XPMenus)
- ComboBoxBarItem (XPMenus)
- TextBox (ToolstripEx)
- ComboBox (ToolstripEx)
- ComboBoxEx (ToolstripEx)
- TextBoxExt (Editor Control)
- CurrencyTextBox (Editor Control)
- ComboBoxAdv (Editor Control)
- ComboBoxDropDown (Editor Control)
- ComboBoxAutoComplete (Editor Control)
- IntegerTextBox (Editor Control)
- DoubleTextBox (Editor Control)
- PercentTextBox (Editor Control)
- Other Microsoft Editor Controls

## Page-level Navigation/TOC (if applicable)
- If the body contains a local Table of Contents for this page, keep it as a bullet/numbered list with links/text as shown.

## Cross References
- References to related sections or controls are included as links to their respective headings.

## RAG Annotations
<!-- tags: [products, windowsforms, controls, bannerText] keywords: [bannerText, FocusMode, EditMode, TextBoxBarItem, TextBox, ComboBox, Syncfusion Windows Forms, controls] -->
```