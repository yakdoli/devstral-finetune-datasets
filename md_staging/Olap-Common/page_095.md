```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_095.jpeg
document_name: Olap Common
page_number: 095
page_id: Olap Common#page_095
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:20:34Z
fidelity: lossless
-->

# Essential OlapCommon

## Overview
- Explains the binding of Non-OLAP data to OlapDataManager.
- Demonstrates the sequential diagram for Olap base operations.
- Provides code examples in C# and VB for binding Non-OLAP data.

## Content

### Figure 10: Olap base sequential diagram

![Olap base sequential diagram](https://image-source-url.com/image10.png)

**5.10 Bind the Non-OLAP data to OlapDataManager**

To bind the Non-OLAP data, you should bind an item source to the OlapDataManager's item source property and give the Non-OLAP data report to process the given item source. The item source can be an Enumerable collection or an ITyped List.

#### The following code will illustrate the binding of the Non-OLAP data. Here we have used a sample Enumerable collection “ProductSalesCollection” and a sample Olap report “salesReport”:

##### [C#]

```csharp
ProductSalesCollection productSales = new ProductSalesCollection();
olapDataManager.ItemSource = productSales;

olapDataManager.SetCurrentReport(salesReport);
```

##### [VB]

```vb
Dim productSales As ProductSalesCollection = New ProductSalesCollection()
olapDataManager.ItemSource = productSales

olapDataManager.SetCurrentReport(salesReport)
```

### Sequential Diagram
<!-- tags: [OlapDataManager, Non-OLAP data, binding, Olap report, C#, VB, Enumerable collection] keywords: [OlapDataManager, Non-OLAP data, binding, Olap report, code examples, Enumerable collection, ITyped List] -->
```