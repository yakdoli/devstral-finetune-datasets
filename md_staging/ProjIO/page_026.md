```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_026.jpeg
document_name: ProjIO
page_number: 026
page_id: ProjIO#page_026
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:57:25Z
fidelity: lossless
-->

# Essential ProjIO

```csharp
project.Title = "Sample Project"

' Saving the Project
project.Save("Empty Project.xml")
```

The project summary information added through the above code can be viewed by checking the **Project Information – Advanced Properties** in the **File** menu.

## Empty Project Properties

![Figure: Empty Project Properties](<assets/empty_project_properties.png>)

The **Project** class properties **FYStartDate** and **FiscalYearStart** are used to get or set the Fiscal Year properties. **FYStartDate** defines the fiscal year start month and the **FiscalYearStart** property determines whether the fiscal year numbering has been used in the project.

## 4.1.7 Fiscal Year Properties

The **Project** class properties **FYStartDate** and **FiscalYearStart** are used to get or set the Fiscal Year properties. **FYStartDate** defines the fiscal year start month and the **FiscalYearStart** property determines whether the fiscal year numbering has been used in the project.

## API Reference

### Properties

- **FYStartDate**: Defines the fiscal year start month.
- **FiscalYearStart**: Determines whether the fiscal year numbering has been used in the project.

## Code Examples

```csharp
// Setting Fiscal Year Properties
project.FYStartDate = new DateTime(year, month, day);
project.FiscalYearStart = true;
```

<!-- tags: [Syncfusion, Winforms, ProjIO, Fiscal Year Properties] keywords: [FYStartDate, FiscalYearStart, Project class, fiscal year, start month, numbering] -->
```