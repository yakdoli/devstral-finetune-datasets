```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_235.jpeg
document_name: chart
page_number: 235
page_id: chart#page_235
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:29:04Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Funnel Chart

### **4.5.1.29 Font**

**Gets or sets a font object used for drawing the data point labels.**

#### Details

| **Possible Values**                                     | Specifying font face, size, and style.                                                      |
|---------------------------------------------------------|------------------------------------------------------------------------------------------------|
| **Default Value**                                       | -   FontStyle - Regular                                                                    <br>-   Face Name - MicroSoft Sans Serif                                           <br>-   Size - 8.25                                                                |
| **2D / 3D Limitations**                                | No                                                                                           |
| **Applies to Chart Element**                           | All series and points                                                                       |
| **Applies to Chart Types**                             | All Chart types                                                                              |

Here is some sample code.

#### Series Wide Setting

##### [C#]

```csharp
this.chartControl1.Series[0].Style.DisplayText = true;
this.chartControl1.Series[0].Style.Font.Bold = true;
this.chartControl1.Series[0].Style.Font.Facename = "Arial";
this.chartControl1.Series[0].Style.Text = "Series 1";
```

##### [VB.NET]
```
```


## API Reference

### WinForms-specific conventions
- Properties and methods are listed using exact control names, namespaces, and types.
- Design-time vs. runtime features are explicitly distinguished.
- Using statements and imports are preserved.

### Parameters
- Name | Type | Description | Default | Required

## Code Examples (multi-language supported)
- Extract all code exactly using fenced blocks with proper language identifiers.

### Getting Started

## Page-level Navigation/TOC (if applicable)
- Include a bulleted list of local Table of Contents entries if present on the page.

## Cross References
- Add references to other sections or pages as bullet points, using exact anchor texts.

## RAG Annotations
<!-- tags: [WinForms, Font, Series, Funnel Chart] keywords: [chart, font object, data point labels, MicroSoft Sans Serif, Arial, Series Wide Setting] -->
``` 
