```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_058.jpeg
document_name: diagram
page_number: 058
page_id: diagram#page_058
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:12:16Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

Below are the steps to save a diagram document.

1. Add SaveFileDialog control to the Form.
2. Set the Filter property of SaveFileDialog as `Essential Diagram Files|*.edd|All files|*.*`.
3. Add the following code snippet in your button click event.

```csharp
[C#]

// Checking whether "OK" button is clicked in SaveFileDialog
if (this.saveFileDialog1.ShowDialog(this) == DialogResult.OK)
{
    this.FileName = this.saveFileDialog1.FileName;
    this.diagram1.SaveBinary(this.FileName);
}
```

The `diagram1.SaveBinary()` method saves the diagram file in the given filename.

![Diagram Save Dialog Box](https://via.placeholder.com/500)

Figure 30: Diagram Save Dialog Box

## 3. How to print a Diagram Document

Following are the steps to print a diagram document:

### 1. Page Setup

The Page Setup dialog modifies the Page Settings and Printer Settings information for a given document. The user can enable sections of the dialog to manipulate printing, margins, paper orientation, size, source and to show help and network buttons. `MinMargins` defines the minimum margins a user can select.

## API Reference

### Methods

- `SaveBinary(string fileName)`
  - **Description**: Saves the diagram file in the given filename.
  - **Parameters**:
    - `fileName`: Type `string` - The file name to save the diagram.
  - **Returns**: `void`
  - **Throws**: None

### Example Usage

```csharp
// Example of saving a diagram
if (this.saveFileDialog1.ShowDialog(this) == DialogResult.OK)
{
    this.FileName = this.saveFileDialog1.FileName;
    this.diagram1.SaveBinary(this.FileName);
}
```

<!-- tags: [product, syncfusion, winforms, essential-diagram, save-binary, save-dialog, print, page-setup] keywords: [save, saveFileDialog, diagram, print, margin, orientation, size, network] -->
```