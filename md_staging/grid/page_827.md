```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_827.jpeg
document_name: grid
page_number: 827
page_id: grid#page_827
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:43:02Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates the **List Item Reference Relation** in a grid.
- Explains how to display nested strong-typed collections using **UniformChildList Relation**.

## Content

### Figure 324: ListItemReference Relation

#### Grid with Countries and Their Codes
The grid displays a list of countries along with their corresponding codes, as shown below:

| Id | Country_CountryCode | Country_Name                     |
|----|---------------------|-----------------------------------|
| 0  | US                  | United States                    |
| 1  | CA                  | Canada                           |
| 2  | AU                  | Australia                        |
| 3  | BR                  | Brazil                           |
| 4  | IO                  |                                  |
| 5  | CN                  |                                  |
| 6  | FI                  |                                  |
| 7  | FR                  |                                  |
| 8  | US                  |                                  |
| 9  | CA                  |                                  |
| 10 | AU                  |                                  |
| 11 | BR                  |                                  |
| 12 | IO                  |                                  |
| 13 | CN                  |                                  |
| 14 | FI                  |                                  |
| 15 | FR                  |                                  |
| 16 | US                  |                                  |
| 17 | CA                  |                                  |
| 18 | AU                  |                                  |
| 19 | BR                  |                                  |
| 20 | IO                  |                                  |

#### Dropdown List with Countries and Their Codes
A dropdown list on the grid column shows related country codes and names, as illustrated below:

| CountryCode | Name                       |
|-------------|----------------------------|
| BR          | Brazil                     |
| IO          | British Indian Ocean Territory |
| CN          | China                      |
| FI          | Finland                     |
| FR          | France                     |
| DE          | Germany                    |
| HK          | Hong Kong                  |
| HU          | Hungary                    |
| IS          | Iceland                    |
| IN          | India                      |
| JP          | Japan                      |
| MY          | Malaysia                   |
| SG          | Singapore                  |
| CH          | Switzerland                |
| IO          | British Indian Ocean Territory |

#### Note
For more details, refer to the following browser sample:

```
<Install Location>\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Grouping.Windows\Samples\2.0\Relations And Hierarchy\List Item Reference Demo
```

### 4.3.4.3.5.5 Uniform Child List Relation

#### Overview of UniformChildList Relation
The **UniformChildList** relation is used to map nested strong-typed collections within a parent collection. If a public property is an object, it will be displayed in a nested table. The collection in the example consists of two types of objects: **ParentObj** and **ChildObj**, where every **ParentObj** is associated with a collection of **ChildObj**s, represented by the public property named 'Child'. This results in the creation of a nested table to display the associated children for a given parent.

#### Example

<!-- 
tags: [product, grid, windows forms, list item reference relation, uniform child list relation, nested tables]
keywords: [listitemreferencerelation, uniformchildlist, nested tables, data mapping, parent child relation, country codes]
-->
```