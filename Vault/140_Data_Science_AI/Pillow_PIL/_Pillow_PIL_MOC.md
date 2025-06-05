---
tags:
  - MOC
  - pillow
  - pil
  - python
  - image_processing
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Pillow (PIL Fork) MOC (Map of Content)

This note serves as a central hub for topics related to **Pillow**, the friendly fork of the Python Imaging Library (PIL). It's a powerful library for opening, manipulating, and saving many different image file formats in Python.

## Core Concepts & Components
- "[[Pillow_PIL]]" (Overview)
- "[[Image_Object_Pillow]]" (The `Image` module and class)
- "[[Image_Modes_Pillow]]" (RGB, RGBA, L, P, etc.)
- "[[Image_File_Formats_Pillow]]" (JPEG, PNG, GIF, TIFF, BMP, WebP)

## Basic Operations
- Opening Images (`Image.open()`)
- Saving Images (`image.save()`)
- Displaying Images (`image.show()`)
- Getting Image Attributes (`image.format`, `image.size`, `image.mode`)
- "[[NumPy_Pillow_Conversion]]" (Converting between Pillow Images and NumPy arrays)

## Image Manipulation
- Resizing (`image.resize()`)
- Cropping (`image.crop()`)
- Rotation & Flipping (`image.rotate()`, `image.transpose()`)
- Color Space Conversion (`image.convert()`)
- Pixel Manipulation (`image.load()`, `image.getpixel()`, `image.putpixel()`)
- Filters (`ImageFilter` module - BLUR, CONTOUR, SHARPEN, etc.)
- Image Enhancement (`ImageEnhance` module - Brightness, Contrast, Color, Sharpness)
- Drawing on Images (`ImageDraw` module - shapes, text)

## Notes in this Section

```dataview
LIST
FROM "140_Data_Science_AI/Pillow_PIL"
WHERE file.folder = this.file.folder AND file.name != this.file.name AND !contains(file.name, "MOC")
SORT file.name ASC
```

---
Use this MOC to navigate the Pillow section.