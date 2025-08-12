```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_960.jpeg
document_name: grid
page_number: 960
page_id: grid#page_960
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:52:12Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### 4.3.4.8.3 Word Converter

Export to Word is one of the most common functionalities that are required in the .NET world. The Essential Grid Control has in-built support for Word Export. Users can download the data from the Grouping Grid control into a Word document for offline verification and/or computation. This can be achieved by making use of the GroupingGridWordConverter class. This section will walk you through the conversion of the contents of the grid to a word file as well as discuss the various converter options.

The GroupingGridWordConverter class derives from GridWordConverterBase. It contains a number of methods that helps in exporting different components of the grouping grid. You can be able to export NestedTables as well.

The following table lists the properties offered by Grouping Grid Word Converter. By setting these properties, you could be able to choose the elements you need to export.

| Property       | Description                                                                                                                             |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| ShowHeader     | Specifies if header should be displayed.                                                                                              |
| ShowFooter     | Indicates if footer should be displayed.                                                                                             |

#### Method

Grouping Grid Word Converter control provides a method called GroupingGridToWord. This is the method that does the conversion of grouping grid contents to a word file. It accepts two parameters: grouping grid to be converted and filename of the destination word document.

#### Syntax

**[C\#]**

```csharp
GroupingGridWordConverter converter = new GroupingGridWordConverter();
converter.GroupingGridToWord("Grid.doc", this.gridGroupingControl);
```

**[VB.NET]**

```vb
Dim converter As GroupingGridWordConverter = New GroupingGridWordConverter()
converter.GroupingGridToWord("Grid.doc", Me.gridGroupingControl)
```

#### Events
```


<!-- tags: [product, module, control, api, version, windows forms, essential grid, grouping grid, word converter, gridwordconverterbase, groupinggridwordconverter] keywords: [export to word, offline verification, computation, grid contents, word document, header, footer, nestedtables, groupinggridtoword, grid control] -->
```