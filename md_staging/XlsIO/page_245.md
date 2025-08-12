```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_245.jpeg
document_name: XlsIO
page_number: 245
page_id: XlsIO#page_245
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:04:53Z
fidelity: lossless
-->

## Essential XlsIO

### Sparklines Options by XlsIO

**Sparklines Options by XlsIO:**

MS Excel 2010 provides various options through Sparklines tool ribbon in order to customize the appearance of Sparklines. See *figure 2*.

#### Type

In MS Excel 2010, click Design and then Type in order to customize the Sparkline type for the current Sparklines. XlsIO provides an equivalent API to perform this with simple properties as follows.

```csharp
sparklineGroup.SparklineType = SparklineType.Line
```

#### Show

In MS Excel 2010, click Design and then Show in order to customize the view of the Sparklines with high point, low point, first point, last point, negative point, markers. XlsIO provides an equivalent API to perform this with simple properties as follows.

**Known Limitations:** The Markers can be applied only for the line sparkline type.

```csharp
sparklineGroup.ShowFirstPoint = true;
sparklineGroup.ShowLastPoint = true;
sparklineGroup.ShowHighPoint = true;
sparklineGroup.ShowLowPoint = true;
sparklineGroup.ShowMarkers = true;
sparklineGroup.ShowNegativePoint = true;
```

#### Sparkline Color

The appearance of the Sparklines can be customized by applying colors. Click Design and then select Style. Choose the Sparkline color option in order to customize the Sparklines. XlsIO provides an equivalent API to perform this with simple property as follows.

```csharp
sparklineGroup.SparklineColor = Color.Blue;
```

#### Marker Color

The appearance of points in the sparklines can be customized by applying colors to it. Click Design and then select Style. Choose the Marker Color option to customize the appearance of points in the Sparklines. XlsIO provides an equivalent API to perform this with simple properties as follows.

```csharp
```

## Page-level Navigation/TOC (if applicable)
- If the body contains a local Table of Contents for this page, keep it as a bullet/numbered list with links/text as shown. Do not create links that don’t exist.
- Ignore global site TOC or breadcrumbs unless the page explicitly describes them.

## Cross References
See also:
- Sparklines
- MS Excel 2010
- Guide for using the Sparklines tool ribbon
- Equivalent APIs provided by XlsIO

## RAG Annotations
- <!-- tags: [XlsIO, Sparklines, MS Excel 2010, Syncfusion Winforms, API, version 11.4.0.26] keywords: [Sparklines, Customization, Excel, Design, Type, Show, Marker, Color, XlsIO, C#, Properties, Methods, Line type, High point, Low point, First point, Last point, Negative point, Marker color, Sample code] -->
```
```