```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_228.jpeg
document_name: pdf
page_number: 228
page_id: pdf#page_228
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:37:40Z
fidelity: lossless
-->

# Metafile

## Overview
- This page demonstrates the use of a metafile to generate a chart image.
- Displays a 3D bar chart with varying data points over specific dates.
- Utilizes a grid layout for clarity and visual distinction.

## Content

### Essential Chart

#### Chart Description
The chart displayed is labeled as an "Essential Chart" and provides a 3D visual representation of data points grouped into different color-coded categories (green and red). The x-axis represents dates, while the y-axis denotes numerical values ranging from 20 to 45. Key features include:

- **Date Range**: The chart spans from May 16, 2005, to September 4, 2005, with specific date markers at regular intervals.
- **Data Representation**: The green 3D blocks indicate higher values, while the red blocks indicate lower values, suggesting a comparison or variation in the dataset.
- **3D Perspective**: The visualization is rendered in a three-dimensional perspective, enhancing the depth and readability of the data distribution.

#### Metafile Integration
The chart is embedded using a metafile, allowing for efficient handling of graphical data without recreating the graphical elements from scratch. This approach is beneficial for maintained images in PDFs and other documents requiring a consistent visual experience.

### User Interface Context
The image is displayed within the Adobe Reader application, showcasing how the metafile can be effectively rendered and embedded in PDF documents. The interface includes standard toolbar options for navigation, editing, and viewing, along with controls for zooming and printing.

## API Reference

### Example of Metafile Usage
- The metafile creation and usage are demonstrated in the context of a charting library provided by Syncfusion for WinForms. The exact code to generate the metafile is not visible in the image, but the library likely includes API methods such as:
  - `CreateMetafile()`
  - `DrawToMetafile(Graphics g)`

### Parameters and Methods
- **CreateMetafile()**
  - Returns a `Metafile` object that can be drawn onto other graphics surfaces.
- **DrawToMetafile(Graphics g)**
  - Renders the current chart onto the specified graphics object `g` into a metafile format.

## Code Examples

### Sample Code to Generate Metafile (C#)
```csharp
using Syncfusion.Windows.Forms.Chart;
using System.Drawing;
using System.Windows.Forms;

public void GenerateMetafileChart()
{
    // Create a chart
    ChartControl chart = new ChartControl();
    // Populate chart data...

    // Create a memory DC and metafile
    using (Bitmap memoryImage = new Bitmap(800, 600))
    using (Graphics memoryGraphics = Graphics.FromImage(memoryImage))
    {
        Rectangle bbox = chart.DisplayRectangle;
        using (Metafile metafile = new Metafile(memoryGraphics, bbox, MetafileFrameUnit.Pixel))
        {
            chart.Export.GraphicsObject.DrawToMetafile(metafile, bbox);
            chart.Refresh();

            // Save the metafile for embedding in PDF
            byte[] metafileData = metafile.Save();
            // Embedding logic for PDF generation...
        }
    }
}
```

### Explanation
The provided code snippet demonstrates how to generate a metafile representation of a chart using the Syncfusion WinForms charting library. This approach ensures that the chart is efficiently rendered and can be embedded in PDF documents or other graphical formats.

## Cross References
- **Related Documentation**: Refer to the Syncfusion WinForms Charting Library documentation for detailed API usage and examples.
- **Previous Sections**: Review prior content on setting up the chart control and configuring data sources.

## Page-level Navigation/TOC (if applicable)
- **Overview**
- **Content**
  - Essential Chart
  - Metafile Integration
- **API Reference**
- **Code Examples**
- **Cross References**

<!-- tags: [Syncfusion, WinForms, Charting, Metafile, PDF, Essential Chart] keywords: [metafile creation, 3D chart, data visualization, date range, API methods, Syncfusion library, chart control, PDF embedding] -->
```