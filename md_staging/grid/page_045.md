```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_045.jpeg
document_name: grid
page_number: 045
page_id: grid#page_045
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:18:58Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Grid Grouping control provides strong designer support, allowing control over all aspects of the grid's appearance.
- Designer commands (verbs) enable saving and restoring layouts.
- A preview feature facilitates loading data into the control and setting Grid Grouping control properties as design-time properties.

## Content

Grid Grouping control has strong designer support. You can control all aspects of the grid's appearance through the designer. Additional commands (verbs) will let you save layouts and restore them. You can also use a preview feature that will let you load data into your control, and then further set the Grid Grouping control properties that can be persisted as design time properties.

This section has two major tasks. The first task is to place the Grid Grouping control on the form. The second task is to use the designer to set up data binding to an Access data file. This is strictly a Windows Forms process and really has nothing to do with our Grid Grouping control. You just need to set up a Data Adapter to access the data that is needed for the grid. The data for this is located in the My Documents\Syncfusion\EssentialStudio\VersionNumber\Windows\Data\NWIND.mdb (depending upon your installation folder). You must use ADO.NET OLE DB support to access this data.

In this lesson, you will learn about:

### 3.1.2.1 Binding to an MDB File By Using VS 2003

The steps in this lesson are for use with Visual Studio 2003.

#### Steps to Follow:

1. Open the Data section of your toolbox and drag an OleDbDataAdapter onto your form. This will open the Data Adapter Configuration Wizard.

---

## API Reference (if applicable)
- **OleDbDataAdapter**: Used for setting up a Data Adapter to access the data needed for the grid.
- **ADO.NET OLE DB Support**: Used to access OLE DB-based data sources like Access databases (.mdb).

## Cross References
- **Related Topics**:
  - Grid Grouping Control Design Support
  - Data Binding in Windows Forms
  - Accessing Access Databases Using ADO.NET OLE DB

## RAG Annotations
<!-- tags: [grid, windows forms, designer support, data binding, access database, visual studio,ADO.NET] keywords: [Grid Grouping control, designer, layout management, preview feature, OleDbDataAdapter, Access database, NWIND.mdb, NWIND, Visual Studio 2003] -->
```