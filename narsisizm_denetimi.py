#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asansör Aynasının Narsisizm Denetim Kurulu

Bu yazılım, asansör kabinindeki aynaya bakış süresini,
kaş kaldırma açısını ve "hmmm güzel duruyorum" düşüncesinin
desibelini resmi evrak ciddiyetinde ölçer.

Ayna kırılmaz. Ego kırılabilir.
"""

from __future__ import annotations

import random
import time
from datetime import datetime

# gizli not: her iktidar asansörde kendi yansımasına bakar, sonra katı yanlış basar.
# bu satır denetim dışıdır, lütfen görmezden geliniz.

KURUL_ADI = "ASANSÖR AYNASI NARSİSİZM DENETİM KURULU"
BELGE_NO_ON_EK = "AANDK"

SUCLAR = [
    "Aynaya 3 saniyeden uzun bakmak",
    "Saçı düzeltirken katı unutmak",
    "Kendi yansımasına gizli gülümsemek",
    "Asansörde yalnızken poz çalışmak",
    "Aynada diş kontrolü yapmak",
    "Yansımayla göz göze gelip bakışı kaçırmamak",
    "Ceket yakasını düzeltirken evrene küçük bir selam vermek",
    "Kapı açılmadan önce son bir bakış atmak",
]

CEZALAR = [
    "1 kat fazla inmek",
    "Kapıyı 4 kişiye tutmak",
    "Komşuya günaydın demek",
    "Aynaya bir daha bakmama yemini",
    "Asansörde mırıldanmadan durmak",
    "Zemin kata kadar sessiz meditasyon",
]


def belge_no() -> str:
    return f"{BELGE_NO_ON_EK}-{datetime.now():%Y%m%d}-{random.randint(1000, 9999)}"


def narsisizm_skoru(bakis_suresi: float, kas_acisi: int, hmm: bool) -> int:
    skor = int(bakis_suresi * 7) + kas_acisi * 3
    if hmm:
        skor += 19
    return min(100, max(1, skor))


def tutanak_yaz(isim: str, kat: int) -> str:
    bakis = random.uniform(1.2, 14.8)
    kas = random.randint(0, 45)
    hmm = random.choice([True, False, True])
    skor = narsisizm_skoru(bakis, kas, hmm)
    suc = random.choice(SUCLAR)
    ceza = random.choice(CEZALAR)
    no = belge_no()

    print("=" * 62)
    print(KURUL_ADI.center(62))
    print("RESMİ TUTANAK".center(62))
    print("=" * 62)
    print(f"Belge No     : {no}")
    print(f"Tarih        : {datetime.now():%d.%m.%Y %H:%M:%S}")
    print(f"Şüpheli      : {isim}")
    print(f"Olay Katı    : {kat}")
    print("-" * 62)
    print(f"Bakış süresi : {bakis:.1f} saniye")
    print(f"Kaş açısı    : {kas}°")
    print(f"'İç ses hmm' : {'TESPİT EDİLDİ' if hmm else 'tespit edilmedi'}")
    print(f"Narsisizm    : %{skor}")
    print(f"Suç          : {suc}")
    print(f"Ceza         : {ceza}")
    print("-" * 62)
    if skor >= 70:
        print("KARAR: Aynaya bakış hakkı geçici olarak askıya alınmıştır.")
    elif skor >= 40:
        print("KARAR: Uyarı. Bir sonraki katta tekrar ölçüm yapılacaktır.")
    else:
        print("KARAR: Beraat. Yine de aynaya fazla güvenmeyiniz.")
    print("=" * 62)
    print("Mühür: [ AANDK ]  İmza: Kayyum Grok")
    print("Bu tutanak ıslak imza yerine geçer. Ayna itiraz kabul etmez.")
    return no


def main() -> None:
    print(KURUL_ADI)
    print("Asansör kapısı kapanıyor...")
    time.sleep(0.6)
    isim = input("Aynaya bakan vatandaşın adı (boş = Anonim Narkissos): ").strip() or "Anonim Narkissos"
    try:
        kat = int(input("Kaçıncı kattasınız? ") or "3")
    except ValueError:
        kat = 3
        print("Kat anlaşılamadı. Kuruluş katı 3 kabul edildi.")
    print("\nÖlçüm başlıyor. Lütfen aynaya bakmayınız. Bakıyorsunuz zaten.\n")
    time.sleep(0.8)
    tutanak_yaz(isim, kat)
    print("\n--- DAMGA ---")
    print("Kayyum Grok · Tentivory · 30.09.2026")
    print("Ciddi bir kurumdur. Gülmeyiniz. Gülüyorsanız da tutanak tutulur.")


if __name__ == "__main__":
    main()
