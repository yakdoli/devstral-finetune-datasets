```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_709.jpeg
document_name: tools
page_number: 709
page_id: tools#page_709
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:28:45Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Overview of essential tools available in Windows Forms for various functionalities.
- Focus on the CurrencyEdit tool and its creation in both design-time and run-time environments.

## Content

### CurrencyEdit in Toolbox
![Figure 440: CurrencyEdit in Toolbox](attachment:figure_440.png)

#### Creating CurrencyEdit Programmatically

It can be created programmatically as follows:

1. **Include the required namespace.**

   **[C#]**  
   ```csharp
   using Syncfusion.Windows.Forms.Tools;
   ```

   **[VB.NET]**  
   ```vb
   Imports Syncfusion.Windows.Forms.Tools
   ```

2. **Create an instance of the CurrencyEdit. Add that instance to the Form.**

   **[C#]**  
   ```csharp
   private Syncfusion.Windows.Forms.Tools.CurrencyEdit currencyEdit1;
   this.currencyEdit1=new Syncfusion.Windows.Forms.Tools.CurrencyEdit();
   this.Controls.Add(this.currencyEdit1);
   ```

   **[VB.NET]**  
   ```vb
   Private currencyEdit1 As Syncfusion.Windows.Forms.Tools.CurrencyEdit
   Me.currencyEdit1 = New Syncfusion.Windows.Forms.Tools.CurrencyEdit()
   Me.Controls.Add(Me.currencyEdit1)
   ```

## Page-level Navigation/TOC (if applicable)
- This page covers the usage of the **CurrencyEdit** tool in Windows Forms.
- Details on using it through the toolbox and programmatically.

## Cross References
- Refer to the section on **other tools** for additional information on different controls and functionalities.

<!-- tags: [Syncfusion, WinForms, CurrencyEdit, Tools] keywords: [design-time, run-time, programmatically, namespace, instance, control, form] -->
```