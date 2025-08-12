```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_025.jpeg
document_name: Olap Common
page_number: 025
page_id: Olap Common#page_025
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:16:24Z
fidelity: lossless
-->

# Essential OlapCommon

## Content

### Dimension Element

#### Overview
A `dimension` object is a fundamental component in OLAP reporting, composed of basic information such as **Name, Hierarchy, Level, and Members**. This section details how to create and understand the structure of a dimension element, emphasizing its hierarchical organization and properties.

#### Description
A simple `dimension` object contains basic attributes such as name, hierarchy, level, and members. By specifying the hierarchy and level name, the dimension element can be created. The dimension element includes hierarchical details and information about each level and member within that hierarchy.

---

#### Hierarchical Details
- **Hierarchy Element**:  
  Each element of a dimension can be summarized using a **hierarchy**. A hierarchy represents a parent-child relationship, where a parent member consolidates its child members. Parent members can be further aggregated, forming a hierarchy that can be summarized at various levels.  
  **Example**:  
  - May 2005 → Second Quarter 2005 → Year 2005.

- **Level Element**:  
  A level element is a child of the hierarchy element and contains a set of members that share the same rank within the hierarchy.  
  **Example**: May 2005, June 2005, etc., are members at the same level (months).

- **Member Element**:  
  A member element represents a member of a specific level in a cube and is a child of a hierarchy element. Each member has properties that describe its details.

---

#### Member Properties
Member properties encapsulate basic information about each member in a tuple. This includes the member name, parent level, the number of children, and other metadata. These properties are available for all members at a given level.

---

### Table of Dimensional Properties

| Name          | Description                                                                 | Type | Value it accepts | Reference Link                                     |
|---------------|-----------------------------------------------------------------------------|------|------------------|-----------------------------------------------------|
|               | collection of elements that comes under the categorical axis.              |      |                  |                                                     |
| TogglePivot   | Used to swap the elements in the column axis and row axis.                | bool | True/False      | -                                                   |
| Tag           | Holds the backup information of the OLAP Report.                           | CLR. | String          | [Tag property in OlapReport](#)                   |

---

## Cross References

- **See also**: Hierarchy Overview, OLAP Report Tag Reference

---

### RAG Annotations

<!-- tags: [olap, dimension, hierarchy, level, member, WinForms, Syncfusion] keywords: [dimension object, hierarchy, level element, member element, toggle pivot, backup information, olap report] -->
```