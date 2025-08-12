```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_080.jpeg
document_name: QTP
page_number: 080
page_id: QTP#page_080
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:06:31Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview
- Details on how to get the description of checkbox cells and normal cells in Essential Grid.
- Explanation of the GetDescription method for retrieving descriptions of grid cells.

## Content

### 7.2.1 How to get the description of the Check Box Cells and Normal Cells in Essential Grid

#### Supported method to get the Description of GridCells
The **GetDescription** method is used to get the description of the check box, push button, and normal cells in Essential Grid's record and reply process. This method returns the description of the check box, push button, and normal cells as well.

---

### Use Case Scenarios
This feature enables you to get the description of checkbox, push button, and normal cells in QTP testing.

#### Methods Table

| Method         | Description                                      | Parameters                                              | Return Type |
|----------------|--------------------------------------------------|----------------------------------------------------------|--------------|
| GetDescription | Gets the description of grid cells for Essential Grid. | For the Grid control: <br/> `public object GetDescription(int row, int col)` <br/> For the GridGrouping control: <br/> `public object GetDescription(object row, object col)` | Object       |

---

### Applying the GetDescription Method in QTP

The following code examples illustrate how to use the GetDescription method.

---

#### [For GridControl]

```csharp
SwfWindow("Form1").SwfObject("gridControl1").SetCurrentCell 3,1
MsgBox(SwfWindow("Form1").SwfObject("gridControl1").GetDescription(3,1))
```

---

#### [For GridGroupingControl]

```csharp
SwfWindow("Form1").SwfObject("gridGroupingControl1").SetCurrentCell 3,"Col2"
MsgBox(SwfWindow("Form1").SwfObject("gridGroupingControl1").GetDescription(5,"Col0"))
```

## RAG Annotations
<!-- tags: [Essential Grid, GetDescription method, checkbox cells, normal cells, QTP testing] keywords: [Grid cells, description, Grid control, GridGrouping control, SetCurrentCell, MsgBox, Form1, gridControl1, gridGroupingControl1] -->
```