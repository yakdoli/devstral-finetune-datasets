```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_057.jpeg
document_name: diagram
page_number: 057
page_id: diagram#page_057
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:11:14Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

For more details, see [Diagram Grid](https://link-to-diagram-grid-topic) topic.

## Diagram Builder Functionalities

### 1. How to Open an Existing Diagram Document

Follow the below steps in order to open an existing diagram document:

1. Add OpenFileDialog control to the Form.
2. Set the `Filter` property of OpenFileDialog as **Essential Diagram Palettes|*.edp|Visio Stencils|*.vss; *.vsx|Visio Drawings (Shapes only)|*.vsd; *.vdx|All files|**.
3. Add the below code snippet in your button click event.

```csharp
// Checking whether "OK" button is clicked in OpenFileDialog
if (this.openFileDialog1.ShowDialog(this) == DialogResult.OK)
{
    string FileName = this.openFileDialog1.FileName;
    this.diagram1.LoadBinary(FileName);
    this.diagram1.Refresh();
}
```

The `diagram1.LoadBinary()` method loads the selected diagram file into the diagram document.

![](attachment:DiagramOpenDialogBox.png "Figure 29: Diagram Open Dialog Box")

### 2. How to Save a Diagram Document
```html
<div style="text-align: center;">Figure 29: Diagram Open Dialog Box</div>
```

```html
<h3>2. How to Save a Diagram Document</h3>
```

<!-- tags: [diagram, winforms, openFileDialog, loadBinary, refresh, diagram open dialog box, diagram document] keywords: [diagram builder functionalities, open diagram document, load diagram file, refresh diagram, diagram save, windows forms] -->
```