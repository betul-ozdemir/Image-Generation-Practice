clc;                   %Komut penceresi temizlendi
clear;                 %Önceki tüm değişkenler hafızadab silindi
close all;             %Açık olan tüm grafik pencereleri kapatıldı



dosya_adi = 'img.png'               %Görüntü yüklendi
img_orijinal = imread("img.png")    %Resim okundu


if size(img_orijinal, 3) == 3          %Renkli resim (RGB) kullanıldığı için resim griye çevrildi
    img_gri = rgb2gray(img_orijinal);
else
    img_gri = img_orijinal;
end

figure;                               %Kontrol
imshow(img_gri);
title('Gri Seviye Görüntü')


gurultu_orani = 0.05;                    %Hataları simüle etmek için %5 oranında 'Tuz ve Biber' (Salt&Papper) gürültüsü eklendi
img_gurultulu = imnoise(img_gri, 'salt & pepper', gurultu_orani);

figure('Name', 'Gürültü Konrolü');       

subplot(1, 2 ,1);
imshow(img_gri);
title('Orijinal Gri Görüntü');

subplot(1, 2, 2);
imshow(img_gurultulu);
title('Gürültülü Görüntü');


% Yöntem 1 -- Ortalama (Mean/ Averaging) Filtresi

filtre_cekirdegi = fspecial('average', [3 3]);
img_ortalama = imfilter(img_gurultulu, filtre_cekirdegi);

figure('Name', 'Ortalama Filtre Kontrolü');
imshow(img_ortalama);
title('Mean Filtresi Görüntüsü');

% Yöntem 2 -- Medyan (Median) Filtresi

img_medyan = medfilt2(img_gurultulu, [3 3]);

figure('Name', 'Medyan Filtre Kontrolü');
imshow(img_medyan);
title('Medyan Filtresi Görüntüsü');

% Yöntem 3 -- Gauss (Gaussian) Filtresi

sigma_degeri = 1;
img_gauss = imgaussfilt(img_gurultulu, sigma_degeri);

figure('Name', 'Gauss Filtre Kontrolü');
imshow(img_gauss);
title('Gauss Filtresi Görüntüsü');

%Analitik Başarı Metrikleri

% MSE Hesaplamaları

mse_ortalama = immse(img_ortalama, img_gri);
mse_medyan = immse(img_medyan, img_gri);
mse_gauss = immse(img_gauss, img_gri);

% PSNR Hesaplamaları

psnr_ortalama = psnr(img_ortalama, img_gri);
psnr_medyan = psnr(img_medyan, img_gri);
psnr_gauss = psnr(img_gauss, img_gri);


%Sonuçları Gösterme

Filtre_Turu = {'Ortalama (Mean)'; 'Medtan (Medaian)'; 'Gaus (Gaussian)'};
MSE = [mse_ortalama; mse_medyan; mse_gauss];
PSNR = [psnr_ortalama; psnr_medyan; psnr_gauss];

Sonuc_Tablosu = table(Filtre_Turu, MSE, PSNR)

disp(Sonuc_Tablosu);

%Görselletştirme

figure('Color', [1 1 1], 'Position', [100, 100, 1100, 700]);

subplot(2, 3, 1);
imshow(img_gri);
title('1. Orjinal Görüntü', 'FontWeight', 'bold');

subplot(2, 3, 2);
imshow(img_gurultulu);
title('2. Gürültülü Görüntü', 'FontWeight', 'bold');

% Ortalama Filtre Sonucu
subplot(2, 3, 4);
imshow(img_ortalama);
title(sprintf('3. Ortalama Filtre\nPSNR: %.2f dB', psnr_ortalama));

% Medyan Filtre Sonucu
subplot(2, 3, 5);
imshow(img_medyan);
title(sprintf('4. Medyan Filtre\nPSNR: %.2f dB', psnr_medyan));

% Gauss Filtre Sonucu
subplot(2, 3, 6);
imshow(img_gauss);
title(sprintf('5. Gauss Filtresi\nPSNR: %.2f dB', psnr_gauss));



