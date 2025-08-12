```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_378.jpeg
document_name: XlsIO
page_number: 378
page_id: XlsIO#page_378
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:11:48Z
fidelity: lossless
-->

**Essential XlsIO**

```csharp
// Creating Template Marker Processor
// Northwind Customers Table
ITemplateMarkersProcessor marker =
    workbook.CreateTemplateMarkersProcessor();
marker.AddVariable("Sales", arrSalesPerson);

// Processing the markers in the template
marker.ApplyMarkers();
```

## Output

| Sales Person Name                | Sold     |
|-----------------------------------|----------|
| Andy Bernard                      | $45,000 |
| Jim Halpert                       | $34,000 |
| Karen Fillippelli                | $75,000 |
| Phyllis Lapin                    | $56,500 |
| Stanley Hudson                    | $46,500 |
| Bernard Shah                      | $48,000 |
| Patricia McKenna                  | $34,000 |
| Antonio Moreno Taquería           | $90,000 |
| Thomas Hardy                      | $56,500 |
| Christina Berglund                | $46,500 |
| Hanna Moos                        | $45,000 |
| Frédérique Citeaux                | $34,000 |
| Martin Sommer                     | $75,000 |
| Laurence Lebihan                  | $56,500 |
| Elizabeth Lincoln                 | $25,000 |
| Victoria Ashworth                 | $45,000 |
| Patricio Simpson                  | $34,000 |
| Marketing Manager                 | $75,000 |
| Yang Wang                         | $56,500 |
| Pedro Afonso                      | $46,500 |
| Elizabeth Brown                   | $45,000 |
| Sven Ottlieb                      | $34,000 |
| Janine Labrune                    | $75,000 |
| Ann Devon                         | $88,000 |
| Roland Mendel                     | $76,500 |

**Figure 103**

### 4.5.5 Template Markers

<!-- tags: [Essential XlsIO, Template Markers, Northwind Customers Table, Template Marker Processor] keywords: [template markers, workbook, ApplyMarkers, arrSalesPerson, Sales Person Name, Sold] -->
```