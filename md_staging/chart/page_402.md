```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_402.jpeg
document_name: chart
page_number: 402
page_id: chart#page_402
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:41:19Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Illustration of setting Chart labels using the ChartFormatAxisLabel Event.
- Explanation on how to specify a set of custom labels to dictate intervals.
- Reference to using custom text for labeling in charts.

## Content

### Illustrates setting Chart labels using ChartFormatAxisLabel Event

The chart below demonstrates the use of custom labels on the x-axis when the event triggers.

**Y-Axis**: Represents the values ranging from -200 to 800.

**X-Axis**: The labels are set to represent months: 1st Month, 2nd Month, 3rd Month, 4th Month, 5th Month, and 6th Month. These labels are dynamically set when specific events trigger.

#### Figure 258: Customized Chart Labels

**Description**: A bar chart illustrating the Y-Axis values for each month on the X-Axis, with labels set when event triggers.

### Specify a set of custom labels thereby dictating the intervals as well

#### 1. Using Custom Text

| ChartAxis Property              | Description                                                                                          |
|----------------------------------|------------------------------------------------------------------------------------------------------|
| TickLabelsDrawingMode           | - **AutomaticMode**: Labels will be determined by the engine.<br>- **UserMode**: Labels from the Labels collection will be used.<br>- **BothUserAndAutomaticMode**: Both labels from the automatic mode and user mode will be rendered.<br>- **None**: Labels will not be rendered. |
| Labels                          | A custom collection that lets you fully customize the labels that gets generated. The TickLabelsDrawingMode should be set to **UserMode** or **BothUserAndAutomaticMode**. |

## Page-level Navigation/TOC (if applicable)
- **Illustrates setting Chart labels using ChartFormatAxisLabel Event**
- **Specify a set of custom labels thereby dictating the intervals as well**
  - **1. Using Custom Text**

## Cross References
- See also: Chart, ChartAxis, TickLabelsDrawingMode, Labels collection.

<!-- tags: [chart, chartaxis, winforms, syncfusion, 11.4.0.26] keywords: [chartlabels, customlabels, usermode, automaticmode, labels, intellitage, sdk, eventtriggers, winformscontrols, chartaxisproperty] -->
```