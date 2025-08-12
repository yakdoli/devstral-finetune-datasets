```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_063.jpeg
document_name: Olap Common
page_number: 063
page_id: Olap Common#page_063
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:18:22Z
fidelity: lossless
-->

## Essential OlapCommon

```vb
IncludeAvailableMembers = True

' Adding the Member properties to the Dimension Element
dimElementRow.MemberProperties.Add(New MemberProperty("Title", "[Employee].[Employees].[Title]"))
dimElementRow.MemberProperties.Add(New MemberProperty("Phone", "[Employee].[Employees].[Phone]"))
dimElementRow.MemberProperties.Add(New MemberProperty("Email Address", "[Employee].[Employees].[Email Address]"))

Dim dimElementColumn As DimensionElement = New DimensionElement()
' Specifying the Dimension Name
dimElementColumn.Name = "Product"
' Specifying the Hierarchy and level name for the Dimension Element
dimElementColumn.AddLevel("Product Categories", "Category")
dimElementColumn.MemberProperties.Add(New MemberProperty("Dealer Price", "[Product].[Product Categories].[Dealer Price]"))
dimElementColumn.MemberProperties.Add(New MemberProperty("Standard Cost", "[Product].[Product Categories].[Standard Cost]"))

' Adding Row Members
olapReport.SeriesElements.Add(dimElementRow)

'''Adding Column Members
olapReport.CategoricalElements.Add(measureElementColumn)
```

### 4.3.11.2 Sample Report for Non-OLAP data

The following code snippet illustrates the sample `OlapReport` for an `OlapDataManager`:

#### [C#]

```csharp
OlapReport olapReport = new OlapReport();
olapReport.Name = "Sales Report";

// Specifying the Row Dimension Element
DimensionElement dimElementRow = new DimensionElement();
```

## Boilerplate Footer
© 2013 Syncfusion. All rights reserved. | Page
```

<!-- tags: [OlapCommon, OlapReport, OlapDataManager, Syncfusion, Winforms, DimenionElement] keywords: [olap, report, dimension element, olap manager, sample, sales report, employer, employee, title, phone, email address, product categories, dealer price, standard cost] -->
