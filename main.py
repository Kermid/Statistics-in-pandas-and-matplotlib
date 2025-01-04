import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gmean
from scipy.stats import skew


df = pd.read_csv('dane.csv')

df_subset = df[['squareMeters', 'price']]
print(df_subset.head())


price_bins = [0, 100000, 200000, 300000, 400000, 500000, 1000000, 1500000, 2000000, 2500000]  # ZAKRESY DLA CENY
price_labels = ['0-100k', '100k-200k', '200k-300k', '300k-400k', '400k-500k', '500k-1m', '1m-1,5m', '1,5m-2m', '2m-2,5m']

# Tworzymy nowe kolumny dla przypisania przedziałów cenowych
df['price_bin'] = pd.cut(df['price'], bins=price_bins, labels=price_labels, right=False)

# Obliczamy liczbę mieszkań w każdym przedziale
price_distribution = df['price_bin'].value_counts().sort_index()

# Wyświetlenie wyniku dla cen
print("Rozkład cen mieszkań:")
print(price_distribution)

# Ustalamy przedziały dla powierzchni mieszkań (np. 0,1m², 0,2m², ... do 2,5m²)
size_bins = [0, 10, 20, 30, 40, 50, 100, 150, 200, 250]  # Możesz dostosować w zależności od danych
size_labels = ['0-10m²', '10-20m²', '20-30m²', '30-40m²', '40-50m²', '50-100m²', '100-150m²', '150-200m²', '200-250m²']

# Tworzymy nowe kolumny dla przypisania przedziałów powierzchniowych
df['size_bin'] = pd.cut(df['squareMeters'], bins=size_bins, labels=size_labels, right=False)

# Obliczamy liczbę mieszkań w każdym przedziale powierzchni
size_distribution = df['size_bin'].value_counts().sort_index()

# Wyświetlenie wyniku dla powierzchni
print("Rozkład powierzchni mieszkań:")
print(size_distribution)

#SREDNIAAA
# Obliczanie średniej dla kolumny 'price' (ceny mieszkań)
mean_price = df['price'].mean()
print(f"Średnia cena mieszkań: {round(mean_price)} PLN")

# Obliczanie średniej dla kolumny 'squareMeters' (wielkosci mieszkan)
mean_price = df['squareMeters'].mean()
print(f"Średnia wielkosc mieszkania: {round(mean_price)} m^2")

#SREDNIA GEOMETRYCZNA
# Usuwamy lub zastępujemy NaN (brakujące wartości) przed obliczeniem średniej geometrycznej
df_cleaned = df.dropna(subset=['price', 'squareMeters'])

# Obliczanie średniej geometrycznej dla kolumny 'price' (ceny mieszkań)
geometric_mean_price = gmean(df_cleaned['price'])

# Obliczanie średniej geometrycznej dla kolumny 'squareMeters' (powierzchnie mieszkań)
geometric_mean_square_meters = gmean(df_cleaned['squareMeters'])

# Wyświetlanie wyników
print(f"Średnia geometryczna ceny mieszkań: {geometric_mean_price:.0f} PLN")
print(f"Średnia geometryczna powierzchni mieszkań: {geometric_mean_square_meters:.0f} m²")

#MODALNA
# Obliczanie wartości modalnej (najczęściej występującej) dla kolumny 'price' (ceny mieszkań)
mode_price = df['price'].mode()[0]  # Wybieramy pierwszy wynik, jeśli jest więcej niż jedna moda

# Obliczanie wartości modalnej (najczęściej występującej) dla kolumny 'squareMeters' (powierzchnie mieszkań)
mode_square_meters = df['squareMeters'].mode()[0]  # Wybieramy pierwszy wynik

# Wyświetlanie wyników
print(f"Wartość modalna ceny mieszkań: {mode_price} PLN")
print(f"Wartość modalna powierzchni mieszkań: {mode_square_meters} m²")

# MEDIANA/WARTOSC SRODKOWA
# Obliczanie wartości środkowej (mediany) dla kolumny 'price' (ceny mieszkań)
median_price = df['price'].median()

# Obliczanie wartości środkowej (mediany) dla kolumny 'squareMeters' (powierzchnie mieszkań)
median_square_meters = df['squareMeters'].median()

# Wyświetlanie wyników
print(f"Wartość środkowa ceny mieszkań (mediana): {median_price} PLN")
print(f"Wartość środkowa powierzchni mieszkań (mediana): {median_square_meters} m²")

#KWARTYLE
# Obliczanie Q1 i Q3 dla kolumny 'price' (ceny mieszkań)
q1_price = df['price'].quantile(0.25)  # Pierwszy kwartyl
q3_price = df['price'].quantile(0.75)  # Trzeci kwartyl

# Obliczanie Q1 i Q3 dla kolumny 'squareMeters' (powierzchnie mieszkań)
q1_square_meters = df['squareMeters'].quantile(0.25)  # Pierwszy kwartyl
q3_square_meters = df['squareMeters'].quantile(0.75)  # Trzeci kwartyl

# Wyświetlanie wyników
print(f"Pierwszy kwartyl (Q1) ceny mieszkań: {q1_price} PLN")
print(f"Trzeci kwartyl (Q3) ceny mieszkań: {q3_price} PLN")
print(f"Pierwszy kwartyl (Q1) powierzchni mieszkań: {q1_square_meters} m²")
print(f"Trzeci kwartyl (Q3) powierzchni mieszkań: {q3_square_meters} m²")

#ODCHYLENIE PRZECIETNE
# Obliczanie odchylenia przeciętnego dla kolumny 'price' (ceny mieszkań)
mean_price = df['price'].mean()
average_deviation_price = (df['price'] - mean_price).abs().mean()

# Obliczanie odchylenia przeciętnego dla kolumny 'squareMeters' (powierzchnie mieszkań)
mean_square_meters = df['squareMeters'].mean()
average_deviation_square_meters = (df['squareMeters'] - mean_square_meters).abs().mean()

print(f"Odchylenie przeciętne ceny mieszkań: {average_deviation_price:.2f} PLN")
print(f"Odchylenie przeciętne powierzchni mieszkań: {average_deviation_square_meters:.2f} m²")


#WARIANCJA
# Wariancja populacyjna dla kolumny 'price'
population_variance_price = df['price'].var(ddof=0)

# Wariancja populacyjna dla kolumny 'squareMeters'
population_variance_square_meters = df['squareMeters'].var(ddof=0)

print(f"Wariancja populacyjna ceny mieszkań: {population_variance_price:.2f} PLN^2")
print(f"Wariancja populacyjna powierzchni mieszkań: {population_variance_square_meters:.2f} m²^2")

#ODCHYLENIE STANDARDOWE
# Obliczanie odchylenia standardowego dla kolumny 'price' (ceny mieszkań)
std_price = df['price'].std()

# Obliczanie odchylenia standardowego dla kolumny 'squareMeters' (powierzchnie mieszkań)
std_square_meters = df['squareMeters'].std()


print(f"Odchylenie standardowe ceny mieszkań: {std_price:.2f} PLN")
print(f"Odchylenie standardowe powierzchni mieszkań: {std_square_meters:.2f} m²")

#TYPOWY OBASZAR ZMIENNOSCI

# Średnia i odchylenie standardowe dla kolumny 'price' (ceny mieszkań)
mean_price = df['price'].mean()
std_price = df['price'].std()

# Typowy obszar zmienności dla 'price'
typical_range_price_min = mean_price - std_price
typical_range_price_max = mean_price + std_price

# Średnia i odchylenie standardowe dla kolumny 'squareMeters' (powierzchnie mieszkań)
mean_square_meters = df['squareMeters'].mean()
std_square_meters = df['squareMeters'].std()

# Typowy obszar zmienności dla 'squareMeters'
typical_range_square_meters_min = mean_square_meters - std_square_meters
typical_range_square_meters_max = mean_square_meters + std_square_meters


print(f"Typowy obszar zmienności ceny mieszkań: od {typical_range_price_min:.2f} PLN do {typical_range_price_max:.2f} PLN")
print(f"Typowy obszar zmienności powierzchni mieszkań: od {typical_range_square_meters_min:.2f} m² do {typical_range_square_meters_max:.2f} m²")

#ODCHYLENIE CWIARTKOWE

q1_price = df['price'].quantile(0.25)
q3_price = df['price'].quantile(0.75)

# Obliczanie odchylenia ćwiartkowego dla 'price'
iqd_price = (q3_price - q1_price) / 2

q1_square_meters = df['squareMeters'].quantile(0.25)
q3_square_meters = df['squareMeters'].quantile(0.75)

# Obliczanie odchylenia ćwiartkowego dla 'squareMeters'
iqd_square_meters = (q3_square_meters - q1_square_meters) / 2


print(f"Odchylenie ćwiartkowe ceny mieszkań: {iqd_price:.2f} PLN")
print(f"Odchylenie ćwiartkowe powierzchni mieszkań: {iqd_square_meters:.2f} m²")

#WSKAZNIK SKOSNOSCI

# Obliczanie wskaźnika skośności dla 'price' (ceny mieszkań)
skewness_price = df['price'].skew()

# Obliczanie wskaźnika skośności dla 'squareMeters' (powierzchnie mieszkań)
skewness_square_meters = df['squareMeters'].skew()

# Wyświetlanie wyników
print(f"Wskaźnik skośności ceny mieszkań: {skewness_price:.2f}")
print(f"Wskaźnik skośności powierzchni mieszkań: {skewness_square_meters:.2f}")

#KLASYCZNO-POZYCYJNY WSKAZNIK ASYMETRII

# Obliczanie kwartylów i mediany dla 'price' (ceny mieszkań)
q1_price = df['price'].quantile(0.25)
q3_price = df['price'].quantile(0.75)
median_price = df['price'].median()

# Klasyczno-pozycyjny wskaźnik asymetrii dla 'price'
ap_price = (q3_price + q1_price - 2 * median_price) / (q3_price - q1_price)

# Obliczanie kwartylów i mediany dla 'squareMeters' (powierzchnie mieszkań)
q1_square_meters = df['squareMeters'].quantile(0.25)
q3_square_meters = df['squareMeters'].quantile(0.75)
median_square_meters = df['squareMeters'].median()

# Klasyczno-pozycyjny wskaźnik asymetrii dla 'squareMeters'
ap_square_meters = (q3_square_meters + q1_square_meters - 2 * median_square_meters) / (q3_square_meters - q1_square_meters)

# Wyświetlanie wyników
print(f"Klasyczno-pozycyjny wskaźnik asymetrii ceny mieszkań: {ap_price:.2f}")
print(f"Klasyczno-pozycyjny wskaźnik asymetrii powierzchni mieszkań: {ap_square_meters:.2f}")

# POZYCYJNY WSKAZNIK ASYMETRII

# Obliczanie kwartylów i mediany dla 'price' (ceny mieszkań)
q1_price = df['price'].quantile(0.25)
q3_price = df['price'].quantile(0.75)
median_price = df['price'].median()

# Pozycyjny wskaźnik asymetrii dla 'price'
pos_asymmetry_price = (q3_price - median_price) / (median_price - q1_price)

# Obliczanie kwartylów i mediany dla 'squareMeters' (powierzchnie mieszkań)
q1_square_meters = df['squareMeters'].quantile(0.25)
q3_square_meters = df['squareMeters'].quantile(0.75)
median_square_meters = df['squareMeters'].median()

pos_asymmetry_square_meters = (q3_square_meters - median_square_meters) / (median_square_meters - q1_square_meters)

print(f"Pozycyjny wskaźnik asymetrii ceny mieszkań: {pos_asymmetry_price:.2f}")
print(f"Pozycyjny wskaźnik asymetrii powierzchni mieszkań: {pos_asymmetry_square_meters:.2f}")

#KLASYCZNY WSKAZNIK ASYMETRII
# Obliczanie klasycznego współczynnika asymetrii dla price
skewness_price = skew(df['price'])

# Obliczanie klasycznego współczynnika asymetrii dla squareMeters
skewness_square_meters = skew(df['squareMeters'])

print(f"Klasyczny współczynnik asymetrii ceny mieszkań: {skewness_price:.2f}")
print(f"Klasyczny współczynnik asymetrii powierzchni mieszkań: {skewness_square_meters:.2f}")

#WSPOLCZYNNIK KORELACJI PEARSONA

correlation_price_size = df['price'].corr(df['squareMeters'])
print(f"Współczynnik korelacji Pearsona między ceną a powierzchnią mieszkań: {correlation_price_size:.2f}")

# histogram dla ceny
plt.figure(figsize=(10, 6))
plt.hist(df['price'], bins=10, color='blue', edgecolor='black', alpha=0.7)
plt.title('Histogram dla Ceny mieszkań', fontsize=14)
plt.xlabel('Cena (PLN)', fontsize=12)
plt.ylabel('Liczba mieszkań', fontsize=12)
plt.show()

#histogram dla powierzchni

plt.figure(figsize=(10, 6))
plt.hist(df['squareMeters'], bins=10, color='blue', edgecolor='black', alpha=0.7)
plt.title('Histogram dla powierzchni mieszkań', fontsize=14)
plt.xlabel('Powierzchnia mieszkań (m²)', fontsize=12)
plt.ylabel('Liczba mieszkań', fontsize=12)
plt.show()