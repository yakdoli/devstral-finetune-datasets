```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_579.jpeg
document_name: grid
page_number: 579
page_id: grid#page_579
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:25:45Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## 4.2.2.14 Record Navigation Bar

### Overview
- Demonstrates how to display a Grid Data Bound Grid within a Grid Record Navigation control.
- Provides a look similar to Microsoft Access.

### Content

#### Figure 229: Multi Row Record

- **Note**: For more details, refer the following browser sample:

```
<Install Location>\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Windows\Samples\2.0\Data Bound\Multi Row Record Demo
```

#### Example

Using the following code example, you can switch the display of the records from the NorthWind's Customers table between displaying a single row per record and multiple rows per record. The `Binder.LayoutColumns` function can be used to break the records into multiple rows. The record can be broken by inserting a "." in the `LayoutColumns()` function of the `GridHierarchyLevel` class.

**C# Code Example:**

```csharp
// "." indicates a new row.
binder.LayoutColumns(new string[] { "CustomerID", "CompanyName", 
                                   "ContactTitle", "ContactName", ".", 
                                   "Address", "City", ".", 
                                   "PostalCode", "Country", "Phone", "Fax", "Region" });
```

**VB.NET Code Example:**

```vbnet
' "." indicates a new row.
binder.LayoutColumns(New String() { "CustomerID", "CompanyName", 
                                    "ContactTitle", "ContactName", ".", 
                                    "Address", "City", ".", 
                                    "PostalCode", 
                                    "Country", "Phone", "Fax", "Region" })
```

### Record Navigation Bar

It is possible to display a Grid Data Bound Grid within a Grid Record Navigation control. This combination will give you a look similar to Microsoft Access.

## Code Examples

### C#

```csharp
GridModel gridModel = gridDataBoundGrid1.Model;
GridModelDataBinder binder = gridDataBoundGrid1.Binder;

// "." indicates a new row.
binder.LayoutColumns(new string[] { "CustomerID", "CompanyName",
                                   "ContactTitle", "ContactName", ".",
                                   "Address", "City", ".",
                                   "PostalCode", "Country", "Phone", "Fax", "Region" });
```

### VB.NET

```vbnet
Dim gridModel As GridModel = gridDataBoundGrid1.Model
Dim binder As GridModelDataBinder = gridDataBoundGrid1.Binder

' "." indicates a new row.
binder.LayoutColumns(New String() { "CustomerID", "CompanyName",
                                    "ContactTitle", "ContactName", ".",
                                    "Address", "City", ".",
                                    "PostalCode",
                                    "Country", "Phone", "Fax", "Region" })
```

## Page-level Navigation/TOC (if applicable)
- No further TOC is present in this section.

## Cross References
- See also: [Syncfusion Grid Navigation Documentation](#)

### RAG Annotations
```html
<!-- tags: [Syncfusion, Grid, WinForms, DataBinding, HierarchyLevels, NavigationBar, MultiRowRecord] keywords: [LayoutColumns, GridDataBoundGrid, HierarchyLevel, Microsoft Access] -->
```

```