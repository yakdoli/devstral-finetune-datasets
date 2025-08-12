```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_092.jpeg
document_name: Olap Common
page_number: 092
page_id: Olap Common#page_092
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:21:05Z
fidelity: lossless
-->

# Essential Olap Common

## Sequential Diagram

The following sequential diagram shows the workflow of OlapBase when a user gives input as an OlapReport.

<div align="center">
 <img src="seq_diagram.png" alt="Olap Base sequential diagram" />
 <p>Figure 9: Olap Base sequential diagram</p>
</div>

## 5.9 Bind the MDX Query to OlapDataManager

### Overview
- MDX queries are one of the inputs accepted by the `OlapDataManager` to process the data in the connected data source.
- There are two ways to pass the MDX query to the `OlapDataManager`.

### WinForms-specific conventions
- **Property Binding**: Through the `MdxQuery` property.
- **Method Binding**: Through the `ExecuteCellSet()` method argument.

### Content

MDX queries are one of the inputs accepted by the `OlapDataManager` to process the data in the connected data source. To bind the MDX query to the `OlapDataManager`, you can use either of the following two methods:

1. **Through the `MdxQuery` property**  
   - Assign the MDX query string directly to the `MdxQuery` property of the `OlapDataManager`.

2. **Through the `ExecuteCellSet()` method argument**  
   - Pass the MDX query as an argument when invoking the `ExecuteCellSet()` method on the `OlapDataManager`.

## Page-level Navigation/TOC

- **Sequential Diagram**
- **5.9 Bind the MDX query to OlapDataManager**

### API Reference (if applicable)
- Relevant properties and methods can be referenced in the API documentation for more details.

### Code Examples (multi-language supported)
Here is an example of how to bind an MDX query using both methods:

```csharp
// Using MdxQuery property
OlapDataManager olapDataManager = new OlapDataManager();
olapDataManager.MdxQuery = "SELECT FROM [YourCube].[YourView]";

// Using ExecuteCellSet method
CellSet cellSet = olapDataManager.ExecuteCellSet("SELECT FROM [YourCube].[YourView]");
```

## Cross References
- [Refer to the OlapDataManager documentation for more detailed information.](#OlapDataManager-documentation)

## RAG Annotations
<!-- tags: Olap Common, OlapDataManager, MDX query, property binding, method binding keywords: MDX query, OlapDataManager, MdxQuery, ExecuteCellSet -->
```