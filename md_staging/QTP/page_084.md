```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_084.jpeg
document_name: QTP
page_number: 084
page_id: QTP#page_084
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:06:45Z
fidelity: lossless
-->

## Applying CollapseNode and ExpandNode methods in QTP

The following code examples illustrate how to use the CollapseNode and ExpandNode methods.

```csharp
SwfWindow("QTPTreeViewAdv").SwfObject("Node1").CollapseNode("Node2");
SwfWindow("QTPTreeViewAdv").SwfObject("Node1").ExpandNode("Node2");
```

### 7.4 Essential Chart

#### 7.4.1 How to get the displayed text in the X-axis and Y-axis

**Supported method to get the displayed text in the X-axis and Y-axis**

The `GetXAxisText` and `GetYAxisText` methods are used to get the displayed text in the X-axis and Y-axis. This method returns the displayed text in string format.

**Use Case Scenarios**

This feature enables you to get the displayed text in the X-axis and Y-axis in QTP testing.

#### Methods Table

| Method       | Description                                         | Parameters                  | Return Type |
|--------------|-----------------------------------------------------|------------------------------|--------------|
| GetXAxisText | Gets the displayed text of the X-axis in Essential Chart. | public string GetXAxisText() | String       |
| GetYAxisText | Gets the displayed text of the Y-axis in Essential Chart. | public string GetYAxisText() | String       |

<!-- tags: syncfusion, essential tools, qtp, essential chart, x-axis, y-axis, text retrieval, winforms keywords: collapse, expand, node, treeview, axis text -->
```