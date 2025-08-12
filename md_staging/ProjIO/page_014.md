```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_014.jpeg
document_name: ProjIO
page_number: 014
page_id: ProjIO#page_014
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:56:46Z
fidelity: lossless
-->

# 4 Concepts and Features

## 4.1 Project

You can open, modify, and create Project files using the Project Class. The Project class has a structure similar to the MS Project document. The Project class is useful in creating MS Projects in XML format. It can also be used to open or modify the existing Project files in XML format.

### 4.1.1 Properties, Methods, and Events Tables for Project

#### 4.1.1.1 Constructors

Table 4: Project Constructor

| Name             | Description                          |
|------------------|--------------------------------------|
| Project.Project() | Initializes a new instance of the Project class |

#### 4.1.1.2 Properties

Table 5: Project Properties

| Property      | Description                               |
|---------------|-------------------------------------------|
| SaveVersion   | Gets or sets the version of Microsoft Office Project from which the project was saved. |
| UID           | Gets or sets the unique ID of the project. |
| Name          | Gets or sets the name of the project.     |
| Title         | Gets or sets the title of the project.    |
| Subject       | Gets or sets the subject of the project.  |
| Category      | Gets or sets the category of the project. |
| Company       | Gets or sets the company that owns the project. |
| Manager       | Gets or sets the manager of the project.  |
| Author        | Gets or sets the author of the project.   |
| CreationDate  | Gets or sets the date when the project was created. |
| Revision      | Gets or sets the number of times a project has been saved. |
| LastSaved     | Gets or sets the date the project was last saved. |
| ScheduleFromStart | True if the project is scheduled from the start date. |
| StartDate     | Gets or sets the start date of the project. Required if ScheduleFromStart is true. |
```