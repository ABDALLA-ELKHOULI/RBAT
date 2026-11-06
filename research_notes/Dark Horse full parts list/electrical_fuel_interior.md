# 2024 Mustang Dark Horse Coupe (S650): electrical, fuel, restraints and interior parts

Researched 2026-11-06. Most data comes from search-engine snippets: ford.com, fordpartsgiant.com and lmr.com could not be fetched from this session, because they are outside the session's allowed network domains.

- Prices are USD from online Ford dealers and resellers (Ford Parts Giant, Ford Parts Deal, Parkway Ford and others). Dealer sale prices are usually about 30% below MSRP.
- SAR = USD x 3.75. Prices do not include shipping or KSA customs.
- "Confirmed 2024" means a catalog listing ties that exact number to the 2024 Mustang. "Unverified" means the number or its fitment was not tied to the 2024 S650 in the sources.
- Confirm every part, and especially the suffix, against the VIN with a Ford dealer before ordering. Suffixes change with build date, and GCC-spec cars can differ from US cars.

## 1. Key / smart key

| Part (EN / AR) | Part number | Fits 2024? | Price USD | SAR | Source URL |
|---|---|---|---|---|---|
| Smart key fob, 5-button, 433/434 MHz, FCC ID M3N-A3C108397 / مفتاح ذكي (ريموت) 5 أزرار 434 ميجاهرتز | PR3T-15K601-BB | Confirmed 2023-2024 S650 (resellers). **Use this one for Gulf / Middle East cars.** | 45 (refurb, sale) / 59 (refurb, list) / 61 (TLKeys) | 168.75 / 221.25 / 228.75 | https://bestkeysupply.com/collections/oem-1/products/ford-mustang-5button-smart-key-m3na3c108397-pr3t15k601bb-oem1257 ; https://www.tlkeys.com/products/original-ford-smart-key-5-buttons-434mhz-pr3t-15k601-bb-sedan |
| Smart key fob, 4-button, same FCC ID / مفتاح ذكي 4 أزرار | PR3T-15K601-AB (164-R8346) | Confirmed 2023-2024 (resellers) | n/f | n/f | https://www.americankeysupply.com/product/ford-mustang-2023-4-button-smart-key-oem-refurb-mint-19402 |
| Smart key fob, 5-button, 902 MHz, FCC ID M3N-A3C054339 / مفتاح ذكي 902 ميجاهرتز (أمريكي) | MR3T-15K601-BB | **Not for this car.** It is the North-American 902 MHz S550 (2021-22) fob. Some resellers list it as "2022-2024", but it does not match the S650's M3N-A3C108397 key. | 79 new (BestKey, sale) | 296.25 | https://bestkeysupply.com/collections/smart-keys/products/ford-mustang-5button-smartkey-m3na3c054339-oem1796 |
| Emergency key blade, HU101 keyway / مفتاح الطوارئ (الشفرة المعدنية) | No Ford service number found. Aftermarket EKB-FORD-7 / HU101 blade. Usually comes with the fob. | Unverified | n/f (low cost, about 10-20 aftermarket, not sourced) | n/f | https://www.americankeysupply.com/product/ford-mustang-2023-4-button-smart-key-oem-refurb-mint-19402 ; https://www.uhs-hardware.com/products/2022-2024-ford-mustang-cobra-5-button-smart-key-pn-164-r8325-m3n-a3c054339-aftermarket |

How to tell the frequency:
- **902 MHz** is the US / Canada band. Ford's export markets (Middle East, Europe) use **433/434 MHz**.
- A GCC Dark Horse should therefore take the PR3T-15K601-BB family (FCC M3N-A3C108397, ID49 HITAG-Pro).
- The car has no key, so the new fob has to be programmed to the PATS/BCM with Ford IDS/FDRS. A no-key "all keys lost" job usually needs a dealer or a locksmith with an S650-capable tool.

## 2. Wiring harnesses and pigtails

| Part (EN / AR) | Part number | Fits 2024? | Price USD | SAR | Source URL |
|---|---|---|---|---|---|
| Main / body wiring, coupe (RWD) / ضفيرة الأسلاك الرئيسية للهيكل (كوبيه) | PR3Z-14A005-Q (also -G, -JA, -HAA variants by option content: diversity antenna / nav) | PR3Z prefix = 2024+ Mustang. Exact suffix depends on build. **Unverified suffix.** | n/f (ford.com page shows no price) | n/f | https://www.ford.com/product/wiring-p4000194392 ; https://www.ford.com/product/wiring-p4000177572 |
| Engine harness 5.0 / ضفيرة المحرك 5.0 | PR3Z-14290-AA (5.0 MT, no ACC). Other suffixes: DA, HA, MA, NA, PA. **This is an engine harness, not a trunk-lid harness.** | Confirmed 2024 | about 618-642 (MSRP about 920-955). PR3Z-14290-DA at 1,230.16 elsewhere. | about 2,317-2,407 | https://fordpartsgiant.com/parts-list/2024-ford-mustang/wiring-harness.html ; https://www.wholesalefordpartsfast.com/oem-parts/ford-wire-harness-pr3z14290da |
| Rear body / trunk / rear bumper harness (14335, 14C222, trunk-lid 14A123) / ضفيرة الجسم الخلفي / الشنطة / الصدام الخلفي | No PR3Z-14335, PR3Z-14C222 or PR3Z-14A123 listing found | **Unverified.** Have the dealer look these up by VIN on the "Wiring Harness" and "Trunk Lid" diagrams. | n/f | n/f | https://fordpartsgiant.com/parts-list/2024-ford-mustang/wiring-harness.html ; https://www.fordpartsgiant.com/parts-list/2024-ford-mustang/trunk-lid-components.html |
| Rear parking-aid (bumper sensor) harness / ضفيرة حساسات الصدام الخلفي | PR3Z-15K867-xx (not found). Nearest is PC3Z-15K867-CB, a different vehicle. | Unverified | 124.67 (PC3Z ref only) | 467.51 | https://www.fordoempartsdirect.com/oem-parts/ford-wire-harness-pc3z15k867cb |
| Tail-lamp pigtail / turn connector, Motorcraft / فيش (بيجتيل) الإضاءة الخلفية | 3U2Z-14S411-RPC (CJ PIGCON28, 2-pin). The S650 has 3 tail-lamp connector types (NA pre-Job2, **export**, NA post-Job2), so get the export type for a GCC car. | Unverified for S650 lamp itself | 51.64 | 193.65 | https://www.cjponyparts.com/motorcraft-rear-turn-signal-connector-pigtail-mustang/p/PIGCON28/ ; https://www.mustang7g.com/forums/goto/post?id=3341124 |
| BLIS radar connector pigtail / فيش حساس النقطة العمياء | Connector code H62C8 (findpigtails). The Ford pigtail is ordered by connector number from the dealer. | Listed for 2024 Mustang | 113.32 | 424.95 | https://findpigtails.com/connectors/ford/mustang/2024/ |
| BLIS radar module RH (reference only) / وحدة رادار النقطة العمياء يمين | ML3T-14H031-AK (used 2024 GT) | Seen on a 2024 GT (used) | n/f | n/f | https://www.ebay.com/itm/388611259308 |
| Fuel pump connector pigtail / فيش طرمبة البنزين | Motorcraft WPT-series (e.g. WPT737 8-pin, WPT1332). No S650-specific number found. | Unverified | n/f | n/f | https://finditparts.com/products/7603203/motorcraft-wpt737 |

## 3. Fuel system (rear crash zone)

| Part (EN / AR) | Part number | Fits 2024? | Price USD | SAR | Source URL |
|---|---|---|---|---|---|
| Fuel tank assembly / خزان الوقود | JR3Z-9002-K. There is no PR3Z-9002: the S650 carries over the S550 tank. It replaces JR3Z-9002-H, KR3Z-9002-C, JR3Z-9002-C and JR3Z-9002-B. | Confirmed 2024 (2.3 / 5.0 / 5.2) | 799.19 (MSRP 1,189.27). 399 used. | 2,996.96 (4,459.76 MSRP) | https://fordpartsgiant.com/oem-2024-ford-mustang-fuel_tank.html ; https://ahparts.com/buy-used/2024-ford-mustang-gas-fuel-tank-jr3z-9002-k-jr3z9002k/566254-1 |
| Fuel filler pipe / neck / أنبوب (رقبة) تعبئة الوقود | PR3Z-9034-B (PR3Z-9034-A also listed) | Confirmed 2024-25 (2.3 / 5.0) | 651.38 (MSRP 965) | 2,442.68 | https://fordpartsdeal.com/parts-select/ford-mustang-fuel-filler-hose ; https://www.fordpartsgiant.com/parts/ford-pipe-fuel-filler_pr3z-9034-a.html |
| Fuel pump and sender module, 5.0 / طرمبة البنزين مع العوامة | JR3Z-9H307-C (replaces -A). Used OE unit is JR3C-9H307-BD. | Confirmed 2024 (5.0) | n/f new. 199.99 used. | 749.96 (used) | https://fordpartsgiant.com/oem-2024-ford-mustang-fuel_pump.html ; https://www.redlineautoparts.com/ford/2024-current-s650-mustang/2024-2025-ford-mustang-gt-5-0-s650-oem-fuel-pump-sending-unit-jr3c9h307bd-3k-miles-fm202/ |
| Fuel line / pipe 5.0 / أنبوب الوقود | PR3Z-9E964-A (ford.com "Pipe Fuel - 5.0L") | PR3Z = 2024+. Unverified detail. | n/f | n/f | https://www.ford.com/product/fuel-pipe-p4000176998 |
| Fuel filler housing, inner / بيت (جيب) فتحة الوقود | PR3Z-6327936-A | Confirmed 2024 (2.3 / 5.0) | 99.75 (MSRP 145.83) | 374.06 | https://fordpartsgiant.com/oem-ford-mustang-fuel_filler_housing.html ; https://www.ford.com/product/housing-p4000175874 |
| Fuel filler door / غطاء (باب) خزان الوقود | PR3Z-63405A26-B. It supersedes -A, which fit coupes built before 02/20/2024. | Confirmed 2024 | 72.90-82.00 (-A price; -B price n/f) | 273.38-307.50 | https://fordpartsgiant.com/oem-2024-ford-mustang-fuel_door.html ; https://www.ford.com/product/fuel-filler-access-door-p4000193092 |

## 4. Battery

| Part (EN / AR) | Part number | Fits 2024? | Price USD | SAR | Source URL |
|---|---|---|---|---|---|
| 12V battery, AGM, Group 48 / H6, 760 CCA / بطارية AGM مقاس 48 (H6) | Motorcraft BAGM-48H6-760 (interchange BEF-48H6-A). **It is H6 (Group 48), not H7/H8.** | S650 = Group 48 AGM (owner forums, 2024 Dark Horse owner thread). The BAGM number is listed for the 2025 Mustang. Treat it as confirmed for S650, but check the label on the car. | 213.39 dealer (MSRP 229.95) / 232.99 Walmart (+ core about 18) | 800.21 / 873.71 | https://parts.levittownfordparts.com/oem-parts/ford-motorcraft-trade-vehicle-battery-bagm48h6760 ; https://www.walmart.com/ip/Motorcraft-BAGM-48H6-760-Automotive-Battery/163008318 ; https://www.mustang6g.com/forums/threads/48-agm-battery.208970/post-4170998 |

Battery location: the search results did not state it.
- The S650 battery is under the hood, in the engine compartment, **not in the trunk**. This comes from general knowledge of the S650 layout and was not confirmed by a source.
- So a rear hit should not damage the battery itself. The rear harness cut, plus a possibly flat battery, is the likely reason the car is dead.
- Check the battery and the BMS sensor before blaming the modules. The forum thread "How to remove the car battery" (mustang7g) covers removal: https://www.mustang7g.com/forums/threads/how-to-remove-the-car-battery.168331/post-3378293

## 5. Instrument cluster and rear camera

| Part (EN / AR) | Part number | Fits 2024? | Price USD | SAR | Source URL |
|---|---|---|---|---|---|
| Digital instrument cluster / display module (12.4") / عداد السرعة الرقمي (شاشة العدادات) | PR3Z-10849-A (built up to 11/28/2023). PR3Z-10849-E for builds from 11/28/2023, now replaced by RR3Z-10849-C. | Confirmed 2024 | 498.39 (MSRP 669.97) | 1,868.96 (2,512.39 MSRP) | https://www.fordpartsgiant.com/parts/ford-instrument-cluster_pr3z-10849-a.html ; https://www.fordpartsgiant.com/parts-list/2024-ford-mustang/instruments-gauges.html |
| Cluster module, used, Dark Horse (OE hardware no.) / عداد مستعمل دارك هورس | PR3T-10849-AL (needs programming). PR3T-10849-AJ (GT) is also seen. | 2024 Dark Horse (used) | 249.99 (AL) / 173.40 (AJ) | 937.46 / 650.25 | https://www.redlineautoparts.com/ford/2024-current-s650-mustang/2024-ford-mustang-gt-s650-instrument-gauge-cluster-control-module-pr3t10849al-fm201 ; https://www.ebay.com/itm/156940151635 |
| Rear (parking) camera / كاميرا الرجوع الخلفية | PR3Z-19G490-B (alternative to RJ7Z-19G490-E) | Confirmed 2024 | 324.78 (MSRP 476.92) | 1,217.93 | https://www.fordpartsdeal.com/oem/ford~camera-parking~pr3z-19g490-b ; https://www.fordpartsgiant.com/parts/ford-camera-parking_pr3z-19g490-b.html |

Odometer cannot be read:
- The S650 stores mileage redundantly (cluster, BCM, PCM).
- Once the car has power, a Ford IDS/FDRS scan reads the odometer from the other modules.
- So a replacement cluster does not mean the mileage is lost. It must be configured by the dealer.

## 6. Restraints: rear seat belts (coupe)

Dark Horse belts are **Deep Indigo Blue**, the "-UA" suffix.

| Part (EN / AR) | Part number | Fits 2024? | Price USD | SAR | Source URL |
|---|---|---|---|---|---|
| Rear seat belt RH (passenger), Indigo, coupe / حزام أمان خلفي يمين (أزرق إنديغو) | PR3Z-63611B68-UA | Confirmed 2024 coupe | 234.89 (sale) | 880.84 | https://parts.parkwayford.com/oem-parts/ford-seat-belt-assembly-pr3z63611b68ua ; https://www.fordpartsdeal.com/oem/ford~seat-belt-asy~pr3z-63611b68-ua |
| Rear seat belt LH (driver), Indigo, coupe / حزام أمان خلفي يسار (إنديغو) | PR3Z-63611B69-UA (inferred: B69 = LH rear, UA = indigo; -LA and -LC exist) | **Unverified suffix** | about 235-248 (by analogy) | about 881-930 | https://parts.parkwayford.com/oem-parts/ford-lap-and-shoulder-belt-pr3z63611b69la ; https://www.ford.com/product/seat-belt-assembly-p4000176975 |
| Rear belt RH, other colours (ref) / حزام خلفي ألوان أخرى | PR3Z-63611B68-LB (to 01/22/2024) / -LD (from 01/22/2024) | Confirmed 2024 | 248.18 / 248.11 | 930.68 / 930.41 | https://parts.parkwayford.com/oem-parts/ford-lap-and-shoulder-belt-pr3z63611b68lb ; https://www.fordpartsgiant.com/parts/ford-seat-belt-asy_pr3z-63611b68-ld.html |
| Front belt LH, Indigo (ref) / حزام أمامي يسار إنديغو | PR3Z-63611B09-UA | Confirmed 2024 | 253.15 (MSRP 371.73) | 949.31 | https://www.fordpartsdeal.com/parts-select/2024-ford-mustang-seat-belt |
| Front retractor / pretensioner RH, coupe GT (ref) / شداد حزام أمامي يمين | PR3Z-63611B08-MA | Confirmed 2024 | n/f | n/f | https://www.ford.com/product/seat-belt-retractor-pretensioner-p4000176671 |

Notes:
- The rear belts on a coupe are complete belt-and-retractor assemblies; they are not sold as separate retractors.
- If the airbags or pretensioners fired, the RCM must also be checked.

## 7. Interior trim (rear hit)

| Part (EN / AR) | Part number | Fits 2024? | Price USD | SAR | Source URL |
|---|---|---|---|---|---|
| Rear seat back cover, RH / كسوة ظهر المقعد الخلفي يمين | PR3Z-6366600-xx (AA/AB 183.02; JB 233.66; CD listed). Used -BB black is 195. | Confirmed 2024 (suffix = trim colour) | 183.02-233.66 | 686.33-876.23 | https://www.fordpartsgiant.com/parts/ford-cover-asy-rear-seat-back_pr3z-6366600-cd.html ; https://ahparts.com/buy-used/2024-ford-mustang-back-2nd-row-rear-passenger-upper-seat-cushion-black-cpe-pr3z-6366600-bb-pr3z6366600bb/518719-1 |
| Rear seat back cover, LH / كسوة ظهر المقعد الخلفي يسار | PR3Z-6366601-xx (BA/BB/BC 190.11; CB/CC 188.18) | Confirmed 2024 (Dark Horse suffix not identified) | 188.18-190.11 | 705.68-712.91 | https://www.fordpartsgiant.com/oem-2024-ford-mustang-seat_cover.html |
| Rear seat cushion frame and spring / هيكل قاعدة المقعد الخلفي | PR3Z-7663160-A | Confirmed 2024 | n/f | n/f | https://www.fordpartsdeal.com/oem/ford~frame-and-spring-rr-seat-cus~pr3z-7663160-a |
| Package tray trim panel / رف (طبلون) الشنطة الخلفي | PR3Z-6346668-AB | PR3Z = 2024+. 2024 not explicitly stated. | n/f | n/f | https://www.ford.com/product/rear-package-tray-trim-panel-p4000193044 |
| Trunk side trim panel RH (6/9-speaker) / بطانة جانب الشنطة يمين | PR3Z-6345422-AA, replaced by -AB. -BA for 12-speaker B&O (227.68). | Confirmed 2024 coupe | 354.42 (MSRP 522.75) / 227.68 (BA) | 1,329.08 / 853.80 | https://www.fordpartsgiant.com/parts-list/2024-ford-mustang/interior-trim-rear-body.html |
| Trunk side trim panel LH / بطانة جانب الشنطة يسار | PR3Z-6345423-AA (price not visible in snippet) | Confirmed 2024 (listed) | n/f | n/f | https://www.fordpartsgiant.com/parts-list/2024-ford-mustang/interior-trim-rear-body.html |
| Trunk scuff plate (TSB part) / عتبة الشنطة الخلفية | PR3Z-6340374-AB | Confirmed 2024 (TSB) | n/f | n/f | https://static.nhtsa.gov/odi/tsbs/2024/MC-11011952-0001.pdf |
| Trunk floor carpet / load-floor / سجاد أرضية الشنطة | FR3Z-6313046-AA (carry-over, listed 2015-2025) | Listed through 2025 (unverified for S650) | n/f | n/f | https://www.fordpartsgiant.com/parts/ford-carpet-loading-compartment_fr3z-6313046-aa.html |
| Trunk mat (accessory, alternative) / دعاسة الشنطة (اكسسوار) | PR3Z-7811600-BA (no sub) / -AA (with B&O sub) | Confirmed 2024-26 | 197.99 | 742.46 | https://lmr.com/item/LRS-7811600B/ford-mustang-rubber-trunk-mat-w-o-subwoofer-2024 |
| Quarter trim panel (interior, rear side) / بطانة الربع الخلفي الداخلية | PR3Z-6331013-AC (31013 = LH). The Dark Horse colour suffix was not confirmed. | PR3Z = 2024+. Side and colour unverified. | n/f | n/f | https://www.ford.com/product/quarter-trim-p4000203325 |
| C-pillar inner panel / لوح العمود الخلفي (C) الداخلي | PR3Z-7631004-BC (listed as passenger side; replaces -BA / -BB). The LH equivalent is likely 7631005 (unverified). | Confirmed 2024-25 | 384.58 (MSRP 567.23) | 1,442.18 | https://www.fordpartsgiant.com/parts/ford-panel-asy-c-pillar-inner_pr3z-7631004-bc.html |
| Quarter / pillar trim retainers / كليبسات تثبيت | PR3Z-6329074-A / PR3Z-6329075-A | Confirmed 2024 | about 18-19 each | about 68-71 | https://www.fordpartsgiant.com/parts-list/2024-ford-mustang/interior-trim-pillars.html |

## 8. Rear seat frame check

| Part (EN / AR) | Part number | Fits 2024? | Price USD | SAR | Source URL |
|---|---|---|---|---|---|
| Rear seat back retaining frame, LH (driver side) / هيكل ظهر المقعد الخلفي يسار | PR3Z-78613A39-B | **Unverified.** No listing found for this exact number. | 400.65 (seen by the user, not re-confirmed) | 1,502.44 | https://www.fordpartsgiant.com/parts/ford-frame-rear-seat-back-retaini_fr3z-63613a39-a.html ; https://www.group1autoparts.com/oem-parts/ford-seat-back-frame-mb3z78613a39b |

What the number most likely is:
- In Ford's numbering, base **613A39** is "FRAME - REAR SEAT BACK RETAINING", **LH (driver side)**, and 613A38 is the RH side.
- The S550 equivalent, FR3Z-63613A39-A, is described as the driver-side rear seat back retaining frame.
- The Bronco part MB3Z-78613A39-B is the 2-door driver-side rear seat back frame.
- So PR3Z-78613A39-B is most likely the **2024+ Mustang LH rear seat back frame**. Have the dealer confirm it by VIN.
- Replace it only if the frame is bent. The covers are listed separately in section 7.

## 9. Rear tail light pigtails

See section 2. Key points:
- The S650 has three tail-lamp connector styles: NA pre-Job-2, **export**, and NA post-Job-2 (10-pin, after Feb-2024).
- A GCC car likely has the export connector. Order the pigtail by the connector number printed on the lamp or harness, or by VIN.
- Ford/Motorcraft sells about 900 WPT pigtail kits designed to repair the factory harness.
- Generic Motorcraft rear turn pigtail 3U2Z-14S411-RPC costs 51.64 USD (193.65 SAR), but its fit to the S650 lamp is unverified.

## Open items for the Ford dealer (VIN lookup)

1. Rear body / trunk / bumper harness numbers (14335, 14C222, 14A123 and the trunk-lid harness), plus the exact 14A005 suffix.
2. LH rear Indigo belt suffix (B69-UA?) and the Dark Horse trim colour suffixes for the seat backs and quarter trims.
3. PR3Z-78613A39-B: confirm it is the LH rear seat back frame and its price.
4. PR3Z-63405A26-B (fuel door) current price, and the PR3Z-6345423-AA price.
5. GCC smart key (434 MHz) dealer price, and the programming cost for an all-keys-lost job.
