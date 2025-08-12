```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_384.jpeg
document_name: tools
page_number: 384
page_id: tools#page_384
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:09:41Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- The Calculator control can be added to a Windows Forms application using the Toolbox.
- Steps to create the Calculator control both visually (via drag-and-drop) and programmatically.

## Content
### 3.5.2.3.2 Creating Calculator control
The Calculator control can be available to the designer by just dragging-and-dropping the Calculator control from the toolbox onto the form.

![](assets/image.png){width=0.5; caption="Figure 190: CalculatorControl in Toolbox"}

It can be created programmatically using the below steps.

1. **Include the required namespace.**
   
   **[C#]**  
   ```csharp
   using Syncfusion.Windows.Forms.Tools;
   ```

   **[VB.NET]**  
   ```vbnet
   Imports Syncfusion.Windows.Forms.Tools
   ```

2. **Declare and create an instance of the Calculator control class.**

   **[C#]**  
   ```csharp
   private Syncfusion.Windows.Forms.Tools.CalculatorControl
   calculatorControl1;
   
   // Create an instance of the Calculator control
   this.calculatorControl1 = new CalculatorControl();
   ```

## API Reference
- **Namespace**: `Syncfusion.Windows.Forms.Tools`
- **Class**: `CalculatorControl`

## Code Examples
For more examples, refer to the official documentation or sample projects provided by Syncfusion.

## Cross References
- This guide assumes a basic understanding of Syncfusion Windows Forms Controls.

<!-- tags: [windows forms, calculator control, drag-and-drop, toolbox] keywords: [syncfusion, windows forms, tools, calculator, namespace, declare, create] -->
```