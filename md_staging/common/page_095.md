```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_095.jpeg
document_name: common
page_number: 095
page_id: common#page_095
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:03:54Z
fidelity: lossless
-->

## Overview
- Overview of using the MultiTarget Manager to configure machine settings for a specific .NET target framework.
- Steps for selecting a target framework version and refreshing an application for building.
- Instructions for migrating projects using Syncfusion’s project migration tool.

## Content

### MultiTarget Manager

#### 1. Using the MultiTarget Manager
Syncfusion Essential Studio Multi-Target Manager is used to configure the machine for a given target framework. To do this:

1. **Figure 88: Essential Studio MultiTarget Manager x.x.x.x Dialog**
   - The dialog allows you to select a target framework from a drop-down list.
   - This configuration process may take 30 seconds to 1 minute.

2. **Select required version**
   - Select the required framework version from the drop-down list provided:
     - **Available Framework versions to target**: `4.0`
   - Click the **Perform Action** button to initiate the configuration.
   - Upon completion, the Multitarget Manager will open a confirmation dialog.

3. **Figure 89: Multitarget Manager**
   - Confirmation message indicates that the requested action has been completed for the `4.0 Framework`.
   - Click **OK** to proceed.

#### 2. Open and refresh an application
- **Open an application**: After the framework is set, open your project.
- **Refresh the application**: Before building, refresh the application to ensure it is ready for the new framework version.

**Note**: The target value and the registry value will be changed to the selected framework version.

### 1.13.7 Project Migration

#### Overview
- The project migration tool facilitates moving project files to a given Syncfusion Essential Studio Version.

#### Steps for migrating a project
1. Open the project migration tool.
2. Select the source project files and the target Syncfusion Essential Studio Version.
3. Follow the prompts to complete the migration process.

This section provides an overview of how to migrate a project using Syncfusion’s migration tool, ensuring a smooth transition to a new version of the framework.

#### Figure 88: Essential Studio MultiTarget Manager x.x.x.x Dialog
![](image.png)
**Caption**: The dialog for selecting and performing an action on a target framework version.

#### Figure 89: Multitarget Manager
![](image.png)
**Caption**: Confirmation dialog indicating the completion of the target framework configuration.

## API Reference (if applicable)
No specific API details are outlined in this section, but you can refer to the relevant Syncfusion documentation for detailed API information about project migration and multi-target framework management.

## Code Examples (if applicable)
No code examples are provided in this section, as the focus is on guiding the migration process rather than showcasing code implementation.

## RAG Annotations
<!-- tags: multitarget-manager, project-migration, .net-framework, syncfusion-essential-studio version:Syncfusion Winforms 11.4.0.26 -->
<!-- keywords: multitarget, framework versions, configuration, build, migration, target framework -->
```