@echo off
::
color 08

:: Başlangıç mesajı
echo *******************************************
echo     Gerekli Kutuphaneler Indiriliyor...
echo *******************************************
echo.

:: requests ve colorama kütüphanelerini yükleme

echo Yuklenen Kutuphane: requests
pip install requests
echo.

echo Yuklenen Kutuphane: colorama
pip install colorama
echo.

:: Yukleme tamamlandi
echo ****************************************
echo    Kutuphaneler Sorunsuz Yuklendi !
echo ****************************************
echo.

:: Kapanma mesaji
pause
