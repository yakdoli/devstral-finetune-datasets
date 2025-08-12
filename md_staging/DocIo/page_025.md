```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_025.jpeg
document_name: DocIo
page_number: 025
page_id: DocIo#page_025
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:29:58Z
fidelity: lossless
-->

## Overview

- DOM Basics (DLS) - Document Logical Structure [DLS] enables interaction with Word documents.
- Lists and options such as bookmarks, styles, sections, and body elements are detailed.
- Creating a platform application in various frameworks (e.g., Windows, ASP.NET, ASP.NET MVC) is demonstrated.

## Content

### Note:

- **DOM Basics (DLS) - Document Logical Structure**
  - A model that allows interaction with Word documents.
  - Features include:
    - **Bookmarks**: List of bookmarks (MS Word: Insert > Bookmarks...).
    - **Styles**: List of document styles (MS Word: Format > Styles and Formatting).
    - **Sections**: Sections collection (Each section has its own PageSetup options and HeaderFooters).
    - **TextBodyItem**: Base class for container elements like paragraphs and tables.
    - **ParagraphItem**: Elements containing formatted text, pictures, symbols, bookmark markers, fields, etc.

### 3.2 Creating Platform Application

This section guides the step-by-step process to create the following platform applications:

- **Windows**
- **ASP.NET**
- **WPF**
- **Silverlight**
- **ASP.NET MVC**

#### Windows Application

1. Open **Microsoft Visual Studio**.
2. Go to the **File** menu and click **New Project**.
3. In the **New Project** dialog box, select the **Windows Forms Application** template.
4. Name the project and click **OK**.

## API Reference

- **DLS API**:
  - **Bookmarks**: List of document bookmarks.
  - **Styles**: List of document styles.
  - **Sections**: Each section includes PageSetup options and HeaderFooters.
  - **TextBodyItem**: Base class for document elements.
  - **ParagraphItem**: Contains formatted text, pictures, symbols, etc.

## Code Examples

```csharp
// Example: Creating a new Windows Forms Application
public class Program
{
    public static void Main()
    {
        Application.EnableVisualStyles();
        Application.SetCompatibleTextRenderingDefault(false);
        Application.Run(new MainForm());
    }
}
```

## Page-level Navigation/TOC

- **3.2 Creating Platform Application**: Detailed steps to create various platform applications.
- **Windows Application**: Guide to setting up a Windows Forms Application.

## Cross References

- Refer to the official Microsoft documentation for further details on creating applications in different frameworks.

## RAG Annotations

<!-- tags: [DocIO, Document Logical Structure, DLS, Windows Application, Windows Forms Application, ASP.NET, ASP.NET MVC, Syncfusion Winforms] 
keywords: [DOM Basics, Bookmarks, Styles, Sections, TextBodyItem, ParagraphItem, Windows Forms, New Project] -->
```