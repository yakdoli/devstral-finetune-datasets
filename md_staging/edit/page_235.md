```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_235.jpeg
document_name: edit
page_number: 235
page_id: edit#page_235
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:08:04Z
fidelity: lossless
-->

## Overview
- Enabling fast load mode by setting the ConvertOnLoad property.
- Overview of localization and globalization aspects in the software market.
- Demonstration of how the Find dialog in Edit Control is localized to French and Spanish.

## Content

### Configure Fast Load Mode

The ConvertOnLoad property of the Edit Control should be set to **False** to enable the fast load mode. By default, this property is set to **True**.

#### Code Examples

**[C\#]**
```csharp
// Enable the fast load mode.
this.editControl1.ConvertOnLoad = false;
```

**[VB.NET]**
```vb.net
' Enable the fast load mode.
Me.editControl1.ConvertOnLoad = False
```

### 4.13 Localization and Globalization

In the age of globalization, the market for all goods becomes more and more internationalized, enforcing the need to provide information in a variety of languages. This is especially true for the software market, where the product itself consists of exclusive localizable information. Translation and customization of software involves a variety of specialists such as programmers, translators, localization engineers, quality assurance (QA) specialists, and project managers. International users of computer software expect their software to talk to them in their own language. This is not only a matter of convenience or of national pride, but a matter of productivity. Users who understand a product fully will be more skilled in handling it, and will avoid making mistakes. So, users will prefer applications in their language and adapted to their cultural environment.

The following images show how the Find dialog in Edit Control is localized to French and Spanish.

#### Figure 78: Find dialog localized to French
![Find dialog localized to French](image_for_french_localization.png)

### Figure 78: Find dialog localized to French

## RAG Annotations
<!-- tags: [product, module, control, api, version?] keywords: [ConvertOnLoad, fast load mode, localization, globalization, Edit Control, C#, VB.NET, French, Spanish, localizable information, software market, translation, software customization] -->
```