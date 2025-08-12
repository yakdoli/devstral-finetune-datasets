```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_039.jpeg
document_name: chart
page_number: 039
page_id: chart#page_039
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:17:33Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- The Chart Wizard interface provides options for controlling the appearance of the ChartControl ToolBar.
- The toolbar selection enables customization of the chart control's interface.
- Individual toolbar items can be edited to customize their image, name, and tooltip.

## Content

The image shown is the Chart Wizard interface, a tool for designing and customizing chart controls within Windows Forms applications. The interface includes various sections for managing the chart's properties.

### Chart Wizard Interface

#### Main Features
- **Auto Run Wizard**: Controls the appearance of the ChartControl ToolBar.
- **ToolBar Options**:
  - **Visible**: Sets the toolbar's visibility.
  - **Back Color**: Adjusts the background color of the toolbar.
  - **Button Style**: Customizes the appearance of individual toolbar buttons.
  - **Button Width**: Defines the width of the buttons.
  - **Button Height**: Defines the height of the buttons.

#### Chart Control Preview
- A sample chart is displayed on the right side, labeled as `chartControl1`.
- The chart includes data bars with values such as 73, 17, and 20.

#### Navigation
- **Apply**: Applies the current changes to the toolbar.
- **Finish**: Completes the wizard process.
- **Cancel**: Cancels any changes made during the wizard.
- **Prev/Next**: Navigates between different sections of the wizard.

#### Editing Items
- **Edit Items**: Invokes an editor for changing the image, name, and tooltip of individual items in the toolbar.

### Figure Description
**Figure 19: ToolBar button selected in ChartWizard**

#### Figure Content
- The toolbar button settings are highlighted, showing options for visibility, background color, and button dimensions.
- The chart display confirms the changes applied to the ChartControl ToolBar.

### Edit Item
- Clicking the **Edit Items** button opens an editor to customize individual toolbar items.
- The editor provides options to:
  - Change the image of the toolbar item.
  - Edit the name of the toolbar item.
  - Modify the tooltip for the toolbar item.

## API Reference (if applicable)
### Chart Control Toolbar Customization
- **Visible**: Configures the visibility of the toolbar.
- **Back Color**: Sets the background color of the toolbar.
- **Button Style**: Customizes toolbar button appearance.
- **Button Width**: Defines the width of toolbar buttons.
- **Button Height**: Defines the height of toolbar buttons.

### Code Examples
- The wizard is used programmatically to apply and finalize customizations:
  ```csharp
  // Example code for customizing the ChartControl ToolBar
  chartControl1.ChartWizardOptions.ToolBarVisible = true;
  chartControl1.ChartWizardOptions.ToolBarBackColor = Color.LightGray;
  chartControl1.ChartWizardOptions.ToolBarButtonWidth = 22;
  chartControl1.ChartWizardOptions.ToolBarButtonHeight = 22;
  ```

## Cross References
- See also: [Tooltip Customization for Toolbar Items](tooltip-customization-for-toolbar-items.md)

## RAG Annotations
<!-- tags: [chart, windows-forms, toolBar, syncfusion] keywords: [chartControl, toolbar customization, visibility, back color, button dimensions, edit items] -->
```