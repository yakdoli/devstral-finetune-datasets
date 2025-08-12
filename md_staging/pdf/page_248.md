```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_248.jpeg
document_name: pdf
page_number: 248
page_id: pdf#page_248
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:38:53Z
fidelity: lossless
-->

# Essential PDF

## Overview

- Sets various PDF document settings such as page mode, page scaling, page layout, orientation, and page transitions.
- Configures viewer preferences and page settings using C# and VB.NET.

## Content

### Configuring PDF Document Settings

#### C#

```csharp
// To set UseOC page Mode.
doc.ViewerPreferences.PageMode = PdfPageMode.UseOC;

// Setting pagescale option as None
doc.ViewerPreferences.PageScaling = PageScalingMode.None;

// To set two column left page layout.
doc.ViewerPreferences.PageLayout = PdfPageLayout.TwoColumnLeft;

// Sets page transition.
doc.PageSettings.Transition.PageDuration = 1;
doc.PageSettings.Transition.Duration = 1;
```

#### VB.NET

```vb
' To set landscape page orientation.
doc.PageSettings.Orientation = PdfPageOrientation.Landscape

' To set UseOC page Mode.
doc.ViewerPreferences.PageMode = PdfPageMode.UseOC

' Setting pagescale option as None
doc.ViewerPreferences.PageScaling = PageScalingMode.None

' To set two column left page layout.
doc.ViewerPreferences.PageLayout = PdfPageLayout.TwoColumnLeft

'Sets page transition.
doc.PageSettings.Transition.PageDuration = 1
doc.PageSettings.Transition.Duration = 1
```

### Explanation

- **Page Mode**: Specifies how the document should be viewed upon opening. Here, `UseOC` is set, indicating that Optional Content Groups (OCGs) should be displayed.
- **Page Scaling**: Sets the initial page display scale. `None` indicates no scaling.
- **Page Layout**: Configures the layout of the document. `TwoColumnLeft` specifies a two-column layout with the left column active.
- **Page Transition**: Defines the duration for page transitions when navigating between pages.

## RAG Annotations

<!-- tags: [pdf, document settings, viewer preferences, page scaling, page layout, page transitions, C#, VB.NET] keywords: [PdfPageMode, PageScalingMode, PdfPageLayout, PageSettings, Transition, page duration, Syncfusion Winforms] -->
```