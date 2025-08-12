---
title: "QTP - Syncfusion SDK Documentation"
type: "api-documentation"
framework: "syncfusion"
version: "v11"
processing_mode: "Process Isolation (프로세스 격리)"
extracted_date: "1754726866.473016"
optimized_for: ["llm-training", "rag-retrieval"]
scaling_approach: "3"
---

<!-- 페이지 1 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_001.jpeg
document_name: QTP
page_number: 001
page_id: QTP#page_001
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:01:23Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview
- A professional testing solution for Syncfusion Winforms.
- Version 11.4.0.26 of Essential Studio 2013 Volume 4.
- Comprehensive testing tools tailored for ease of innovation.

## Content

### Introduction to Essential QuickTest Professional

Essential QuickTest Professional is a specialized testing module designed to facilitate robust testing for Syncfusion Winforms applications. This version, part of Essential Studio 2013 Volume 4, provides a suite of tools and features aimed at simplifying the testing process for professional developers.

#### Key Features
- **Automation**: Automate repetitive testing tasks to save time and resources.
- **User-Friendly Interface**: Intuitive and easy-to-navigate interface for efficient testing workflows.
- **Integration**: Seamless integration with Syncfusion Winforms to enhance testing capabilities.
- **Comprehensive Reporting**: Detailed reports to track and analyze test outcomes.

### Getting Started with Essential QuickTest Professional

#### Installation
- **Prerequisites**: Ensure that Syncfusion Winforms is properly installed and configured.
- **Setup**: Follow the provided installation guide to set up Essential QuickTest Professional on your development environment.

#### Basic Workflow
1. **Project Creation**: Create a new test projectspecific to your application needs.
2. **Test Case Design**: Define test cases to cover various functionalities of your application.
3. **Execution**: Run the tests and monitor the progress.
4. **Analysis**: Review the results and conduct necessary debugging.

### Advanced Testing Capabilities

#### Defect Tracking
- **Logging**: Automatically log and track defects for detailed analysis.
- **Integration with third-party defect tracking systems**: Enhance collaboration and streamline workflows.

#### Parametrization
- **Dynamic Testing**: Use parametrized tests to cover multiple scenarios with a single test case.
- **Variables and Parameters**: Flexible management of test variables and parameters for dynamic testing needs.

### Best Practices for Efficient Testing

- **Modular Testing**: Organize tests into modules for better management and execution.
- **Continuous Integration**: Integrate testing into the CI/CD pipeline for automated testing.
- **Performance Optimization**: Use optimization techniques to improve test execution speed and efficiency.

## API Reference

### Namespaces and Classes
- **Syncfusion.Testing.QuickTest**: Contains the core classes and functionalities for Essential QuickTest Professional.
- **Syncfusion.Testing.QuickTest.Controls**: Provides additional controls and utilities for testing Syncfusion Winforms applications.

#### Methods and Properties
- **RunTest()**: Executes the defined test cases.
- **LogResult()**: Records test results and logs for analysis.
- **SetParameters()**: Configures parameters for dynamic testing.

## Code Examples

### Example 1: Basic Test Setup

```csharp
using Syncfusion.Testing.QuickTest;

// Initialize QuickTest Professional
var tester = new QuickTestEngine();

// Define a new test project
var project = tester.CreateProject("MyApplicationTests");

// Add a test case
var testCase = project.CreateTestCase("BasicFunctionalityTest");
testCase.AddParameter("TestType", "Functional");

// Execute the test
testCase.Run();

// Analyze the results
var report = tester.GenerateReport();
Console.WriteLine(report);
```

### Example 2: Parametrized Testing

```csharp
using Syncfusion.Testing.QuickTest;

// Set up parametrized test case
var parametricTestCase = project.CreateTestCase("ParametrizedTest");
parametricTestCase.AddParameter("TestData", "DataSample1");
parametricTestCase.AddParameter("TestData", "DataSample2");

// Run test cases with parameters
parametricTestCase.Run();

// Analyze results for each data set
var parametricReport = tester.GenerateReport();
Console.WriteLine(parametricReport);
```

## Page-level Navigation/TOC (if applicable)

- [Overview]
  - Key Features
- [Content]
  - Introduction to Essential QuickTest Professional
  - Getting Started with Essential QuickTest Professional
  - Advanced Testing Capabilities
  - Best Practices for Efficient Testing
- [API Reference]
  - Namespaces and Classes
  - Methods and Properties
- [Code Examples]
  - Example 1: Basic Test Setup
  - Example 2: Parametrized Testing

## Cross References

- See also: [Syncfusion Winforms Documentation](https://www.syncfusion.com/documentation/windowsforms)
- See also: [Essential Studio Testing Framework](https://www.syncfusion.com/products/essentialstudio/testing)

## RAG Annotations

<!-- tags: [Syncfusion Winforms, Essential QuickTest Professional, testing, automation, version 11.4.0.26] keywords: [testing, automation, Essential Studio, Syncfusion, toolkits, testing tools, documentation] -->
```

---

<!-- 페이지 2 -->

```html
```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_005.jpeg
document_name: QTP
page_number: 005
page_id: QTP#page_005
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:01:52Z
fidelity: lossless
-->
# Essential QuickTest Professional

Essential QuickTest Professional comes with numerous samples as well as extensive documentation to guide you step-by-step. This user guide provides detailed information on the features and functionalities of Essential QuickTest Professional and is organized in the following order:

## Install and Configuration of Essential QuickTest Professional
This section provides details about installing and configuring Essential QuickTest Professional, which is mandatory before you start using the add-on.

## Samples and Locations
This section provides the location of the installed samples, source code location, and the location of the assemblies for the source.

## Licensing, Patches and Uninstallation
This section covers information on licensing and patches. It also covers the uninstallation process.

## Assembly information
This section provides details about the assembly name, type name, and control type in table format. This table is used to write the swfconfig file.

## Frequently Asked Questions
This section comprises an assembled list of questions and answers to provide expert solutions on the product and its usage for every control that is supported.

## Known Issues
This section lists existing issues with the product that have not yet been solved.

## Supported Controls
Essential QuickTest Professional supports only certain methods exclusive to each control. This section lists these controls and their methods.

### 1.2 Prerequisites and Compatibility
This section covers the requirements that are mandatory for installing Essential Test Studio. It also lists the operating systems and browsers that are compatible with the product.

#### Prerequisites
The following are the prerequisites:

| Testing Environments | Requirements |
|----------------------|--------------|
| 1) QuickTest Professional version 9.5 and above | |
| 2) QuickTest Professional .NET add-in | |

<!-- tags: [product, Essential QuickTest Professional, Install and Configuration, Samples and Locations, Licensing, Patches and Uninstallation, Assembly information, Frequently Asked Questions, Known Issues, Supported Controls, Prerequisites and Compatibility, Testing Environments, requirements] keywords: [installation, configuration, samples, licensing, patches, assembly, questions, issues, controls, prerequisites, compatibility] -->
```
```

---

<!-- 페이지 3 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_009.jpeg
document_name: QTP
page_number: 009
page_id: QTP#page_009
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:02:06Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview
- Installation guide for Syncfusion Essential QTP 11.1.0.21.
- Focus on setting up Essential QTP 2013 Vol. 1.

## Content

### Installation Wizard

#### Figure: Select Destination Location
![Figure: Select Destination Location](description)

This figure illustrates the welcome screen for the Syncfusion Essential QTP installation. The setup interface includes the following elements:

- **Title**: "Welcome to Syncfusion Essential QTP 2013 Vol. 1 Setup"
- **Message**: "Thank you for the information provided. Authorized features have been unlocked. The Setup Wizard has the information needed to proceed with installation."
- **Buttons**:
  - `Back`
  - `Next`
  - `Cancel`

The interface is designed to guide the user through the installation process after providing the required information.

#### Step-by-Step Installation Guide

5. Click **Next**. The Select the installation folder window opens.

## Copyright Information

© 2013 Syncfusion. All rights reserved.

<!-- tags: [syncfusion, winforms, essential qtp, installation, setup] keywords: [syncfusion, winforms, essential qtp, installation process, setup wizard, authorized features] -->
```

---

<!-- 페이지 4 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_013.jpeg
document_name: QTP
page_number: 013
page_id: QTP#page_013
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:02:16Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview
- Installing Syncfusion Essential QTP Add-on
- Step-by-step guide to installing the add-on
- Completion confirmation after installation

## Content

### Installing Essential QTP

The following screenshot depicts the installation process of the Syncfusion Essential QTP Add-on.

**Figure 7: Installing Screen**

![Figure 7: Installing Screen](https://i.imgur.com/os5Wylh.png)

- **Window Title Bar:** "Syncfusion Essential QTP 11.1.0.21 Setup"
- **Installation Message:** "Please wait while the setup installs Essential QTP Add-on."
- **Status Bar:** Displayed as "Copying new files," indicating the progress of the installation.
- **Progress Bar:** Shows the current status of the file copying process.
- **Buttons:** Includes options to **Back**, **Next**, and **Cancel** for user interaction.
- **Footer:** "Syncfusion Inc," confirming the source of the add-on.

The following screen is displayed once the installation is completed.

## Cross References
- See also: [Unclear - further reference or next steps not specified in the content.]

<!-- tags: Syncfusion, Winforms, QuickTest Professional, Installation, Add-on, QTP, Syncfusion Inc. keywords: installation process, Syncfusion Essential QTP Add-on, progress bar, installation completion -->
```

---

<!-- 페이지 5 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_017.jpeg
document_name: QTP
page_number: 017
page_id: QTP#page_017
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:02:26Z
fidelity: lossless
-->

## Essential QuickTest Professional

### Content

```xml
<Controls>
    <CustomRecord>
        <Component>
            <DllName>C:\Program files\Syncfusion\Essential TestStudio\&lt;Version Number&gt;\Bin\2.0\GridControl.dll</DllName>
            <TypeName>Syncfusion.TestStudio.Grid.GridControl</TypeName>
            </Component>
    </CustomRecord>
    <CustomReplay>
        <Component>
            <Context>AUT</Context>
            <DllName>C:\Program files\Syncfusion\Essential TestStudio\&lt;Version number&gt;\Bin\2.0\GridControl.dll</DllName>
            <TypeName>Syncfusion.TestStudio.Grid.GridControl</TypeName>
            </Component>
        </CustomReplay>
    </Control>
    .........
</Controls>
```

**Note:** Ensure that the element `<DllName>` contains the correct path to the corresponding DLL.

7. Save the SwfConfig.xml file.

8. Restart QTP once the SwfConfig.xml file is saved to refresh the mappings to the required controls, before starting the test.

**Note:** Mapping for the required controls can be done in a similar manner.

### 2.2 Sample and Location

This section contains the location of the samples, source code, and assemblies.

#### Samples Location

The samples for Essential QuickTest Professional are available at the following locations:

- Grid samples- (installed location of the product)\Examples\Samples\Grid\
- Tools samples- (installed location of the product)\Examples\Samples\Tools\
- Chart samples- (installed location of the product)\Examples\Samples\Chart\
- Schedule samples- (installed location of the product)\Examples\Samples\Schedule\
- Diagram samples- (installed location of the product)\Examples\Samples\Diagram\

**Note:** By default, the installed location of the product corresponds to `<Drive>:\Program Files\Syncfusion\Essential QuickTest Professional\<version number>\`.

The executable files for the samples are available under the following location:

## API Reference

### Code Examples

The executable files for the samples are available under the following location:

<!-- tags: [Essential QuickTest Professional, Samples, Location, Mapping, DLL, SwfConfig.xml, QTP, version: 11.4.0.26] keywords: [Essential QuickTest Professional, Grid samples, Tools samples, Chart samples, Schedule samples, Diagram samples, executable files, installed location, SwfConfig.xml, DLL mappings, QTP] -->
```html


---

<!-- 페이지 6 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_021.jpeg
document_name: QTP
page_number: 021
page_id: QTP#page_021
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:02:41Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview
- This page provides information on how to test Syncfusion controls using Essential QuickTest Professional for testing.
- It lists the required assembly, type, and control name for testing various Syncfusion controls, including Essential Chart, Essential Schedule, and Essential Diagram.

## Content

### For Essential Chart

| Assembly Name         | Type Name                               | Control Name                             |
|-----------------------|-----------------------------------------|------------------------------------------|
| ChartControl.dll     | Syncfusion.TestStudio.Chart.ChartControl | Syncfusion.Windows.Forms.Chart.ChartControl |

### For Essential Schedule

| Assembly Name         | Type Name                               | Control Name                             |
|-----------------------|-----------------------------------------|------------------------------------------|
| ScheduleControl.dll   | Syncfusion.TestStudio.Schedule.ScheduleControl | Syncfusion.Windows.Forms.Schedule.ScheduleControl |

### For Essential Diagram

| Assembly Name    | Type Name                          | Control Name                        |
|------------------|------------------------------------|-------------------------------------|
| Diagram.dll      | Syncfusion.TestStudio.Diagram.Diagram | Syncfusion.Windows.Forms.Diagram.Controls.Diagram |

## API Reference

### WinForms-specific conventions
- The control names and types provided are specific to the Syncfusion WinForms library and are used for integration with Essential QuickTest Professional.

## Code Examples

None provided in the document snippet.

## Cross References

- For more detailed configurations and usage examples, refer to the official Syncfusion documentation.

## RAG Annotations

<!-- tags: [product, module, control, api, version?] keywords: [Syncfusion, WinForms, QuickTest Professional, Testing, ChartControl, ScheduleControl, DiagramControl, Control Name, Type Name, Assembly Name] -->
```

---

<!-- 페이지 7 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_025.jpeg
document_name: QTP 
page_number: 025
page_id: QTP#page_025
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:02:53Z
fidelity: lossless
-->
# Essential QuickTest Professional

---

## Overview
- Demonstrates the interface of QuickTest Professional.
- Focuses on the usage of the "Record" tool within the software.
- Illustrates the layout and tools available in the "Test*" window.

---

## Content

### Screenshot of QuickTest Professional Interface

The figure below shows the QuickTest Professional interface, specifically highlighting the "Record" tool within the "[Test*]" window.

#### Interface Details
- **Menu Bar:** Various menu options such as "File," "Edit," "View," "Insert," "Automation," "Resources," "Debug," "Tools," "Window," and "Help."
- **Toolbar:** Contains several icons and tools for various functionalities, including "Run," "Record," and other test-related actions.
- **Test Pane:** Displays the "Test Flow" for the current test being edited.
- **Editor Area:** Shows the "Test" page and current action details within "Action1."
- **Data Table:** A table for variables, parameters, and other data-related operations.

#### Figure Description
The figure below depicts the QuickTest Professional interface, highlighting the various components and tools available within the "[Test*]" window when using the "Record" tool.

![QuickTest Professional Interface](#)
*Figure 12: QuickTest Professional – [Test*] Window showing Record tool.*

---

### Explanation of Key Components
1. **Menu Bar:**
   - Provides access to various functions and settings within the software.
   - Includes options for file management, editing, viewing, inserting, automating, and debugging tests.

2. **Toolbar:**
   - Offers quick access to frequently used tools and actions, such as starting or stopping recording, running tests, and debugging.

3. **Test Pane:**
   - Displays the hierarchical structure of the test being built or edited.
   - Shows "Action1," indicating the first action within the test.

4. **Editor Area:**
   - The main area where the test steps are recorded and edited.
   - Displays the current action being recorded or modified.

5. **Data Table:**
   - Used to manage variables and parameters for the test.
   - Contains columns labeled from A to L and rows for data entry.

---

### Usage of the "Record" Tool
The "Record" tool allows users to perform actions within the application being tested and have those actions recorded automatically within the QuickTest Professional interface. This facilitates the creation of automated test scripts without manually typing or modifying code.

---

## Cross References
- Refer to the QuickTest Professional User Guide for detailed instructions on using the "Record" tool.
- Additional documentation on test execution and debugging can be found in related sections of the guide.

---

<!-- tags: [syncfusion, winforms, quicktest-professional, test-tool, record-tool] keywords: [quicktest professional, record tool, menu bar, toolbar, test pane, editor area, data table, test interface] -->
```

---

<!-- 페이지 8 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_029.jpeg
document_name: QTP
page_number: 029
page_id: QTP#page_029
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:03:12Z
fidelity: lossless
-->

## Essential QuickTest Professional

### Overview
- Introduction to recording and running test settings for Windows-based applications.
- Configuring the recording environment to include specific applications.
- Starting the recording process and opening the application specified in the path.

### Content

#### Figure 16: Record and Run Settings with the Application Location

![Record and Run Settings Dialog](https://via.placeholder.com/300x300?text=Figure+16)

**Description**:
The "Record and Run Settings" dialog shows various options for configuring how tests are recorded and run. The settings allow users to:
- Record and run tests on any open Windows-based application.
- Record and run tests on specific applications opened by QuickTest or via the Desktop shell.
- Record and run tests on applications specified in the list below the dialog.

To proceed:
1. Click **OK** to confirm the settings and start the recording process.

**Note**: The recording starts. The application in the given path is opened as shown below.

### Page-level Navigation/TOC (if applicable)
- Essential QuickTest Professional
  - Overview
  - Content
    - Figure 16: Record and Run Settings with the Application Location
    - Description
    - Steps to proceed

### Cross References
See also: [Application Details Configuration], [Recording Test Basics], [QuickTest Professional Overview]

## RAG Annotations
<!-- tags: test automation, application settings, recording, Windows applications, QuickTest Professional keywords: record and run, application location, path configuration, test settings -->
```

---

<!-- 페이지 9 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_033.jpeg
document_name: QTP
page_number: 033
page_id: QTP#page_033
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:03:23Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview
- Describes the low-level recording feature of QTP.
- Explains how to stop the recording and refers to creating and recording tests.
- Provides steps for running a test using the Syncfusion namespace.

## Content

### Summary of Low-Level Recording
- Low-level recording is the default recording method when the Configuring Essential QuickTest Professional section steps are not followed.
- Recording can be stopped by clicking the Stop button in the toolbar.

#### Completing the Test Creation and Recording
- The process of creating and recording the test is completed.

### 3.2 Running a Test

#### Running the Test
On recording, all user actions are noted with the corresponding method names of the Syncfusion namespace. Errors can be checked while running a test. To run a test, follow these steps:

1. Click **Run** in the toolbar.
   - The **Run** dialog box is displayed. The **Results Location** tab is highlighted by default.

   ![Run Dialog](Run_Dialog "Run Dialog")
   **Figure 19: Run Dialog**

In the **Results Location** tab, two options are provided:
- **New run results folder**: Allows the results of the test to be written to the specified location.
- **Temporary run results folder (overwrites any existing temporary results)**: Allows the results to be stored in the temporary location.

2. Click the required option.

## API Reference (if applicable)
- None provided in this section.

## Code Examples (multi-language supported)
- None provided in this section.

## Page-level Navigation/TOC (if applicable)
- None provided in this section.

## Cross References
- See also: Configuring Essential QuickTest Professional, Syncfusion namespace, test execution.

<!-- tags: [product, module, control, api, version?] keywords: [low-level recording, QTP, test recording, running a test, Syncfusion namespace, results location, test execution, QTP#page_033] -->
```

---

<!-- 페이지 10 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_037.jpeg
document_name: QTP
page_number: 037
page_id: QTP#page_037
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:03:36Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview
- The Keyword view is designed for users who are not experts in VB scripts.
- It provides a table-format summary of controls, user actions, operation values, and documentation.
- The controls used are listed in a tree-view format under the Item header.

## Content

### Keyword View

#### Overview of Keyword View
The Keyword view is meant for persons who are not experts in VB scripts. Keyword view contains the controls used, the user-actions or operations performed, values involved in the operation, and the documentation summary in a table format. The controls used are listed under the Item header in a tree-view format as shown below.

#### Visual Representation of Keyword View
![Keyword View](image_url_to_Figure_23)

Figure 23: Keyword View

#### Editing the Test in Keyword View
To edit the test in Keyword view, you can perform any of the following actions:

1. You can right-click any of the items listed under the Item header and choose one of the options available in the displayed menu as shown below.

## RAG Annotations
<!-- tags: [syncfusion-sdk, QTP, keyword-view, controls, operations, documentation] keywords: [Keyword view, VB scripts, User actions, Values, Documentation summary, tree-view format, editing, right-click menu] -->
```

---

<!-- 페이지 11 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_041.jpeg
document_name: QTP
page_number: 041
page_id: QTP#page_041
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:03:47Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview
- Steps to open saved tests using the Open Test dialog.
- Details on displaying the saved test name and path upon opening.

## Content

### Opening a Saved Test

#### Note:
The Open Test dialog box is displayed with a list of saved tests.

**Figure 27: Open Test Dialog**

![Open Test Dialog](https://i.imgur.com/figure27.png)

**Steps:**
1. The Open Test dialog box is displayed with a list of saved tests.
   - **Look in:** ishekmumsl.Documents/Hp/QuickTest Professional/Tests
   - **File name:** A file browser view is displayed showing Test 1.
   - **Files of type:** QuickTest Tests

2. Select the required test and click Open.

#### Note:
The saved test is opened with its name and the complete path as the name of the window. By default, Expert View of the Test is opened.

The following image shows the mouse pointer pointing towards the path and file displayed as the window name.

## API Reference
- **Open Test Dialog:** Displays a list of saved tests.
- **Expert View:** Opens the test in a detailed mode for editing.

## Code Examples
```csharp
// Example of opening a test file
void OpenTest()
{
    string filePath = @"C:\ishkumar\Documents\HP\QuickTest Professional\Tests\Test1";
    if (System.IO.File.Exists(filePath))
    {
        // Open the test file
        OpenTestDialog(filePath);
    }
    else
    {
        MessageBox.Show("The specified test file does not exist.");
    }
}
```

## Cross References
See also: "Working with Test Files" for more information on test file management.

<!-- tags: [QuickTest Professional, Open Test, Test Files, Expert View, Windows Forms] keywords: [Test Management, UI Testing, Test Automation, UI Test Framework, File Operations] -->
```

---

<!-- 페이지 12 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_045.jpeg
document_name: QTP
page_number: 045
page_id: QTP#page_045
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:04:02Z
fidelity: lossless
-->

## Content

Here is the extracted content from the image:

### Grid Control Methods

| Method | Description |
|---|---|
| RemoveRow(int from, int to) | Removes a range of rows specified for the Grid control. |
| ScrollToCell(int rowIndex, int colIndex) | Scrolls the grid so that the cell will be visible for replay. |
| HideRow(int from, int to) | Hides a range of rows specified for the Grid control. |
| ShowHiddenRow(int from, int to) | Shows a range of rows specified for the Grid control, which were hiding. |
| HideCol(int from, int to) | Hides a range of columns specified for the Grid control. |
| ShowHiddenCol(int from, int to) | Shows a range of columns specified for the Grid control. |
| int GetSelectedRowIndex() | Returns the top row index of the selected row. |
| GetSelectedColIndex() | Returns the column index of the selected column. |
| Color GetCellBackColor(int row, int col) | Gets the back color of the cell. |
| string GetName() | Gets the name of the Grid control object. |

### GridDataBoundGrid Methods

| Method | Description |
|---|---|
| CellButtonClick(int row, int col) | Raises the click on the cell button. |
| CellDoubleClick(int row, int col) | Raises the cell double-click. |
| CollapseRow(int rowIndex) | Collapses the row for the specified row index. |
| DeleteRow(int from, int to) | Deletes the specified rows. |
| ExpandRow(int rowIndex) | Expands the Row for the specified row index. |
| MouseDown(int row, int col, string button) | Raises a click in the grid. |
| MoveColumn(int fromColumn, int count, int target) | Moves a range of columns. |
|  | |

## API Reference

### Grid Control

- **RemoveRow(int from, int to)**: Removes a range of rows specified for the Grid control.
- **ScrollToCell(int rowIndex, int colIndex)**: Scrolls the grid so that the cell will be visible for replay.
- **HideRow(int from, int to)**: Hides a range of rows specified for the Grid control.
- **ShowHiddenRow(int from, int to)**: Shows a range of rows specified for the Grid control, which were hiding.
- **HideCol(int from, int to)**: Hides a range of columns specified for the Grid control.
- **ShowHiddenCol(int from, int to)**: Shows a range of columns specified for the Grid control.
- **int GetSelectedRowIndex()**: Returns the top row index of the selected row.
- **GetSelectedColIndex()**: Returns the column index of the selected column.
- **Color GetCellBackColor(int row, int col)**: Gets the back color of the cell.
- **string GetName()**: Gets the name of the Grid control object.

### GridDataBoundGrid

- **CellButtonClick(int row, int col)**: Raises the click on the cell button.
- **CellDoubleClick(int row, int col)**: Raises the cell double-click.
- **CollapseRow(int rowIndex)**: Collapses the row for the specified row index.
- **DeleteRow(int from, int to)**: Deletes the specified rows.
- **ExpandRow(int rowIndex)**: Expands the Row for the specified row index.
- **MouseDown(int row, int col, string button)**: Raises a click in the grid.
- **MoveColumn(int fromColumn, int count, int target)**: Moves a range of columns.

## Code Examples

No code examples are provided in the image.

<!-- tags: [Grid control, GridDataBoundGrid, methods, syncfusion winforms] keywords: [RemoveRow, ScrollToCell, HideRow, ShowHiddenRow, HideCol, ShowHiddenCol, GetSelectedRowIndex, GetSelectedColIndex, GetCellBackColor, GetName, CellButtonClick, CellDoubleClick, CollapseRow, DeleteRow, ExpandRow, MouseDown, MoveColumn] -->
```

---

<!-- 페이지 13 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_049.jpeg
document_name: QTP
page_number: 049
page_id: QTP#page_049
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:04:23Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview
- Overview of various methods and properties related to grid controls.
- Functions to manipulate and query grid rows, columns, and ranges.
- Includes methods for resizing, selecting, grouping, and determining column and row states.

## Content

### Grid Control Methods

The following table lists the methods and their descriptions for grid controls:

| Method Name | Description |
|-------------|-------------|
| GetSelectedRowIndex() | Returns the top row index of the selected row. |
| GetSelectedRowRange() | Returns the Top and Bottom row of the selected row range. |
| GetTableName(object row) | Obtains the table name for a given Row. |
| GetTableNameByLevel(int level) | Gets the level of the table for the given table name. |
| GroupBy(string tablename, string column, string status) | Defines grouping and ungrouping of specified columns. |
| MouseDown(object row, object col, string button) | Raises the MouseDown. |
| MouseDownOnRowHeader(int row, int col, string button) | Raises the MouseDown on the RowHeader. |
| MoveColumn(string tablename, object fromColumn, object count, object target) | Moves a range of columns. |
| IsColSorted(int col) | Determines whether the column is sorted. |
| IsGroupExpanded(object row) | Determines whether the specified group is expanded. |
| IsGroupRow(object row) | Determines whether the specified row is a caption row or caption section. |
| IsRecord(object record) | Determines whether the specified row is a record. |
| IsRecordExpanded(object record) | Determines whether the specified record is expanded. |
| ResizeColumn(string tablename, int fromColumn, int to, int width) | Resizes the specified column. |
| ResizeRow(string tablename, int fromRow, int to, int height) | Resizes the specified rows. |
| SelectRange(string range, int top, int left, int bottom, int right) | Selects the range. |
| SelectRecord(object row, string status) | Selects a record for the GridGroupingControl. |

## API Reference

### Methods

#### GetSelectedRowIndex()
- **Returns**: The top row index of the selected row.

#### GetSelectedRowRange()
- **Returns**: The Top and Bottom row of the selected row range.

#### GetTableName(object row)
- **Parameters**:
  - `object row`: The row object for which the table name is obtained.
- **Returns**: The table name for the given Row.

#### GetTableNameByLevel(int level)
- **Parameters**:
  - `int level`: The level for which the table name is obtained.
- **Returns**: The level of the table for the given table name.

#### GroupBy(string tablename, string column, string status)
- **Parameters**:
  - `string tablename`: The name of the table to group.
  - `string column`: The column to group by.
  - `string status`: The status indicating grouping or ungrouping.
- **Description**: Defines grouping and ungrouping of specified columns.

#### MouseDown(object row, object col, string button)
- **Parameters**:
  - `object row`: The row object for the MouseDown event.
  - `object col`: The column object for the MouseDown event.
  - `string button`: The button type for the MouseDown event.
- **Description**: Raises the MouseDown event.

#### MouseDownOnRowHeader(int row, int col, string button)
- **Parameters**:
  - `int row`: The row number for the MouseDown event.
  - `int col`: The column number for the MouseDown event.
  - `string button`: The button type for the MouseDown event.
- **Description**: Raises the MouseDown event on the RowHeader.

#### MoveColumn(string tablename, object fromColumn, object count, object target)
- **Parameters**:
  - `string tablename`: The name of the table.
  - `object fromColumn`: The starting column to move.
  - `object count`: The number of columns to move.
  - `object target`: The target position for the moved columns.
- **Description**: Moves a range of columns.

#### IsColSorted(int col)
- **Parameters**:
  - `int col`: The column index to check.
- **Returns**: A boolean indicating whether the column is sorted.

#### IsGroupExpanded(object row)
- **Parameters**:
  - `object row`: The row object to check.
- **Returns**: A boolean indicating whether the specified group is expanded.

#### IsGroupRow(object row)
- **Parameters**:
  - `object row`: The row object to check.
- **Returns**: A boolean indicating whether the specified row is a caption row or caption section.

#### IsRecord(object record)
- **Parameters**:
  - `object record`: The record object to check.
- **Returns**: A boolean indicating whether the specified row is a record.

#### IsRecordExpanded(object record)
- **Parameters**:
  - `object record`: The record object to check.
- **Returns**: A boolean indicating whether the specified record is expanded.

#### ResizeColumn(string tablename, int fromColumn, int to, int width)
- **Parameters**:
  - `string tablename`: The name of the table.
  - `int fromColumn`: The starting column to resize.
  - `int to`: The ending column to resize.
  - `int width`: The new width for the columns.
- **Description**: Resizes the specified column.

#### ResizeRow(string tablename, int fromRow, int to, int height)
- **Parameters**:
  - `string tablename`: The name of the table.
  - `int fromRow`: The starting row to resize.
  - `int to`: The ending row to resize.
  - `int height`: The new height for the rows.
- **Description**: Resizes the specified rows.

#### SelectRange(string range, int top, int left, int bottom, int right)
- **Parameters**:
  - `string range`: The name of the range to select.
  - `int top`: The top boundary of the range.
  - `int left`: The left boundary of the range.
  - `int bottom`: The bottom boundary of the range.
  - `int right`: The right boundary of the range.
- **Description**: Selects the specified range.

#### SelectRecord(object row, string status)
- **Parameters**:
  - `object row`: The row object to select.
  - `string status`: The status for the GridGroupingControl.
- **Description**: Selects a record for the GridGroupingControl.

## Cross References
- See also: GridGroupingControl, Table operations, Row and Column manipulation.

<!-- tags: [Grid, Grouping, Control, Table, Row, Column, Select, Resize, MouseDown, GroupBy, Range, Record, Expand] keywords: [GridGroupingControl, table, row, column, select, resize, groupby, range, record, expand, collapse] -->
```

---

<!-- 페이지 14 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_053.jpeg
document_name: QTP
page_number: 053
page_id: QTP#page_053
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:04:59Z
fidelity: lossless
-->

## Overview
- Provides details on the methods and descriptions for various UI components in Syncfusion WinForms.
- Covers DropDown(), Select(), SetDockState(), SetFloatState(), and other methods relevant to UI controls.
- Includes examples for CommandBar, DataListView, and DateTimePickerAdv controls.

## Content

### Control Methods
This section outlines the methods and their corresponding usage for different controls in the Syncfusion WinForms framework.

#### DropDown
| Method | Description |
|--------|-------------|
| `DropDown()` | Shows the drop-down list. |

#### ComboDropDown
| Method | Description |
|--------|-------------|
| `DropDown()` | Shows the drop-down list. |
| `Select(object item)` | Selects the item in the list. |

#### CommandBar
| Method | Description |
|--------|-------------|
| `DropDown()` | Shows the drop-down list. |
| `SetDockState(string dockState)` | Changes the dock state. |
| `SetFloatState(int x, int y)` | Sets the CommandBar to float. |

#### DataListView
| Method | Description |
|--------|-------------|
| `Select(string item)` | Selects the specified item. |
| `Return()` | Performs click on the focused item. |

#### DateTimePickerAdv
| Method | Description |
|--------|-------------|
| `void CheckEnabled(object on, string checkState);` | Interface to check the enabled state of the DateTimePickerAdv. |
| `void ChangeValue(object on, string dateTime);` | Interface to change the value of the DateTimePickerAdv. |

---

## API Reference

### DateTimePickerAdv Methods
- **`void CheckEnabled(object on, string checkState);`**
  - **Description:** Interface to check the enabled state of the DateTimePickerAdv.
- **`void ChangeValue(object on, string dateTime);`**
  - **Description:** Interface to change the value of the DateTimePickerAdv.

---

<!-- tags: [syncfusion, winforms, controls, commandbar, dataview, datetimepickeradv, methods] keywords: [dropdown, select, floatstate, dockstate, interface, enabledstate, changevalue] -->
```

---

<!-- 페이지 15 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_057.jpeg
document_name: QTP
page_number: 057
page_id: QTP#page_057
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:05:13Z
fidelity: lossless
-->

## Content

### TabPageAdv Methods

| Method               | Description                                                |
|----------------------|------------------------------------------------------------|
| SelectPage(object tab) | Selects the tab page in the TabPageAdv control.        |
| RightClick(object tab) | Performs a rightclick on the tab page in the TabPageAdv control. |
| ClosePage(object tab) | Closes the tab page in the TabPageAdv control.          |

### XPTaskBar

| Method                | Description                                               |
|-----------------------|-----------------------------------------------------------|
| Expand(string headerText) | Expands the content area of the task bar box.        |
| Collapse(string headerText) | Collapses the content area of the task bar box.     |
| ItemClick(string headerText, string itemText) | Performs click on the item described in the tag. |

### Helper Functions

| Method                                           | Description                                                                 |
|--------------------------------------------------|-----------------------------------------------------------------------------|
| string GetTag(int itemIndex)                    | Retrieves the tag information for the given item index.                    |
| string GetHeaderText()                          | Retrieves the group or header text of the task bar box being called.        |
| string GetItemText(int itemIndex)               | Retrieves the item text for the given item index from the task bar box called |
| int GetTaskBarBoxCount()                       | Gets the number of task bar boxes in the XPTaskBar.                          |
| int GetExpandedTaskBarBoxCount()                | Gets the number of expanded task bar boxes.                                 |
| int GetCollapsedTaskBarBoxCount()              | Gets the number of collapsed task bar boxes.                                |
| bool FindItem(string itemText, out string headerText, out int itemIndex); | Helps to find an item's existence.                                       |

### TextBoxExt

## API Reference

### Methods

#### Expand(string headerText)
- **Description**: Expands the content area of the task bar box.

#### Collapse(string headerText)
- **Description**: Collapses the content area of the task bar box.

#### ItemClick(string headerText, string itemText)
- **Description**: Performs click on the item described in the tag.

#### string GetTag(int itemIndex)
- **Description**: Retrieves the tag information for the given item index.

#### string GetHeaderText()
- **Description**: Retrieves the group or header text of the task bar box being called.

#### string GetItemText(int itemIndex)
- **Description**: Retrieves the item text for the given item index from the task bar box called.

#### int GetTaskBarBoxCount()
- **Description**: Gets the number of task bar boxes in the XPTaskBar.

#### int GetExpandedTaskBarBoxCount()
- **Description**: Gets the number of expanded task bar boxes.

#### int GetCollapsedTaskBarBoxCount()
- **Description**: Gets the number of collapsed task bar boxes.

#### bool FindItem(string itemText, out string headerText, out int itemIndex)
- **Description**: Helps to find an item's existence.

## Code Examples

### C# Example: Expanding a Task Bar Box

```csharp
// Example code to expand a task bar box
xptaskBar.Expand("Header Text");
```

### C# Example: Collapsing a Task Bar Box

```csharp
// Example code to collapse a task bar box
xptaskBar.Collapse("Header Text");
```

### C# Example: Clicking an Item in a Task Bar Box

```csharp
// Example code to click an item in a task bar box
xptaskBar.ItemClick("Header Text", "Item Text");
```

## Page-level Navigation/TOC

- **TabPageAdv Methods**
- **XPTaskBar**
- **Helper Functions**
- **TextBoxExt**

## Cross References

- Related controls and features in Syncfusion Winforms.
- Additional functionality descriptions and examples can be found in the main documentation.

<!-- tags: [Syncfusion Winforms, TabPageAdv, XPTaskBar, Helper Functions, TextBoxExt] keywords: [TabPageAdv, XPTaskBar, GetTag, GetHeaderText, GetItemText, Expand, Collapse, ItemClick, ToolBarBox, FindItem] -->
```

---

<!-- 페이지 16 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_061.jpeg
document_name: QTP
page_number: 061
page_id: QTP#page_061
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:05:36Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview
- Lists methods and descriptions for interacting with various user interface controls such as `SelectSecondaryTab`, `TrackBarEx`, `RangeSlider`, `NavigationView`, and `TabBarSplitterControl`.
- Provides a concise explanation for each method and its usage in the context of Essential QuickTest Professional.

## Content

### SelectSecondaryTab
| Method                       | Description                                      |
|------------------------------|--------------------------------------------------|
| `SelectSecondaryTab(int index)` | Selects the secondary tab page based on the given index. |

### TrackBarEx
#### Methods and Descriptions
| Method               | Description          |
|----------------------|----------------------|
| `SetValue(int value)` | Sets the value.     |

### RangeSlider
#### Methods and Descriptions
| Method               | Description          |
|----------------------|----------------------|
| `SetValue(int min, int max)` | Sets the values. |

### NavigationView
#### Methods and Descriptions
| Method               | Description                                      |
|----------------------|--------------------------------------------------|
| `Select(int x, int y)` | Clicks the specified x and y value.          |
| `ActivateBar(string barName)` | Selects the bar based on the given name. |

### TabBarSplitterControl
#### Methods and Descriptions
| Method                       | Description                                      |
|------------------------------|--------------------------------------------------|
| `Select(string tab)`         | The name of the selected tab.                   |
| `SetSplitterPosition(string tab, int vSplit, int hSplit)` | The splitter position in the tab bar page. |
| `string GetTabName(int index)` | The label in the tab page can be found by passing the index. |

## 4.3 Essential Chart
The following are the recorded methods and their corresponding descriptions for Essential Chart:

<!-- tags: [syncfusion, Essential QuickTest Professional, Essential Chart, user interface controls, version 11.4.0.26] keywords: [SelectSecondaryTab, TrackBarEx, RangeSlider, NavigationView, TabBarSplitterControl, methods, descriptions, user interface, chart] -->
```

---

<!-- 페이지 17 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_065.jpeg
document_name: QTP
page_number: 065
page_id: QTP#page_065
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:05:50Z
fidelity: lossless
-->

## 5 Known Issues

The following are the known issues in various platforms that are yet to be solved.

### 5.1 General

Documentation column is not supported in the Keyword View.

### 5.2 Essential Grid

Grid does not support drop-down controls such as Combo box, Grid List control, and so on.

### 5.3 Essential Tools

The following are the list of tools with their respective known issues:

#### Group Bar

When the Stacked Mode is set to true, the NavigationPanelButtonClick is not recorded.

#### GroupView

When the button view is set to false, the drag-and-drop, or re-ordering, of the GroupView item is not recorded. On clicking the re-ordered item, the index is recorded correctly.

#### DateTimePickerAdv

1. The events on the header panel that are inside the pop-up window cannot be replayed. The SetCurrentCell and ResizeRow events of the Syncfusion.QuickTestProfessional.Grid that are associated with the Calendar are triggered by the pop-up window. These events are recorded, but cannot be played back in the replay. While replaying, they should be manually removed.
   
2. Once the calendar events are handled, the replay works slower. This is because of the 'for each' loop in the replay, which enables you to trace all the controls that are inside the pop-up window and then show or hide them as you need.
```

---

<!-- 페이지 18 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_069.jpeg
document_name: QTP
page_number: 069
page_id: QTP#page_069
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:06:01Z
fidelity: lossless
-->

## Overview
- Configuring Syncfusion assemblies with QTP (QuickTest Professional).
- Steps to replace the SwfConfig.xml file in HP QTP.
- Verifying and saving the new configuration for Syncfusion assembly integration.

## Content

### Essential QTP Configurator
When setting up the configuration for Syncfusion assemblies in QTP, the Essential QTP Configurator provides a visual interface for specifying the QTP Assemblies Location and Product Version. This tool assists in configuring the swfconfig.xml file, which dictates the integration of Syncfusion components with QTP.

#### Section: Configuring Syncfusion Assemblies
The **Configure SwfConfig File** interface allows users to:
- **QTP Assemblies Location**: Specify the directory containing the necessary libraries, such as `Files (x86)\Syncfusion\Essential QTP\10.4.0.53\bin\3.5`.
- **Product Version**: Enter the version of the product (10.403.0.53 in this example).
- After entering the required details, users can click the **Check & Configure** button to verify the configuration and generate the swfconfig.xml file.

#### Section: Assembly List
The listed assemblies include:
- ButtonAdv.dll
- CalculatorControl.dll
- ChartControl.dll
- CheckBoxAdv.dll
- ColorPickerUIAdv.dll
- ComboBoxAutoComplete.dll
- ComboBoxDropDown.dll
- CommandBar.dll
- Among others, ensuring all essential controls are included for automation.

#### Warning Dialog for Overwriting Configuration
Upon generating the swfconfig.xml file, a dialog prompts the user to confirm whether to replace the existing configuration:
- **You have Syncfusion assemblies configured already in the SwfConfig.xml file of HP QTP. Do you want to replace that?**
- **Select 'No' to skip the replacing and select 'Cancel' to abort.**

**Action Required**: Click **Yes** to save and open the new swfconfig.xml file, effectively replacing the existing configuration.

## Important Instructions
4. **After generating the swfconfig.xml file**, the system will ask whether you want to open it. **Click Yes** to save and open the new swfconfig.xml file.

## Cross References
See also: SwfConfig.xml file configuration in HP QTP for detailed instructions on Synfusion assembly integration.

<!-- tags: [QTP, swfconfig, Syncfusion, assembly configuration, HP QTP] keywords: [QTP, swfconfig, Syncfusion, assembly integration, configuration tool] -->
```

---

<!-- 페이지 19 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_073.jpeg
document_name: QTP
page_number: 073
page_id: QTP#page_073
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:06:16Z
fidelity: lossless
-->

## Essential QuickTest Professional

### SwfConfig.xml File Structure

The `SwfConfig.xml` file will look like the following:

```xml
[XML]
<?xml version="1.0" encoding="UTF-8" ?>
<Controls>
    <Control Type="Syncfusion.Windows.Forms.Grid.GridControl">
        <CustomRecord>
            <Component>
                <Context>AUT</Context>
                <DllName>C:\Program Files\Syncfusion\Essential TestStudio\<Version Number>\Bin\2.0\GridControl.dll</DllName>
                <TypeName>Syncfusion.TestStudio.Grid.GridControl</TypeName>
            </Component>
        </CustomRecord>
        <CustomReplay>
            <Component>
                <Context>AUT</Context>
                <DllName>C:\Program files\Syncfusion\Essential TestStudio\<Version number>\Bin\2.0\GridControl.dll</DllName>
                <TypeName>Syncfusion.TestStudio.Grid.GridControl</TypeName>
            </Component>
        </CustomReplay>
    </Control>
    .........
</Controls>
```

**Note**: Ensure that the `<DllName>` element contains the correct path to the corresponding DLL.

### Steps to Handle SwfConfig.xml

7. Save the `SwfConfig.xml` file.

8. Restart QTP once the `SwfConfig.xml` file is saved to refresh the mappings to the required controls before starting the test.

**Note**: Mapping for the required controls can be done in a similar manner.

## 7.1.2 How to Know Whether My SwfConfig File Holds an Invalid Assembly Path Reference

### Overview
- This section explains how to identify if the `swfconfig` file contains an invalid assembly path reference.

### Steps to Verify

1. Open the Syncfusion Essential QTP Configurator located at (Installed location of Essential QuickTest Professional)\\Utilities\\SwfConfigUtility\\SwfConfigUtility.exe.

### Additional Information
- Use the Syncfusion Essential QTP Configurator tool to ensure that the paths in the `swfconfig` file are valid and point to the correct assemblies.

## API Reference (if applicable)

### WinForms-specific conventions
- The `SwfConfig.xml` file is crucial for mapping controls and their corresponding DLLs for automation purposes.

### Code Examples

```csharp
// Example of a control mapping in SwfConfig.xml
<Control Type="Syncfusion.Windows.Forms.Grid.GridControl">
    <CustomRecord>
        <Component>
            <Context>AUT</Context>
            <DllName>C:\Path\To\Your\Dll\GridControl.dll</DllName>
            <TypeName>Syncfusion.TestStudio.Grid.GridControl</TypeName>
        </Component>
    </CustomRecord>
</Control>
```

### Cross References
- For more information on configuring essential assemblies, refer to the Syncfusion documentation on control mapping.

<!-- tags: [syncfusion-sdk, swfconfig, qtp, control-mapping] keywords: [swfConfigUtility, dllname, typename, syncfusion.windows.forms.grid.gridcontrol] -->
```


---

<!-- 페이지 20 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_077.jpeg
document_name: QTP
page_number: 077
page_id: QTP#page_077
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:06:36Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview
- Steps to configure and utilize the Essential QTP Configurator.
- Managing and loading XML files for QTP configurations.

### Detailed Configure SConfiguration
1. **Configuration Window**:
   - **Configure SwfConfig file**: Displays information for configuring the SwfConfig file.
   - **QTP Assemblies Location**: Specifies where QTP assemblies are located.
   - **Product Version**: Provides the version number of the product.

2. **File Management**:
   - **Fit Assembly Name**: Identifies the assembly name associated.
   - **ProductVersion**: Indicates the associated product version.
   - **Check & Configure**: Allows checking and configuring the settings.
   - **Date Modified**: Displays the last modified date for trackers.

3. **File Selection**:
   - **Save As Dialog**:
     - **Selecting Location**: Choose a directory for saving a new configuration file.
     - **File Format**: Saves the file in XML format.

### Opening XML Files
5. The dialog box shown is used to open an XML file. Click **Yes** if you want to read the XML file.

## Content
### Configuring and Opening XML Files
- **Configuration Window**:
  - **Assembly Information**:
    - **Assembly Name**: Lists the names of included assemblies.
    - **Product Version**: Indicates the product version for each assembly.
  
- **File Interaction**:
  - **Save As Dialog**:
    - **Directory Navigation**: Navigate to the desired location to save XML files.
    - **File Type Selection**: Save files as XML (`.xml`).
  
  - **Warning Dialog**:
    - **Essential QTP Utility**: Prompts whether to open the XML file.
    - **Options**:
      - **Yes**: Opens the XML file.
      - **No**: Cancels the operation.

### Processing XML Data
- **Assembly Table**:
  - **Columns**:
    - **AssemblyName**: Lists all registered assemblies.
    - **ProductVersion**: Indicates the associated product version for each assembly.
    - **DateModified**: Shows the date each assembly was last modified.

- **Save Report**:
  - Allows generating and saving a report summarizing the configuration details.

## API Reference (if applicable)
- **Classes**:
  - `SwfConfigUtility`: Handles configuration and setup for swfconfig files.
  - `SaveAsDialog`: Manages the dialog for saving files.

## Code Examples (multi-language supported)
- **Configure SConfiguration Interaction**:
  ```csharp
  using Syncfusion.Winforms.QTP;
  
  // Open the configuration window
  SwfConfigUtility.OpenSwfConfig();
  
  // Save the configuration as an XML file
  SwfConfigUtility.SaveAs("config.xml");
  
  // Validate and configure the settings
  bool success = SwfConfigUtility.CheckAndConfigure();
  if (!success)
  {
      MessageBox.Show("Failed to configure settings.");
  }
  ```

## Page-level Navigation/TOC (if applicable)
- Step-by-step guide to configuring and utilizing the Essential QTP Configurator.
- Detailed instructions on managing XML files for QTP configurations.

## Cross References
- Refer to the general documentation for more details on XML file management in QTP.

<!-- tags: [syncfusion-winforms, qtp-configurator, xml-file-management, essential-quicktest-professional] keywords: [configuration, xml, assemblies, product version, swfconfig, save as, warning dialog, reporting, date modified] -->
```

---

<!-- 페이지 21 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_081.jpeg
document_name: QTP
page_number: 081
page_id: QTP#page_081
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:06:55Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview
- Explains how to set the current cell in a Grid using the SetCurrentCell method.
- Covers use cases for GridControl, GridGroupingControl, and GridDataBoundControl.
- Demonstrates usage examples for QTP testing.

## Content

### 7.2.2 How to set the current cell in Grid

The `SetCurrentCell` method is used to set the current cell in Grid or activate a cell as the current cell in Grid. This method is used in `GridControl`, `GridGroupingControl`, and `GridDataBoundControl`.

**Use Case Scenarios**  
This method enables a Grid cell in QTP testing.

#### Methods Table

| Method           | Description                             | Parameters                                                                     | Return Type |
|------------------|-----------------------------------------|--------------------------------------------------------------------------------|-------------|
| SetCurrentCell   | Sets the location of current cell in Essential Grid             | For the Grid control: <br> `public void SetCurrentCell(int row, int col)` | Void        |
|                  |                                         | For the GridGrouping control: <br> `public void SetCurrentCell(object row, object col)` | Void        |
|                  |                                         | For GridDataBoundGrid control: <br> `public void SetCurrentCell(int row, int col)` | Void        |

**Note:** GridGrouping control uses iterated rows to set the current cell in the respective tables.

The following code examples illustrate how to use the `SetCurrentCell` method.

#### For GridControl
```csharp
SwfWindow("Form1").SwfObject("gridControl1").SetCurrentCell 3,1
```

#### For GridGroupingControl
```csharp
SwfWindow("Form1").SwfObject("gridGroupingControl1").SetCurrentCell 3,"Col2"
```

## API Reference (if applicable)
- **Namespace:** Syncfusion.Windows.Forms.Grid
- **Class:** GridControl, GridGroupingControl, GridDataBoundControl
- **Method:** SetCurrentCell

#### Parameters
| Name | Type | Description | Default | Required |
|------|------|-------------|---------|----------|
| row  | int  | Row index of the cell | NA      | Yes     |
| col  | int/object | Column index or name of the cell | NA     | Yes     |

#### Returns
- `Type`: Void
- `Description`: No return value; sets the current cell.

## Code Examples (if applicable)
The code examples provided above illustrated the usage of the `SetCurrentCell` method in GridControl and GridGroupingControl.

## Page-level Navigation/TOC (if applicable)
- This page is part of the "Essential QuickTest Professional" section in the user guide, focusing on setting the current cell in a Grid.

<!-- tags: [Essential QuickTest Professional, GridControl, GridGroupingControl, GridDataBoundControl, SetCurrentCell] keywords: [set current cell, Grid, GridControl, GridGroupingControl, GridDataBoundControl, QTP testing, return type, parameters, method description] -->
```

---

<!-- 페이지 22 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_085.jpeg
document_name: QTP
page_number: 085
page_id: QTP#page_085
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:07:15Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview
- Demonstrates how to apply the GetXAxisText and GetYAxisText methods in QTP.
- Explains how to find the count of a series within a chart.
- Details the process to find the maximum Y-axis value in the specified region.

## Content

### Applying GetXAxisText and GetYAxisText Method in QTP

The following code examples illustrate how to get the displayed text.

```plaintext
MsgBox(SwfWindow("ChartDemo").SwfObject("chart1").GetXAxisText())
MsgBox(SwfWindow("ChartDemo").SwfObject("chart1").GetYAxisText())
```

#### 7.4.2 How to find the count of a series within the chart

##### Supported method to find the series count within the chart
The GetSeriesCount method is used to get the series count within the chart. This method returns the displayed text in integer format.

##### Use Case Scenarios
This feature enables you to get the count of a series within the chart in QTP testing.

##### Methods Table

| Method         | Description                   | Parameters                                        | Return Type |
|----------------|-------------------------------|---------------------------------------------------|-------------|
| GetSeriesCount | Gets the series count within the chart in Essential Chart. | public in GetSeriesCount() | Int         |

##### Applying GetSeriesCount in QTP
The following code example illustrates how to get the series count in the chart.

```plaintext
[For Chart Control]
MsgBox(SwfWindow("ChartDemo").SwfObject("chart1").GetSeriesCount())
```

#### 7.4.3 How to find the maximum Y-axis value in the specified region

##### Supported method to find the maximum Y-axis value in the specified region
The GetMaxYValue method is used to get the displayed maximum value in the Y-axis. This method returns the displayed value in double format.

---

<!-- tags: [product, module, control, api, version?] keywords: [GetXAxisText, GetYAxisText, GetSeriesCount, GetMaxYValue, QTP, chart, series count, maximum Y-axis value, WinForms] -->
```

---

<!-- 페이지 23 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_089.jpeg
document_name: QTP
page_number: 089
page_id: QTP#page_089
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:07:28Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview
- How to connect nodes using the `ConnectNodes` method in QTP testing.
- Use of the `ResizeNode` method to adjust node size in diagram controls.

## Content

### The ConnectNodes Method

#### Overview of ConnectNodes
The `ConnectNodes` method is used to connect the specified nodes using connectors.

#### Use Case Scenarios
This feature enables you to connect the specified nodes using connectors in the chart control in QTP testing.

#### Methods Table
| Method         | Description                                      | Parameters                                                                 | Return Type |
|-----------------|--------------------------------------------------|---------------------------------------------------------------------------|--------------|
| `ConnectNodes` | Connects the specified nodes using connectors.  | `public void ConnectNodes(string startNode, string endNode, string connector)` | `void`       |

#### Applying ConnectNodes in QTP
The following code examples illustrate how to connect the specified nodes using connectors in the chart control.

##### Code Example
```csharp
[For Diagram Control]
SwfWindow("Simple Flow Diagram").SwfObject("diagram").SelectNode "EllipseStart"
SwfWindow("Simple Flow Diagram").SwfObject("diagram").ConnectNodes "RectangleProcess", "RectangleProcess", "LineConnector"
```

### 7.6.3 How to resize the node

#### Overview of Resizing Nodes
The `ResizeNode` method is used to resize the node size in diagram control.

#### Use Case Scenarios
This feature enables you to resize the node in the diagram control.

#### Methods Table
| Method       | Description                                | Parameters | Return Type |
|--------------|--------------------------------------------|------------|--------------|
| `ResizeNode` | Resizes the node size in diagram control. |            |              |

## API Reference (if applicable)
- **Namespace**: `Syncfusion.WinForms.Diagram.Controls`
- **Class**: DiagramControl
  - **Methods**:
    - `public void ConnectNodes(string startNode, string endNode, string connector)`
      - **Parameters**:
        - `startNode`: The identifier of the starting node.
        - `endNode`: The identifier of the ending node.
        - `connector`: The type of connector to use.
      - **Return Type**: `void`
    - `public void ResizeNode(SIZE size)`
      - **Parameters**:
        - `size`: The new size for the node.
      - **Return Type**: `void`

## Code Examples (multi-language supported)

#### C# Example for Connecting Nodes
```csharp
SwfWindow("Simple Flow Diagram").SwfObject("diagram").ConnectNodes("Node1", "Node2", "LineConnector");
```

#### C# Example for Resizing Nodes
```csharp
SwfWindow("Simple Flow Diagram").SwfObject("diagram").ResizeNode(new System.Drawing.Size(100, 50));
```

## RAG Annotations
<!-- tags: QTP, Syncfusion Winforms, DiagramControl, ConnectNodes, ResizeNode version: 11.4.0.26 -->
<!-- keywords: QTP, ConnectNodes, ResizeNode, node resizing, node connection, chart control, diagram control -->
```

---

<!-- 페이지 24 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_002.jpeg
document_name: QTP
page_number: 002
page_id: QTP#page_002
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:01:23Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Contents

### 1. Introduction

- **1.1 Introduction to Essential QuickTest Professional** ..... 4
- **1.2 Prerequisites and Compatibility** ..... 5
- **1.3 Documentation** ..... 6

### 2. Installation and Deployment

- **2.1 Installation and Configuration** ..... 7
  - **2.1.1 Installation** ..... 7
  - **2.1.2 Configuration** ..... 14
    - **2.1.2.1 Automatic Configuration** ..... 14
    - **2.1.2.2 Manual Configuration** ..... 15
- **2.2 Sample and Location** ..... 17
- **2.3 Licensing, Patches and Uninstallation** ..... 18
- **2.4 Assembly information** ..... 18

### 3. Getting Started

- **3.1 Creating and Recording a Test** ..... 22
- **3.2 Running a Test** ..... 33
- **3.3 Editing a Test** ..... 35
- **3.4 Saving a Test** ..... 39
- **3.5 Running the Saved Test** ..... 40

### 4. Supported Controls and Methods

- **4.1 Essential Grid** ..... 43
- **4.2 Essential Tools** ..... 51
- **4.3 Essential Chart** ..... 61
- **4.4 Essential Schedule** ..... 63
- **4.5 Essential Diagram** ..... 63

### 5. Known Issues

- **5.1 General** ..... 65
- **5.2 Essential Grid** ..... 65
- **5.3 Essential Tools** ..... 65

### 6. Utilities

- **67**

## Summary

- Covers the installation, configuration, and basic usage of QuickTest Professional.
- Includes sections on supported controls, known issues, and utilities.

## Navigation

- Provides detailed information on different document sections and their respective page numbers for easy navigation.

<!-- tags: [syncfusion, winforms, quicktest professional, installation, deployment, controls, known issues, utilities, version 11.4.0.26] keywords: [installation, configuration, essential grid, essential tools, essential chart, essential schedule, essential diagram, documentation, test automation, syncfusion, winforms, quicktest] -->
```

---

<!-- 페이지 25 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_006.jpeg
document_name: QTP
page_number: 006
page_id: QTP#page_006
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:01:38Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview
- Describes the .NET Framework version compatibility.
- Lists other requirements such as Essential Studio compatibility.
- Outlines the operating system compatibility of Essential QuickTest Professional.
- Explains the available documentation types and their locations.

## Content

### Essential Requirements

| **.NET Framework** | **.Net Framework version 2.0, 3.5, 4.0, or 4.5** |
| --- | --- |
| **Other Requirements** | Essential Studio (User Interface edition – Windows Forms) of the same version as the Essential QTP Add-on. |

### Compatibility

#### Operating Systems
Essential QuickTest Professional is compatible with the following operating systems:

- Microsoft Windows XP
- Microsoft Windows Vista
- Microsoft Windows 7
- Microsoft Windows 8.1
- Microsoft Windows Server 2003
- Microsoft Windows Server 2008

### 1.3 Documentation

Syncfusion provides the following documentation segments which cover all the necessary information pertaining to Essential QuickTest Professional.

| **Type of documentation** | **Location** |
| --- | --- |
| Readme | (Installed location of Essential QTP)\ReadMe\ReadMe.htm |
| Class Reference | (Installed location of Essential QTP)\Help\ClassReference.chm |

## RAG Annotations
<!-- tags: [syncfusion winforms, essential qtp, documentation, compatibility requirements] keywords: [essential quicktest professional, .net framework, essential studio, operating systems, readme, class reference, installed location] -->
```

---

<!-- 페이지 26 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_010.jpeg
document_name: QTP
page_number: 010
page_id: QTP#page_010
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:01:50Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview

- This page provides instructions on selecting the installation folder for Syncfusion Essential QTP 11.1.0.21.
- Steps to install the application in the default location or choose a custom location are detailed.
- Describes the options available in the Installation options window.

## Content

### Select Installation Folder

Figure 4 illustrates the interface for selecting the installation folder for Syncfusion Essential QTP 11.1.0.21.

#### Installation Folder Selection

1. **Default Installation**: To install in the default location, click **Next**.
2. **Custom Location**: You can also browse to choose a required location. When you click **Browse** to select the desired location, the Destination Location screen displays the selected location.

### Installation Options

Once the installation folder is chosen, proceed as follows:

- Click **Next** to open the Installation options window.
- Choose one of the following installation options as required:

  - **Typical**: Installs most common program features.
  - **Custom**: Allows you to choose the program to be installed and where it should be installed.
  - **Complete**: Installs all of the feature programs.

## Code Examples

No code examples are present in this section.

## Addendum

This documentation is part of the Syncfusion Winforms user guide for version 11.4.0.26, tailored for users setting up the Essential QTP component.

<!-- tags: [Essential QTP, installation, folder selection, Syncfusion Winforms, installation options] keywords: [installation folder, Syncfusion Essential QTP, default location, custom installation, typical installation, complete installation] -->
```

---

<!-- 페이지 27 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_014.jpeg
document_name: QTP
page_number: 014
page_id: QTP#page_014
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:02:01Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview
- The installation process of Syncfusion Essential QTP has been completed.
- Describes the configuration process involving the swfconfig file and how it maps Syncfusion controls to their corresponding custom server libraries.

## Content

### 2.1.2 Configuration
An XML file in QTP called **swfconfig** is the configuration file located at `(Installed location of Essential QuickTest Professional)\<version-2.0, 3.5, or 4.0>\swfconfig`, which contains all the mapping information for QTP to recognize Syncfusion controls. In **swfconfig**, the controls are mapped to their corresponding custom server libraries (Essential QuickTest Professional DLLs) by giving the fully qualified name of the DLL.

**Note:** The fully qualified name is the name of the file mentioned with its complete path.

Any event that is triggered while working with a Syncfusion control, either by the user or the program activity, will be handled by the corresponding method in the custom library (DLL) given as the `<DllName>` tag under the `<Control>` tag.

An XML file can be configured in one of two ways, automatically or manually.

#### 2.1.2.1 Automatic Configuration
This section provides the details about the configuration of the swfconfig file using the SwfConfigUtility. Refer to the Utility section of this document.

## API Reference (if applicable)

## Code Examples (multi-language supported)

## Page-level Navigation/TOC (if applicable)

## Cross References
- See also: `Syncfusion Essential QTP`
- `swfconfig` file mapping

## RAG Annotations
<!-- tags: [Syncfusion, Winforms, QTP, swfconfig, version-11.4.0.26, Essential QuickTest Professional, configuration] keywords: [essential, qtp, configfile, dllmapping, swfconfig] -->
```
```

---

<!-- 페이지 28 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_018.jpeg
document_name: QTP
page_number: 018
page_id: QTP#page_018
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:02:14Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview
- (Installed location of the product)\Examples\Samples\Bin\

---

## Content

### Note
There is no sample browser available to run the samples for Essential QuickTest Professional. You have to manually run the exe from the above-mentioned location.

#### Source Code Location
The source code for Essential QuickTest Professional is available at the following location:
- (Installed location of the product)\Src\

#### Assemblies Location
The assemblies are available under the following location:
- (Installed location of the product)\Bin\

### 2.3 Licensing, Patches and Uninstallation
This section deals with license keys, patches, and the uninstallation process.

#### Licensing
Essentialqtaddonsetup is the setup file for Essential QuickTest Professional, which can be installed with the same license key that has been used to install Essential Studio. Essential QuickTest Professional does not require a separate license.

#### Patches
Patches are not provided for Essential QuickTest Professional. In case of any fix requested by the user, the assemblies are sent. These assemblies are then to be placed under the following location:
`(Installed location of the product)\Bin\`

#### Uninstallation
Uninstallation can be done with the help of the `unis000` file that is available in the installed location. Double-clicking the file uninstalls Essential QuickTest Professional.

---

### 2.4 Assembly information
The following table shows the assembly information for each of the controls supported by Essential QuickTest Professional.

#### For Essential Grid
(No further content provided in the image)

---

_legal text (to be ignored)
© 2013 Syncfusion. All rights reserved.
Page 18 |

<!-- tags: [Essential QuickTest Professional, licensing, uninstallation, assemblies, source code, patching, Syncfusion Winforms, 11.4.0.26] keywords: [Essential QuickTest Professional, Essential Studio, installation, license key, assemblies, source code, unis000, uninstallation, Essential Grid, QTP, Syncfusion] -->
```

---

<!-- 페이지 29 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_022.jpeg
document_name: QTP
page_number: 022
page_id: QTP#page_022
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:02:30Z
fidelity: lossless
-->

# Getting Started

Essential QuickTest Professional lets you test applications with different Syncfusion controls, and allows playback of scripts. The following is a list of chapters containing information on the functionality of this software.

## 3.1 Creating and Recording a Test

To create a new test:

1. Open QTP by double-clicking the QuickTest Professional icon.

**Note:** The QuickTest Professional – Add-in Manager window is displayed.

2. Select the .NET check box under the **Add-in** header. This ensures that .NET add-in is installed.

![QuickTest Professional - Add-In Manager](image.png)

### Figure 9: QuickTest Professional - Add-In Manager

---

## API Reference (if applicable)

No specific API reference is mentioned in the document slice.

## Code Examples (multi-language supported)

No code examples are present in the given document slice.

## Page-level Navigation/TOC (if applicable)

No page-level navigation or TOC is present in the given document slice.

## Cross References

No explicit cross references are present in the given document slice.

## RAG Annotations

```html
<!-- tags: [QTP, Essential QuickTest Professional, chapter list, adding add-ins, test creation, .NET add-in] keywords: [test applications, Syncfusion controls, playback of scripts, QuickTest Professional icon, Add-in Manager, .NET add-in, Web, Visual Basic, ActiveX, testing ActiveX objects, maximize performance, object identification reliability] -->
```
```html
<!-- anchor: QTP#page_022#getting-started -->
``` 
```html
<!-- anchor: QTP#page_022#creating-and-recording-a-test -->
```
```html
<!-- anchor: QTP#page_022#note -->
```
```html
<!-- anchor: QTP#page_022#figure-9 -->
```
```html
<!-- anchor: QTP#page_022#api-reference -->
```
```html
<!-- anchor: QTP#page_022#code-examples -->
```
```html
<!-- anchor: QTP#page_022#page-level-navigation-toc -->
```
```html
<!-- anchor: QTP#page_022#cross-references -->
```
```html
<!-- anchor: QTP#page_022#rag-annotations -->
```
```html
<!-- Page-level Navigation/TOC (if applicable) JSON -->
```
```html
<!-- Cross References JSON -->
```
```html
<!-- RAG Annotations JSON -->
```

---

<!-- 페이지 30 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_026.jpeg
document_name: QTP
page_number: 026
page_id: QTP#page_026
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:02:45Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview
- Describes the configuration of the Record and Run Settings dialog box in Essential QuickTest Professional.
- Focuses on the Web settings within the Record and Run Settings dialog box.
- Includes instructions for navigating to the Windows Applications tab.

## Content

### Record and Run Settings

#### Web Tab

The Web tab of the Record and Run Settings dialog box allows you to configure settings for recording and running tests on open browsers. The following options are available:

1. **Record and run test on any open browser**:
   - This option is selected by default, allowing tests to run on any currently open browser.

2. **Open the following address when a record or run session begins**:
   - Allows you to specify a URL to open when a recording or running session starts.
   - Example: `http://newtours.demoaut.com`

3. **Open the following browser when a record or run session begins**:
   - Allows you to select a specific browser to open when a session starts.
   - Example: `Microsoft Internet Explorer`

4. **Do not record and run on browsers that are already open**:
   - Prevents recording and running tests on already open browsers.

5. **Close the browser when the test closes**:
   - Ensures that the browser is closed after the test completes.

#### Windows Applications Tab

After configuring the Web settings, you can click the **Windows Applications** tab to set up recording and running for Windows applications.

## API Reference

- **`Record and Run Settings`**: Dialog box for configuring testing settings in Essential QuickTest Professional.
- **`Web Tab`**: Configures settings specific to web browser-based testing.
- **`Windows Applications Tab`**: Configures settings specific to Windows application-based testing.

## Code Examples

No specific code examples are provided in this content.

## Page-level Navigation/TOC
- **Record and Run Settings**: Guides users through setting up browser-specific configurations.
- **Windows Applications**: Instructions for configuring settings applicable to Windows-based applications.

## Cross References

- **Related Topic**: [How to Configure Record and Run Settings](#related-topic-link)

<!-- tags: syncfusion, essential-quicktest-professional, Record and Run Settings, Web settings, Windows Applications, version: 11.4.0.26 keywords: Web tab, Windows tab, browser, record, run, settings, configuration, QuickTest Professional, API, browser-specific settings -->
```

---

<!-- 페이지 31 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_030.jpeg
document_name: QTP
page_number: 030
page_id: QTP#page_030
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:03:00Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview
- This page demonstrates the integration of the Grid Control in applications and the use of the SwfConfig file to map controls to their respective DLLs.
- Focuses on user interactions with the Grid Control and the corresponding actions logged in the running application.
- Explains how method names from the Syncfusion namespace are recorded and displayed based on user interactions.

## Content

### Grid Control Usage
Figure 17 illustrates the use of the Grid Control in an application.

![Figure 17: Application using Grid Control](assets/figure17.png)

1. Perform required valid user-action in the application.

#### Note: SwfConfig File Mapping
- Whenever the user performs any action involving the Syncfusion control used in the application, the SwfConfig file maps the control to the corresponding DLL.
- The DLL renders the correct method names of the Syncfusion namespace that will be called respective to the user-actions performed.
- These method names are then recorded and displayed in the screen behind the running application, as shown below.

## API Reference
### Method Names Recording
- The Grid Control logs user-action methods from the Syncfusion namespace.
- Recorded method names reflect the actions performed, enabling testing and validation of control behavior.

## Code Examples
```csharp
// Example: Performing a user-action on the Grid Control
grid.PerformAction("SelectRow", rowIndex);

// Example: Recording user-action method names
recordedMethods.Add("SelectRow(rowIndex)");
```

## Page-level Navigation/TOC (if applicable)
- [Grid Control Usage]
- [SwfConfig File Mapping]
- [Method Names Recording]

### Cross References
- See also: [Essential QuickTest Professional Documentation](#essential-quicktest-professional-documentation)
- See also: [Syncfusion Grid Control Reference](#syncfusion-grid-control-reference)

<!-- tags: [syncfusion, winforms, grid control, qtp, swfconfig, method recording, dll mapping] keywords: [grid control, user-action, method names, swfconfig, dll, quicktest professional, essential qtp] -->
```

---

<!-- 페이지 32 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_034.jpeg
document_name: QTP
page_number: 034
page_id: QTP#page_034
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:03:13Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Note: Selecting one option renders the other unavailable.

### Overview
- Review the process of selecting a required location for executing a test.
- Learn about the test results display after running a QuickTest Professional (QTP) application with recorded Syncfusion controls.
- Understand the test completion and result summary shown in the Test Results dialog box.

## Content

### Step-by-Step Instructions
1. Select the required location by clicking the specified icon.
2. QTP starts the running process, opening the application containing recorded Syncfusion controls. It executes all recorded events in a continuous flow.
3. Upon completion, the Test [Result_Written_Location] - Test Results dialog box is displayed, summarizing the test results.

#### Test Results Display

The following is a screenshot of the Test Results dialog box:

![Figure 20: Test Results](https://example.com/figure_20)

### Test Results Summary

#### Test Details
- **Test**: Test
- **Results name**: Res1
- **Time Zone**: Eastern Standard Time
- **Run started**: 9/15/2009 - 6:48:55
- **Run ended**: 9/15/2009 - 6:49:08

#### Iteration Results
| Iteration # | Results |
|-------------|---------|
| 1           | Passed  |

#### Status Summary
| Status                  | Times |
|-------------------------|-------|
| Passed                  | 22    |
| Failed                  | 0     |
| Warnings                | 0     |

### Completion of Test
The process of running the test is completed.

#### Additional Resources
- For detailed information on running scripts, refer to the QTP help document.

## RAG Annotations
<!-- tags: QuickTest Professional, Test Results, Syncfusion controls, version 11.4.0.26 keywords: QTP, test execution, test results, iteration, status summary -->
```

---

<!-- 페이지 33 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_038.jpeg
document_name: QTP
page_number: 038
page_id: QTP#page_038
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:03:26Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview
- Demonstrates editing user actions in the QuickTest Professional grid view by showing the usage of right-click options for manipulating grid control items.

## Content

### Editing in Keyword View – Right-click

#### Overview
The figure illustrates the process of editing actions using the "Keyword View" in the QuickTest Professional interface. It focuses on the manipulation of grid control objects via right-click actions like cutting, copying, and pasting.

#### Detailed Description
- **Figure 24: Editing in Keyword View – Right-click**
  - The figure displays the QuickTest Professional environment with a focus on the grid control actions and values. The right-click menu options for a selected grid control are highlighted, allowing for actions such as Cut, Copy, and Paste.
  
  - The grid columns show:
    - **Value**: Numeric and alphanumeric values associated with grid control entries.
    - **Documentation**: Summary descriptions, with many entries marked as "<No documentation summary is available for this...>".

#### Example Workflow
For example, clicking **Cut** in the menu will cause the row representing a user-action to be removed. You can then right-click on any other item and click **Paste** on the menu displayed. This causes the row to be pasted before the right-clicked item.

## API Reference (if applicable)
N/A

## Code Examples (multi-language supported)
N/A

## Page-level Navigation/TOC (if applicable)
N/A

## Cross References
- Refer to related sections on test editing and manipulation in the QuickTest Professional user guide.

<!-- tags: [QuickTest Professional, keyword view, grid control, test editing, version 11.4.0.26] keywords: [right-click, cut, copy, paste, grid control] -->
```

---

<!-- 페이지 34 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_042.jpeg
document_name: QTP
page_number: 042
page_id: QTP#page_042
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:03:39Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview

- Opens a test file in **QuickTest Professional** and prepares it for execution.
- Describes the process of running a saved test using the toolbar.

## Content

### Steps to Run a Test

1. **Open the Test:**
   - The test file `Test1` is open, as shown in Figure 28.

   ![Figure 28: Test Opened](#)

   The test contains multiple actions targeting a grid control, including:
   - Moving the grid window to specified positions.
   - Setting current cells, cell data, radio buttons, checkboxes, and entering text.
   - Using the `SwfWindow` and `SwfObject` methods to interact with the grid control.

2. **Review the Expert View:**
   - In the **Expert View**, detailed lines of the test script are visible. These lines include commands such as:
     ```
     SwfWindow("GridControl").Move 456,247
     SwfWindow("GridControl").SwfObject("gridControl1").SetCurrentCell 11,4
     SwfWindow("GridControl").SwfObject("gridControl1").SetCellData 13,1,"456.00"
     SwfWindow("GridControl").SwfObject("gridControl1").SetCellData 13,2,"-739.00"
     SwfWindow("GridControl").SwfObject("gridControl1").SetColumnWidth 1,200
     SwfWindow("GridControl").SwfObject("gridControl1").SetCellContents 16,2,"new_value"
     ```
     and so on.

3. **Run the Test:**
   - Click the **Run** button on the toolbar to execute the test.

4. **For More Details:**
   - Additional information on running the test can be found in the **Running a Test** topic in this document.

### Completion of the Process

The process of running a saved test is now complete.

## Cross References

- **Refer to the Running a Test topic** in this document for more details on executing the test.

<!-- tags: [syncfusion-sdk, essential-quicktest-professional, test-execution, test-running, gridcontrol] keywords: [test, grid, swfwindow, swfobject, move, setcurrentcell, setcelldata, setcolumnwidth, syncfusion winforms, qtp] -->
```

---

<!-- 페이지 35 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_046.jpeg
document_name: QTP
page_number: 046
page_id: QTP#page_046
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:03:54Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Methods

| **Method**                                      | **Description**                                           |
|-------------------------------------------------|-----------------------------------------------------------|
| ResizeColumn(int fromColumn, int to, int width)| Resizes the specified columns.                           |
| ResizeRow(int fromRow, int to, int height)     | Resizes the specified rows.                              |
| SelectRange(string range, int top, int left, int bottom, int right)| Selects the range.                |
| SetCellData(int row, int col, string str)      | Sets the cell value of the cell.                         |
| SetCellCheckBox(int row, int col, string str)  | Sets the cell value of the check box cell.              |
| SetCellRadioButton(int row, int col, string str)| Sets the cell value of the radio button cell.           |
| SetCurrentCell(int row, int col)               | Sets the location of current cell.                       |
| SetScrollPosition(int vScrollPosition, int hScrollPosition)| Sets the scroll position.                  |
| SortColumn(int col, string sortBehavior)       | Sorts the column.                                        |

## Helper Functions

| **Function**                                  | **Description**                                           |
|-----------------------------------------------|-----------------------------------------------------------|
| BeginEdit(int row, int col)                  | Brings the editing cursor in the specified grid cell.    |
| string GetCellType(int row, int col)         | Retrieves the CellType for the given cell coordinates.    |
| string GetCellBackColor(int row, int col)    | Retrieves the Back color for the given cell coordinates.  |
| int GetColumnCount()                         | Retrieves the number of columns used.                    |
| int GetVisibleColumnCount()                  | Retrieves the number of visible columns.                 |
| int GetColumnIndex(string name)              | Finds the column index for the given column name, returns 0 if search fails.  |
| Int GetCurrentCellImageIndex(int row, int col)| Gets the image index of the current cell.                |
| string GetFormattedText(int row, int col)    | Retrieves the formatted cell value.                     |
| bool IsColumnVisible(int col)                | Checks if the column is visible.                        |
| bool IsFormulaCell(int row, int col, out string formula, out string computedValue)| For a given row and column index, IsFormulaCell points to the formula used in that cell and the result |

## Cross References
See also:
- [Syncfusion documentation](https://www.syncfusion.com/documentation)

<!-- tags: [syncfusion, winforms, quicktest professional, api, methods, helper functions] keywords: [resizecolumn, resizerow, selectrange, setcelldata, setcellcheckbox, setcellradiobutton, setcurrentcell, setscrollposition, sortcolumn, beginedit, getcelltype, getcellbackcolor, getcolumncount, getvisiblecolumncount, getcolumnindex, getcurrentcellimageindex, getformattedtext, iscolumnvisible, isformulacell] -->
```

---

<!-- 페이지 36 -->

```html
<!--  
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_050.jpeg
document_name: QTP
page_number: 050
page_id: QTP#page_050
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:04:11Z
fidelity: lossless
-->

## Overview
- Describes various methods applicable to grid controls, highlighting functionality for setting cell values, managing scroll positions, and performing operations like sorting and resizing.
- Explains methods specific to `GridListControl` for resizing columns and rows, selecting ranges, and retrieving the control name.
- Lists the `GetName()` method for `TabBarSplitterControl`, indicating functionality to retrieve the name of the `TabBarControl`.

## Content

| Method                              | Description                                    |
|-------------------------------------|------------------------------------------------|
| SetCellData(object row, object col, string str) | Sets the cell value of the cell.              |
| SetCellCheckBox(object row, object col, string str) | Sets the cell value of the check box cell.  |
| SetCellRadioButton(object row, object col, string str) | Sets the cell value of the radio button cell. |
| SetCurrentCell(object row, object col) | Sets the location of current cell.            |
| SetScrollPosition(int vScrollPosition, int hScrollPosition) | Sets the scroll position.                 |
| SortColumn(string tablename, object col, string sortBehavior, bool cntrl) | Sorts the column.                      |
| SelectRecords(object row, object count) | Selects multiple records for the GridGroupingControl.                                      |
| ScrollToColumn(string tablename, object col) | The grid will scroll to the given column.    |
| ScrollToRow(int row)               | The grid will scroll to the given row.        |
| AddNewRow(string objn)             | A new row will be added.                      |
| string GetFormattedText(int row, int col) | Retrieves the formatted cell value.         |
| string GetName()                   | Gets the name of the Grid control object.     |

### GridListControl

| Method                              | Description                                    |
|-------------------------------------|------------------------------------------------|
| ResizeColumn(object fromColumn, int to, int width) | Resizes the specified columns.             |
| ResizeRow(int fromRow, int to, int height) | Resizes the specified rows.                 |
| SelectRow(int top, int bottom)     | Selects the range.                            |
| string GetName()                   | Gets the name of the GridListControl object    |

### TabBarSplitterControl

| Method                              | Description                                    |
|-------------------------------------|------------------------------------------------|
| GetName()                          | Gets the name of the TabBarControl.            |

## API Reference (if applicable)

The table above lists various methods and their descriptions relevant to grid controls, `GridListControl`, and `TabBarSplitterControl` in Syncfusion Winforms. These methods provide functionality for setting and retrieving values, managing grid views, and interacting with control elements.

## Code Examples (multi-language supported)

While no explicit code examples are provided in the image, the methods listed can be used in code as follows:

```csharp
// Example usage of SetCellData
grid.SetCellData(row, col, "newValue");

// Example usage of ResizeColumn
listControl.ResizeColumn("columnName", 50, 100);

// Example usage of GetName
string controlName = tabSplitterControl.GetName();
```

These examples illustrate how the methods described can be integrated into a C# application.

## Page-level Navigation/TOC (if applicable)

This page provides comprehensive documentation for grid-related controls in Syncfusion Winforms, focusing on methods applicable to grid manipulation and control management.

## Cross References

See also:
- Documentation for other grid-related controls and functionalities in Syncfusion Winforms.
- Additional API references and examples for Syncfusion Winforms controls.

<!-- tags: [syncfusion-sdk, syncfusion-winforms, grid-controls, gridlistcontrol, tabbarsplittercontrol, api-reference] keywords: [setcelldata, scrollposition, sortcolumn, resizecolumn, resizerow, selectrow, getname, gridcontrols, winforms] -->
```

---

<!-- 페이지 37 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_054.jpeg
document_name: QTP
page_number: 054
page_id: QTP#page_054
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:04:34Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview
- The section describes interfaces and methods related to managing date-time pickers, docking windows, and group bars in a Syncfusion WinForms application.
- Focus on calendar functionalities, docking features, and navigation panel handling.

## Content

### Date-Time Picker Related Methods

| Method | Description |
| --- | --- |
| `void ShowPopupWindow(object visible, object x, object y);` | Interface to show the calendar popup. |
| `void ShowCalendar(object visible);` | Interface to show the calendar in the popup window. |
| `void SetCalendarValue(object visible, string calValue);` | Interface to set the Calendar value of the `DateTimePickerAdv` control. |
| `void PopupClose(object visible);` | Interface to close the popup window. |
| `void SetTodayValue(string str);` | Interface to set the today value when the today button is clicked. |
| `void SetNoValue(string str);` | Interface to set the null value when the None button is clicked. |
| `System.DateTime GetCalendarValue();` | Returns the current value in the `DateTimePickerAdv` control. |

### DockingManager

| Method | Description |
| --- | --- |
| `DockStateChange(string dock, string prevState, string ctrl, string hostForm, string dockingStyle)` | Changes the docking window according to the specified current and previous state (i.e., Pinned, Unpinned, Tabbed, and MDIChild). |
| `VisibilityChange(string ctrlName, string visibility)` | Changes the visibility of the docked control according to the specified state. |
| `ActivateControl(string ctrlName)` | Activates the specified control. |
| `FloatStateChange(string ctrlName, string x, string y, string width, string height)` | Changes the state of the docking window into a floating state with the specified location and size. |

### GroupBar

| Method | Description |
| --- | --- |
| `SelectGroup(object index, string itemText)` | Selects the GroupBar item. |
| `DropDownButtonClick()` | Simulates click in the Navigation pane drop-down button. |

## API Reference

### Methods

- **ShowPopupWindow**: Displays a calendar popup window.
- **ShowCalendar**: Displays the calendar within the popup window.
- **SetCalendarValue**: Sets the value of the `DateTimePickerAdv` control.
- **PopupClose**: Closes the popup window.
- **SetTodayValue**: Sets the value to the current date when the "Today" button is clicked.
- **SetNoValue**: Sets a null value when the "None" button is clicked.
- **GetCalendarValue**: Retrieves the current value from the `DateTimePickerAdv` control.
- **DockStateChange**: Changes the docking state of a window based on the specified parameters.
- **VisibilityChange**: Adjusts the visibility of a docked control.
- **ActivateControl**: Activates the specified control.
- **FloatStateChange**: Floats a docking window with specified dimensions and position.
- **SelectGroup**: Selects an item in the GroupBar.
- **DropDownButtonClick**: Simulates a click on the drop-down button in the Navigation pane.

## Code Examples

### C# Example for DateTimePickerAdv

```csharp
// Example for setting the calendar value
void SetCalendarValueExample()
{
    // Assuming dateValue is a valid date string
    string dateValue = "2023-08-09";
    Syncfusion.Windows.Forms.Tools.DateTimePickerAdv dateTimePicker = new Syncfusion.Windows.Forms.Tools.DateTimePickerAdv();
    dateTimePicker.SetCalendarValue(true, dateValue);
}
```

### C# Example for DockingManager

```csharp
// Example for changing the docking state
void ChangeDockingStateExample()
{
    string dock = "Docked";
    string prevState = "Unpinned";
    string ctrl = "MyControl";
    string hostForm = "Form1";
    string dockingStyle = "Tabbed";
    DockingManager.DockStateChange(dock, prevState, ctrl, hostForm, dockingStyle);
}
```

### C# Example for GroupBar

```csharp
// Example for selecting a group in the GroupBar
void SelectGroupBarExample()
{
    object index = 0;
    string itemText = "Group 1";
    GroupBar.SelectGroup(index, itemText);
}
```

## Page-level Navigation/TOC (if applicable)

- Date-Time Picker Related Methods
- DockingManager
- GroupBar

## Cross References

- See also: `DateTimePickerAdv`, `DockingManager`, `GroupBar`, `Navigation Pane`, `Popup Window`.

<!-- tags: [Syncfusion, WinForms, DateTimePickerAdv, DockingManager, GroupBar, NavigationPane, PopupWindow] keywords: [calendar, date, time, docking, group, bar, state, visibility, floating, drop-down] -->
```

---

<!-- 페이지 38 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_058.jpeg
document_name: QTP
page_number: 058
page_id: QTP#page_058
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:04:58Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview
- Lists the methods and their descriptions for interacting with different controls.
- Covers methods for managing text in `TextBoxExt`, state management in `ThemedCheckButton`, and node operations in `TreeViewAdv`.

## Content

### Text Box Methods
Below are the methods for the `TextBoxExt` control:

| Method                  | Description                            |
| ----------------------- | -------------------------------------- |
| `Set(string text)`     | Sets the text in the `TextBoxExt`.     |
| `SelectText(string selText, object start, object length)` | Selects the text in the `TextBoxExt`. |

### ThemedCheckButton Methods
Below are the methods for the `ThemedCheckButton` control:

| Method                  | Description                           |
| ----------------------- | ------------------------------------- |
| `Set(string chkState)` | Sets the `CheckState` of the `CheckBox` in the `DateTimeAdv`. |
| `string GetCheckState()` | Gets the `CheckState` of the `CheckBox` in the `DateTimeAdv`. |

### TreeViewAdv Methods
Below are the methods for managing nodes in the `TreeViewAdv` control:

| Method                                             | Description                                           |
| -------------------------------------------------- | ----------------------------------------------------- |
| `CollapseNode(string fullPath)`                  | Collapses the specified node.                          |
| `ExpandNode(string fullPath)`                    | Expands the specified node.                            |
| `SetCheckState(string fullPath, string checkState)` | Sets the specified state of the `CheckBox/OptionButton` for the specified node. |
| `SelectNodeWithModifierKeys(string fullPath, string ctrl, string shift)` | Selects the specified node according to the selection mode. |
| `BackupNodeDetails(string fullPath)`             | Backs up the node details before editing.             |
| `EditNode(string nodeText)`                      | Edits the specified node.                             |
| `DragDrop(string fullPath)`                      | Performs the drag and drop operation for nodes in the `SelectedNodes` list, added during the drag-over event. |
| `AddToSelectedNodeList(string fullPath)`         | Adds the specified node into the selected node list during the drag-over event. |
| `DoubleClick(string fullPath)`                   | Handles the double-click event of `TreeViewAdv`.       |

## API Reference (if applicable)
- **Namespace**: `Syncfusion.WinForms.Controls`
- **Class**: `TextBoxExt`
  - **Methods**:
    - `Set(string text)`
    - `SelectText(string selText, object start, object length)`
- **Class**: `ThemedCheckButton`
  - **Methods**:
    - `Set(string chkState)`
    - `string GetCheckState()`
- **Class**: `TreeViewAdv`
  - **Methods**:
    - `CollapseNode(string fullPath)`
    - `ExpandNode(string fullPath)`
    - `SetCheckState(string fullPath, string checkState)`
    - `SelectNodeWithModifierKeys(string fullPath, string ctrl, string shift)`
    - `BackupNodeDetails(string fullPath)`
    - `EditNode(string nodeText)`
    - `DragDrop(string fullPath)`
    - `AddToSelectedNodeList(string fullPath)`
    - `DoubleClick(string fullPath)`

## Code Examples (multi-language supported)
The methods can be used in your application as shown below:

```csharp
using Syncfusion.WinForms.Controls;

// Example for TextBoxExt
TextBoxExt textBox = new TextBoxExt();
textBox.Set("Hello, World!");
textBox.SelectText("Hello", 0, 5);

// Example for ThemedCheckButton
ThemedCheckButton checkBox = new ThemedCheckButton();
checkBox.Set("Checked");
string currentState = checkBox.GetCheckState();

// Example for TreeViewAdv
TreeViewAdv treeView = new TreeViewAdv();
treeView.CollapseNode("/NodePath");
treeView.EditNode("Node Text");
```

## Page-level Navigation/TOC (if applicable)
- **TextBoxExt Methods**
- **ThemedCheckButton Methods**
- **TreeViewAdv Methods**
- **API Reference**
- **Code Examples**

## Cross References
- See also: Methods for DateTimeAdv, CheckBox, OptionButton, and related controls.

## RAG Annotations
<!-- tags: [TextBoxExt, ThemedCheckButton, TreeViewAdv, Methods, Syncfusion Winforms, 11.4.0.26] keywords: [Set, SelectText, CheckState, Node, DragDrop, DoubleClick, Expand, Collapse] -->
```

---

<!-- 페이지 39 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_062.jpeg
document_name: QTP
page_number: 062
page_id: QTP#page_062
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:05:24Z
fidelity: lossless
-->

# ChartControl

## Method Description

| Method                              | Description                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| **RegionClick(double x, double y)** | The point on the chart region to be clicked.                                                               |
| **RegionRightClick(double x, double y)** | The point on the chart region to be right-clicked.                                                       |
| **RegionDoubleClick(double x, double y)** | The point on the chart region to be double-clicked.                                                   |
| **TitleClick(int x, int y)**       | The region on the title to be clicked.                                                                     |
| **LegendClick(int x, int y)**      | The region on the legend to be clicked.                                                                   |
| **SetItemCheckState(string itemtext, string checkstate)** | Setting the legend item check box.                                                       |
| **SetLegendFloatingLocation(int x, int y)** | The location of the legend if it is floating.                                                      |
| **SetLegendNonFloatingLocation(object pos, object align)** | The location of the fixed position in or on the QTP.                                     |
| **SetTitleFloatingLocation(int x, int y)** | The location of the legend if it is floating.                                                      |
| **SetTitleNonFloatingLocation(object pos, object align)** | The location of the fixed position in or on the QTP.                                     |
| **ZoomXAxis(object min, object max)** | The values of X-coordinates to zoom the chart.                                                           |
| **ZoomYAxis(object min, object max)** | The values of Y-coordinates to zoom the chart.                                                           |
| **int GetSeriesCount();**         | Gets the count of series within the chart.                                                                 |
| **int GetPointsCount(int series);** | The point count on the specified series.                                                                 |
| **double GetMaxYValue(int series, int point);** | The maximum Y-value of the specified point.                                                   |
| **double GetXvalue(int series, int point);** | The X-value of the specified point.                                                                |
| **string GetChartType(int series);** | Gets the type of the chart.                                                                              |
| **string GetXAxisText();**       | Gets the text that appeared on the X-axis.                                                                |
| **string GetYAxisText();**       | Gets the text that appeared on the Y-axis.                                                                |

## Copyright Information
© 2013 Syncfusion. All rights reserved.
<!-- tags: [ChartControl, methods, description, syncfusion, winforms, QTP, version:11.4.0.26] keywords: [RegionClick, RegionRightClick, RegionDoubleClick, TitleClick, LegendClick, SetItemCheckState, SetLegendFloatingLocation, SetLegendNonFloatingLocation, SetTitleFloatingLocation, SetTitleNonFloatingLocation, ZoomXAxis, ZoomYAxis, GetSeriesCount, GetPointsCount, GetMaxYValue, GetXvalue, GetChartType, GetXAxisText, GetYAxisText] -->
```

---

<!-- 페이지 40 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_066.jpeg
document_name: QTP
page_number: 066
page_id: QTP#page_066
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:05:41Z
fidelity: lossless
-->

# Docking Manager

- When two controls are in tabbed style and you click on the inactive tab and drag it outside the tabbed mode, it will not replay properly. In order to avoid this problem, select the tab that is going to be dragged, click on the tab, and drag it outside.
- When a floating form state is changed to an MDIChild state and MDIChild state is changed to a floating form state, it will not replay properly.

## Ribbon Control

The Quick access panel customize menu will not be recorded.

<!-- tags: [Winforms, Docking Manager, Ribbon Control, version 11.4.0.26] keywords: [tabbed style, inactive tab, MDIChild state, floating form state, replay, Quick access panel customize menu] -->
``` 


---

<!-- 페이지 41 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_070.jpeg
document_name: QTP
page_number: 070
page_id: QTP#page_070
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:05:49Z
fidelity: lossless
-->

## Essential QuickTest Professional

### Overview
- An image showcasing the "Essential QTP Configurator" for configuring the SwfConfig.xml file.
- Steps to configure and save the SwfConfig.xml file and restart QTP for updated control mappings.
- Reference to the SwfConfig.xml file and its role in test setup.

### Content

#### QTP Configuration Setup
The "Essential QTP Configurator" is a tool used to configure the SwfConfig.xml file. This file is crucial for mapping controls in the test environment. Below is a step-by-step process to set up the configuration:

1. **Configure SwfConfig file**:  
   - **QTP Assemblies Location**:  
     ```
     Files (x86)\Syncfusion\Essential QTP\10.4.0.53\bin\3.5
     ```
   - **Product Version**:  
     ```
     10.403.0.53
     ```

2. **Assembly Details**:
   Below is a table listing assemblies and their details:
   | AssemblyName             | ProductVersion | Date Modified | Size   |
   |--------------------------|----------------|---------------|-------|
   | ButtonAdv.dll           | 10.403.0.53    | 1/23/2013     | 6.5 KB |
   | CalculatorControl.dll   | 10.403.0.53    | 1/23/2013     | 7.5 KB |
   | ChartControl.dll        | 10.403.0.53    | 1/23/2013     | 28 KB  |
   | CheckBoxAdv.dll         | 10.403.0.53    | 1/23/2013     | 6.5 KB |
   | ColorPickerUIAdv.dll    | 10.403.0.53    | 1/23/2013     | 7.5 KB |
   | ComboBoxAutoComplete.dll| 10.403.0.53    | 1/23/2013     | 16 KB  |
   | ComboBoxDropDown.dll    | 10.403.0.53    | 1/23/2013     | 16 KB  |
   | CommandBar.dll          | 10.403.0.53    | 1/23/2013     | 20 KB  |

3. **Configuration Report**:
   - Click **Check & Configure** to ensure all assemblies are correctly mapped.
   - Click **Save Report** to save the configuration details.

4. **File Confirmation Prompt**:
   Upon configuration completion, a dialog appears asking if you want to open the swfconfig.xml file:
   ```
   Swfconfig.Xml file configured.
   Do you want to open the swfconfig.xml file?
   Yes | No
   ```

#### Restart QTP for Updated Mappings
5. **Restart QTP**:  
   Restart QTP once the SwfConfig.xml file is saved to refresh the mappings to the required controls before starting the test.

### Figure Reference
- **Figure 32**: Opening the new SwfConfig.xml File
  This figure shows the dialog confirming the completion of the SwfConfig.xml file configuration and the option to open the file.

## See also
- Documentation on QTP test environments and control configurations
- Reference to product version and assembly details

<!-- tags: [syncfusion-qtp, winforms, essential-qtp-configurator] keywords: [swfconfig, qtp testing, controls mapping] -->
```

---

<!-- 페이지 42 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_074.jpeg
document_name: QTP
page_number: 074
page_id: QTP#page_074
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:06:12Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview
- Configuring QTP assemblies and swfconfig file settings.
- Entering the location of QTP assemblies and product version details.
- Validating swfconfig file references and saving the configuration.

## Content

### Configuring QTP Assemblies

1. Open the "Essential QTP Configurator" window.
   - The window provides fields to configure the swfconfig file along with QTP Assemblies Location and Product Version.
   - Below is an example screenshot of the configurator:

   ![Essential QTP Configurator Window](image)

2. Enter the QTP assemblies' location in the **QTP Assemblies Location** textbox.
   - Example path: `Files (x86)\Syncfusion\Essential QTP\10.4.0.53\bin\3.5`

3. Enter the Essential Studio version with framework in the **Product Version** textbox.
   - Example version: `10.403.0.53`

4. After entering the details, click **Check & Configure**.
   - This step will validate the swfconfig file.

5. If the swfconfig file holds the valid reference path, the swfconfig utility shows the dialog box to save the `swfconfig.xml` file.

### Step-by-Step Configuration

Here's the step-by-step process for configuring QTP assemblies:

1. **Open the Configurator:**
   - Launch the "Essential QTP Configurator".

2. **Enter the QTP Assemblies Location:**
   - In the **QTP Assemblies Location** textbox, input the path to the QTP assemblies.
     - Example: `Files (x86)\Syncfusion\Essential QTP\10.4.0.53\bin\3.5`

3. **Enter the Product Version:**
   - In the **Product Version** textbox, input the version of the Essential Studio framework.
     - Example: `10.403.0.53`

4. **Check Configuration:**
   - Click the **Check & Configure** button to validate the swfconfig file.

5. **Save the Configuration:**
   - If the configuration is valid, the swfconfig utility will display a dialog to save the `swfconfig.xml` file.

   ![Final Configurator Window](image)

## API Reference

- **Configure SwfConfig file**
- **QTP Assemblies Location** 
- **Product Version**

## Code Examples

```xml
<AssemblyInfo>
    <AssemblyLocation>Files (x86)\Syncfusion\Essential QTP\10.4.0.53\bin\3.5</AssemblyLocation>
    <ProductVersion>10.403.0.53</ProductVersion>
</AssemblyInfo>
```

## Tags and Keywords
<!-- tags: [QTP, swfconfig, Essential Studio, WinForms, product version] keywords: [Essential QTP Configurator, QTP Assemblies Location, Product Version, swfconfig.xml, swfconfig file] -->
```

---

<!-- 페이지 43 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_078.jpeg
document_name: QTP
page_number: 078
page_id: QTP#page_078
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:06:30Z
fidelity: lossless
-->

## Why are Syncfusion controls not recognized even after adding the custom libraries?

The following are the troubleshooting steps to get the Syncfusion controls recognized in the QTP environment.

1. Make sure that the DLL path of the custom libraries is properly written in the SwfConfig.xml file. Refer to the Configuring Essential QuickTest Professional topic in this user guide for more details.
2. There are chances for typing errors to occur in the SwfConfig.xml. Ensure that there are no typing errors in the file and try replacing SwfConfig.xml at the correct location and restart QTP.
3. Sometimes the Syncfusion controls may not be recognized due to differences in the version numbers of Essential Studio and Essential QuickTest Professional, or .NET framework and Essential QuickTest Professional that are being used. Check if the version numbers of the assembly that is used to build the application and the Essential QuickTest Professional assembly are the same. If not, this can be solved by rebuilding the Custom Libraries with the required Syncfusion references and .NET framework. If you do not have the corresponding versions of Essential QuickTest Professional and Essential Studio, please contact us specifying the version of Essential QuickTest Professional that is required.
4. If the DLLs are the right version and are mapped correctly, and if the SwfConfig.xml is perfect, but there is still an issue of recognizing Syncfusion controls, then reinstall the .NET add-in for QTP. If the AUT (Application Under Test) is recorded as a WinObject (object in the Windows Environment), make a cross check with a small .NET application using a non-Syncfusion control to see if this control is also not recognized. If so, the problem is with the QTP or .NET add-in installed. Thus, we can isolate the problem with the .NET controls being recognized. SwfObject would be the right way to be recognized after the .NET add-in install.

## How do I know that Essential QuickTest Professional works as expected?

When Syncfusion control events are recorded, they should be able to record with the method that is handled in the custom library (DLL). This will not occur if the mapping is not correct. If the mapping in the DLLName tag of the SwfConfig.xml does not point to the required DLL, the recording would be seen as in the sample script below, which is a low-level recording already explained in the document.

```csharp
[QTP]
SwfWindow("GridDataBoundGrid CellTypes").SwfObject("gridDataBoundGrid2").SetCurrentCell 1,2
```
```

---

<!-- 페이지 44 -->

```markdown
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_082.jpeg
document_name: QTP
page_number: 082
page_id: QTP#page_082
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:06:45Z
fidelity: lossless
-->

# 7.3 Essential Tools

## Overview
- Explanation of methods to select XPToolBar and check/uncheck CheckBoxAdv controls in QTP testing.
- Description of supported methods and use case scenarios for these controls.
- Methods table including descriptions, parameters, and return types.

### 7.3.1 How to select the XPTool bar without ID

The `Select` method is used to select the `Barltem` of the `XPToolBar`. The click action is performed to select the `Barltem` of a tool.

#### Supported method to select the Barltem of XPToolBar
The select method selects the `Barltem` of the `XPToolBar`. The click action is performed to select the `Barltem` of a tool.

#### Use Case Scenarios
This feature enables you to select the `Barltem` of `Xptools` while clicking on a `Barltem` in QTP testing.

#### Methods Table

| Method   | Description                          | Parameters                               | Return Type |
|----------|--------------------------------------|------------------------------------------|-------------|
| Select   | Select the Barltem of XPToolBar     | public void Select(string ID)           | Void        |
|          | Essential Tools                     |                                          |             |

#### Applying GetDescription Method in QTP
The following code example illustrates how to use the `select` method.

```csharp
SwfWindow("XPToolBarDemo").SwfObject("XPToolBar1").Select("ID")
```

### 7.3.2 How to check and uncheck the CheckBoxAdv

#### Supported method to check status of CheckBoxAdv
The `GetCheckState` method is used to find whether the `checkBoxAdv` is in checked or unchecked status. This method returns the answer in string.

#### Use Case Scenarios
This feature enables you to find whether the `checkBoxAdv` is checked or unchecked in QTP testing.

#### Methods Table

| Method      | Description                      | Parameters | Return Type |
|-------------|----------------------------------|------------|-------------|
| GetCheckState | Determine whether CheckBoxAdv is checked or unchecked. | None     | String    |

## API Reference (if applicable)
- **Namespace**: Syncfusion.WinForms.Controls
- **Class**: CheckBoxAdv
  - **Methods**:
    - `GetCheckState()`: Returns the check state of the CheckBoxAdv.

## Code Examples (multi-language supported)
- The example demonstrates how to interact with `XPToolBar` and `CheckBoxAdv` controls using QTP scripting.

```csharp
// Example to select a Barltem without ID
SwfWindow("XPToolBarDemo").SwfObject("XPToolBar1").Select("ID");

// Example to check the state of CheckBoxAdv
SwfWindow("Form").SwfObject("CheckBoxAdv1").GetCheckState();
```

## Page-level Navigation/TOC (if applicable)
- 7.3 Essential Tools
  - 7.3.1 How to select the XPTool bar without ID
  - 7.3.2 How to check and uncheck the CheckBoxAdv

## Cross References
- See also: 
  - XPToolBar for more information on toolbar interaction.
  - CheckBoxAdv for more details on checkbox functionality.

<!-- tags: [Scripting, QTP, syncing, XPToolBar, CheckBoxAdv] keywords: [XPToolBar, Barltem, CheckBoxAdv, GetCheckState, Select, QTP] -->
```

---

<!-- 페이지 45 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_086.jpeg
document_name: QTP
page_number: 086
page_id: QTP#page_086
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:07:06Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Use Case Scenarios

This feature enables you to get the maximum Y-axis value of a specified region in QTP testing.

### Methods Table

| Method        | Description                                                              | Parameters                                                                  | Return Type |
|---------------|--------------------------------------------------------------------------|------------------------------------------------------------------------------|-------------|
| GetMaxYValue | Get the                                                                 | public double GetMaxYValue(int series, int point)                       | double      |
|               | Maximum Y axis value of specified region in Essential Chart.          |                                                                              |             |

### Applying GetMaxYValue Method in QTP

The following code example illustrates how to get the displayed text.

```csharp
[For Chart Control]

MsgBox(SwfWindow("ChartDemo").SwfObject("chart1").GetMaxYValue(10,2))
```

### 7.5 Essential Schedule

#### 7.5.1 How to reschedule the appointment to another timeline

##### Supported method to reschedule the appointment to another timeline in the schedule control

The ItemDrag method is used to reschedule the appointment to another timeline in the schedule control. The appointments are rescheduled to other dates based on the given start and end time.

##### Use Case Scenarios

This feature enables you to reschedule the appointment to another timeline in the schedule control in QTP testing.

#### Methods Table
| Method  | Description | Parameters | Return Type |
|---------|-------------|------------|-------------|
|         |             |            |             |
|         |             |            |             |

---

<!-- tags: [product, module, control, api, version?] keywords: [k1, k2, ...] -->
```

---

<!-- 페이지 46 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_090.jpeg
document_name: QTP
page_number: 090
page_id: QTP#page_090
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:07:18Z
fidelity: lossless
-->

# Resizing Nodes in Diagram Control

## Overview
- Explains how to resize nodes in a diagram control using the `ResizeNode` function.
- Includes examples demonstrating the usage of `ResizeNode` in QTP.

## Content

### Method Description

Below is a table summarizing the method details:

| **Method Name** | **Description** | **Signature** | **Return Type** |
|------------------|------------------|---------------|------------------|
| **ResizeNode** | Resizes the node in diagram control. | public void ResizeNode(string name, float offsetX, float offsetY) | void |

### Applying ResizeNode in QTP

The following code examples illustrate how to resize the node size in the diagram control.

#### Code Example for Diagram Control

```csharp
[For Diagram Control]
SwfWindow("Simple Flow Diagram").SwfObject("diagram1").SelectNode("EllipseStart"
SwfWindow("Simple Flow Diagram").SwfObject("diagram1").ResizeNode("LineConnectror1",-42.467853,0.00000
```

### API Reference

#### Namespace: `DocuSyncfusionQuickTestProfessional`

##### Method: `ResizeNode`

**Signature:**
```csharp
public void ResizeNode(string name, float offsetX, float offsetY)
```

**Parameters:**
- **name:** Type - `string`  
  Description - The name of the node to resize.
- **offsetX:** Type - `float`  
  Description - The horizontal offset for resizing.
- **offsetY:** Type - `float`  
  Description - The vertical offset for resizing.

**Returns:**
- `void`

### Code Examples

#### Example 1: Resizing a Node in a Diagram Control

```csharp
// Selects a specific node in the diagram control
SwfWindow("Simple Flow Diagram").SwfObject("diagram1").SelectNode("EllipseStart"

// Resizes the selected node using specified offsets
SwfWindow("Simple Flow Diagram").SwfObject("diagram1").ResizeNode("LineConnectror1",-42.467853,0.00000
```

## Page-level Navigation/TOC (if applicable)
- Applying ResizeNode in QTP
- API Reference
- Code Examples

<!-- tags: [syncfusion, qtp, diagram control, resize node, code examples] keywords: [resize, node, diagram, qtp, method, signature, parameters, return, code example, swfwindow, flow diagram, ellipsetart, lineconnectror, offset] -->
```

---

<!-- 페이지 47 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_003.jpeg
document_name: QTP
page_number: 003
page_id: QTP#page_003
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:01:23Z
fidelity: lossless
-->

# Frequently Asked Questions

## Overview
- Covers general troubleshooting and configuration questions.
- Provides instructions for working with Syncfusion controls in QTP.
- Includes detailed explanations for Essential Grid, Tools, Chart, Schedule, and Diagram.

## Content

### 7.1 General
- **7.1.1 How to manually configure Syncfusion control to work with QTP**
- **7.1.2 How to know whether my swfconfig file holds an invalid assembly path reference**
- **7.1.3 How to fetch installation information related to the Syncfusion QTP add-on**
- **7.1.4 Why are Syncfusion controls not recognized even after adding the custom libraries?**
- **7.1.5 How do I know that Essential QuickTest Professional works as expected?**

### 7.2 Essential Grid
- **7.2.1 How to get the description of the Check Box Cells and Normal Cells in Essential Grid**
- **7.2.2 How to set the current cell in Grid**

### 7.3 Essential Tools
- **7.3.1 How to select the XPTool bar without ID**
- **7.3.2 How to check and uncheck the CheckBoxAdv**
- **7.3.3 How to collapse and expand the specified node in TreeViewADV**

### 7.4 Essential Chart
- **7.4.1 How to get the displayed text in the X-axis and Y-axis**
- **7.4.2 How to find the count of a series within the chart**
- **7.4.3 How to find the maximum Y-axis value in the specified region**

### 7.5 Essential Schedule
- **7.5.1 How to reschedule the appointment to another timeline**
- **7.5.2 How to reschedule the timeline of an appointment**

### 7.6 Essential Diagram
- **7.6.1 How to change the node to a new position**
- **7.6.2 How to connect the specified nodes using connectors**
- **7.6.3 How to resize the node**

<!-- tags: Syncfusion Winforms, QTP, Essential QuickTest Professional, configuration, troubleshooting, Essential Grid, Essential Tools, Essential Chart, Essential Schedule, Essential Diagram, Syncfusion Controls, swfconfig, assembly path, Custom Libraries, XPTool bar, CheckBoxAdv, TreeViewADV, X-axis, Y-axis, appointment timeline, nodes, connectors, resizing -->
```

---

<!-- 페이지 48 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_007.jpeg
document_name: QTP
page_number: 007
page_id: QTP#page_007
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:01:38Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Installation and Deployment

This section covers information on the install location, samples, licensing, and uninstallation of the recent version of Essential QuickTest Professional.

### Installation and Configuration

This topic explains the installation process for Syncfusion Essential QuickTest Professional and the configuration details about the `swfconfig` file.

#### Installation

This section provides specifics on the installation of Syncfusion Essential QuickTest Professional.

To install Essential Test Studio:

> **Note:** The installation procedures are the same for every Essential Test Studio setup, regardless of the volume of the Test setup.

1. Double-click the Syncfusion Essential Test Studio Setup file.

> **Note:** Setup - Syncfusion Essential QuickTest Professional dialog box opens.

![Syncfusion Essential QTP Setup Screenshot](images/syncfusion_essential_qtp_setup.png)

**Figure:** Syncfusion Essential QTP 11.1.0.21 Setup Window

The **Setup Wizard** will install Syncfusion Essential QTP 11.1.0.21 on your computer. Click "Next" to continue or "Cancel" to exit the Setup Wizard.

## Footer
© 2013 Syncfusion. All rights reserved.

<!-- tags: [syncfusion, qtp, installation, configuration, setup] keywords: [syncfusion, essential quicktest professional, essential test studio, swfconfig, 11.1.0.21, setup wizard] -->
```

---

<!-- 페이지 49 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_011.jpeg
document_name: QTP
page_number: 011
page_id: QTP#page_011
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:01:49Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview
- Installation options for Syncfusion Essential QTP
- Selection of different install types: Typical, Custom, Complete
- Next steps after choosing an install option

## Content

### Syncfusion Essential QTP Installation Options
The Syncfusion Essential QTP installer offers three installation options, each tailored to different user needs and requirements:

1. **Typical**
   - Installs the most common program features.
   - Recommended for most users.
   - Icon: Illustrates a standard setup.

2. **Custom**
   - Allows users to choose which program features will be installed and where they will be installed.
   - Recommended for advanced users.
   - Icon: Indicates a customizable setup.

3. **Complete**
   - All program features will be installed.
   - Requires the most disk space.
   - Icon: Shows a full setup.

### Installation Steps
Once the installation option is selected:
1. Click `Next`.
2. The `Ready to Install` dialog will open.

## Figure: Installation Options Screen

**Figure 5: Installing options Screen**

## Summary
This page details the installation options available for Syncfusion Essential QTP, along with the instructions to proceed with the installation process.

## API Reference
None

## Code Examples
None

## Page-level Navigation/TOC
- Typical Installation
- Custom Installation
- Complete Installation
- Next Step: Ready to Install

## Cross References
- None

<!-- tags: [quicktest, prof, syncfusion, winforms, installation, qtp, version:11.4.0.26] keywords: [installation options, typical, custom, complete, ready to install, qtp] -->
```


---

<!-- 페이지 50 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_015.jpeg
document_name: QTP
page_number: 015
page_id: QTP#page_015
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:02:01Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview
- Provides details on手动配置 `swfconfig` 文件。
- Explains the steps to configure QTP to use the custom libraries shipped with Essential QuickTest Professional.

## Content

### 2.1.2.2 Manual Configuration

This section provides details about the manual configuration of the `swfconfig` file.

#### Steps to Configure QTP to use the Custom Libraries shipped in Essential QuickTest Professional

1. Navigate to the following path:
   ```
   (Installed location of Essential QuickTest Professional)\Config
   ```
   <!-- Note: You will find three folders, named 2.0, 3.5 and 4.0 here. The folders 2.0, 3.5 and 4.0 consist of swfconfig files for .NET 2.0, .NET 3.5 and .NET 4.0 frameworks respectively. -->
   
2. Open the `swfconfig` file by double-clicking it. You can view the mapping for all the supported controls here. The sample code below maps the grid control to its corresponding DLL.

#### Example Mapping in XML

```xml
[XML]

<CC Control Type="Syncfusion.Windows.Forms.Grid.GridControl">
<CustomRecord>
<Component>
<Context>AUT</Context>
<DllName>C:\Program files\Syncfusion\Essential TestStudio\<Version Number>\Bin\2.0\GridControl.dll</DllName>
<TypeName>Syncfusion.TestStudio.Grid.GridControl</TypeName>
</Component>
</CustomRecord>
<CustomReplay>
<Component>
<Context>AUT</Context>
<DllName>C:\Program files\Syncfusion\Essential TestStudio\<Version number>\Bin\2.0\GridControl.dll</DllName>
<TypeName>Syncfusion.TestStudio.Grid.GridControl</TypeName>
</Component>
</CustomReplay>
</Control>
```

#### Note on DLL Path

In the preceding code, the fully qualified name of the DLL given in the `<DllName>` tag assumes that you have installed the Essential QuickTest Professional in the following default path:
```
C:\Program Files\Syncfusion\Essential QuickTest Professional\<Version number>\
```

If you have installed Essential QuickTest Professional in any other path, you need to give the correct path of the DLL in all the `<DllName>` tags. For example, if Essential QuickTest Professional is located in `D:\Essential QuickTest Professional\<Version number>`, then the code should be as follows:

## API Reference
- Namespace: `Syncfusion.Windows.Forms.Grid`
- Class: `GridControl`
- DLL: `GridControl.dll`

## Code Examples

### Example: Mapping Grid Control

```xml
<CC Control Type="Syncfusion.Windows.Forms.Grid.GridControl">
<CustomRecord>
<Component>
<Context>AUT</Context>
<DllName>D:\Essential QuickTest Professional\<Version number>\Bin\2.0\GridControl.dll</DllName>
<TypeName>Syncfusion.TestStudio.Grid.GridControl</TypeName>
</Component>
</CustomRecord>
<CustomReplay>
<Component>
<Context>AUT</Context>
<DllName>D:\Essential QuickTest Professional\<Version number>\Bin\2.0\GridControl.dll</DllName>
<TypeName>Syncfusion.TestStudio.Grid.GridControl</TypeName>
</Component>
</CustomReplay>
</Control>
```

## Page-level Navigation/TOC (if applicable)
- Manual Configuration
- Steps to Configure QTP to use the Custom Libraries shipped in Essential QuickTest Professional

## Cross References
- No direct cross references provided on this page.

<!-- tags: [Essential QuickTest Professional, Manual Configuration, swfconfig, QTP, custom libraries, .NET frameworks, Syncfusion, WinForms] keywords: [Manual Configuration, swfconfig file, QTP, custom libraries, .NET frameworks, Syncfusion, WinForms] -->
```

---

<!-- 페이지 51 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_019.jpeg
document_name: QTP
page_number: 019
page_id: QTP#page_019
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:02:24Z
fidelity: lossless
-->

## Syncfusion Windows Forms Controls Mapping

### Grid Controls

| Assembly Name                   | Type Name                                | Control Name                              |
|----------------------------------|------------------------------------------|--------------------------------------------|
| GridControl.dll                 | Syncfusion.TestStudio.Grid.GridControl  | Syncfusion.Windows.Forms.Grid.GridControl |
| GridDataBoundGrid.dll           | Syncfusion.TestStudio.Grid.GridDataGrid | Syncfusion.Windows.Forms.Grid.GridDataGrid |
| GridGroupingControl.dll         | Syncfusion.TestStudio.Grid.GridGroupingControl | Syncfusion.Windows.Forms.Grid.GridGroupingControl |
| GridListControl.dll             | Syncfusion.TestStudio.Grid.GridListControl | Syncfusion.Windows.Forms.Grid.GridListControl |
| TabBarSplitterControl.dll       | Syncfusion.TestStudio.Grid.TabBarControl | Syncfusion.Windows.Forms.TabBarControl      |


### Essential Tools

| Assembly Name                   | Type Name                                | Control Name                              |
|----------------------------------|------------------------------------------|--------------------------------------------|
| RibbonControlAdv.dll            | Syncfusion.TestStudio.Tools.RibbonControlAdv | Syncfusion.Windows.Forms.Tools.RibbonControlAdv |
| DockingManager.dll              | Syncfusion.TestStudio.Tools.DockingManager | Syncfusion.Windows.Forms.Tools.DockingManager |
| XPMenus.dll                     | Syncfusion.TestStudio.Tools.XPMenus      | Syncfusion.Windows.Forms.Tools.XPMenus.BarControlInternal |
| PopupMenu.dll                   | Syncfusion.TestStudio.Tools.XPMenus      | Syncfusion.Windows.Forms.Tools.XPMenus.MenuGrid |
| CommandBar.dll                  | Syncfusion.TestStudio.Tools.CommandBar   | Syncfusion.Windows.Forms.Tools.XPMenus.CommandBarExt |
| XPToolBar.dll                   | Syncfusion.TestStudio.Tools.XPToolBar    | Syncfusion.Windows.Forms.Tools.XPMenus.XPToolBar |
| TreeViewAdv.dll                 | Syncfusion.TestStudio.Tools.TreeViewAdv  | Syncfusion.Windows.Forms.Tools.TreeViewAdv |
| CalculatorControl.dll           | Syncfusion.TestStudio.Tools.CalculatorControl | Syncfusion.Windows.Forms.Tools.CalculatorControl |
| ProgressBarAdv.dll              | Syncfusion.TestStudio.Tools.ProgressBarAdv | Syncfusion.Windows.Forms.Tools.ProgressBarAdv |
```

---

<!-- 페이지 52 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_023.jpeg
document_name: QTP
page_number: 023
page_id: QTP#page_023
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:02:37Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview
- Steps to launch and navigate the QuickTest Professional interface.
- Introduction to the Start Page and Test tabs.
- Description of the features and functionality available in QuickTest Professional.

## Content

### Getting Started
1. **Launching QuickTest Professional**
   - Open the QuickTest Professional application.
   - Click OK to proceed.

2. **Understanding the Start Page**
   - **Description**: The QuickTest Professional – [Start Page] window is displayed. There are two tabs, Start Page and Test, in the main pane of the window. The content under the Start Page tab is displayed by default.

#### Start Page Display

##### QuickTest Professional Interface
- **Welcome Section**:
  - **Welcome to HP QuickTest Professional**, the advanced solution for functional test and regression test automation.
  - This next-generation automated testing solution uses the concept of keyword-driven testing to enhance test creation and maintenance.
  - QuickTest Professional caters to both technical and non-technical users, empowering the entire testing team to create sophisticated test suites.

##### Navigation Bar
- **Process Guidance List**:
  - **Keyword-Driven Testing**
  - **Application Areas**
  - **Business Components**

##### Recently Used Files
- **Submit feedback** about QuickTest on the Send Feedback and Win Web page to become eligible to win prizes in special prize drawings.
- **Don't show the Start Page window on startup**: Check this option if desired.

##### Content Tab
- **What's New?**
  - Manage Your Test Data
  - Test Your GUI and UI-less Application Functionality in One Test
  - New Run Results Viewer
  - Help QuickTest Identify Your Objects as a Manual Tester Would – VISUALLY
  - Collaborate with Developers to Pinpoint Defects Using Log Tracking
  - "Out-of-the-Box" Support for Web 2.0 Toolkit Applications
  - New Web Testing Capabilities
  - New Silverlight Add-in
  - Extend Silverlight and WPF Support
  - Use Extensibility Accelerator for Web Add-in Extensibility Development

#### Figure: QuickTest Professional – [Start Page]
![QuickTest Professional Start Page](image_url_placeholder)

### New Test Creation
- **Click the New Test icon** on the Start Page.

## API Reference (if applicable)
- No specific APIs are mentioned in this section of the documentation.

## Code Examples (if applicable)
- This section does not include any code examples. (If present, provide here.)

## Page-level Navigation/TOC (if applicable)
- Steps to navigate the QuickTest Professional interface are provided in the content section.

## RAG Annotations
- <!-- tags: [quicktest professional, start page, gui testing, ui-less application testing, test automation, keyword-driven testing, process guidance, web applications, silverlight support, wpf support, web add-in extensibility] keywords: [welcome page, new run results viewer, log tracking, silverlight add-in, extensibility accelerator, visual identification, keyword-driven testing, application areas, business components, test data management, gui and ui-less testing, seamless test functionality, collaborative defect pinpointing, web 2.0 toolkit support, web testing capabilities, silverlight support] -->
```

---

<!-- 페이지 53 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_027.jpeg
document_name: QTP
page_number: 027
page_id: QTP#page_027
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:02:55Z
fidelity: lossless
-->

## Overview
- Configuring Record and Run Settings for Windows Applications in QuickTest Professional
- Customizing application testing options
- Adding specific applications for testing

## Content

### Record and Run Settings for Windows Applications

The content under the tab is displayed, as shown in the figure below:

![Record and Run Settings for Windows Applications](#)

**Figure 14: Record and Run Settings-Windows Applications**

**Note:** The `Record and run only on` option button is selected by default, and the check boxes selected under it ensure that only the applications opened by QuickTest and added applications are tested.

1. **To add an application for testing**, click the + button in the `Application details:` frame as shown in the figure above.

## API Reference

No specific API reference provided in this content.

## Code Examples

No code examples provided in this content.

## Cross References

See also:
- [Record and Run Settings Overview]
- [Customizing Application Testing in QTP]

<!-- tags: [Windows Applications, Record and Run Settings, QuickTest Professional, Application Testing, Syncfusion Winforms, QTP] keywords: [record, run, settings, test, applications, configuration, default options, custom testing, application details, application testing, Windows-based applications, Syncfusion] -->
```

---

<!-- 페이지 54 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_031.jpeg
document_name: QTP
page_number: 031
page_id: QTP#page_031
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:03:05Z
fidelity: lossless
-->

## Overview
- Demonstrates the use of high-level recording in QuickTest Professional (QTP) for Syncfusion controls.
- Highlights differences between high-level and low-level recording methods.
- Provides an example of Syncfusion control recognition in QTP.

## Content

### High-Level Recording in QuickTest Professional

The image shows a QuickTest Professional interface executing a script targeting a Syncfusion GridControl. The grid displays various types of cells, including:

- **CheckBox Cells**: Cell A3 and B3 with checkboxes.
- **PushButton Cells**: Cell A7 and B7 with push buttons labeled "PushButton 1" and "PushButton 2".
- **Password Cells**: Cell A10 is filled with asterisks to represent password input.
- **Currency Cells**: Cells A13 and B13 display monetary values: "$456.00" and "(€739.00)".
- **MaskEdit Cells**: Cell A16 and B16 show formatted input: "(440-091-11)" and "( -- )".
- **Formula Cell**: Cell G6 contains a formula: "4 + 2 + 2 = 8".
- **Radio Button Cells**: Cell A19 and B19 with radio buttons labeled "radio 0" and "radio 1".

The script recorded in QTP includes the following commands:

```plaintext
1: SwWindow("GridControl").Activate
2: SwWindow("GridControl").SwObject("gridControl1").SetCurrentCell 14,4
3: SwWindow("GridControl").Move 336,246
4: SwWindow("GridControl").SwObject("gridControl1").SetCurrentCell 15,6
```

#### Explanation of Recording

This is called **high-level recording** because:

- The events are recorded with the method names of the `Syncfusion` namespace after QTP recognizes the Syncfusion control.
- Unlike low-level recording, where the Syncfusion controls are not recognized by QTP, and events are recorded using default method names.

**Low-Level Recording vs. High-Level Recording**:

- **Low-Level Recording**: QTP does not recognize Syncfusion controls and records events using default method names.
- **High-Level Recording**: QTP recognizes Syncfusion controls and records events with the correct method names, providing more precise and maintainable test scripts.

### Observations

- The QTP interface is shown in **Expert View**, indicating a detailed view of the recorded actions.
- The red "Recording" bar at the bottom of the QTP interface indicates that the recording is in progress.
- The grid in the Syncfusion application is clearly demonstrated, illustrating various input types and cell functionalities.

## API Reference

### Namespaces and Methods

#### Syncfusion Namespace
- **SwWindow**: Used to interact with the grid window.
- **SwObject**: Used to manipulate specific objects within the grid.
- **Activate**: Activates the grid control.
- **SetCurrentCell**: Sets the focus to a particular cell in the grid.
- **Move**: Moves the cursor to a specific position.

## Code Examples

### High-Level Recording Example
```csharp
SwWindow("GridControl").Activate;
SwWindow("GridControl").SwObject("gridControl1").SetCurrentCell(14, 4);
SwWindow("GridControl").Move(336, 246);
SwWindow("GridControl").SwObject("gridControl1").SetCurrentCell(15, 6);
```

### Low-Level Recording Example
```csharp
// Default method names without Syncfusion recognition
SwWindow("GridControl").Activate;
SwWindow("GridControl").SwObject("gridControl1").ActiveCell(14, 4);
SwWindow("GridControl").Move(336, 246);
SwWindow("GridControl").SwObject("gridControl1").ActiveCell(15, 6);
```

## Cross References

- Refer to the Syncfusion QuickTest Professional integration documentation for more details on configuration and setup.
- See the QTP user guide for general information on low-level and high-level recording techniques.

## RAG Annotations
<!-- tags: [quicktest professional, qtp, syncfusion gridcontrol, high-level recording, low-level recording, gridcontrol example, api recognition] keywords: [syncfusion, qtp, gridcontrol, high-level, low-level, recording, test automation, checkbox, pushbutton, password, currency, maskedit, formula, radiobutton] -->
```

---

<!-- 페이지 55 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_035.jpeg
document_name: QTP
page_number: 035
page_id: QTP#page_035
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:03:31Z
fidelity: lossless
-->

## Editing a Test

### Overview
- Describes how to edit a test in QuickTest Professional, supporting two views: Keyword view and Expert view.
- Highlights the switching mechanism between views using the tab at the bottom left of the test screen.
- Focuses on managing testing processes using scripts in the Expert view.

### Content

#### Editing a Test

A test can be edited in either the Keyword view or in the Expert view. You can switch between these views by selecting the required tab at the bottom left of the QuickTest Professional test screen.

#### Editing in Expert View

This view is specially provided for the experts in VB script. In the Expert view, the VB scripts are generated while recording. You can also manually write scripts to the existing scripts in this view. So, this view can be used as a tool for managing the testing process in a more controlled manner. You can add scripts to trigger events manually.

**The following image shows adding a script line to the Expert View pane.**

![QuickTest Professional - Expert View Script Pane](https://example.com/path/to/image)

### Figure: QuickTest Professional - Expert View Script Pane

The screenshot displays the Expert View pane in QuickTest Professional, showing various script commands being entered. The script lines include actions such as setting cell data, current cells, clicking, and modifying radiobutton and checkbox states within a `gridControl1` object. The interface provides tools for recording, running, and stopping scripts, as well as managing resources and debugging options.

### Code Examples

```vb
SwfWindow("GridControl").SwfObject("gridControl1").SetCellData 13,2,"-739.00"
SwfWindow("GridControl").SwfObject("gridControl1").SetCurrentCell 16,2
SwfWindow("GridControl").SwfObject("gridControl1").SetCurrentCell 10,2
SwfWindow("GridControl").SwfObject("gridControl1").SetCellData 10,2,"rwftew"
SwfWindow("GridControl").SwfObject("gridControl1").Click
SwfWindow("GridControl").SwfObject("gridControl1").SetCurrentCell 4,1
SwfWindow("GridControl").SwfObject("gridControl1").SetCellCheckBox 4,1,"ON"
SwfWindow("GridControl").SwfObject("gridControl1").SetCurrentCell 4,2
SwfWindow("GridControl").SwfObject("gridControl1").SetCellCheckBox 4,2,"OFF"
```

### RAG Annotations
<!-- tags: [test-editing, expert-view, vb-script, syncfusion-qtp] keywords: [keyword view, expert view, script management, test process, manual triggers] -->
```

---

<!-- 페이지 56 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_039.jpeg
document_name: QTP
page_number: 039
page_id: QTP#page_039
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:03:49Z
fidelity: lossless
-->

## Editing on Keyword View – Drop-down

### Note

All the items under the Item header are represented as a drop-down list.

![Figure 25: Editing on Keyword View – Drop-down](https://i.imgur.com/ExampleImageURL.png)

You can then run the edited test.

**For more details on running the edited test, refer to Editing on Expert View topic.**

---

## 3.4 Saving a Test

Saving a test is like saving any other document or picture. To save a test, follow the steps below:

### Additional Information

<!-- tags: save-test, syncfusion-qtp, version:11.4.0.26 keywords: saving-test, keyword-view, expert-view, drop-down, editing-test -->
```

---

<!-- 페이지 57 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_043.jpeg
document_name: QTP
page_number: 043
page_id: QTP#page_043
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:03:58Z
fidelity: lossless
-->

# Supported Controls and Methods

## Overview

- The controls supported by Essential QuickTest Professional include: Essential Grid, Essential Tools, Essential Chart, Essential Schedule, and Essential Diagram.
- By supported methods, we mean those methods that are recorded in QTP.

## 4 Supported Controls and Methods

The following controls are supported by Essential QuickTest Professional:

- Essential Grid
- Essential Tools
- Essential Chart
- Essential Schedule
- Essential Diagram

**By supported methods, we mean those methods that are recorded in QTP.**

### 4.1 Essential Grid

Essential Grid supports the following controls:

- GridControl
- GridDataBoundGrid
- GridGroupingControl
- GridListControl
- TabBarSplitterControl

The following are the recorded methods and their corresponding descriptions for Essential Grid:

#### Grid Control

| Method                     | Description                                      |
|----------------------------|--------------------------------------------------|
| CellButtonClick(int row, int col) | Raises the click on the cell button.         |
| CellDoubleClick(int row, int col) | Raises the cell double-click.                |
| GetDescription(int row, int col)  | Gets the description of grid cells.         |
| MouseDown(int row, int col, string button) | Raises a click in the grid.             |
| MoveColumn(int fromColumn, int count, int target) | Moves a range of columns.          |
| MoveRow(int from, int count, int target) | Moves a range of rows from the specified location to a target location. |
| ResizeColumn(int fromColumn, int to, int width) | Resizes the specified columns.      |
| ResizeRow(int fromRow, int to, int height) | Resizes the specified rows.           |
| SelectRange(string range, int top, int left, int | Selects the range.                 |

## References

- **Copyright:** © 2013 Syncfusion. All rights reserved.
- **Page:** 43

<!-- tags: [Essential Grid, GridControl, GridDataBoundGrid, GridGroupingControl, GridListControl, TabBarSplitterControl, CellButtonClick, GetDescription, MoveColumn, MoveRow, ResizeColumn, ResizeRow, SelectRange] keywords: [Essential QuickTest Professional, Recorded Methods, Syncfusion Winforms, Grid Control, Grid Methods] -->
```

---

<!-- 페이지 58 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_047.jpeg
document_name: QTP
page_number: 047
page_id: QTP#page_047
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:04:12Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview
- Provides a list of methods and properties for interacting with grid controls.
- Includes functionalities for retrieving cell values, managing grid visibility, sorting columns, and more.
- Focuses on GridControl and GridGroupingControl interactions.

## Content

### GridControl Methods

| Method                              | Description                                                                 |
|-------------------------------------|-----------------------------------------------------------------------------|
| object GetCellData(int row, object col) | For the given Row and Column objects, the cell value of that cell can be obtained. |
| int GetRowCount()                  | Retrieves the number of rows used.                                      |
| ScrollToCell(int rowIndex, int colIndex) | Scrolls the grid so as the cell to be visible for replay.                    |
| HideRow(int from, int to)          | Hides a range of rows specified for the GridControl.                     |
| HideCol(int from, int to)          | Hides a range of columns specified for the GridControl.                   |
| int GetSelectedRowIndex()          | Returns the top row index of the selected row.                            |
| int GetSelectedColIndex()          | Returns the column index of the selected column.                         |
| int GetSelectedRowCount()          | Returns the number of selected rows.                                     |
| int GetSelectedColCount()          | Returns the number of selected columns.                                  |
| string GetSelectedRowRange()       | Returns the Top and Bottom row of the selected row range.                 |
| string GetSelectedColRange()       | Returns the left and right column of the selected column range.          |
| bool IsColSorted(int col)          | Determines whether the column is sorted.                                 |
| string GetColSortOrder(int col)    | Returns the sort order of the sorted column (Ascending or Descending).    |
| string GetName()                   | Gets the name of the Grid DataBoundGrid object.                          |

### GridGroupingControl Methods

| Method                         | Description                     |
|--------------------------------|----------------------------------|
| CellButtonClick(object row, object col) | Raises the cell button click. |
| CellDoubleClick(object row, object col) | Raises the cell double-click. |
| CollapseRecord(object record) | Collapses the record.           |

## Page-level Navigation/TOC (if applicable)
- The page provides detailed information about the methods available for managing grid controls.
- The content is structured to help users understand how to interact with GridControl and GridGroupingControl effectively.

<!-- tags: [Syncfusion, QuickTest Professional, GridControl, GridGroupingControl, WinForms] keywords: [GetCellData, GetRowCount, ScrollToCell, HideRow, HideCol, GetSelectedRowIndex, GetSelectedColIndex, GetSelectedRowCount, GetSelectedColCount, GetSelectedRowRange, GetSelectedColRange, IsColSorted, GetColSortOrder, GetName, CellButtonClick, CellDoubleClick, CollapseRecord] -->
```

---

<!-- 페이지 59 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_051.jpeg
document_name: QTP
page_number: 051
page_id: QTP#page_051
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:04:28Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview

- Describes methods to interact and manipulate tab controls in WinForms applications.
- Lists essential tools and controls supported by Syncfusion WinForms.
- Provides a reference for setting and retrieving properties of tab-related controls.

## Content

### 4.2 Essential Tools

The following controls are supported by Essential Tools.

- ButtonAdv
- CalculatorControl
- CheckBoxAdv
- ColorPickerUIAdv
- ComboBoxAutoComplete
- ComboDropDown
- CommandBar
- DataListView
- DateTimePickerAdv
- DockingManager
- GroupBar
- GroupView
- MultiColumnComboBox
- PopUpMenu
- ProgressBarAdv
- RadioButtonAdv
- RibbonControlAdv
- ScrollerFrame
- TabbedMDI
- TabControlAdv
- XPTaskBar
- TextBoxExt
- ThemedCheckedButton
- TreeViewAdv
- XPMenus
- XPToolBar
- SplitContainerAdv
- TabSplitterContainer
- TrackBarEx
- RangeSlider

### Table of Tab Control Methods

| Method                      | Description                                                                 |
|-----------------------------|-----------------------------------------------------------------------------|
| GetTabName(int index)      | The label in the tab page can be known by passing the index.                 |
| Select(string tab)         | The name of the selected tab.                                               |
| SetSplitterPosition(string tab, int vSplit, int hSplit) | The splitter position in the tab bar page. |

## Code Examples

```csharp
// Example: Selecting a tab by name
tabControl1.Select("Settings");

// Example: Getting the name of a tab using index
string tabName = tabControl1.GetTabName(0);

// Example: Setting the splitter position of a tab
tabControl1.SetSplitterPosition("Design", 250, 150);
```

## Cross References

- Refer to the **User Guide** for detailed information on setting up and configuring tabs and controls in WinForms applications.
- For more details on the SplitContainerAdv and TabSplitterContainer controls, see the respective sections in the **Controls Documentation**.

<!-- tags: [Syncfusion, Winforms, tab control, essential tools] keywords: [tabControl, GetTabName, Select, SetSplitterPosition, ButtonAdv, CheckBoxAdv, ComboDropDown, TabbedMDI, TrackBarEx, RangeSlider] -->
``` 


---

<!-- 페이지 60 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_055.jpeg
document_name: QTP
page_number: 055
page_id: QTP#page_055
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:04:43Z
fidelity: lossless
-->

# GroupView

| Method                | Description                                                                 |
|-----------------------|------------------------------------------------------------------------------|
| SelectItem(object item) | Selects the GroupView item.                                               |
| DropItem(int index, object source) | Drag and drop the GroupView item.                                  |

## MultiColumnComboBox

| Method         | Description                                                                      |
|----------------|----------------------------------------------------------------------------------|
| DropDown()     | Shows the hidden grid in the MultiColumnComboBox.                              |
| SelectIndex(int index) | Selects the given index.                                                 |

## PopupMenu

| Method         | Description                                                                     |
|----------------|---------------------------------------------------------------------------------|
| Select(string barText) | Selects the item from the pop-up menu.                              |

## ProgressBarAdv

| Method           | Description                                                           |
|------------------|----------------------------------------------------------------------|
| SetValue(int value) | Assigns the Progress bar value.                                   |
| int GetValue()  | Gets the current value of the ProgressBar.                            |

## RadioButtonAdv

| Method           | Description                                                             |
|------------------|-----------------------------------------------------------------------|
| Set()           | Changes Checked property to true.                                   |
| bool IsSet()    | Shows whether the RadioButtonAdv is set.                             |

## API Reference
- Name: SelectItem(object item)
  - Description: Selects the GroupView item.
- Name: DropItem(int index, object source)
  - Description: Drag and drop the GroupView item.
- Name: DropDown()
  - Description: Shows the hidden grid in the MultiColumnComboBox.
- Name: SelectIndex(int index)
  - Description: Selects the given index.
- Name: Select(string barText)
  - Description: Selects the item from the pop-up menu.
- Name: SetValue(int value)
  - Description: Assigns the Progress bar value.
- Name: GetValue()
  - Description: Gets the current value of the ProgressBar.
- Name: Set()
  - Description: Changes Checked property to true.
- Name: IsSet()
  - Description: Shows whether the RadioButtonAdv is set.

<!-- tags: [Syncfusion Winforms, GroupView, MultiColumnComboBox, PopupMenu, ProgressBarAdv, RadioButtonAdv] keywords: [SelectItem, DropItem, DropDown, SelectIndex, Select, SetValue, GetValue, Set, IsSet, item, index, barText, value, Checked property] -->
```

---

<!-- 페이지 61 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_059.jpeg
document_name: QTP
page_number: 059
page_id: QTP#page_059
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:04:57Z
fidelity: lossless
-->

# Essential QuickTest Professional Functions

## Content

### Tree Operations

| Method                     | Description                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| SelectNode(string fullPath)| Selects the node in SingleSelect mode.                                    |
| RMouseDown(int x, int y)  | Performs a right mouse click.                                              |
| TreeNodeAdv GetNodeFromPath(string fullPath) | Gets the tree node from the path.                          |
| Point GetPointFromNode(TreeNodeAdv node) | Returns the TextBounds point of the specified node.           |
| RightClickNode(string fullPath) | Right-clicks the specified node.                                      |

### XPMenus Operations

| Method                    | Description                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| Select(string text)      | Performs click on a bar item.                                               |
| string TraceParentRoot(string barItemText) | For the given text of the required menu, TraceParentRoot will retrieve the full path as recoded. |
| int MenuItemPos(string ParentText, string barItemText) | For the given text of the required menu, MenuItemPos will return the position of the menu item. |

### XPToolBar Operations

| Method               | Description                                                          |
|----------------------|----------------------------------------------------------------------|
| Select(string ID)   | Performs click in the baritem.                                         |
| Popup(string ID)    | Shows the popup of the parent bar item.                                |

### XPTaskBar Operations

| Method                   | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| Expand(string headerText)| Expands the content area of the task bar box.                          |
| Collapse(string headerText) | Collapses the content area of the task bar box.                     |
| ItemClick(string headerText, string itemTag) | Performs a click in the item described in the tag. |
```

---

<!-- 페이지 62 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_063.jpeg
document_name: QTP
page_number: 063
page_id: QTP#page_063
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:05:09Z
fidelity: lossless
-->

## 4.4 Essential Schedule

The following are the recorded methods and their corresponding descriptions for Essential Schedule:

### Schedule Control

| Method                              | Description                                              |
|-------------------------------------|----------------------------------------------------------|
| `DblClick(int row, int col)`       | Double-click a schedule row.                            |
| `RightClick(int row, int col)`     | Right-click a schedule row.                             |
| `TimeDrag(int row, int col, object newStartTime, object newEndTime)` | Adjust the timeline for an appointment. |
| `ItemDrag(int row, int col, object newStartTime, object newEndTime)` | Move appointment to some other timeline. |
| `Scroll(int value)`                | Scroll the schedule control.                             |

## 4.5 Essential Diagram

The following are the recorded methods and their corresponding descriptions for Essential Diagram:

### Diagram Control

| Method                                  | Description                                             |
|-----------------------------------------|---------------------------------------------------------|
| `ConnectNodes(string startNode, string endNode, string connector)` | Connects the specified nodes using the connector. |
| `SelectNode(string name)`              | Selects a diagram node.                                 |
| `DblClick(string name)`               | Double-clicks a diagram node.                           |
| `RotateNode(string node, float offset)` | Rotates a diagram node to the given offset.           |
| `ResizeNode(string node, float offsetX, float OffsetY)` | Resizes a diagram node to the given offset. |
| `MoveNode(string node, float offsetX, float OffsetY)` | Moves a diagram node to a new location. |
| `Zoom(float magnification)`           | Zoom the diagram view.                                   |
```

---

<!-- 페이지 63 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_067.jpeg
document_name: QTP
page_number: 067
page_id: QTP#page_067
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:05:21Z
fidelity: lossless
-->

# 6 Utilities

## 6.1 Configuring the SwfConfig file

An XML file in QTP called SwfConfig is the configuration file located at `(Installed location of Essential QuickTest Professional)\Config\<version-2.0, 3.5, or 4.0>\swfconfig`, which contains all the mapping information for QTP to recognize Syncfusion controls. Using the SwfConfig utility, users can easily configure the `SwfConfig.xml` file in HP QTP.

### Steps to Configure the SwfConfig.xml File

1. Open the Syncfusion Essential QTP Configurator located at `(Installed location of Essential QuickTest Professional)\Utilities\SwfConfigUtility\SwfConfigUtility.exe`.
   - Enter the QTP assemblies' location in the **QTP Assemblies Location** textbox.
   - Enter the Essential Studio version with framework in the **Product Version** textbox.
   - After entering the details, click **Check & Configure**. It will create the `swfconfig.xml` file for that particular version.

   ![Creating the SwfConfig.xml File for Essential Studio 10.3](attachment/SwfConfigUtility.png)

   **Figure 29: Creating the SwfConfig.xml File for Essential Studio 10.3**

2. Then Essential QTP Configurator shows the dialog box for appending the `swfconfig.xml` file. Click **Yes** to append the `swfconfig.xml` file in the QTP machine.

<!-- tags: [Essential QuickTest Professional, SwfConfig, Syncfusion controls, QTP, HP, XML configuration, Essential QTP Configurator, SwfConfigUtility. ] keywords: [Essential QuickTest Professional, SwfConfig, Syncfusion controls, QTP, HP, XML configuration, Essential QTP Configurator, SwfConfigUtility, product version, QTP assemblies, creating XML files, appending, verification utility, Essential Studio] -->
```

---

<!-- 페이지 64 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_071.jpeg
document_name: QTP
page_number: 071
page_id: QTP#page_071
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:05:33Z
fidelity: lossless
-->

# 7 Frequently Asked Questions

## 7.1 General

### 7.1.1 How to manually configure Syncfusion control to work with QTP

#### Steps to Configure QTP to use the Custom Libraries shipped in Essential QuickTest Professional

1. Navigate to the following path:
   ```
   (Installed location of Essential QuickTest Professional)\Config
   ```
   **Note:** You will find three folders here: 2.0, 3.5, and 4.0. The folders 2.0, 3.5, and 4.0 consist of `swconfig` files for .NET 2.0, .NET 3.5, and .NET 4.0 frameworks respectively.

2. Open the `swconfig` file by double-clicking it. You can view the mapping for all the supported controls here. Given below is the sample code that maps the grid control to its corresponding DLL.

   ```xml
   [XML]
   <CC ControlType="Syncfusion.Windows.Forms.Grid.GridControl">
     <CustomRecord>
       <Component>
         <Context>AUT</Context>
         <DllName>C:\Program files\Syncfusion\Essential TestStudio\<Version Number>\Bin\2.0\GridControl.dll</DllName>
         <TypeName>Syncfusion.TestStudio.Grid.GridControl</TypeName>
       </Component>
     </CustomRecord>
     <CustomReplay>
       <Component>
         <Context>AUT</Context>
         <DllName>C:\Program files\Syncfusion\Essential TestStudio\<Version number>\Bin\2.0\GridControl.dll</DllName>
         <TypeName>Syncfusion.TestStudio.Grid.GridControl</TypeName>
       </Component>
     </CustomReplay>
   </CC>
   ```

## API Reference (if applicable)
- Namespace, Class, Members (Methods/Properties/Events/Enums) in subsections.
- Parameters table: Name | Type | Description | Default | Required
- Returns: Type + description.
- Exceptions: bullet list.

## Code Examples (multi-language supported)
- Extract ALL code exactly. Use fenced blocks with language: ```csharp, ```vb, ```xml, ```xaml, ```js, ```css, ```ts, ```python.
- Keep full signatures, imports/usings, comments, region markers.
- Inline code in text should be wrapped with backticks.

## Page-level Navigation/TOC (if applicable)
- If the body contains a local Table of Contents for this page, keep it as a bullet/numbered list with links/text as shown. Do not create links that don’t exist.
- Ignore global site TOC or breadcrumbs unless the page explicitly describes them.

## Cross References
- Add See also: bullet list of explicit links/texts present on the page. Do not fabricate.

## RAG Annotations
- At the end, add an HTML comment with tags and keywords derived ONLY from visible content: <!-- tags: [product, module, control, api, version?] keywords: [k1, k2, ...] -->
- Add optional per-section anchors as HTML comments before each H2/H3 to aid chunking, using IDs derived from the heading (kebab-case), e.g., <!-- anchor: QTP#page_071#getting-started -->. Do not add if the heading text is unclear.
```

<!-- tags: [Syncfusion Winforms, QTP, configuration, control mapping, swconfig] keywords: [Syncfusion, Essential QuickTest Professional, grid control, DLL mapping, XML configuration] -->

---

<!-- 페이지 65 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_075.jpeg
document_name: QTP
page_number: 075
page_id: QTP#page_075
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:05:55Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview
- The Essential QTP Configurator tool is used to configure QTP assemblies.
- It checks and configures the swfconfig file based on the specified QTP assemblies location and product version.
- A version conflict error can occur due to invalid assembly reference paths.

## Content

### Configuring SwfConfig File

The Essential QTP Configurator allows you to configure the swfconfig file. Here's a step-by-step guide on how to use it:

1. **Open the Configurator**: Launch the Essential QTP Configurator tool.
2. **Specify Assemblies Location**: Enter the location of the QTP assemblies in the "QTP Assemblies Location" field.
3. **Set Product Version**: Input the required product version in the "Product Version" field.
4. **Check & Configure**: Click the "Check & Configure" button to validate and update the swfconfig file.
5. **Save Report**: After checking and configuring, you can save the report for future reference.

#### Version Conflict Error
If a version conflict error occurs, it indicates that the swfconfig file contains an invalid assembly reference path. Here are the steps to handle this:

1. **Identify the Issue**: Upon encountering the error message box, verify the swfconfig file's contents.
2. **Correct Assembly Reference**: Update the swfconfig file to resolve any incorrect assembly references.
3. **Retry Configuration**: Repeat the configuration process after making necessary corrections.

#### Sample Configuration Interface

The figure below shows the Essential QTP Configurator interface.

![Essential QTP Configurator Interface](attachment)

#### Handling Version Conflicts

If you get the error message box with a version conflict error, the swfconfig file holds an invalid assembly reference path. The interface will prompt you with options to resolve the conflict.

![Version Conflict Dialog](attachment)

### Resolving Version Conflicts

- **Error Dialog**: The tool will display a dialog indicating a version conflict.
- **Action Required**: Address the invalid assembly reference paths in the swfconfig file.
- **Retry Configuration**: After correcting the issue, retry the configuration process.

## API Reference

The Essential QTP Configurator operates by manipulating the swfconfig file, which contains references to various assemblies. Below are the key components involved:

- **AssemblyName**: Lists the names of the assemblies referenced.
- **ProductVersion**: Specifies the version of each assembly.
- **DateModified**: Indicates the last modification date for each assembly.
- **Size**: Displays the size of each assembly.

### Example Table of Assemblies

| AssemblyName             | ProductVersion | DateModified   | Size    |
|--------------------------|----------------|----------------|---------|
| ButtonAdv.dll           | 10.403.0.53    | 1/23/2013      | 6.5 KB  |
| CalculatorControl.dll   | 10.403.0.53    | 1/23/2013      |         |
| ChartControl.dll        | 10.403.0.53    | 1/23/2013      |         |
| CheckBoxAdv.dll         | 10.403.0.53    | 1/23/2013      |         |
| ColorPickerUIAdv.dll    | 10.403.0.53    | 1/23/2013      |         |
| ComboBoxAutoComplete.dll | 10.403.0.53    | 1/23/2013      |         |
| ComboBoxDropDown.dll     | 10.403.0.53    | 1/23/2013      |         |
| CommandBar.dll          | 10.403.0.53    | 1/23/2013      |         |

## Code Examples

### C# Example

```csharp
// Configuring the swfconfig file programmatically
public void ConfigureSwfConfig()
{
    var configurator = new EssentialQTPConfigurator();
    configurator.AssembliesLocation = @"Files (x86)\Syncfusion\Essential QTP\10.4.0.53\bin\3.5";
    configurator.ProductVersion = "10.403.0.53";
    configurator.CheckAndConfigure();
    configurator.SaveReport();
}
```

### XML Configuration

```xml
<swfconfig>
    <assembly name="ButtonAdv.dll" version="10.403.0.53" />
    <assembly name="CalculatorControl.dll" version="10.403.0.53" />
    <!-- Add other assemblies as needed -->
</swfconfig>
```

## RAG Annotations

<!-- tags: [Essential QTP Configurator, swfconfig file, version conflict error, assembly reference path, Syncfusion Winforms] keywords: [QTP, assembly version, configuration tool, error handling, assembly list, product version] -->
```

---

<!-- 페이지 66 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_079.jpeg
document_name: QTP
page_number: 079
page_id: QTP#page_079
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:06:23Z
fidelity: lossless
-->

# Essential QuickTest Professional

```csharp
SwfWindow("GridDataBoundGrid CellTypes").SwfObject("gridDataBoundGrid2").SetCellData 1,2,"435.00"
SwfWindow("GridDataBoundGrid CellTypes").SwfObject("gridDataBoundGrid2").SetCurrentCell 2,1
SwfWindow("GridDataBoundGrid CellTypes").SwfObject("gridDataBoundGrid2").SetCellCheckBox 2,1,"ON"
SwfWindow("GridDataBoundGrid CellTypes").SwfObject("gridDataBoundGrid2").SetCurrentCell 3,1
SwfWindow("GridDataBoundGrid CellTypes").SwfObject("gridDataBoundGrid2").SetCellCheckBox 3,1,"OFF"
```

If the mapping points to the wrong version, then no scripts will be generated. The right version would be the same version as the AUT developed. For an example, if the AUT is developed in 7.3.0.20, the custom libraries (DLLs) should also be developed in 7.3.0.20. This means that Essential QuickTest Professional version 7.3.0.20 is required. With proper versions and proper mapping, the record will appear as shown in the script below:

```csharp
[QTP]
SwfWindow("GridDataBoundGrid CellTypes").SwfObject("gridDataBoundGrid2").SetCurrentCell 1,2
SwfWindow("GridDataBoundGrid CellTypes").SwfObject("gridDataBoundGrid2").SetCellData 1,2,"435.00"
SwfWindow("GridDataBoundGrid CellTypes").SwfObject("gridDataBoundGrid2").SetCurrentCell 2,1
SwfWindow("GridDataBoundGrid CellTypes").SwfObject("gridDataBoundGrid2").SetCellCheckBox 2,1,"ON"
SwfWindow("GridDataBoundGrid CellTypes").SwfObject("gridDataBoundGrid2").SetCurrentCell 3,1
SwfWindow("GridDataBoundGrid CellTypes").SwfObject("gridDataBoundGrid2").SetCellCheckBox 3,1,"OFF"
```

In the above scripts, `SetCurrentCell`, `SetCellData`, and `SetCellCheckBox` are the methods of Grid control.

> For the list of methods that will be recorded for all the supported controls, refer to the Supported Controls topic. You can also visit our Knowledge Base for Essential QuickTest Professional at the following link for more details: [http://www.syncfusion.com/support/kb/tag/QTP](http://www.syncfusion.com/support/kb/tag/QTP)

## 7.2 Essential Grid

<!-- tags: [winforms, essential quicktest professional, grid, dll, aut, testing] keywords: [Essential QuickTest, GridDataBoundGrid, SetCellData, SetCurrentCell, SetCellCheckBox, AUT, version, Syncfusion, WinForms] -->
```

---

<!-- 페이지 67 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_083.jpeg
document_name: QTP
page_number: 083
page_id: QTP#page_083
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:06:40Z
fidelity: lossless
-->

## Overview
- Demonstrates the use of the `GetCheckState` method to get the check state of a `CheckBoxAdv` control.
- Explains how to collapse and expand nodes in `TreeViewADV` using the `CollapseNode` and `ExpandNode` methods.

## Content

### GetCheckState Method
The GetCheckState method retrieves the check state of the `CheckBoxAdv` control.

| GetCheckState | public string GetCheckState() | string |
|---------------|---------------------------------|--------|
| Get the check state of the `CheckBoxAdv` control in **Essential Tools**. |  |  |

#### Applying GetCheckState Method in QTP
The following code example illustrates how to use the `GetCheckState` method.

```csharp
SwfWindow("QTPCheckBoxAdv").SwfObject("checkBox").GetCheckedState.Set "On"
MsgBox(SwfWindow("QTPCheckBoxAdv").SwfObject("checkBox").GetCheckedState())
```

#### 7.3.3 How to collapse and expand the specified node in TreeViewADV
- **Supported method to collapse and expand the specified node in TreeViewADV**
  - The `CollapseNode` method is used to collapse the specified node in `TreeViewADV`. The path of the node must be passed in the `CollapseNode` method.
  - The `ExpandNode` method is used to expand the specified node in `TreeViewADV`.

**Use Case Scenarios**
This feature enables you to collapse and expand the specified node in `TreeViewADV` in QTP testing.

### Methods Table

| Method       | Description                                   | Parameters                             | Return Type |
|--------------|-----------------------------------------------|----------------------------------------|--------------|
| CollapseNode | Collapse the specified node in `TreeViewADV` in Essential Tools. | public void CollapseNode(string fullPath) | Void        |

## API Reference

### Methods
- **CollapseNode**:  
  - **Description**: Collapses the specified node in `TreeViewADV` in Essential Tools.  
  - **Parameters**:  
    - `string fullPath`: The path of the node to collapse.  
  - **Return Type**: Void  

## Code Examples

### Example: Using CollapseNode
```csharp
SwfWindow("QTPCheckBoxAdv").SwfObject("treeView").CollapseNode("/nodePath");
```

## Page-level Navigation/TOC (if applicable)
- Getting Started
- Methods
- Examples

### Cross References
- See also: `ExpandNode` method, `CheckBoxAdv` control, `TreeViewADV` control

## RAG Annotations
<!-- tags: [Features, checkbox, treeview, control, method, QTP, version 11.4.0.26] keywords: [GetCheckState, CollapseNode, ExpandNode, TreeViewADV, CheckBoxAdv] -->
```

---

<!-- 페이지 68 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_087.jpeg
document_name: QTP
page_number: 087
page_id: QTP#page_087
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:06:57Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview

- Demonstrates how to reschedule appointments in schedule control using the `ItemDrag` and `TimeDrag` methods.
- Explains the parameters and usage of the `ItemDrag` and `TimeDrag` methods in QTP testing.
- Provides code examples for applying `ItemDrag` and `TimeDrag` in QTP.

## Content

### Applying ItemDrag in QTP

The following code example illustrates how to reschedule the appointment in schedule control.

```csharp
[For Schedule Control]
SwfWindow("GridSchedulerDemo").SwfObject("Scheduler").
ItemDrag("Appointment1", "10/02/2012", "14/02/2013", "10/02/2013", "14/02/2014")
```

### 7.5.2 How to reschedule the timeline of an appointment

#### Supported method to reschedule the timeline of an appointment in the schedule control

The `TimeDrag` method is used to reschedule the timeline of the appointment in the schedule control. The appointments are rescheduled to another time based on the new start time and new end time.

#### Use Case Scenarios

This feature enables you to reschedule the timeline of appointments in the schedule control in QTP testing.

### Methods Table

| Method   | Description                                                                 | Parameters                                                                                      | Return Type |
|----------|-----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|-------------|
| TimeDrag | Reschedule the timeline to another appointment in the schedule control. | public void TimeDrag(string apptSubject, string oldStartTime, string oldEndTime, string newStartTime, string newEndTime) | void        |

### Applying TimeDrag in QTP

The following code example illustrates how to reschedule the timeline of the appointment in the schedule control.

---

<!-- tags: [syncfusion, qtp, itemdrag, timedrag, schedule control, appointments, timeline, rescheduling, qtp testing] -->
```

---

<!-- 페이지 69 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_091.jpeg
document_name: QTP
page_number: 091
page_id: QTP#page_091
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:07:10Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Index

### A
- Assembly information 18
- Automatic Configuration 14

### C
- Configuration 14
- Configuring the SwfConfig file 67
- Creating and Recording a Test 22

### D
- Documentation 6

### E
- Editing a Test 35
- Essential Chart 61, 84
- Essential Diagram 63, 88
- Essential Grid 43, 65, 79
- Essential Schedule 63, 86
- Essential Tools 51, 65, 82

### F
- Frequently Asked Questions 71

### G
- General 65, 71
- Getting Started 22

### H
- How do I know that Essential QuickTest Professional works as expected? 78
- How to change the node to a new position 88
- How to check and uncheck the CheckBoxAdv 82
- How to collapse and expand the specified node in TreeViewADV 83
- How to connect the specified nodes using connectors 88
- How to fetch installation information related to the Syncfusion QTP add-on 76

### K
- Known Issues 65

### L
- Licensing, Patches and Uninstallation 18

### M
- Manual Configuration 15

### P
- Prerequisites and Compatibility 5

### R
- Running a Test 33
- Running the Saved Test 40

### S
- Sample and Location 17

### Questions on Obtaining Information within Chart
- How to find the count of a series within the chart 85
- How to find the maximum Y-axis value in the specified region 85

### Questions on Obtaining Information within Grid
- How to get the description of the Check Box Cells and Normal Cells in Essential Grid 80
- How to set the current cell in Grid 81

### Questions on Obtaining Information within Schedule/XPToolbar
- How to get the displayed text in the X-axis and Y-axis 84
- How to select the XPtool bar without ID 82

### Miscellaneous
- How to know whether my swfconfig file holds an invalid assembly path reference 73
- How to manually configure Syncfusion control to work with QTP 71
- How to reschedule the appointment to another timeline 86
- How to reschedule the timeline of an appointment 87
- How to resize the node 89

## Installation and Configuration
- Installation 7
- Installation and Configuration 7
- Installation and Deployment 7

## Introduction
- Introduction to Essential QuickTest Professional 4

<!-- tags: [product, syncfusion, winforms, essential quicktest professional, qtp, user guide, index, windows forms, gui testing, automation, testing tools, version 11.4.0.26] keywords: [installation, configuration, testing, syncfusion, qtp, essential chart, essential diagram, essential grid, essential schedule, essential tools, licensing, patches, uninstallation, manual configuration, prerequisites, compatibility, sample, location, documentation, frequently asked questions, known issues, getting started, running tests, node position, check box, tree view, grid, xptoolbar, resource] -->
```

---

<!-- 페이지 70 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_004.jpeg
document_name: QTP
page_number: 004
page_id: QTP#page_004
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:01:23Z
fidelity: lossless
-->

Essential QuickTest Professional

## Overview

This topic gives an introduction to the new Essential QuickTest Professional. It answers the following questions:
- What is Essential QuickTest Professional and how is it linked with QuickTest Professional (QTP)?
- Who can use the product or for whom is this product intended?
- What is the product used for?

You will also get an overview of what this manual has to offer.

### 1.1 Introduction to Essential QuickTest Professional

Essential QuickTest Professional is an add-on shipped with Essential Studio products offered by Syncfusion. It has been specially designed to meet the requirements of professionals who test the applications designed (using Syncfusion controls) with HP QuickTest Professional software.

Essential QuickTest Professional contains custom libraries, which help HP QuickTest Professional software recognize Syncfusion controls. These custom libraries are built with the help of QuickTest Professional .NET add-in extensibility. For more details, refer to HP QuickTest Professional help.

![Diagram showing the flow of Essential QuickTest Professional integration](Diagram image)

The custom libraries allow Syncfusion controls to be used as a native object inside the QTP testing environment and enable testing of applications in QTP. Essential QuickTest Professional will help you to perform regression test on your application containing Syncfusion controls and thereby increase the reliability of the end product. The following chapters demonstrate the usage of our custom library in QTP.

```markdown

<!-- tags: [product, module, control, api, version?] keywords: [Essential QuickTest Professional, Syncfusion, HP QuickTest Professional, custom libraries, testing environment, regression test, reliability] -->
```

---

<!-- 페이지 71 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_008.jpeg
document_name: QTP
page_number: 008
page_id: QTP#page_008
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:01:35Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview
- Guide to setting up Essential QuickTest Professional.
- Provides a step-by-step process to enter user information and proceed with the installation.
- Applies to Syncfusion Essential QTP 11.1.0.21 Setup.

## Content

### Setup Process
#### Step 1: Initial Setup Screen
- **Figure 1: Setup - Essential QuickTest Professional Welcome screen**
  - Click Next to proceed.

#### Step 2: User Information
- **Figure 2: User Information screen**
  - A screen opens prompting the user to enter:
    - **User Name** in the corresponding text box.
    - **Organization** details.
    - **Unlock Key**.
  - The screen includes an option to **Get a Free Evaluation Key**.

#### Instructions
1. Enter your name, organization, and the license key in the corresponding text boxes.
2. **Note:** Use the Essential Studio Unlock Key as the Unlock Key for Essential Testing Studio.
   - For versions previous to 6.3.0.6, use “Syncfusion199” as the Unlock Key.

### Validation of Unlock Key
3. Click Next. The unlock key will be validated.

## References
- **Syncfusion Inc.**: The developer and provider of the software.

## Copyright
- © 2013 Syncfusion. All rights reserved.

## RAG Annotations
<!-- tags: [essential quicktest professional, user information, setup, syncfusion winforms, license key, unlock key, evaluation key, testing studio, syncfusion software, version 11.1.0.21] keywords: [essential quicktest, user info, setup guides, syncfusion tools, license validation, test studio, setup process, software setup, remote access, technical documentation] -->
```

---

<!-- 페이지 72 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_012.jpeg
document_name: QTP
page_number: 012
page_id: QTP#page_012
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:01:48Z
fidelity: lossless
-->

## Content

### Overview

- The page describes the steps to begin the installation of the Syncfusion Essential QTP 11.1.0.21 Setup.
- It provides instructions for reviewing or changing installation settings and exiting the wizard if needed.
- The installation process is initiated by clicking the "Install" button.

### Installation Wizard

#### Figure 6: Ready to Install Screen

The Syncfusion Essential QTP 11.1.0.21 Setup window is displayed, indicating that the Set-up Wizard is ready to begin the installation of Essential Studio. The user is given the following options:

- **Click "Install"** to begin the installation.
- **Click "Back"** to review or change any of the installation settings.
- **Click "Cancel"** to exit the wizard.

#### Steps to Proceed

9. Click **Install**. The installation process starts displaying the Installing screen as shown in the following screenshot.

## Page-level Navigation/TOC (if applicable)
- None found in the provided content.

## Cross References
- Related to the installation process of Syncfusion Essential QTP.
- Likely part of a larger guide or user manual for QuickTest Professional.

## RAG Annotations
<!-- tags: [installation, setup, syncfusion-essential-qtp, version: 11.1.0.21] keywords: [Syncfusion, Essential QTP, installation wizard, setup screen, install, back, cancel] -->
```

---

<!-- 페이지 73 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_016.jpeg
document_name: QTP
page_number: 016
page_id: QTP#page_016
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:01:58Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview
- Detailed steps for selecting and copying control segments for testing.
- Instructions for modifying the SwfConfig.xml file.
- Example展示了如何将控制元素插入到配置文件中。

## Content

### Configuring Control Testing

#### Step-by-Step Instructions

1. **Select the Control Segments**:
   - Select the segment of the code containing the controls to be tested.

2. **Copy the Selected Code**:
   - On the `Edit` menu, click `Copy`.

   **Note:** While selecting the code for copying, exclude the following lines of code:
   ```xml
   <?xml version="1.0" encoding="UTF-8" ?>
   ```

3. **Open the SwfConfig.xml File**:
   - Open the SwfConfig.xml file located under the following location:
     `<QuickTest Professional Installation Path>\dat\SwfConfig.xml`

4. **Paste into the SwfConfig.xml File**:
   - Paste the copied segment under the `<?xml>` tag in SwfConfig.xml.

   **Note:** The SwfConfig.xml file will look like the following after modification:
   ```xml
   <?xml version="1.0" encoding="UTF-8" ?>
   <Controls>
       <CC>
           <Control Type="Syncfusion.Windows.Forms.Grid.GridControl">
               <CustomRecord>
                   <Component>
                       <Context>AUT</Context>
                   </Component>
               </CustomRecord>
           </Control>
       </CC>
   </Controls>
   ```

### Related Documentation
- For more information on configuring controls for testing, refer to the Syncfusion Test Studio documentation.

## API Reference

### Namespaces and Classes
- **Namespace**: Syncfusion.TestStudio.Grid
- **Class**: GridControl

### Usage in Configuration
- The `GridControl` is typically used for managing and testing grid-related functionality in applications.

## Code Examples

### Sample XML Configuration
```xml
<?xml version="1.0" encoding="UTF-8" ?>
<Controls>
    <CC>
        <Control Type="Syncfusion.Windows.Forms.Grid.GridControl">
            <CustomRecord>
                <Component>
                    <Context>AUT</Context>
                </Component>
            </CustomRecord>
        </Control>
    </CC>
</Controls>
```

### Explanation
- This configuration specifies the use of the `GridControl` for automating tasks related to grid controls in the application under test (AUT).

## RAG Annotations
<!-- tags: [Syncfusion Winforms, Essential QuickTest Professional, GridControl, Test Automation, SwfConfig.xml, Configuration, Control Testing] keywords: [Syncfusion.TestStudio.Grid, GridControl, AUT, Context, Control Type, Custom Record, Component] -->
```

---

<!-- 페이지 74 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_020.jpeg
document_name: QTP
page_number: 020
page_id: QTP#page_020
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:02:14Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview
- Lists the various advanced controls provided in the Syncfusion Test Studio for Windows Forms.
- Highlights the dll files and namespaces associated with these controls.

## Content

### List of Advanced Controls and their Corresponding DLLs and Namespaces

| DLL File                         | Test Studio Namespace                                  | Windows Forms Namespace                             |
|-----------------------------------|-------------------------------------------------------|-------------------------------------------------------|
| CheckBoxAdv.dll                  | Syncfusion.TestStudio.Tools.CheckBoxAdv              | Syncfusion.Windows.Forms.Tools.CheckBoxAdv          |
| RadioButtonAdv                   | Syncfusion.TestStudio.Tools.RadioButtonAdv            | Syncfusion.Windows.Forms.Tools.RadioButtonAdv        |
| ColorPickerUIAdv.dll             | Syncfusion.TestStudio.Tools.ColorPickerUI             | Syncfusion.Windows.Forms.Tools.ColorPickerUIAdv      |
| DateTimePickerAdv.dll            | Syncfusion.TestStudio.Tools.DateTimePickerAdv         | Syncfusion.Windows.Forms.Tools.DateTimePickerAdv    |
| ThemedCheckBox.dll               | Syncfusion.TestStudio.Tools.ThemedCheckbox            | Syncfusion.Windows.Forms.Tools.ThemedCheckBox        |
| ButtonAdv.dll                    | Syncfusion.TestStudio.Tools.ButtonAdv                 | Syncfusion.Windows.Forms.Tools.ButtonAdv             |
| TextBoxExt.dll                   | Syncfusion.TestStudio.Tools.TextBoxExt                | Syncfusion.Windows.Forms.Tools.TextBoxExt            |
| MultiColumnComboBox.dll          | Syncfusion.TestStudio.Tools.MultiColumnComboBox        | Syncfusion.Windows.Forms.Tools.MultiColumnComboBox    |
| TabControlAdv.dll                | Syncfusion.TestStudio.Tools.TabControlAdv             | Syncfusion.Windows.Forms.Tools.TabControlAdv         |
| ScrollerFrame.dll                | Syncfusion.TestStudio.Tools.ScrollerFrame             | Syncfusion.Windows.Forms.Tools.ScrollBarCustomDraw   |
| GroupBar.dll                     | Syncfusion.TestStudio.Tools.GroupBar                  | Syncfusion.Windows.Forms.Tools.GroupBar              |
| GroupView.dll                    | Syncfusion.TestStudio.Tools.GroupView                 | Syncfusion.Windows.Forms.Tools.GroupView             |
| TaskBarBox.dll                   | Syncfusion.TestStudio.Tools.TaskBarBox                | Syncfusion.Windows.Forms.Tools.XPTaskBarBox           |
| ComboDropDown.dll                 | Syncfusion.TestStudio.Tools.ComboDropDown            | Syncfusion.Windows.Forms.Tools.ComboDropDown         |
| DataListView.dll                 | Syncfusion.TestStudio.Tools.DataListView              | Syncfusion.Windows.Forms.Tools.DataListView          |
| ComboBoxAutoComplete.dll         | Syncfusion.TestStudio.Tools.ComboBoxAutoComplete      | Syncfusion.Windows.Forms.Tools.ComboBoxAutoComplete  |
| TabbedMDI.dll                    | Syncfusion.TestStudio.Tools.TabbedMDI                 | Syncfusion.Windows.Forms.Tools.MDITabPanel           |

### WinForms-specific conventions
- The table above outlines the DLL files, their respective namespaces in the Syncfusion Test Studio, and their mappings in the Syncfusion Windows Forms tools for advanced controls.

## Page-level Navigation/TOC (if applicable)
- This page contains a summary listing of various advanced controls provided in the Syncfusion Test Studio and their corresponding namespaces for Windows Forms applications.

## Cross References
- Refer to the main section of the guide for additional information on implementing these controls in your projects.

<!-- tags: [Windows Forms, Test Studio, advanced controls, DLL, namespace, version 11.4.0.26] keywords: [CheckBoxAdv, RadioButtonAdv, ColorPickerUIAdv, DateTimePickerAdv, ThemedCheckBox, ButtonAdv, TextBoxExt, MultiColumnComboBox, TabControlAdv, ScrollerFrame, GroupBar, GroupView, TaskBarBox, ComboDropDown, DataListView, ComboBoxAutoComplete, TabbedMDI] -->
```


---

<!-- 페이지 75 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_024.jpeg
document_name: QTP
page_number: 024
page_id: QTP#page_024
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:02:36Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview
- **Main Title:** Essential QuickTest Professional
- Key features of QuickTest Professional are highlighted.
- Demonstrates how to start recording a test in the QuickTest interface.
- Emphasizes the use of the "Record" option in the toolbar for test automation.

## Content

### Main Interface Overview

The image displays the **QuickTest Professional - [Start Page]**. Below is a detailed description of the interface:

#### Toolbar
- **Menu Bar:** Contains standard options such as File, Edit, View, Insert, Automation, Resources, Debug, Tools, Window, and Help.
- **Tool Buttons:** Includes icons for New, Open, Save, Record, Run, Stop, and various test-related actions.
- **Main Pane:** Displayed below the toolbar, includes tabs such as **Start Page** and **Test**.
  
#### Welcome Panel
- **Welcome!**
  - Introduces HP QuickTest Professional, highlighting its advanced automation solution for functional and regression testing.
  - Highlights key concepts like keyword-driven testing to enhance test creation and maintenance.
  - Emphasizes meeting the needs of both technical and non-technical users to create sophisticated test suites.
- **Process Guidance List**
  - Highlights areas such as:
    - **Keyword-Driven Testing**
    - **Application Areas**
    - **Business Components**
  
#### Recently Used Files
- Allows users to submit feedback about QuickTest on the **Send Feedback and Win Prizes** Web page.
- Provides an option to disable the Start Page window on startup.

#### Key Features in the Start Page
- **"What's New?" Section:** Lists several new features, summarizing updates such as:
  - Runtime Data configuration.
  - GUI and API-less Application Functionality in One Test.
  - New Run Results Viewer.
  - Visual Relation identification for Manual Testing.
  - Log Tracking for defect pinpointing.
  - Support for Web 2.0 Toolkit Applications.
  - New Web Testing Capabilities.
  - New Silverlight Add-in.
  - WPF and Silverlight Add-in Extensibility.
  - Extensibility Accelerator for Web Add-in Extensibility Development.

### Instructions for Recording a Test
After reviewing the start page, you can proceed to create a test:
1. **Create a New Test:** Alternatively, you can click the **Test tab** in the main pane or access the **Test sub-menu** under the **New menu** in the Menu bar.
2. **Start Recording:**
   - **Step 5:** Click the **Record** button in the toolbar to initiate the recording process.

## Figure: QuickTest Professional – [Start Page] showing New Test icon

The figure illustrates the **QuickTest Professional - [Start Page]**, emphasizing the **New Test icon** and starting point for creating a new test.

## API Reference (if applicable)
Not applicable for this page.

## Code Examples (multi-language supported)
Not applicable for this page.

## Page-level Navigation/TOC (if applicable)
Not applicable for this page.

## Cross References
See also:
- Essential QuickTest Professional documentation.
- Detailed guide on using QuickTest Professional for functional and regression testing.

## RAG Annotations
<!-- tags: [syncfusion-sdk, QTP, QuickTest Professional, testing, automation, performance, windows, testing tools, automation tools] -->
keywords: [QuickTest Professional, functional testing, regression testing, automation testing, keyword-driven testing, API, GUI testing, Extensibility, Add-in, runtime data, log tracking, WPF, Silverlight, Test, recording,]
```

---

<!-- 페이지 76 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_028.jpeg
document_name: QTP
page_number: 028
page_id: QTP#page_028
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:02:58Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Application Details

The **Application Details** dialog box is displayed. It allows you to configure the application settings required for testing. The dialog includes fields for specifying the application path, working folder, program arguments, and additional options.

### Dialog Screenshot

Figure 15: Application Details

![Application Details Dialog Box](https://<image_url>)

### Steps to Configure Application Details

1. **Application Path**
   - **Browse and select the path of the application** that is to be tested by clicking the **Browse** button (📁) for the **Application** label.

2. **Working Folder Path**
   - **Browse and select the path of the working folder** by clicking the **Browse** button (📁) for the **Working folder** label.

### Notes

- **Launch Application**:
  - **Selecting the Launch application check box** launches the application immediately after clicking **OK** in the current dialog.
  
- **Include Descendant Processes**:
  - **The Include descendant processes check box** includes all the processes that are descendant to the current process.
  
- **Default Settings**:
  - **Both these check boxes will be selected by default**.

3. **Confirm Settings**
   - **Click OK** to save the configuration.

### Displayed Paths

- **Note**: The path of the application and working folder are displayed in the **Application details** frame as shown in the screenshot.

## Cross References

- For more information on setting the Record and Run Settings, click **Help** in the **Application Details** dialog.

<!-- tags: [application details, essential quicktest professional, syncfusion winforms, 11.4.0.26, testing configuration, launch application, include descendant processes] keywords: [application path, working folder, program arguments, dialog box, testing, environment variables, record and run settings] -->
```

---

<!-- 페이지 77 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_032.jpeg
document_name: QTP
page_number: 032
page_id: QTP#page_032
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:03:10Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview
- Demonstrates the behavior of a default recording without recognizing Syncfusion controls.
- Highlights the interactions with various cell types, such as checkbox, pushbutton, password, and currency cells, within the GridControl.
- Explains how the recorded actions may not fully capture the functionality of Syncfusion-specific controls.

## Content

### Understanding Default Recording in QuickTest Professional

The image above showcases the behavior of the QuickTest Professional tool when recording interactions with a GridControl that contains various Syncfusion-specific controls. The expert view on the top half of the image shows the resultant script generated by the tool:

```plaintext
1. SwfWindow("GridControl").Move 414,308
2. SwfWindow("GridControl").SwfObject("gridControl1").Click 321,313
3. SwfWindow("GridControl").SwfEditor("SwfEditor").SetCaretPos 0,0
4. SwfWindow("GridControl").SwfObject("gridControl1").Click 344,61
5. SwfWindow("GridControl").SwfEditor("SwfEditor").SetCaretPos 0,0
6. SwfWindow("GridControl").SwfEditor("SwfEditor").Type "hrhrhy"
7. SwfWindow("GridControl").SwfObject("gridControl1").Click 99,254
8. SwfWindow("GridControl").SwfEdit("SwfEdit").SetSecure "4ab06ef0588b07eb464dc06d7bea069c"
9. SwfWindow("GridControl").SwfObject("gridControl1").Click 151,258
10. SwfWindow("GridControl").SwfEdit("SwfEdit").SetSecure "4ab06ef0643014756206f225d00f02d5096773a8cca3c31
11. SwfWindow("GridControl").Move 386,364
```

#### Key Observations:
- The script includes mouse clicks at specific coordinates and attempts to interact with `SwfEditor` and `SwfEdit` controls.
- The actions involve setting caret positions and entering secured text, indicative of interactions with password fields or secure input areas.

#### GridControl Layout and Interaction Points:
The bottom half of the image depicts the GridControl interface, which contains various cell types:

| Row | Description                           | Example                             |
|-----|---------------------------------------|-------------------------------------|
| 3   | CheckBox Cells                       | A checkbox is marked in column C. |
| 7   | PushButton Cells                     | Includes "PushButton 1" and "PushButton 2". |
| 10  | Password Cells                       | Displays masked input represented by `******`. |
| 13  | Currency Cells                       | Displays formatted currency values like `$456.00` and `($739.00)`. |
| 16  | MaskEdit Cells                       | Contains formatted editing examples such as `(449-091-11)` and `( -- )`. |

### Importance of Recognizing Syncfusion Controls

Syncfusion controls offer enhanced functionality beyond standard Windows Forms controls. When QTP does not recognize these controls, the generated scripts may not accurately capture all the rich functionalities or properProcesses. This defaults to a more general approach, potentially leading to incomplete or inefficient test automation.

### Conclusion

The figure illustrates that without explicit recognition of Syncfusion controls, the test script may fall back on generic event handling, leading to a compromised simulation of genuine user interactions. Proper integration of Syncfusion controls into test automation frameworks ensures more accurate and effective test coverage.

## API Reference (if applicable)

This page does not provide specific API references, but the actions depicted involve interaction with the following:
- `SwfWindow`
- `SwfObject`
- `SwfEditor`
- `SwfEdit`

For more detailed API information, refer to the Syncfusion documentation specific to GridControl and related controls.

## Code Examples

The script provided in the expert view represents typical interaction recorded by QuickTest Professional. However, utilizing Syncfusion-specific APIs would provide more accurate and robust test automation capabilities.

## Page-level Navigation/TOC (if applicable)

- [Figure 18: Default recording without recognizing Syncfusion control](#fig18)

### Cross References

- Refer to the Syncfusion documentation on GridControl and its specific cell types for detailed information on handling these controls in QTP.

<!-- tags: [quicktest, syncfusion-grid, test-automation, cell-types, version-11.4.0.26] keywords: [checkbox, pushbutton, password, currency, maskedit, gridcontrol] -->
```

---

<!-- 페이지 78 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_036.jpeg
document_name: QTP
page_number: 036
page_id: QTP#page_036
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:03:38Z
fidelity: lossless
--> 

# Essential QuickTest Professional

## Content

### Figure 21: Editing in Expert view

You can run the edited test to check whether the newly added or changed scripts affect the running process by showing the changes in the running application.

#### Note:
Sometimes, the newly added or changed script may have an error causing the whole application to fail. In such a case, the Test Results dialog will show the failure as shown below:

![Figure 22: Test Results when Testing Fails](https://images/syncfusion.com/documentation/images/quicktest-professional/test-results-dialog.jpg)

**Figure 22: Test Results when Testing Fails**

For more details on running the test, refer to the previous section.

### Editing in Keyword View

## API Reference

## Code Examples

- In this section, you can find examples related to the editing process in both Expert view and Keyword view, as well as handling script errors during testing.

<!-- tags: [Syncfusion, WinForms, QuickTest Professional, Test Results, Script Errors, Expert View, Keyword View] keywords: [testing, scripts, errors, application failure, results summary, test iterations] -->
```

---

<!-- 페이지 79 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_040.jpeg
document_name: QTP
page_number: 040
page_id: QTP#page_040
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:03:47Z
fidelity: lossless
-->

# Essential QuickTest Professional

1. Click the **Save** button in the toolbar. The **Save Test** dialog box is displayed.

![Save Test Dialog](image_url)

Figure 26: Save Test Dialog

2. Select the location to save the file from the **Save in:** drop-down list.
3. Type the file name of the file to be saved in the text box adjacent to the **File name** label.
4. Click **Save**.

The test is saved.

## 3.5 Running the Saved Test

The tests that have been saved can be replayed later. To run a saved test, follow the steps below:

1. Click **Open** on the toolbar.

### Additional Information

- The "Save Test" dialog allows users to specify the location and name for saving their test files.
- After saving, the test can be rerun by simply opening the saved file.

## Code Examples

Here is an example of how to programmatically save a test using C#:

```csharp
// Assuming the test object is available
Test test = ...;

// Save the test programmatically
test.Save("Test1", @"C:\QuickTest\Testing", QuickTest.TestType.Functional);
```

This code demonstrates saving a test named "Test1" to the specified directory.

## References

For more information on saving and running tests, refer to the following resources:

- **QuickTest Professional User Guide**
- **Syncfusion Winforms Documentation**

<!-- tags: [QuickTest Professional, Syncfusion Winforms, save test, run saved test] keywords: [Save Test Dialog, Save in, File name, Save button, Open, saved test, replay, rerun, code examples, user guide, documentation] -->
```

---

<!-- 페이지 80 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_044.jpeg
document_name: QTP
page_number: 044
page_id: QTP#page_044
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:03:59Z
fidelity: lossless
-->

## QuickTest Professional Grid Functions

### Overview

- **Grid Functions** for modifying and interacting with grid cells.
- Includes methods for setting cell values, checkbox states, radio buttons, current cell location, and scroll positions.
- Helper functions to manage grid editing, retrieve cell types, column counts, and extract formatted cell text.
- Methods to check if a cell contains a formula and retrieve its computed value.
- Functions to insert, remove, and manipulate rows and columns dynamically.

### Content

#### Grid Interaction Functions

- **SetCellData(int row, int col, string str)**
  - Sets the cell value of the cell.
- **SetCellCheckBox(int row, int col, string str)**
  - Sets the cell value of the check box cell.
- **SetCellRadioButton(int row, int col, string str)**
  - Sets the cell value of the radio button cell.
- **SetCurrentCell(int row, int col)**
  - Sets the location of the current cell.
- **SetScrollPosition(int vScrollPosition, int hScrollPosition)**
  - Sets the scroll position.

#### Helper Functions

- **BeginEdit(int row, int col)**
  - Brings the editing cursor in the specified grid cell.
- **EndEdit(int row, int col)**
  - Finishes the editing mode of the cell specified.
- **string GetCellType(int row, int col)**
  - Retrieves the CellType for the given cell coordinates.
- **int GetColumnCount()**
  - Retrieves the number of columns used.
- **int GetColumnlndex(string name)**
  - Finds the column index for the given column name, returns 0 if search fails.
- **string GetFormattedText(int row, int col)**
  - Retrieves the formatted cell format.
- **bool IsFormulaCell(int row, int col, out string formula, out string computedValue)**
  - For a given row and column index, IsFormulaCell points to the formula used in that cell and the result of the formula. This also returns "false" if this cell is not a formula cell.
- **object GetCellData(int row, int col)**
  - For the given Row and Column objects, the cell value of that cell can be obtained.
- **int GetRowCount()**
  - Retrieves the number of rows used.
- **InsertColumn(int insertAt, int count)**
  - Inserts a range of columns from the specified location.
- **InsertRow(int insertAt, int count)**
  - Inserts a range of rows from the specified location.
- **RemoveColumn(int from, int to)**
  - Removes a range of columns specified for the Grid.

#### RAG Annotations

- This section provides a comprehensive list of functions related to grid manipulation and interaction in the Syncfusion Winforms environment. These functions allow developers to programmatically modify grid contents, manage scroll positions, and perform various cell and grid-level operations efficiently.

### Tags and Keywords
<!-- tags: [grid, winforms, syncfusion, gridfunctions, cellinteraction, helperfunctions, datamanipulation, scrolling] keywords: [SetCellData, SetCellCheckBox, SetCellRadioButton, SetCurrentCell, SetScrollPosition, BeginEdit, EndEdit, GetCellType, GetColumnCount, GetColumnlndex, GetFormattedText, IsFormulaCell, GetCellData, GetRowCount, InsertColumn, InsertRow, RemoveColumn] -->
```

---

<!-- 페이지 81 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_048.jpeg
document_name: QTP
page_number: 048
page_id: QTP#page_048
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:04:19Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview
- Provides methods for interacting with Grid and Table elements in a WinForms application.
- Includes functions for collapsing and expanding groups, retrieving cell data, getting row and column counts, and managing grid details.

## Content

### WinForms Methods

The following table lists methods for working with Grid and Table elements:

| Method Name | Description |
|-------------|-------------|
| `CollapseGroup(object row)` | Collapses the group. |
| `ExpandGroup(object row)` | Expands the group. |
| `ExpandRecord(object record)` | Expands the record. |
| `FindRecordInGrid(string tableObject, string columnName, string data)` | Returns the first index of the searched data for the given column of the table, as located in the NestedDisplayElements. |
| `FindRecordInTable(string tableObject, string columnName, string data)` | Returns the first index of the searched data for the given column. |
| `GetAbsoluteRowIndex(int RowIndex)` | Retrieves the absolute RowIndex. |
| `GetBackColor(int row)` | Gets the backcolor of the record. |
| `GetCellBackColor(object row, object col)` | Gets the backcolor of the Cell. |
| `GetCellData(object row, object col)` | For the given Row and Column objects, the cell value of that cell can be obtained. |
| `GetChildCount(object row)` | Gets the child count for the given caption row and a record row. |
| `GetDescription(object row, object col)` | Gets the description of grid cells. |
| `GetColumnCount()` | Returns the sort order of the sorted column (Ascending or Descending). |
| `GetColSortOrder(int col)` | Returns the sort order of the sorted column (Ascending or Descending). |
| `GetColumnName(string tablename, int colindex)` | For a given table name and column index, the column name in which an element resides can be obtained. |
| `GetDetails()` | Gets details like table, record, and table descriptor. |
| `GetLevelByTableName(string name)` | Gets the level of table for the given table name. |
| `GetRowCount()` | Retrieves the number of rows used. |
| `GetRowElement(object row)` | Gets the row element. |
| `GetSelectedColIndex()` | Returns the Left column index of the selected |

## API Reference

### Methods

#### CollapseGroup(object row)
**Description**: Collapses the group.

#### ExpandGroup(object row)
**Description**: Expands the group.

#### ExpandRecord(object record)
**Description**: Expands the record.

#### FindRecordInGrid(string tableObject, string columnName, string data)
**Description**: Returns the first index of the searched data for the given column of the table, as located in the NestedDisplayElements.

#### FindRecordInTable(string tableObject, string columnName, string data)
**Description**: Returns the first index of the searched data for the given column.

#### GetAbsoluteRowIndex(int RowIndex)
**Description**: Retrieves the absolute RowIndex.

#### GetBackColor(int row)
**Description**: Gets the backcolor of the record.

#### GetCellBackColor(object row, object col)
**Description**: Gets the backcolor of the Cell.

#### GetCellData(object row, object col)
**Description**: For the given Row and Column objects, the cell value of that cell can be obtained.

#### GetChildCount(object row)
**Description**: Gets the child count for the given caption row and a record row.

#### GetDescription(object row, object col)
**Description**: Gets the description of grid cells.

#### GetColumnCount()
**Description**: Returns the sort order of the sorted column (Ascending or Descending).

#### GetColSortOrder(int col)
**Description**: Returns the sort order of the sorted column (Ascending or Descending).

#### GetColumnName(string tablename, int colindex)
**Description**: For a given table name and column index, the column name in which an element resides can be obtained.

#### GetDetails()
**Description**: Gets details like table, record, and table descriptor.

#### GetLevelByTableName(string name)
**Description**: Gets the level of table for the given table name.

#### GetRowCount()
**Description**: Retrieves the number of rows used.

#### GetRowElement(object row)
**Description**: Gets the row element.

#### GetSelectedColIndex()
**Description**: Returns the Left column index of the selected.

## Code Examples

### Example: Retrieving Cell Data
```csharp
object row = grid.Rows[0];
object col = grid.Columns[0];
string cellData = (string)grid.GetCellData(row, col);
```

### Example: Getting the Description of Grid Cells
```csharp
string description = grid.GetDescription(row, col);
```

## Page-level Navigation/TOC
- Methods for Grid and Table Interaction
- Description of each method

## Cross References
- Refer to the Grid and Table sections for more details on these elements.

## RAG Annotations
<!-- tags: Grid, Table, WinForms, QuickTest, Method, Property, Version: 11.4.0.26 -->
```

---

<!-- 페이지 82 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_052.jpeg
document_name: QTP
page_number: 052
page_id: QTP#page_052
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:04:46Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview
- NavigationView

The following are the recorded methods and their corresponding descriptions for Essential Tools:

## ButtonAdv

| Method      | Description                          |
|-------------|--------------------------------------|
| Click(string text) | Performs click action on the ButtonAdv control. |

## CalculatorControl

| Method      | Description                          |
|-------------|--------------------------------------|
| SetValue(int value) | The value will be appended to the calculated value. |
| SetAction(string action) | The action will be paused at the calculated value. |
| double GetCalculatedValue() | Helps to get the current value from the text area. |
| SetCalculatedValue(double value) | Sets the value in the text area as specified in the argument. |

## CheckBoxAdv

| Method      | Description                          |
|-------------|--------------------------------------|
| Set(string chkState) | The CheckState of the CheckBoxAdv. |

### Helper Function

| Method      | Description                          |
|-------------|--------------------------------------|
| string GetCheckState() | Gets the CheckState of the CheckBoxAdv. |

## ColorPickerUIAdv

| Method      | Description                          |
|-------------|--------------------------------------|
| SelectColor(object color) | The color that has to be selected. |

## ComboBoxAutoComplete

```html
<!-- tags: [syncfusion, tools, methods, descriptions, essential, buttonadv, calculatorcontrol, checkboxadv, colorpickeruiadv, comboboxautocomplete] keywords: [syncfusion winforms, method descriptions, essential tools, qtp, 11.4.0.26] -->
``` 
```(UI from 0.0 to 0.0)

---

<!-- 페이지 83 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_056.jpeg
document_name: QTP
page_number: 056
page_id: QTP#page_056
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:04:59Z
fidelity: lossless
-->

# RibbonControlAdv

| Method                   | Description                                                                 |
|--------------------------|------------------------------------------------------------------------------|
| RibbonMenuButtonClick() | Clicks the Ribbon menu button.                                             |
| SelectRibbonMenuItem(object item) | Selects the ribbon menu item.                                   |
| Close()                 | Closes the parent form of RibbonControlAdv.                                |
| Activate()              | Activates the parent form of RibbonControlAdv.                             |
| Maximize()              | Maximizes the parent form of RibbonControlAdv.                             |
| Minimize()              | Minimizes the parent form of RibbonControlAdv.                             |
| Restore()               | Restores the parent form of RibbonControlAdv.                              |
| SelectTab(object tabItem) | Selects the Ribbon Tab item.                                           |
| MinimizingPanel()       | Minimizes the Ribbon Tab panel.                                            |
| MaximizingPanel()       | Maximizes the Ribbon Tab panel.                                            |

## ScrollerFrame

| Method               | Description                                              |
|----------------------|----------------------------------------------------------|
| ScrollValue(int value) | The position of the scroll to be specified.          |

## TabbedMDIManager

| Method                   | Description                                           |
|--------------------------|-------------------------------------------------------|
| ClosePage(object tabPage) | Closes the specified tab page.                       |
| SelectPage(object tab)       | Selects the specified tab page.                    |

### TabControlAdv

```markdown
© 2013 Syncfusion. All rights reserved.
``` 


---

<!-- 페이지 84 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_060.jpeg
document_name: QTP
page_number: 060
page_id: QTP#page_060
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:05:09Z
fidelity: lossless
-->

# Helper Functions

| Function                | Description                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| string GetTag(int itemIndex)          | Retrieves the tag information for the given itemIndex. |
| string GetHeaderText()                | Retrieves the group/header text of the task bar box called from. |
| string GetItemText(int itemIndex)     | Retrieves the item text for the given item index from the task bar box called. |
| int GetTaskBarBoxCount()              | Number of task bar boxes. |
| int GetExpandedTaskBarBoxCount()      | Number of expanded task bar boxes. |
| GetCollapsedTaskBarBoxCount()         | Number of collapsed task bar boxes. |
| bool FindItem(string itemText, out string headerText, out int itemIndex) | Helps to find if an item exists. |

## SplitContainerAdv

| Method                 | Description                               |
|------------------------|-------------------------------------------|
| MoveSplitter(int distance) | Adjusts the distance of the splitter. |
| CollapsePanel(string collapse) | Collapses the panel.              |

## TabSplitterContainer

| Method                  | Description                                       |
|-------------------------|---------------------------------------------------|
| Collapse(string collapse)       | Collapses the pane to the bottom.              |
| ChangeOrientation(string orientation) | Changes the orientation.                 |
| MoveSplitter(int position)      | Adjusts the position of the splitter.           |
| SwapPanes(string swap)          | Swaps primary and secondary panes.              |
| SelectPrimaryTab(int index)     | Selects the primary tab page based on the given index. |

<!-- tags: [Syncfusion Winforms, Helper Functions, SplitContainerAdv, TabSplitterContainer] keywords: [GetTag, GetHeaderText, GetItemText, GetTaskBarBoxCount, GetExpandedTaskBarBoxCount, GetCollapsedTaskBarBoxCount, FindItem, MoveSplitter, CollapsePanel, Collapse, ChangeOrientation, MoveSplitter, SwapPanes, SelectPrimaryTab] -->
```

---

<!-- 페이지 85 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_064.jpeg
document_name: QTP
page_number: 064
page_id: QTP#page_064
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:05:23Z
fidelity: lossless
-->

## Overview
- Describes the `Scroll(double x, double y)` method for scrolling the diagram view.

## Content

### Scroll Method

The `Scroll(double x, double y)` method is used to scroll the diagram view based on the provided `x` and `y` coordinates. This method facilitates interactive navigation within the diagram by adjusting the view position.

#### Parameters

| Name  | Type   | Description                          |
|-------|--------|--------------------------------------|
| `x`   | double | The horizontal scrolling increment.  |
| `y`   | double | The vertical scrolling increment.    |

#### Description

This method scrolls the diagram view by the specified horizontal (`x`) and vertical (`y`) amounts. It is useful for implementing interactive panning or zooming functionalities within the application.

## API Reference

### Namespace and Class
- **Namespace**: Syncfusion.Windows.Forms.Diagram
- **Class**: Diagram

### Method
- **Name**: Scroll
- **Signature**: `public void Scroll(double x, double y)`
- **Parameters**:
  - `x`: A `double` representing the horizontal scroll increment.
  - `y`: A `double` representing the vertical scroll increment.
- **Returns**: None
- **Exceptions**: None explicitly mentioned.

## Code Examples

### Example: Scrolling the Diagram View

```csharp
// Assuming 'diagram' is an instance of the Diagram class
diagram.Scroll(100.0, 50.0); // Scrolls the diagram by 100 units horizontally and 50 units vertically.
```

## See also
- [Diagram Class Documentation](#)
- [Interactive Navigation Methods](#)

<!-- tags: Essential QuickTest Professional, scroll, diagram, method, parameter, winforms, 11.4.0.26 -->
```

---

<!-- 페이지 86 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_068.jpeg
document_name: QTP
page_number: 068
page_id: QTP#page_068
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:05:35Z
fidelity: lossless
-->

## Essential QuickTest Professional

### Overview
- This page provides instructions on configuring the Essential QTP Configurator and appending the swfconfig.xml file.

## Content

### Configuring SwfConfig File

#### Figure 30: Appending the SwfConfig File

The Essential QTP Configurator tool allows you to configure and append the swfconfig.xml file. Here is the process explained:

1. **Access the Configurator**:
   - Open the Essential QTP Configurator.
   - Navigate to the "Configure SwfConfig file" section.

2. **Locate and Enter the QTP Assemblies**:
   - In the QTP Assemblies Location field, specify the path to your QTP assemblies, for example: `Files (x86)\Syncfusion\Essential QTP\10.4.0.53\bin\3.5`.

3. **Enter the Product Version**:
   - Enter the product version in the designated field. For example, `10.403.0.53`.

4. **Check and Configure**:
   - Click the "Check & Configure" button to verify the configuration.

5. **Save Report**:
   - Optionally, save the configuration report using the "Save Report" button.

6. **Review the Assembly List**:
   - A list of assembly names and their corresponding product versions will be displayed, such as:
     - `ButtonAdv.dll` - `10.403.0.53`
     - `CalculatorControl.dll` - `10.403.0.53`
     - `ChartControl.dll` - `10.403.0.53`
     - `ColorPickerUIAdv.dll` - `10.403.0.53`
     - `ComboBoxAutoComplete.dll` - `10.403.0.53`
     - `CommandBar.dll` - `10.403.0.53`
     - And others.

7. **Append the swfconfig.xml File**:
   - If your system already has a swfconfig.xml file, a dialog box will appear asking you whether to append or replace the existing file.
   - **Replace Existing File**:
     - Click **Yes** to replace the old swfconfig.xml file with the current framework swfconfig.xml file.
   - **Keep Both Files**:
     - Click **No** if you wish to keep both files in the same folder.

### Do You Want to Append the Swfconfig.xml File?
A dialog box will prompt you with the following message:  
"**Do you want to append the swfconfig.xml file?**"  
Click **Yes** or **No** based on your requirements.

## API Reference (if applicable)

None specified in this section.

## Code Examples (multi-language supported)

None applicable in this section.

## Page-level Navigation/TOC (if applicable)

None additional content provided in this section.

## Cross References

None relevant cross-references in this section.

## RAG Annotations
<!-- tags: [QTP Configurator, swfconfig.xml, QTP assemblies, version configuration] keywords: [append, replace, configuration, dialog box, assembly names, product versions] -->
```

---

<!-- 페이지 87 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_072.jpeg
document_name: QTP
page_number: 072
page_id: QTP#page_072
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:05:56Z
fidelity: lossless
-->

## Essential QuickTest Professional

### Overview
- Important notes about DLL paths
- Alternative installation paths for `Essential QuickTest Professional`
- XML code snippets for custom configuration

### Content

#### Path Assumptions and Customization

**Note:** In the preceding code, the fully qualified name of the DLL given in the `<DllName>` tag assumes that you have installed the Essential QuickTest Professional in the following default path:

**Default Path:**
```plaintext
C:\Program Files\Syncfusion\Essential QuickTest Professional\<Version number>\
```

If you have installed Essential QuickTest Professional in any other path, you need to give the correct path of the DLL in all the `<DllName>` tags. For example, if Essential QuickTest Professional is located in `D:\Essential QuickTest Professional\<version number>`, then the code should be as follows:

```xml
[XML]

<Control Type="Syncfusion.Windows.Forms.Grid.GridControl">
    <CustomRecord>
        <Component>
            <Context>AUT</Context>
            <DllName>D:\Essential TestStudio\<Version Number>\Bin\2.0\GridControl.dll</DllName>
            <TypeName>Syncfusion.TestStudio.Grid.GridControl</TypeName>
        </Component>
    </CustomRecord>
</CustomReplay>
<Component>
    <Context>AUT</Context>
    <DllName>D:\Essential TestStudio\<Version number>\Bin\2.0\GridControl.dll</DllName>
    <TypeName>Syncfusion.TestStudio.Grid.GridControl</TypeName>
</Component>
</CustomReplay>
</Control>
```

#### Steps for Customizing Configuration

1. **Select Controls to Test:**
   - Select the segment of the code containing the controls to be tested.

2. **Copy Selected Code:**
   - On the Edit menu, click Copy.

**Note:** While selecting the code for copying, exclude the following lines of code:

```xml
[XML]

<?xml version="1.0" encoding="UTF-8" ?>
```

3. **Open Configuration File:**
   - Open the `SwfConfig.xml` file located under the following location:
   ```plaintext
   <QuickTest Professional Installation Path>\dat\SwfConfig.xml
   ```

4. **Paste Copied Segment:**
   - Paste the copied segment under the `<?xml>` tag in `SwfConfig.xml`.

### API Reference

#### File Paths
- `SwfConfig.xml`: `<QuickTest Professional Installation Path>\dat\SwfConfig.xml`

### Code Examples

#### XML Configuration Snippet
The provided XML snippet illustrates how to configure custom controls within the `SwfConfig.xml` file.

```xml
[XML]

<Control Type="Syncfusion.Windows.Forms.Grid.GridControl">
    <CustomRecord>
        <Component>
            <Context>AUT</Context>
            <DllName>D:\Essential TestStudio\<Version Number>\Bin\2.0\GridControl.dll</DllName>
            <TypeName>Syncfusion.TestStudio.Grid.GridControl</TypeName>
        </Component>
    </CustomRecord>
</CustomReplay>
<Component>
    <Context>AUT</Context>
    <DllName>D:\Essential TestStudio\<Version number>\Bin\2.0\GridControl.dll</DllName>
    <TypeName>Syncfusion.TestStudio.Grid.GridControl</TypeName>
</Component>
</CustomReplay>
</Control>
```

### Page-level Navigation/TOC
- Path Assumptions and Customization
- Steps for Customizing Configuration
- API Reference
- Code Examples

### RAG Annotations
- **Tags:** Essential QuickTest Professional, DLL Path Configuration, XML Configuration, GridControl, SwfConfig.xml
- **Keywords:** CustomRecord, Component, Context, DllName, TypeName, AUT, Syncfusion Windows Forms, GridControl, Version number, Path customization
```

---

<!-- 페이지 88 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_076.jpeg
document_name: QTP
page_number: 076
page_id: QTP#page_076
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:06:16Z
fidelity: lossless
-->

# Essential QuickTest Professional

6. You can get the error details using the configuration file.

## 7.1.3 How to fetch installation information related to the Syncfusion QTP add-on

Open the Syncfusion Essential QTP Configurator located at (Installed location of Essential QuickTest Professional)\Utilities\SwfConfigUtility\SwfConfigUtility.exe.

1. Open the Syncfusion Essential QTP Configurator located at (Installed location of Essential QuickTest Professional)\Utilities\SwfConfigUtility\SwfConfigUtility.exe.

### Figure: Essential QTP Configurator

- **Configure SwfConfig file**
- **QTP Assemblies Location**
- **Product Version** (Eg: 10.202.0.56)
- **AssemblyName**, **ProductVersion**, **DateModified**, **Size**

2. Click the **Save Report** button to get the install information.

3. There is no need to enter the product version and install path details in the respective text boxes.

4. It will then show the save dialog box to save the install information.

## Overview
- Steps to fetch installation information using the Syncfusion Essential QTP Configurator.
- Guide on using the SwfConfigUtility to generate installation reports.

## Content

### Retrieving Installation Information
To retrieve detailed installation information related to the Syncfusion QTP add-on, follow these steps:

1. **Open the Util**: Locate and run the Syncfusion Essential QTP Configurator from the installed location of Essential QuickTest Professional.

   - **Path**: Essential QuickTest Professional)\Utilities\SwfConfigUtility\SwfConfigUtility.exe.

2. **Save the Report**: Click on the **Save Report** button to generate the installation information.

   - **Reason**: No need to manually enter product version or path details.

3. **Save the Information**: A save dialog will appear, allowing you to save the generated installation report.

   - **Result**: The install information will be saved as a file.

### WinForms-specific conventions
- The guide emphasizes the use of automated utilities for fetching detailed installation information, aligning with Syncfusion's preference for structured, accessible documentation.

<!-- tags: [Syncfusion Winforms, Essential QuickTest Professional, QTP, installation information, SwfConfigUtility, product version, installation path, installation report] keywords: [Syncfusion, QTP add-on, configuration file, installation information, SwfConfigUtility, product version, installation path, detailed error details] -->
```

---

<!-- 페이지 89 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_080.jpeg
document_name: QTP
page_number: 080
page_id: QTP#page_080
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:06:31Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview
- Details on how to get the description of checkbox cells and normal cells in Essential Grid.
- Explanation of the GetDescription method for retrieving descriptions of grid cells.

## Content

### 7.2.1 How to get the description of the Check Box Cells and Normal Cells in Essential Grid

#### Supported method to get the Description of GridCells
The **GetDescription** method is used to get the description of the check box, push button, and normal cells in Essential Grid's record and reply process. This method returns the description of the check box, push button, and normal cells as well.

---

### Use Case Scenarios
This feature enables you to get the description of checkbox, push button, and normal cells in QTP testing.

#### Methods Table

| Method         | Description                                      | Parameters                                              | Return Type |
|----------------|--------------------------------------------------|----------------------------------------------------------|--------------|
| GetDescription | Gets the description of grid cells for Essential Grid. | For the Grid control: <br/> `public object GetDescription(int row, int col)` <br/> For the GridGrouping control: <br/> `public object GetDescription(object row, object col)` | Object       |

---

### Applying the GetDescription Method in QTP

The following code examples illustrate how to use the GetDescription method.

---

#### [For GridControl]

```csharp
SwfWindow("Form1").SwfObject("gridControl1").SetCurrentCell 3,1
MsgBox(SwfWindow("Form1").SwfObject("gridControl1").GetDescription(3,1))
```

---

#### [For GridGroupingControl]

```csharp
SwfWindow("Form1").SwfObject("gridGroupingControl1").SetCurrentCell 3,"Col2"
MsgBox(SwfWindow("Form1").SwfObject("gridGroupingControl1").GetDescription(5,"Col0"))
```

## RAG Annotations
<!-- tags: [Essential Grid, GetDescription method, checkbox cells, normal cells, QTP testing] keywords: [Grid cells, description, Grid control, GridGrouping control, SetCurrentCell, MsgBox, Form1, gridControl1, gridGroupingControl1] -->
```

---

<!-- 페이지 90 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_084.jpeg
document_name: QTP
page_number: 084
page_id: QTP#page_084
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:06:45Z
fidelity: lossless
-->

## Applying CollapseNode and ExpandNode methods in QTP

The following code examples illustrate how to use the CollapseNode and ExpandNode methods.

```csharp
SwfWindow("QTPTreeViewAdv").SwfObject("Node1").CollapseNode("Node2");
SwfWindow("QTPTreeViewAdv").SwfObject("Node1").ExpandNode("Node2");
```

### 7.4 Essential Chart

#### 7.4.1 How to get the displayed text in the X-axis and Y-axis

**Supported method to get the displayed text in the X-axis and Y-axis**

The `GetXAxisText` and `GetYAxisText` methods are used to get the displayed text in the X-axis and Y-axis. This method returns the displayed text in string format.

**Use Case Scenarios**

This feature enables you to get the displayed text in the X-axis and Y-axis in QTP testing.

#### Methods Table

| Method       | Description                                         | Parameters                  | Return Type |
|--------------|-----------------------------------------------------|------------------------------|--------------|
| GetXAxisText | Gets the displayed text of the X-axis in Essential Chart. | public string GetXAxisText() | String       |
| GetYAxisText | Gets the displayed text of the Y-axis in Essential Chart. | public string GetYAxisText() | String       |

<!-- tags: syncfusion, essential tools, qtp, essential chart, x-axis, y-axis, text retrieval, winforms keywords: collapse, expand, node, treeview, axis text -->
```

---

<!-- 페이지 91 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_088.jpeg
document_name: QTP
page_number: 088
page_id: QTP#page_088
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:06:56Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview
- Guides you through scheduling control using essential diagrams for quick test.
- Demonstrates methods for changing node positions and connecting nodes in essential diagrams.
- Focuses on `MoveNode` method usage for node repositioning.

## Content

### 7.6 Essential Diagram

#### 7.6.1 How to change the node to a new position

**Supported method to change the node to a new position**

The `MoveNode` method is used to change the node to the new position.

**Use Case Scenarios**

This feature enables you to change the node to the new position of the chart control in QTP testing.

**Methods Table**

| Method   | Description                                       | Parameters                                       | Return Type |
|----------|---------------------------------------------------|---------------------------------------------------|-------------|
| MoveNode | Changes the node to the new position.            | public void MoveNode(string name, float offsetX, float offsetY) | void        |

**Applying MoveNode in QTP**

The following code examples illustrate how to change the node to a new position in the chart control.

```csharp
[For Diagram Control]
SwfWindow("Simple Flow Diagram").SwfObject("diagram1").SelectNode "EllipseStart"
SwfWindow("Simple Flow Diagram").SwfObject("diagram1").MoveNode "EllipseStart", 130.000000, 35.000000
```

#### 7.6.2 How to connect the specified nodes using connectors

**Supported method to connect the specified nodes using connectors**

(Note: Content for connecting nodes using connectors is partially visible; further information may be needed to complete this section.)

### WinForms-specific conventions
- Control manipulation in QTP using Syncfusion Winforms.
- Methods such as `MoveNode` for adjusting node positions in diagrams.

## API Reference (if applicable)

No explicit API reference is provided in the visible scope. However, the `MoveNode` method is detailed above.

## Code Examples (multi-language supported)

The code examples provided demonstrate the use of the `MoveNode` method in QTP.

```csharp
[For Diagram Control]
SwfWindow("Simple Flow Diagram").SwfObject("diagram1").SelectNode "EllipseStart"
SwfWindow("Simple Flow Diagram").SwfObject("diagram1").MoveNode "EllipseStart", 130.000000, 35.000000
```

### Cross References

- Refer to the section on using connectors for connecting nodes, which may be detailed in subsequent pages.

## RAG Annotations

<!-- tags: [essential-diagram, qtp, node-positioning, syncfusion-winform] keywords: [MoveNode, chart control, node, diagram, QTP, test automation, version 11.4.0.26, scheduling control] -->
```

---

<!-- 페이지 92 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_092.jpeg
document_name: QTP
page_number: 092
page_id: QTP#page_092
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:07:12Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview
- Saving and managing test cases effectively.
- Comprehensive list of supported controls and methods.
- Troubleshooting utilities for identified issues.
- Resolving issues related to Syncfusion controls not being recognized.

## Content

### Saving a Test
- Provides guidance on how to save a test case within the interface (Page 39).

### Supported Controls and Methods
- Lists the controls and methods supported by the application (Page 43).

### Utilities
- Offers utilities for various functionalities critical to the operation (Page 67).

### Troubleshooting: Why are Syncfusion controls not recognized even after adding the custom libraries?
- Answers common issues regarding control recognition after library integration (Page 78).

## Cross References
- See also: [Saving a Test](#Saving-a-Test), [Supported Controls and Methods](#Supported-Controls-and-Methods), [Utilities](#Utilities)

<!-- tags: [Syncfusion Winforms, QuickTest Professional, Troubleshooting, Documentation] keywords: [test saving, control recognition, utilities, custom libraries] -->
```