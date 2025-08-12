```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_103.jpeg
document_name: HTMLUI
page_number: 103
page_id: HTMLUI#page_103
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:08:37Z
fidelity: lossless
-->

## Essential HTMLUI for Windows Forms

### Displaying HTML Forms in HTMLUI

#### Overview
- HTMLUI provides robust support for displaying HTML forms in Windows Forms applications.
- Forms elements such as text fields, buttons, checkboxes, and radio buttons are supported.
- Users can interact with these elements natively within the HTMLUI control.

#### Description
HTMLUI allows the integration of HTML forms into Windows Forms, enabling a rich interactivity experience. Figure 31 illustrates a sample of how HTML forms are displayed through HTMLUI. The window shows various form elements that can be customized and interacted with directly.

### 4.9 HTML Bookmarks

#### Overview
- HTML bookmarks are a feature in HTMLUI that allows users to switch to specific references in a page.
- This functionality supports both local and external link references for bookmarks.

#### Description
Bookmarks can be utilized to navigate to specific sections within the same page or across different pages. The HTMLUI control facilitates this by enabling the use of anchor tags `#bookmark` for internal linking and external linking to bookmarks in other files.

#### Sample Code

The following HTML code demonstrates how to implement bookmarks:

```html
[HTML]
<html>
<body>
    <a href="Newfile.htm#bookmark"> New file Book mark </a>
    <a href="#bookmark"> Bookmark in same file </a>
    <div id="bookmark"> Syncfusion's HTMLUI Control </div>
</body>
</html>
```

### Conclusion

The HTMLUI control in Syncfusion's Windows Forms offers advanced support for displaying HTML forms and bookmarks. This integration allows developers to create dynamic, interactive interfaces with rich HTML functionality, enhancing the user experience.

### Additional Information
- **Bookmarks** in HTMLUI allow users to navigate to specific sections efficiently.
- The use of `#bookmark` in anchor tags enables both local and external linking capabilities.

### References
- **HTMLUI Forms - Displaying HTML Forms**: Demonstrates the implementation of HTML forms within Windows Forms applications.
- **Bookmarks**: Explains how to use bookmarks for navigation within HTMLUI.

### Further Reading
- For more details on HTMLUI and its features, refer to the Syncfusion documentation and examples.

### Copyright
© 2013 Syncfusion. All rights reserved.

<!-- tags: [HTMLUI, Windows Forms, Bookmarks, HTML Forms, Navigation, Syncfusion] keywords: [HTMLUI, Windows, Form, Bookmarks, HTML Forms, Navigation, Developer, User Experience, Integration, Windows Forms API] -->
```