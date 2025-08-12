```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_229.jpeg
document_name: edit
page_number: 229
page_id: edit#page_229
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:08:36Z
fidelity: lossless
-->

## Content

### Printing and Previewing in Windows Forms

#### Overview

- Invoking the print dialog via code.
- Configuring and viewing the contents of the Edit Control for printing.
- Using the PrintPreview method to review the content before printing.

#### Invoking the Print Dialog

Invoke the print dialog to print the contents of the `editControl`.

##### C#

```csharp
// Invoke the print dialog.
this.editControl.Print();
```

##### VB.NET

```vb
' Invoke the print dialog.
Me.editControl.Print()
```

##### Print Dialog Box

The Figure below shows the Print Dialog Box, where users can specify settings for printing.

![Figure 75: Print Dialog Box](https://example.com/figure75.png)

---

**Figure 75: Print Dialog Box**

#### Previewing Before Printing

Use the `PrintPreview` method to view the contents of the Edit Control before printing.

##### C#

```csharp
// View the contents of the Edit Control before printing.
this.editControl.PrintPreview();
```

##### VB.NET

```vb
' View the contents of the Edit Control before printing.
Me.editControl.PrintPreview()
```

## Footer

© 2013 Syncfusion. All rights reserved.
Page 229
```

<!-- tags: [Syncfusion Winforms, Print Dialog, PrintPreview, Edit Control, Windows Forms, Programming Examples] keywords: [Print Dialog, PrintPreview, Edit Control, Windows Forms, Syncfusion, Print, Preview, C#, VB.NET] -->
