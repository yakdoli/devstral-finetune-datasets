```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_338.jpeg
document_name: tools
page_number: 338
page_id: tools#page_338
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:07:48Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

- Easy Customization of the control through designer without a single piece of code.
- **Smart Tag** - Has advanced smart tag options which lets you to set the properties easily.

### 3.5.2.1.2 Creating ButtonAdv

The ButtonAdv control can be made available through designer by just dragging and dropping the control from the toolbox onto the form.

![Figure 151: ButtonAdv control in the Toolbox](https://i.imgur.com/Xc8d3nX.png)

It can be created programmatically by following the below steps.

1. Include the Tools Windows namespace to `cs` / `vb` file.

   ```csharp
   using Syncfusion.Windows.Forms.Tools;
   ```

   ```vb
   Imports Syncfusion.Windows.Forms.Tools
   ```

2. Create an instance of ButtonAdv control and add it to the form.

   ```csharp
   private Syncfusion.Windows.Forms.ButtonAdv buttonAdv1;
   this.buttonAdv1 = new Syncfusion.Windows.Forms.ButtonAdv();
   this.Controls.Add(this.buttonAdv1);
   ```
```