```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_718.jpeg
document_name: tools
page_number: 718
page_id: tools#page_718
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:30:36Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Content

2. Create an instance of the DomainUpDownExt. Add that instance to the Form.

### C#

```csharp
private Syncfusion.Windows.Forms.Tools.DomainUpDownExt domainUpDownExt1;
this.domainUpDownExt1 = new Syncfusion.Windows.Forms.Tools.DomainUpDownExt();

// Add items.
this.domainUpDownExt1.Items.Add("One");
this.domainUpDownExt1.Items.Add("Two");
this.domainUpDownExt1.Items.Add("Three");
this.domainUpDownExt1.Items.Add("Four");
this.domainUpDownExt1.Items.Add("Five");

this.Controls.Add(this.domainUpDownExt1);
```

### VB.NET

```vb
Private domainUpDownExt1 As Syncfusion.Windows.Forms.Tools.DomainUpDownExt
Me.domainUpDownExt1 = New Syncfusion.Windows.Forms.Tools.DomainUpDownExt()

' Add items.
Me.domainUpDownExt1.Items.Add("One")
Me.domainUpDownExt1.Items.Add("Two")
Me.domainUpDownExt1.Items.Add("Three")
Me.domainUpDownExt1.Items.Add("Four")
Me.domainUpDownExt1.Items.Add("Five")

Me.Controls.Add(Me.domainUpDownExt1)
```

## Footer

© 2013 Syncfusion. All rights reserved.

<!-- tags: [Syncfusion Winforms, DomainUpDownExt, Essential Tools, version: 11.4.0.26] keywords: [Syncfusion, Windows Forms, DomainUpDownExt, Essential Tools, instance, form, add items, C#, VB.NET, synchronize, list box] -->
```