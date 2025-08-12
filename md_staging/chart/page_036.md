```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_036.jpeg
document_name: chart
page_number: 036
page_id: chart#page_036
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:17:54Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Demonstrates the Chart Wizard feature in Syncfusion for manipulating chart axes.
- Provides instructions on using the Chart Wizard to control the appearance of ChartControl axes.
- Explains how to edit and configure axis labels, including default fonts and colors.

## Content

### Chart Wizard Interface
- **Figure 16: Axes button selected in Chart Wizard**
  The image shows the Chart Wizard interface with an emphasis on the Axes selection. The interface includes various options for customizing the chart axes, including Grid Line, Axis Title, and Value Type. Here are the details:
    - **X Axis** settings allow control over features such as:
      - Grid Line (Checked in the example).
      - Axis Title (Placeholder is empty in the example).
      - Position (Options include Near, Center, Far).
    - The **Axes button** indicates that the user can access further configurations related to axis labels, formatting, and intersections.
    - The **Default** chart on the right displays a sample bar chart labeled "chartControl1".

### Methodology for Label Customization
- **Collection Editor Dialog**:
  - Click the **Add** button to add a label to the collection.
  - Select the added label to view its properties on the right side. Properties such as the color, font, value type, and more can be adjusted using the properties window.
  - If a label needs to be removed, select the label and click the **Remove** button.
  - After adding all the values to the collection and making necessary property changes, click **OK** to apply the changes. This same method can be used to edit labels for the y-axis as well.

### WinForms-specific Settings
- The interface also allows users to control additional chart properties such as inter-axis actions (e.g., Intersect Action: MultipleRows).
- Users can apply changes using the **Apply**, **Finish**, or **Cancel** buttons at the bottom of the interface.

## API Reference
- **Namespace**: Syncfusion.Windows.Forms.Chart
- **Classes**:
  - ChartWizard
  - AxesOptions
  - LabelEditor

## Code Examples
```csharp
// Example: Configuring Chart Control Axes
using Syncfusion.Windows.Forms.Chart;

// Create Chart instance
ChartControl chartControl = new ChartControl();

// Accessing Chart Wizard for axis configuration
ChartWizard wizard = new ChartWizard();
wizard.ScrollTo(AxesOption);

// Modifying axis properties
wizard.AxisCollection.Add(new Label());
wizard.AxisCollection[0].Font = new Font("Arial", 10);
wizard.AxisCollection[0].Color = Color.Black;

// Applying changes
wizard.Apply();
```

## Page-level Navigation/TOC
1. Chart Wizard Interface Overview
2. Axes Button Selection and Customization
3. Label Editing via Collection Editor Dialog
4. WinForms-specific APIs and Code Examples

## Cross References
- See also:
  - ChartControl API Documentation
  - ChartWizard Class Reference
  - Syncfusion WinForms Chart Control Customization Guide

<!-- tags: [syncfusion, winforms, chartcontrol, chartwizard, axes, labels] keywords: [chart wizard, axes customization, label editor, chart control, winforms, essential chart, user guide] -->
```