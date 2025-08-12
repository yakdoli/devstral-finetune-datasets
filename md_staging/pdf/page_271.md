```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_271.jpeg
document_name: pdf
page_number: 271
page_id: pdf#page_271
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:42:26Z
fidelity: lossless
-->

## E s s e n t i a l P D F

### Setting the numbering Range for PDF document

**Figure 59: Setting the numbering Range for PDF document**

![Image Description](./image.png)

### 4.2.2 Import Pages

Pages from other documents can be imported to the existing document using the `ImportPage` method. The following code example illustrates this method.

```csharp
// [C#]
doc.ImportPage(ldDoc, page);
doc.ImportPage(ldDoc, pageIndex);
doc.ImportPageRange(ldDoc, startPageIndex, endPageIndex);
```

``` 
© 2013 Syncfusion. All rights reserved.
``` 

<!-- tags: [pdf, import pages, document manipulation, numbering range, Adobe Reader, ImportPage method] keywords: [Syncfusion Winforms, ImportPage, PDF document] -->
``` 
