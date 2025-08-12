```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_052.jpeg
document_name: ProjIO
page_number: 052
page_id: ProjIO#page_052
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:00:18Z
fidelity: lossless
-->

## Overview
- This page discusses the properties and methods related to assignments in a project.
- It details how assignments bind tasks and resources and how to add assignments to a project using the Assignments collection.

## Content

### 4.4.1.3 Methods
Table 15: Assignment Methods

| Method         | Description                                                                 |
|-----------------|-----------------------------------------------------------------------------|
| Equals          | Returns a value indicating whether this instance is equal to a specified object. |
| GetHashCode     | Serves as a hash function for Assignment type.                              |
| GetType         | Gets the type of the current instance.                                     |
| ToString        | Returns a string that represents the current object.                       |

### 4.4.2 Adding Assignments to a Project

Assignments are used to bind the task and resources. The Project class exposes Assignments collection that represents the list of all the Assignment objects in a project. This property can be used to add assignments.

The code below shows adding assignments to a project:

## API Reference (if applicable)

### Properties
| Property           | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| AssnOwner          | Gets or sets the name of the assignment owner.                            |
| AssnOwnerGuid      | Gets or sets the GUID of the assignment owner.                           |
| BudgetCost         | Gets or sets the budgeted amount for cost resources on this assignment.  |
| BudgetWork         | Gets or sets the budgeted work amount for work or material resources on this assignment. |
| ExtendedAttribute  | Gets or sets the value of an extended attribute.                         |
| Baseline           | Gets or sets the collection of baseline values associated with the assignment. |
| F404000 – F4040C8 | Gets or sets Project 2010 assignment enterprise custom field elements.      |
| TimePhasedData     | Gets or sets the time phased data associated with the assignment.         |

## Code Examples (multi-language supported)
- The section provides an overview of how to add assignments to a project using the Assignments collection.

<!-- tags: [syncfusion, winforms, projio, assignments, project, task, resource, method, property, sdk] keywords: [assignments, project class, bindings, add assignment, budget cost, budget work, baseline, extended attribute] -->
```