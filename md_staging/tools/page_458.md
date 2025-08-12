```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_458.jpeg
document_name: tools
page_number: 458
page_id: tools#page_458
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:14:54Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Content

### DateTimePickerAdv Creation

The DateTimePickerAdv can be created programmatically through code as detailed below.

1. **Include the required namespace.**

   ```csharp
   using Syncfusion.Windows.Forms.Tools;
   ```

   ```vbnet
   Imports Syncfusion.Windows.Forms.Tools
   ```

2. **Create an instance of DateTimePickerAdv. Add that instance to the Form.**

   ```csharp
   private Syncfusion.Windows.Forms.Tools.DateTimePickerAdv dateTimePickerAdv1;
   this.dateTimePickerAdv1 = new Syncfusion.Windows.Forms.Tools.DateTimePickerAdv();
   this.Controls.Add(this.dateTimePickerAdv1);
   ```

   ```vbnet
   Private dateTimePickerAdv1 As Syncfusion.Windows.Forms.Tools.DateTimePickerAdv
   Me.dateTimePickerAdv1 = New Syncfusion.Windows.Forms.Tools.DateTimePickerAdv()
   Me.Controls.Add(Me.dateTimePickerAdv1)
   ```

   ![Figure 254: DateTimePickerAdv Created Programmatically](attachmentImagePath)

   **Figure 254: DateTimePickerAdv Created Programmatically**

### See Also

- **Concepts and Features**
- **3.5.3.2.3 Concepts and Features**

## Page-level Navigation/TOC (if applicable)

- **DateTimePickerAdv Creation**
- **See Also**

## Cross References

- **See also:** Concepts and Features, 3.5.3.2.3 Concepts and Features

<!-- tags: [DateTimePickerAdv, Essential Tools, Windows Forms, C#, VB.NET, DateTimePicker, DateTimePickerAdv] keywords: [DateTimePickerAdv creation, Windows Forms, Syncfusion, DateTimePicker, creation code, programmatically add control, C#, VB.NET, example code] -->
```