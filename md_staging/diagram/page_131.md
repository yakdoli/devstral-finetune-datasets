```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_131.jpeg
document_name: diagram
page_number: 131
page_id: diagram#page_131
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:15:17Z
fidelity: lossless
-->

## Label Orientation

### Overview
- Provides functionality to specify the orientation of a node label in Windows Forms diagrams.
- Highlights two label orientation modes: Horizontal and Auto.
- Includes examples of label alignment and wrapping.

---

### Content

#### Essential Diagram for Windows Forms

The following code snippet demonstrates how to format and add a custom label to a node in a diagram:

```csharp
// Format the label text
lbl_Custom.HorizontalAlignment = StringAlignment.Center
lbl_Custom.VerticalAlignment = StringAlignment.Far
// WrapText is true by default

// Add the label to node's label collection
node.Labels.Add(lbl_Custom)
// Add the node to diagram model
diagram1.Model.AppendChild(node)
```

#### Label Alignment and Orientation

The diagrams below illustrate the placement of label text within a node for various alignment options.

**Horizontal/VerticalAlignment:**

- **Nodes with Standard Alignments:**
  - **Top Center**
  - **Center**
  - **Bottom Center**
  - **Top Left**
  - **Middle Left**
  - **Bottom Left**
  - **Top Right**
  - **Middle Right**
  - **Bottom Right**

**Custom Labels:**

- Includes examples of custom alignment and wrapping:
  - **Label_Custom**
  - **Label_Custom**

**Example of WrapText:**

- Demonstrates how text wraps within a node.

**Figure 72: Label**

### 4.4.5 Label Orientation

This feature lets the user specify the orientation of a node label. There are two orientation modes:
- **Horizontal:** Displays the label horizontally.
- **Auto:** Rotates the label based on the node or connector rotation angle.

---

## API Reference

### Members

- **lbl_Custom**: Custom label object.
- **HorizontalAlignment**: Property to set horizontal alignment of the label.
- **VerticalAlignment**: Property to set vertical alignment of the label.
- **WrapText**: Property to enable text wrapping.

### Methods

- **diagram1.Model.AppendChild(node)**: Adds the node to the diagram model.

---

## Code Examples

The following example demonstrates how to add and format a label in a Windows Forms diagram:

```csharp
// Example code: Setting up a custom label
CustomLabel lbl_Custom = new CustomLabel();
lbl_Custom.Text = "Example Label";
lbl_Custom.HorizontalAlignment = StringAlignment.Center;
lbl_Custom.VerticalAlignment = StringAlignment.Far;

Node node = new Node();
node.Labels.Add(lbl_Custom);

Diagram diagram1 = new Diagram();
diagram1.Model.AppendChild(node);
```

---

## Page-level Navigation/TOC

- Label Orientation
  - Overview
  - Essential Diagram for Windows Forms
  - Label Orientation

---

## Cross References

See also:
- Advanced Diagram Customization
- Label Properties and Methods

---

<!-- tags: [Syncfusion Winforms, Label, Orientation, Diagram, Windows Forms] keywords: [lbl_Custom, HorizontalAlignment, VerticalAlignment, WrapText, CustomLabel, Node, DiagramModel] -->
```