```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_117.jpeg
document_name: edit
page_number: 117
page_id: edit#page_117
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:01:23Z
fidelity: lossless
-->

## Essential Edit for Windows Forms

### Specifying and Resetting a Read-Only Region

#### C#

```csharp
// Specify a read-only region.
this.editControl1.MarkAsReadOnly(this.editControl1.Selection.Start,
                                this.editControl1.Selection.End,
                                Color.Orange,
                                Color.Crimson);

// Reset a read-only region.
this.editControl1.RemoveReadOnly(this.editControl1.Selection.Start,
                                this.editControl1.Selection.End);
```

#### VB.NET

```vb
' Specify a read-only region.
Me.editControl1.MarkAsReadOnly(Me.editControl1.Selection.Start,
                              Me.editControl1.Selection.End,
                              Color.Orange, Color.Crimson)

' Reset a read-only region.
Me.editControl1.RemoveReadOnly(Me.editControl1.Selection.Start,
                              Me.editControl1.Selection.End)
```

### Visual Representation of Read-Only Region

The following screenshot shows a read-only region in the code section of the Edit Control.

![Read-Only Region with Orange Background and Crimson Text Color](https://i.imgur.com/qr55.png)

**Figure 39: Read-Only Region with Orange Background and Crimson Text Color**

### Sample Availability

A sample which demonstrates this feature is available in the following sample installation path.

<!-- tags: [Syncfusion Winforms, Essential Edit, Read-Only Region] keywords: [read-only, region, orange background, crimson text, code section, sample path] -->
```