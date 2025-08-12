```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_087.jpeg
document_name: chart
page_number: 087
page_id: chart#page_087
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:20:34Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Explains how to create and customize a Gantt Chart using the Essential Chart for Windows Forms.
- Describes the features and functionality of the Gantt Chart for tracking task durations and progress.
- Includes chart details such as the number of series and Y values per point.

## Content

### 4.4.2.4 Gantt Chart
A Gantt chart is a graphical representation of the duration of tasks against the progression of time. In a Gantt chart, each task takes up one row. The expected time for each task is represented by a horizontal bar whose left end marks the expected beginning of the task and whose right end marks the expected completion of the task. Tasks may run sequentially, in parallel, or overlapping.

#### Description
You could then use another series to represent the completed portion of the different tasks. This new series will then contain data points with their beginning values coinciding with the beginning values of the data points from the previous series and the ending value based on the fraction of the work that has been completed on the task. This way, one can get a quick reading of a project progress by drawing a vertical line through the chart at the current date.

![Chart displaying Gantt Series](Essential_Chart_Gantt_Chart.png)
**Figure 49: Chart displaying Gantt Series**

### Chart Details
- **Number of Y values per point:** 2. (1st is beginning value and the 2nd is the ending value)
- **Number of Series:** One or more.

```markdown

<!-- tags: [essential_chart, windows_forms, gantt_chart, syncfusion_winforms] keywords: [gantt chart, task duration, task progress, chart customization, series details] -->
```