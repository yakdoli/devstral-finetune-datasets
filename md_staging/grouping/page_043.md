```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_043.jpeg
document_name: grouping
page_number: 043
page_id: grouping#page_043
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:00:15Z
fidelity: lossless
-->

# Essential Grouping

groupingEngine.TableDescriptor.RecordFilters.Add(rfd)

```vb
' Display the data after filtering.
For Each rec In groupingEngine.Table.FilteredRecords
    Dim obj As MyObject = CType(rec.GetData(), MyObject)
    If Not (obj Is Nothing) Then
        Console.WriteLine(obj)
    End If
Next rec

' Pause
Console.ReadLine()
```

![Figure 17: Screen Showing the Initial Data Followed by the Same Data Filtered on [D] LIKE 'd1'](/images/grouping#page_043-figure17.png)

13. You can apply more complex filters. Here is the code that will remove any existing filters and filter the property D being d1 or property b equal 2. Note here that since you expect property B to display only numeric data, you must use the = operator in the comparison.

## C#

```csharp
groupingEngine.TableDescriptor.RecordFilters.Clear();
```

## API Reference (if applicable)
Namespace, Class, Members (Methods/Properties/Events/Enums) in subsections.
- Parameters table: Name | Type | Description | Default | Required
- Returns: Type + description.
- Exceptions: bullet list.

## Code Examples (multi-language supported)
- Extract ALL code exactly. Use fenced blocks with language: ```csharp, ```vb, ```xml, ```xaml, ```js, ```css, ```ts, ```python.
- Keep full signatures, imports/usings, comments, region markers.
- Inline code in text should be wrapped with backticks.

## Page-level Navigation/TOC (if applicable)
- If the body contains a local Table of Contents for this page, keep it as a bullet/numbered list with links/text as shown. Do not create links that don’t exist.
- Ignore global site TOC or breadcrumbs unless the page explicitly describes them.

## Cross References
See also: bullet list of explicit links/texts present on the page. Do not fabricate.

## RAG Annotations
<!-- tags: [product, module, control, api, version?] keywords: [k1, k2, ...] -->
```