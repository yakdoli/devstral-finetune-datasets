```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_646.jpeg
document_name: chart
page_number: 646
page_id: chart#page_646
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:58:10Z
fidelity: lossless
--> 

## Overview

- Detailed chart data binding and customization options are covered, including factorial, gamma functions, and data exporting/importing. The document also discusses various chart types, such as line, bar, and area charts, along with performance and localization features.

## Content

### Chart Data and Customization

- **4.12.2.6 Factorial** 556
- **4.12.2.7 F Cumulative Distribution** 557
- **4.12.2.8 Gamma Function** 558
- **4.12.2.9 Gamma Cumulative Distribution** 560

#### Data Importing
- **4.13 Importing** 569
  - **4.13.1 Importing a CSV file** 569
  - **4.13.2 Import Data from XML to a Chart** 570
  - **4.13.3 Import Data from Excel to Chart** 570
- **4.14 Exporting** 571
  - **4.14.1 Exporting as an Image** 571
  - **4.14.2 Exporting to Word Doc** 574
  - **4.14.3 Exporting to Grid** 577
  - **4.14.4 Exporting to Excel** 581
  - **4.14.5 Exporting to PDF** 584

#### Design Features
- **4.15 Design time Features** 586
  - **4.15.1 Chart Templates** 586
  - **4.15.2 Tasks Window** 590
- **4.16 Printing and Print Preview** 594
- **4.17 Data Manipulation** 597
- **4.18 Hit Testing** 600
  - **4.18.1 Chart Coordinates by Point** 600
  - **4.18.2 LegendItem By Point** 601
  - **4.18.3 Chart Area Bounds** 603
- **4.19 Chart control events** 605
  - **4.19.1 Chart Region Events** 606
  - **4.19.2 VisibleRangeChanged Event** 609
  - **4.19.3 ChartFormatAxisLabel Event** 610
  - **4.19.4 PrepareStyle Event** 610
  - **4.19.5 SeriesInCompatible Event** 611
  - **4.19.6 LayoutCompleted Event** 612
  - **4.19.7 ChartAreaPaint Event** 612
  - **4.19.8 ChartLegendFilterItems Event** 613
  - **4.19.9 PreChartAreaPaint Event** 613

#### Chart Data Binding
- **4.2 Chart Data** 43
  - **4.2.1 Binding a DataSet to the Chart** 44
  - **4.2.2 Implementing Custom Data Binding Interfaces** 47
  - **4.2.3 Chart Data Binding with IEnumerables** 50
  - **4.2.4 Data Binding in Chart Through Chart Wizard** 54

#### Localization and Performance
- **4.20 Localization** 613
- **4.3 Improving Performance** 67

#### Chart Types

##### Line Charts
- **4.4 Chart Types** 70
  - **4.4.1 Line Charts** 72
    - **4.4.1.1 Line Chart** 72
    - **4.4.1.2 Spline Chart** 74
    - **4.4.1.3 Rotated Spline Chart** 76
    - **4.4.1.4 Step Line Chart** 78

##### Combination Charts
- **4.4.10 Combination Chart** 153
- **4.4.11 Heat Map Charts** 155
- **4.4.12 Stacking Charts** 158
- **4.4.13 Step Charts** 158
- **4.4.14 Sparkline** 159

##### Bar Charts
- **4.4.2 Bar Charts** 80
  - **4.4.2.1 Bar Chart** 80
  - **4.4.2.2 Stacking Bar Chart** 83
  - **4.4.2.3 StackedBar100 Chart** 85
  - **4.4.2.4 Gantt Chart** 87
  - **4.4.2.5 Histogram Chart** 88
  - **4.4.2.6 Tornado Chart** 91

##### Column Charts
- **4.4.3 Column Charts** 93
  - **4.4.3.1 Column Chart** 93
  - **4.4.3.2 Column Range Chart** 95
  - **4.4.3.3 Stacking Column Chart** 97
  - **4.4.3.4 Stacked Column100 Chart** 99

##### Area Charts
- **4.4.4 Area Charts** 101
  - **4.4.4.1 Area Chart** 102
  - **4.4.4.2 Spline Area Chart** 103
  - **4.4.4.3 Stacking Area Chart** 106
  - **4.4.4.4 StackedArea100 Chart** 108

## API Reference

- **Namespace**: Syncfusion.WinForms.Chart
  - **Class**: Chart
    - **Members**:
      - Methods:
        - BindData()
        - ExportTo()
        - PrepareStyle()
      - Properties:
        - ChartData
        - LegendItems
      - Events:
        - VisibleRangeChanged
        - LayoutCompleted
        - ChartAreaPaint

## Code Examples

```csharp
// Example: Binding a DataSet to the Chart
using Syncfusion.WinForms.Chart;
using System.Data;

Chart chart = new Chart();
DataSet dataSet = new DataSet();
// Populate dataSet with data
chart.DataSource = dataSet;
```

## RAG Annotations

```html
<!-- tags: syncfusion, winforms, chart, data-binding, customization, chart-types, performance-enhancement, localization, factorial, gamma-function, import-export, design-time-features keywords: chart, data binding, line charts, bar charts, area charts, step charts, sparkline, performance, localization, factorial, gamma function, import, export, chart types -->
```

```