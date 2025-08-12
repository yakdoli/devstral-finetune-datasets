```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_133.jpeg
document_name: common
page_number: 133
page_id: common#page_133
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:06:10Z
fidelity: lossless
-->

## Core Reference and Properties

### Reference Properties

The properties window in Syncfusion provides detailed information about the components referenced in your project. For instance, the `Syncfusion.Chart.Silverlight` reference includes the following details:

- **Name**: Syncfusion.Chart.Silverlight
- **Aliases**: `global`
- **Copy Local**: `True`
- **Culture**: (Empty)
- **File Type**: Assembly
- **Identity**: Syncfusion.Chart.Silverlight
- **Path**: C:\Program Files (x86)\Syncfusion\Essential Studio\8.1.0.30\ass...
- **Resolved**: `True`
- **Runtime Version**: v2.0.50727
- **Specific Version**: `True`
- **Strong Name**: `True`
- **Version**: 8.104.0.30

### Copy Local

**Description**: Indicates whether the reference will be copied to the output directory.

**Figure 126: Properties Window**

![Properties Window](#)

## Switching the Framework Version While Upgrading the Project

### Overview
- Provides guidance on switching the framework version during project upgrades.
- Utilizes the **MultiTarget Manager** from the Syncfusion Dashboard.

### Detailed Instructions
1. **Switching Framework Version**:
   - Use the **MultiTarget Manager** to switch the framework version.
   - After switching, remove the `bin` and `obj` folders from your local project directory.
   - Recompile your project to ensure compatibility with the new framework version.

**Reference**: For more details, refer to **Multi-Target Manager**.

## Migrating the Resource Files

### Overview
- Explains how to migrate resource files (.resx) to a newer version of the framework.
- Ensures that resource files are compatible with the updated environment.

### Steps to Migrate Resource Files
1. **Open the Migration Tool**:
   - Navigate to: **Start > Syncfusion > Essential Studio x.x.x.x > Utilities > Migration > ConvertResx(Framework 2.0, 3.5 or 4.0)**.
2. **Choose ResX Files**:
   - Click the **Choose ResX Files** option to begin the conversion process.
3. **Select Files to Convert**:
   - Select the `.resx` files that need to be converted to the newer framework version.

### Note
Ensure that all steps are followed to avoid any issues during the migration process.

## Performance Considerations

### Overview
- While migrating resource files, be aware of performance impacts and best practices.
- Follow the guidelines for smooth and efficient migration without compromising application performance.

### See also
- **Multi-Target Manager**: For detailed instructions on framework version management.
- **Essential Studio Documentation**: For comprehensive insights into migrating and upgrading projects.

<!-- tags: [Syncfusion, Winforms, Essential Studio, Resource Migration, Framework Version, MultiTarget Manager] keywords: [Syncfusion.Chart.Silverlight, .resx files, Copy Local, Multi-Target Manager, Framework, Migration, Resource Files] -->
```