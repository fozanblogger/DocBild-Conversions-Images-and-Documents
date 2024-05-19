@echo off
setlocal

:menu
cls
echo ================================
echo          DocBild Conversion
echo ================================
echo 1. PNG Conversion Options
echo 2. JPG Conversion Options
echo 3. Other Conversion Options
echo 4. PDF Conversion Options
echo 5. DOCX Conversion Options
echo 0. Exit
echo.
set /p choice="Choose an option: "

if %choice%==1 (
    call :png_conversion
) else if %choice%==2 (
    call :jpg_conversion
) else if %choice%==3 (
    call :other_conversion
) else if %choice%==4 (
    call :pdf_conversion
) else if %choice%==5 (
    call :docx_conversion
) else if %choice%==0 (
    exit /b
) else (
    echo Invalid choice. Please try again.
    pause
    goto menu
)

exit /b

:png_conversion
cls
echo ================================
echo       PNG Conversion Options
echo ================================
echo 1. PNG to JPG
echo 2. PNG to PDF
echo 3. PNG to BMP
echo 4. PNG to TIFF
echo 5. PNG to JP2
echo 6. PNG to WebP
echo 0. Back to Main Menu
echo.
set /p png_choice="Choose an option: "

if %png_choice%==1 (
    python img\pngtojpg.py
) else if %png_choice%==2 (
    python img\imagestopdf.py
) else if %png_choice%==3 (
    python img\pngtobmp.py
) else if %png_choice%==4 (
    python img\pngtotiff.py
) else if %png_choice%==5 (
    python img\pngtojp2.py
) else if %png_choice%==6 (
    python img\pngtowebp.py
) else if %png_choice%==0 (
    goto menu
) else (
    echo Invalid choice. Please try again.
    pause
    goto png_conversion
)

goto menu

:jpg_conversion
cls
echo ================================
echo       JPG Conversion Options
echo ================================
echo 1. JPG to PNG
echo 2. JPG to PDF
echo 3. JPG to BMP
echo 4. JPG to TIFF
echo 5. JPG to JP2
echo 6. JPG to WebP
echo 0. Back to Main Menu
echo.
set /p jpg_choice="Choose an option: "

if %jpg_choice%==1 (
    python img\jpgtopng.py
) else if %jpg_choice%==2 (
    python img\imagestopdf.py
) else if %jpg_choice%==3 (
    python img\jpgtobmp.py
) else if %jpg_choice%==4 (
    python img\jpgtotiff.py
) else if %jpg_choice%==5 (
    python img\jpgtojp2.py
) else if %jpg_choice%==6 (
    python img\jpgtowebp.py
) else if %jpg_choice%==0 (
    goto menu
) else (
    echo Invalid choice. Please try again.
    pause
    goto jpg_conversion
     
)
 
  goto menu
:other_conversion
cls
echo ================================
echo       Other Conversion Options
echo ================================
echo 1. CR2 to PNG
echo 2. CR2 to JPG
echo 3. NEF to PNG
echo 4. NEF to JPG
echo 0. Back to Main Menu
echo.
set /p png_choice="Choose an option: "

if %png_choice%==1 (
    python img\cr2topng.py
) else if %png_choice%==2 (
    python img\cr2tojpg.py
) else if %png_choice%==3 (
    python img\neftopng.py
) else if %png_choice%==4 (
    python img\neftojpg.py
) else if %png_choice%==0 (
    goto menu
) else (
    echo Invalid choice. Please try again.
    pause
    goto other_conversion
)


goto menu

:pdf_conversion
cls
echo ================================
echo       PDF Conversion Options
echo ================================
echo 1. PDF to DOC
echo 2. PDF to DOCX
echo 3. PDF to JPG
echo 4. PDF to PNG
echo 5. PDF to RTF
echo 6. PDF to WEBP
echo 0. Back to Main Menu
echo.
set /p pdf_choice="Choose an option: "

if %pdf_choice%==1 (
    python pdf\pdftodoc.py
) else if %pdf_choice%==2 (
    python pdf\pdftodocx.py
) else if %pdf_choice%==3 (
    python pdf\pdftojpg.py
) else if %pdf_choice%==4 (
    python pdf\pdftopng.py
) else if %pdf_choice%==5 (
    python pdf\pdftortf.py
) else if %pdf_choice%==6 (
    python pdf\pdftowebp.py
) else if %pdf_choice%==0 (
    goto menu
) else (
    echo Invalid choice. Please try again.
    pause
    goto pdf_conversion
)

goto menu

:docx_conversion
cls
echo ================================
echo       DOCX Conversion Options
echo ================================
echo 1. Docx to DOC
echo 2. Docx to DOT
echo 3. Docx to DOTX
echo 4. Docx to PDF
echo 0. Back to Main Menu
echo.
set /p docx_choice="Choose an option: "

if %docx_choice%==1 (
    python docx\docxtodoc.py
) else if %docx_choice%==2 (
    python docx\docxtodot.py
) else if %docx_choice%==3 (
    python docx\docxtodotx.py
) else if %docx_choice%==4 (
    python docx\docxtopdf.py
) else if %docx_choice%==0 (
    goto menu
) else (
    echo Invalid choice. Please try again.
    pause
    goto docx_conversion
)

goto menu
