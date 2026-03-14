#!/usr/bin/env python3
"""
Generate a well-formatted PDF from the HOCM teaching markdown.
Uses reportlab with CJK font support (STSong-Light for Chinese).
"""

import re
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm, cm
from reportlab.lib.colors import HexColor, black, white, Color
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont

# Register CJK fonts
pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))

# Color palette
PRIMARY = HexColor('#0077B6')
PRIMARY_DARK = HexColor('#03045E')
ACCENT = HexColor('#FF6B35')
SUCCESS = HexColor('#2EC4B6')
WARNING = HexColor('#FFBE0B')
INFO = HexColor('#4361EE')
TEXT_DARK = HexColor('#1A1A2E')
TEXT_MEDIUM = HexColor('#4A4A68')
LIGHT_BG = HexColor('#F0F7FF')
TABLE_HEADER_BG = HexColor('#0077B6')
TABLE_ALT_BG = HexColor('#F5F9FF')
BORDER_COLOR = HexColor('#D1D5DB')

def create_styles():
    """Create custom paragraph styles with CJK font support."""
    styles = getSampleStyleSheet()

    # Override default styles with CJK font
    base_font = 'STSong-Light'

    styles.add(ParagraphStyle(
        name='CJKTitle',
        fontName=base_font,
        fontSize=22,
        leading=30,
        textColor=PRIMARY_DARK,
        alignment=TA_CENTER,
        spaceAfter=6*mm,
        spaceBefore=4*mm,
    ))

    styles.add(ParagraphStyle(
        name='CJKSubtitle',
        fontName=base_font,
        fontSize=10,
        leading=16,
        textColor=TEXT_MEDIUM,
        alignment=TA_CENTER,
        spaceAfter=8*mm,
    ))

    styles.add(ParagraphStyle(
        name='CJKHeading1',
        fontName=base_font,
        fontSize=16,
        leading=24,
        textColor=PRIMARY_DARK,
        spaceBefore=10*mm,
        spaceAfter=4*mm,
        borderWidth=0,
        borderColor=PRIMARY,
        borderPadding=0,
    ))

    styles.add(ParagraphStyle(
        name='CJKHeading2',
        fontName=base_font,
        fontSize=13,
        leading=20,
        textColor=PRIMARY,
        spaceBefore=6*mm,
        spaceAfter=3*mm,
    ))

    styles.add(ParagraphStyle(
        name='CJKHeading3',
        fontName=base_font,
        fontSize=11,
        leading=17,
        textColor=TEXT_DARK,
        spaceBefore=4*mm,
        spaceAfter=2*mm,
    ))

    styles.add(ParagraphStyle(
        name='CJKBody',
        fontName=base_font,
        fontSize=9.5,
        leading=16,
        textColor=TEXT_DARK,
        alignment=TA_JUSTIFY,
        spaceAfter=2*mm,
    ))

    styles.add(ParagraphStyle(
        name='CJKBullet',
        fontName=base_font,
        fontSize=9.5,
        leading=15,
        textColor=TEXT_DARK,
        leftIndent=8*mm,
        spaceAfter=1.5*mm,
        bulletIndent=3*mm,
    ))

    styles.add(ParagraphStyle(
        name='CJKSubBullet',
        fontName=base_font,
        fontSize=9,
        leading=14,
        textColor=TEXT_MEDIUM,
        leftIndent=14*mm,
        spaceAfter=1*mm,
        bulletIndent=9*mm,
    ))

    styles.add(ParagraphStyle(
        name='CJKBlockquote',
        fontName=base_font,
        fontSize=9,
        leading=15,
        textColor=TEXT_MEDIUM,
        leftIndent=8*mm,
        rightIndent=4*mm,
        spaceAfter=3*mm,
        borderWidth=1,
        borderColor=PRIMARY,
        borderPadding=4*mm,
        backColor=LIGHT_BG,
    ))

    styles.add(ParagraphStyle(
        name='CJKWarning',
        fontName=base_font,
        fontSize=9.5,
        leading=15,
        textColor=HexColor('#92400E'),
        leftIndent=6*mm,
        rightIndent=4*mm,
        spaceAfter=3*mm,
        spaceBefore=2*mm,
        borderWidth=1,
        borderColor=WARNING,
        borderPadding=3*mm,
        backColor=HexColor('#FFFBEB'),
    ))

    styles.add(ParagraphStyle(
        name='CJKTableCell',
        fontName=base_font,
        fontSize=8.5,
        leading=13,
        textColor=TEXT_DARK,
    ))

    styles.add(ParagraphStyle(
        name='CJKTableHeader',
        fontName=base_font,
        fontSize=8.5,
        leading=13,
        textColor=white,
    ))

    styles.add(ParagraphStyle(
        name='CJKFooter',
        fontName=base_font,
        fontSize=8,
        leading=12,
        textColor=TEXT_MEDIUM,
        alignment=TA_CENTER,
    ))

    styles.add(ParagraphStyle(
        name='CJKReference',
        fontName=base_font,
        fontSize=8,
        leading=12,
        textColor=TEXT_MEDIUM,
        leftIndent=4*mm,
        spaceAfter=1*mm,
    ))

    styles.add(ParagraphStyle(
        name='CJKCode',
        fontName=base_font,
        fontSize=7.5,
        leading=11,
        textColor=TEXT_DARK,
        leftIndent=4*mm,
        rightIndent=4*mm,
        spaceAfter=3*mm,
        spaceBefore=2*mm,
        backColor=HexColor('#F3F4F6'),
        borderWidth=0.5,
        borderColor=BORDER_COLOR,
        borderPadding=3*mm,
    ))

    return styles


def make_table(headers, rows, col_widths=None):
    """Create a styled table."""
    styles = create_styles()

    header_cells = [Paragraph(h, styles['CJKTableHeader']) for h in headers]
    data = [header_cells]

    for row in rows:
        data.append([Paragraph(str(cell), styles['CJKTableCell']) for cell in row])

    if col_widths is None:
        available = 170*mm
        col_widths = [available / len(headers)] * len(headers)

    table = Table(data, colWidths=col_widths, repeatRows=1)

    style_commands = [
        ('BACKGROUND', (0, 0), (-1, 0), TABLE_HEADER_BG),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, BORDER_COLOR),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
    ]

    # Alternating row colors
    for i in range(1, len(data)):
        if i % 2 == 0:
            style_commands.append(('BACKGROUND', (0, i), (-1, i), TABLE_ALT_BG))

    table.setStyle(TableStyle(style_commands))
    return table


def add_header_line(story, styles):
    """Add a colored horizontal line."""
    story.append(HRFlowable(
        width="100%", thickness=1.5, color=PRIMARY,
        spaceAfter=3*mm, spaceBefore=1*mm
    ))


def build_pdf(md_path, output_path):
    """Build PDF from HOCM markdown content."""
    styles = create_styles()

    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        rightMargin=18*mm,
        leftMargin=18*mm,
        topMargin=20*mm,
        bottomMargin=20*mm,
        title="阻塞性肥厚型心肌病變教學講義",
        author="新竹臺大醫院 心臟內科",
    )

    story = []

    # ===================== TITLE PAGE =====================
    story.append(Spacer(1, 25*mm))
    story.append(Paragraph(
        "阻塞性肥厚型心肌病變<br/>（Obstructive HCM）<br/>教學講義",
        styles['CJKTitle']
    ))
    story.append(Spacer(1, 8*mm))
    story.append(HRFlowable(width="60%", thickness=2, color=PRIMARY, spaceAfter=8*mm))
    story.append(Paragraph(
        "來源：新竹臺大醫院 心臟內科 曾新育醫師<br/>"
        "日期：2026/02/10<br/>"
        "主題：CV – CVS Meeting 病例討論",
        styles['CJKSubtitle']
    ))
    story.append(Spacer(1, 15*mm))

    # Table of Contents
    story.append(Paragraph("目  錄", styles['CJKHeading1']))
    add_header_line(story, styles)
    toc_items = [
        "1. 病例報告",
        "2. 肥厚型心肌病變概述",
        "3. HCM 治療指引",
        "4. 傳統藥物治療",
        "5. 中隔減積治療（Septal Reduction Therapy）",
        "6. 心肌肌凝蛋白抑制劑（Cardiac Myosin Inhibitors）",
        "7. Mavacamten 臨床試驗",
        "8. Mavacamten 臨床使用",
        "9. Aficamten 介紹",
        "10. 最新治療指引更新",
        "11. 結論與臨床啟示",
    ]
    for item in toc_items:
        story.append(Paragraph(item, styles['CJKBody']))
    story.append(PageBreak())

    # ===================== SECTION 1: 病例報告 =====================
    story.append(Paragraph("1. 病例報告", styles['CJKHeading1']))
    add_header_line(story, styles)

    story.append(Paragraph("基本資料", styles['CJKHeading2']))
    story.append(Paragraph("&#8226; 年齡/性別：73 歲男性", styles['CJKBullet']))
    story.append(Paragraph("&#8226; 主訴：長期胸悶及運動性呼吸困難（Chest tightness and exertional dyspnea）", styles['CJKBullet']))

    story.append(Paragraph("過去病史", styles['CJKHeading2']))
    story.append(make_table(
        ['疾病', '說明'],
        [
            ['HTN', '高血壓'],
            ['DM', '糖尿病'],
            ['Gout', '痛風'],
            ['DU', '十二指腸潰瘍'],
            ['GERD', '胃食道逆流'],
            ['家族史', '無特殊'],
        ],
        col_widths=[40*mm, 130*mm]
    ))
    story.append(Spacer(1, 3*mm))

    story.append(Paragraph("理學檢查", styles['CJKHeading2']))
    story.append(Paragraph("&#8226; 心雜音：Grade II 收縮期雜音，位於左下胸骨緣（LLSB）", styles['CJKBullet']))
    story.append(Paragraph("&#8226; 此位置的收縮期雜音高度提示左心室流出道阻塞（LVOTO）", styles['CJKBullet']))

    story.append(Paragraph("心臟超音波檢查（2018/11/19 UCG）", styles['CJKHeading2']))
    story.append(make_table(
        ['參數', '數值', '臨床意義'],
        [
            ['IVSd（心室中隔舒張期厚度）', '2.0 cm', '顯著增厚（正常 &lt; 1.1 cm）'],
            ['LVPWd（左心室後壁舒張期厚度）', '0.96 cm', '正常範圍'],
            ['IVS/LVPW 比值', '2.08', '非對稱性肥厚（比值 &gt; 1.3）'],
            ['LVEF（左心室射出分率）', '86%', '過度收縮（Hypercontractility）'],
            ['LVOT 壓力差', '58 mmHg', '顯著阻塞（&ge; 30 mmHg 為阻塞性）'],
        ],
        col_widths=[55*mm, 35*mm, 80*mm]
    ))
    story.append(Spacer(1, 3*mm))

    story.append(Paragraph("重要超音波發現", styles['CJKHeading3']))
    story.append(Paragraph("&#8226; HOCM：心室中隔顯著肥厚（2.0 cm），非對稱性肥厚型態", styles['CJKBullet']))
    story.append(Paragraph("&#8226; LVOTO：靜態壓力差 58 mmHg，符合阻塞性肥厚型心肌病變定義", styles['CJKBullet']))
    story.append(Paragraph("&#8226; SAM 陽性：二尖瓣前葉收縮期前移，造成動態性流出道阻塞", styles['CJKBullet']))
    story.append(Paragraph("&#8226; 舒張功能受損：Impaired LV relaxation", styles['CJKBullet']))
    story.append(Paragraph("&#8226; 二尖瓣逆流：MR, mild，通常與 SAM 相關", styles['CJKBullet']))

    story.append(Paragraph("心導管檢查（2018/11/17 CAG + LVG）", styles['CJKHeading2']))
    story.append(Paragraph("&#8226; 冠狀動脈攝影（CAG）：冠狀動脈通暢，排除冠狀動脈疾病", styles['CJKBullet']))
    story.append(Paragraph("&#8226; 左心室攝影（LVG）：確認肥厚型心肌病變", styles['CJKBullet']))
    story.append(Paragraph("&nbsp;&nbsp;- LV apex 收縮壓：160 mmHg；LVOT 收縮壓：105 mmHg；壓力差：55 mmHg", styles['CJKSubBullet']))

    story.append(PageBreak())

    # ===================== SECTION 2: HCM 概述 =====================
    story.append(Paragraph("2. 肥厚型心肌病變概述", styles['CJKHeading1']))
    add_header_line(story, styles)

    story.append(Paragraph("定義", styles['CJKHeading2']))
    story.append(Paragraph(
        "肥厚型心肌病變（Hypertrophic Cardiomyopathy, HCM）是一種以左心室壁異常增厚為特徵的心肌疾病，其肥厚無法以其他心臟或全身性疾病解釋。",
        styles['CJKBody']
    ))

    story.append(Paragraph("診斷標準", styles['CJKHeading2']))
    story.append(make_table(
        ['情況', '左心室壁厚度標準'],
        [
            ['一般成人', '&ge; 15 mm'],
            ['有家族史者', '&ge; 13 mm'],
            ['兒童', 'Z-score &ge; 2'],
        ],
        col_widths=[85*mm, 85*mm]
    ))
    story.append(Spacer(1, 3*mm))

    story.append(Paragraph("分類", styles['CJKHeading2']))
    story.append(make_table(
        ['類型', 'LVOT 壓力差', '特徵'],
        [
            ['阻塞性 HCM（oHCM）', '&ge; 30 mmHg（靜態或誘發後）', '約 70% 患者'],
            ['非阻塞性 HCM', '&lt; 30 mmHg', '約 30% 患者'],
        ],
        col_widths=[50*mm, 65*mm, 55*mm]
    ))
    story.append(Spacer(1, 3*mm))

    story.append(Paragraph("阻塞機制", styles['CJKHeading2']))
    story.append(Paragraph("1. 心室中隔肥厚：基底部中隔突向流出道", styles['CJKBullet']))
    story.append(Paragraph("2. SAM（Systolic Anterior Motion）：二尖瓣前葉在收縮期被吸向流出道（Venturi effect）", styles['CJKBullet']))
    story.append(Paragraph("3. 動態性阻塞：阻塞程度隨生理狀態改變", styles['CJKBullet']))
    story.append(Paragraph("&nbsp;&nbsp;- 增加阻塞：運動、Valsalva、脫水、血管擴張劑", styles['CJKSubBullet']))
    story.append(Paragraph("&nbsp;&nbsp;- 減少阻塞：蹲下、&beta;-阻斷劑、補充液體", styles['CJKSubBullet']))

    # ===================== SECTION 3: 治療指引 =====================
    story.append(Paragraph("3. HCM 治療指引", styles['CJKHeading1']))
    add_header_line(story, styles)

    story.append(Paragraph("2014 ESC 指引 — 第一線藥物治療（Class I, Level B）", styles['CJKHeading2']))
    story.append(Paragraph("&#8226; 非血管擴張型 &beta;-阻斷劑：調整至最大耐受劑量，改善症狀的首選治療", styles['CJKBullet']))
    story.append(Paragraph("&#8226; Verapamil：適用於對 &beta;-阻斷劑不耐受或有禁忌症者", styles['CJKBullet']))
    story.append(Paragraph("&#8226; Disopyramide：建議與 &beta;-阻斷劑併用", styles['CJKBullet']))

    story.append(Paragraph("2020 AHA 指引 — 治療流程", styles['CJKHeading2']))
    story.append(Paragraph(
        "阻塞性 &rarr; 有症狀 &rarr; &beta;-阻斷劑 &rarr; Verapamil/Diltiazem &rarr; 若症狀持續 &rarr; Disopyramide 或 SRT",
        styles['CJKBody']
    ))

    story.append(Paragraph("中隔減積治療適應症（Class I, Level B）", styles['CJKHeading3']))
    story.append(Paragraph("&#8226; 靜態或誘發後 LVOT 壓力差 &ge; 50 mmHg", styles['CJKBullet']))
    story.append(Paragraph("&#8226; NYHA 功能分級 Class III-IV", styles['CJKBullet']))
    story.append(Paragraph("&#8226; 儘管使用最大耐受藥物治療仍有症狀", styles['CJKBullet']))

    story.append(Paragraph("2023 ESC 指引更新", styles['CJKHeading2']))
    story.append(Paragraph(
        "Mavacamten 納入治療流程，建議等級 Class IIa，與 Disopyramide 同級。",
        styles['CJKBody']
    ))

    story.append(Paragraph("2024 AHA 指引更新", styles['CJKHeading2']))
    story.append(Paragraph(
        "Mavacamten 提升為 Class 1 建議，為第二線治療選項之一。Aficamten 目前標示為問號（?），等待更多臨床證據。",
        styles['CJKBody']
    ))

    story.append(PageBreak())

    # ===================== SECTION 4: 傳統藥物治療 =====================
    story.append(Paragraph("4. 傳統藥物治療 — 本病例治療經過", styles['CJKHeading1']))
    add_header_line(story, styles)

    story.append(Paragraph("第一階段：初始治療（2018/11/08，67 歲）", styles['CJKHeading2']))
    story.append(Paragraph("&#8226; 處方：Bisoprolol（Concor）+ Diltiazem（Herbesser）", styles['CJKBullet']))
    story.append(Paragraph("&#8226; 治療反應：初期改善，仍有間歇性胸悶，NYHA Fc II，LVOTO PG 波動於 40-109 mmHg", styles['CJKBullet']))

    story.append(Paragraph("第二階段：症狀惡化與鑑別診斷（2023/09，72 歲）", styles['CJKHeading2']))
    story.append(Paragraph("&#8226; NYHA 功能分級惡化至 Class III", styles['CJKBullet']))
    story.append(make_table(
        ['檢查項目', '結果', '臨床意義'],
        [
            ['心臟磁振造影（CMR）', '非對稱性中隔 HCM，最大壁厚 23.3 mm，無 LGE', '確認 HCM，無明顯纖維化'],
            ['&alpha;-Gal A 酵素活性', '4.63 &mu;M/hr（正常 &gt; 1.2）', '排除 Fabry disease'],
            ['Tc-99 PYP 掃描', 'Visual score 0', '排除心臟類澱粉沉積症'],
            ['免疫固定電泳（IFE）', '陰性', '排除 AL amyloidosis'],
            ['基因檢測', '無突變', '基因陰性 HCM'],
        ],
        col_widths=[50*mm, 55*mm, 65*mm]
    ))
    story.append(Spacer(1, 2*mm))
    story.append(Paragraph("&#8226; HCM Risk-SCD 評分：5 年風險 2.1%，不建議植入 ICD", styles['CJKBullet']))

    story.append(Paragraph("第三階段：藥物調整（2023/12）", styles['CJKHeading2']))
    story.append(Paragraph("&#8226; 停用 Diltiazem（原因：心搏過緩 HR 40 bpm）", styles['CJKBullet']))
    story.append(Paragraph("&#8226; UCG：LVOT 靜態壓力差 182 mmHg，Valsalva 192 mmHg", styles['CJKBullet']))
    story.append(Paragraph("&#8226; 討論中隔減積治療 &rarr; 患者拒絕侵入性治療", styles['CJKBullet']))

    # ===================== SECTION 5: 中隔減積治療 =====================
    story.append(Paragraph("5. 中隔減積治療（Septal Reduction Therapy）", styles['CJKHeading1']))
    add_header_line(story, styles)

    story.append(Paragraph("外科心肌切除術（Surgical Myomectomy）", styles['CJKHeading2']))
    story.append(Paragraph("&#8226; 適應症：異常乳頭肌、過長二尖瓣前葉、內在性二尖瓣疾病、多支血管 CAD、瓣膜性 AS", styles['CJKBullet']))
    story.append(Paragraph("&#8226; 優點：可同時處理二尖瓣問題，長期數據充足，即時持久壓力差下降", styles['CJKBullet']))
    story.append(Paragraph("&#8226; 風險：需開心手術，傳導阻滯（約 2-5% 需永久 PM）", styles['CJKBullet']))

    story.append(Paragraph("酒精中隔消融術（Alcohol Septal Ablation, ASA）", styles['CJKHeading2']))
    story.append(Paragraph("&#8226; 適應症：手術禁忌/高風險、嚴重共病、高齡", styles['CJKBullet']))
    story.append(Paragraph("&#8226; 優點：微創，恢復期短", styles['CJKBullet']))
    story.append(Paragraph("&#8226; 風險：完全 AVB（約 10-20% 需永久 PM），效果可能略遜", styles['CJKBullet']))

    story.append(PageBreak())

    # ===================== SECTION 6: 心肌肌凝蛋白抑制劑 =====================
    story.append(Paragraph("6. 心肌肌凝蛋白抑制劑（Cardiac Myosin Inhibitors）", styles['CJKHeading1']))
    add_header_line(story, styles)

    story.append(Paragraph(
        "Mavacamten（Camzyos）是首創（First-in-class）的小分子選擇性變構抑制劑，作用於心肌肌凝蛋白 ATPase。",
        styles['CJKBody']
    ))

    story.append(Paragraph("藥理作用", styles['CJKHeading2']))
    story.append(make_table(
        ['作用', '說明'],
        [
            ['抑制心肌肌凝蛋白 ATPase', '減少 actin-myosin cross-bridge 形成'],
            ['減少過度收縮', '降低 LVEF 至正常範圍'],
            ['改善舒張功能', '心肌有更長時間舒張'],
            ['降低 LVOT 壓力差', '減少流出道阻塞'],
            ['改善心肌能量代謝', '減少 ATP 消耗'],
        ],
        col_widths=[60*mm, 110*mm]
    ))
    story.append(Spacer(1, 3*mm))

    # ===================== SECTION 7: 臨床試驗 =====================
    story.append(Paragraph("7. Mavacamten 臨床試驗", styles['CJKHeading1']))
    add_header_line(story, styles)

    story.append(Paragraph("EXPLORER-HCM 試驗（Lancet 2021）", styles['CJKHeading2']))
    story.append(Paragraph("&#8226; Phase 3 RCT，n=251（Mavacamten 123 vs 安慰劑 128）", styles['CJKBullet']))
    story.append(make_table(
        ['終點', 'Mavacamten', '安慰劑', 'p 值'],
        [
            ['主要終點（pVO2+NYHA 改善）', '37%', '17%', 'p=0.0005'],
            ['運動後 LVOT PG 變化', '-47 mmHg', '-10 mmHg', 'p&lt;0.0001'],
            ['pVO2 變化', '+1.4 mL/kg/min', '-0.1 mL/kg/min', 'p=0.0006'],
            ['NYHA 改善 &ge; 1 級', '65%', '31%', 'p&lt;0.0001'],
            ['KCCQ-CSS 改善', '+13.6 分', '+4.2 分', 'p&lt;0.0001'],
        ],
        col_widths=[50*mm, 38*mm, 38*mm, 44*mm]
    ))
    story.append(Spacer(1, 3*mm))

    story.append(Paragraph("VALOR-HCM 試驗（JACC 2022）", styles['CJKHeading2']))
    story.append(Paragraph("&#8226; Phase 3 RCT，n=112，符合 SRT 適應症且已轉介 SRT 的患者", styles['CJKBullet']))
    story.append(make_table(
        ['結果', 'Mavacamten', '安慰劑'],
        [
            ['不再符合 SRT 適應症', '82%', '23%'],
            ['NYHA 改善 &ge; 1 級', '63%', '21%'],
            ['NYHA 改善 &ge; 2 級', '27%', '2%'],
        ],
        col_widths=[60*mm, 55*mm, 55*mm]
    ))
    story.append(Spacer(1, 3*mm))

    story.append(Paragraph(
        "Mavacamten 顯著減少 SRT 需求：82% 的患者不再符合 SRT 適應症。",
        styles['CJKBlockquote']
    ))

    story.append(PageBreak())

    # ===================== SECTION 8: 臨床使用 =====================
    story.append(Paragraph("8. Mavacamten 臨床使用 — 本病例", styles['CJKHeading1']))
    add_header_line(story, styles)

    story.append(Paragraph("追蹤時程與結果", styles['CJKHeading2']))
    story.append(make_table(
        ['時間點', 'LVOTO PG（靜態/Valsalva）', 'LVEF', '處置'],
        [
            ['基線（2024/12/10）', '182/192 mmHg', '79.6%', 'NYHA III'],
            ['治療啟動 2025/02/27', '5 mg QD', '—', '—'],
            ['第 4 週', '12/13 mmHg', '76.9%', '依流程評估'],
            ['第 8 週', '10/14 mmHg', '72.5%', '依流程評估'],
            ['第 12 週', '10/8 mmHg', '62.1%', '減量至 2.5 mg'],
            ['第 24 週', '10/16 mmHg', '71.1%', '維持 2.5 mg'],
            ['第 40 週', '16/50 mmHg', '71.6%', '增量至 5 mg'],
            ['第 44 週', '9/22 mmHg', '71.4%', '維持 5 mg'],
        ],
        col_widths=[35*mm, 50*mm, 30*mm, 55*mm]
    ))
    story.append(Spacer(1, 3*mm))

    story.append(Paragraph("治療前後比較", styles['CJKHeading2']))
    story.append(make_table(
        ['參數', '治療前（2018-2024）', '治療後（2025-2026）', '變化'],
        [
            ['NYHA Fc', 'Class III', 'Class II', '改善'],
            ['LVOT Peak PG（靜態）', '51-60 mmHg', '10-12 mmHg', '顯著下降'],
            ['LVOT Peak PG（Valsalva）', '109 mmHg', '8-22 mmHg', '顯著下降'],
            ['SAM', '陽性', '陰性', '消失'],
            ['LVEF', '68%-85%', '62%-76%', '正常化'],
            ['NT-proBNP（pg/mL）', '211-385', '61.3-79.1', '顯著下降'],
        ],
        col_widths=[40*mm, 42*mm, 42*mm, 46*mm]
    ))
    story.append(Spacer(1, 3*mm))

    story.append(Paragraph("Mavacamten 劑量調整原則", styles['CJKHeading2']))
    story.append(Paragraph("&#8226; 起始劑量 5 mg QD，需 LVEF &ge; 55% 才可開始", styles['CJKBullet']))
    story.append(Paragraph("&#8226; 第 4、8、12 週依 LVEF 和 Valsalva LVOT PG 調整", styles['CJKBullet']))
    story.append(Paragraph("&#8226; 維持階段：每 12 週追蹤，LVEF &ge; 55% 且 Valsalva PG &ge; 30 可調升", styles['CJKBullet']))
    story.append(Paragraph("&#8226; 劑量梯度：2.5 &rarr; 5 &rarr; 10 &rarr; 15 mg", styles['CJKBullet']))

    story.append(Paragraph(
        "任一次回診時 LVEF &lt; 50% 則中斷治療。若於 2.5 mg 治療期間發生兩次 LVEF &lt;50%，則永久停藥。",
        styles['CJKWarning']
    ))

    story.append(Paragraph("藥物交互作用", styles['CJKHeading2']))
    story.append(Paragraph(
        "禁止同時併用 Mavacamten 與 &beta;-阻斷劑（BB）及鈣離子阻斷劑（CCB）。"
        "Mavacamten 主要經由 CYP2C19 及 CYP3A4 代謝。",
        styles['CJKWarning']
    ))

    story.append(PageBreak())

    # ===================== SECTION 9: Aficamten =====================
    story.append(Paragraph("9. Aficamten 介紹", styles['CJKHeading1']))
    add_header_line(story, styles)

    story.append(Paragraph("Mavacamten vs Aficamten 比較", styles['CJKHeading2']))
    story.append(make_table(
        ['特性', 'Mavacamten', 'Aficamten'],
        [
            ['半衰期（t1/2）', '6-23 天', '3.5 天'],
            ['CYP 代謝', 'CYP 誘導/CYP450 抑制', '無顯著 CYP 交互作用'],
            ['LVOT 壓力差', '下降', '下降'],
            ['NT-proBNP, cTn', '下降', '下降'],
            ['Peak VO2', '增加', '增加'],
            ['NYHA', '改善', '改善'],
            ['SRT 需求', '下降', '下降'],
            ['心肌纖維化', '穩定/無變化', '間質纖維化下降（ECV）'],
        ],
        col_widths=[50*mm, 60*mm, 60*mm]
    ))
    story.append(Spacer(1, 3*mm))

    story.append(Paragraph("Aficamten Phase 3 — SEQUOIA-HCM（NEJM 2024）", styles['CJKHeading2']))
    story.append(Paragraph("&#8226; n=282（Aficamten 142 vs 安慰劑 142）", styles['CJKBullet']))
    story.append(Paragraph("&#8226; 主要終點：pVO2 +1.74 mL/kg/min（p&lt;0.000006）", styles['CJKBullet']))
    story.append(Paragraph("&#8226; 暫時性 LVEF &lt; 50%：Aficamten 3.5% vs 安慰劑 0.7%", styles['CJKBullet']))

    story.append(Paragraph("Aficamten 的優勢", styles['CJKHeading3']))
    story.append(Paragraph("1. 較短半衰期：藥效調整更靈活，不良反應恢復更快", styles['CJKBullet']))
    story.append(Paragraph("2. 較少藥物交互作用：無顯著 CYP 代謝問題", styles['CJKBullet']))
    story.append(Paragraph("3. 可能改善心肌纖維化：間質 ECV 下降", styles['CJKBullet']))

    story.append(Paragraph(
        "Aficamten（商品名 MYQORZO）已於 2025 年 12 月 19 日獲 FDA 核准，用於治療有症狀的阻塞性肥厚型心肌病變成人患者。",
        styles['CJKBlockquote']
    ))

    # ===================== SECTION 10: 最新指引 =====================
    story.append(Paragraph("10. 最新治療指引更新", styles['CJKHeading1']))
    add_header_line(story, styles)

    story.append(Paragraph("指引重點變化", styles['CJKHeading2']))
    story.append(Paragraph("1. Mavacamten 已納入治療流程", styles['CJKBullet']))
    story.append(Paragraph("&nbsp;&nbsp;- 2023 ESC：Class IIa 建議", styles['CJKSubBullet']))
    story.append(Paragraph("&nbsp;&nbsp;- 2024 AHA：Class 1 建議，第二線治療選項", styles['CJKSubBullet']))
    story.append(Paragraph("2. Aficamten 的定位：目前等待更多臨床證據", styles['CJKBullet']))
    story.append(Paragraph("3. 治療典範轉移：從「修改解剖結構」轉向「針對病理生理機制」", styles['CJKBullet']))

    story.append(PageBreak())

    # ===================== SECTION 11: 結論 =====================
    story.append(Paragraph("11. 結論與臨床啟示", styles['CJKHeading1']))
    add_header_line(story, styles)

    story.append(Paragraph("醫學典範轉移", styles['CJKHeading2']))
    story.append(make_table(
        ['疾病', '傳統治療', '新治療典範'],
        [
            ['胃潰瘍', '胃切除術', '抗生素/PPI'],
            ['冠狀動脈疾病', 'CABG/PCI', 'OMT first'],
            ['肥厚型心肌病變', '心肌切除術', '心肌肌凝蛋白抑制劑'],
        ],
        col_widths=[50*mm, 60*mm, 60*mm]
    ))
    story.append(Spacer(1, 3*mm))

    story.append(Paragraph("本病例的臨床教訓", styles['CJKHeading2']))
    story.append(Paragraph("1. 完整的鑑別診斷非常重要：排除 Fabry disease、心臟類澱粉沉積症、AL amyloidosis", styles['CJKBullet']))
    story.append(Paragraph("2. 傳統藥物治療的限制：&beta;-阻斷劑和 CCB 可能造成心搏過緩", styles['CJKBullet']))
    story.append(Paragraph("3. 心肌肌凝蛋白抑制劑的優勢：針對病理機制，顯著降低 LVOT 壓力差", styles['CJKBullet']))
    story.append(Paragraph("4. Mavacamten 使用注意：定期監測 LVEF，注意藥物交互作用", styles['CJKBullet']))

    story.append(Paragraph("未來展望", styles['CJKHeading2']))
    story.append(Paragraph("&#8226; Aficamten 可能提供更好的藥物動力學特性", styles['CJKBullet']))
    story.append(Paragraph("&#8226; 更多長期追蹤數據將決定心肌肌凝蛋白抑制劑的最終定位", styles['CJKBullet']))
    story.append(Paragraph("&#8226; 可能改變 HCM 的自然病程和預後", styles['CJKBullet']))

    # ===================== 參考文獻 =====================
    story.append(Spacer(1, 8*mm))
    story.append(HRFlowable(width="100%", thickness=1, color=BORDER_COLOR, spaceAfter=3*mm))
    story.append(Paragraph("參考文獻", styles['CJKHeading2']))
    refs = [
        "1. European Heart Journal (2014) 35, 2733-2779 — 2014 ESC HCM Guideline",
        "2. J Am Coll Cardiol. 2020;76(25):e159-e240 — 2020 AHA HCM Guideline",
        "3. Lancet. 2021;397(10293):2467-2475 — EXPLORER-HCM Trial",
        "4. J Am Coll Cardiol. 2022;80(2):95-108 — VALOR-HCM Trial",
        "5. N Engl J Med 2024;390:1849-1861 — Aficamten Phase 3 Trial (SEQUOIA-HCM)",
        "6. European Heart Journal (2023) 00, 1-124 — 2023 ESC HCM Guideline",
        "7. J Am Coll Cardiol. 2024;83(23):2324-2405 — 2024 AHA HCM Guideline Update",
    ]
    for ref in refs:
        story.append(Paragraph(ref, styles['CJKReference']))

    story.append(Spacer(1, 8*mm))
    story.append(HRFlowable(width="100%", thickness=0.5, color=BORDER_COLOR, spaceAfter=3*mm))
    story.append(Paragraph(
        "講義整理者：基於新竹臺大醫院心臟內科曾新育醫師 2026/02/10 CV-CVS Meeting 簡報內容",
        styles['CJKFooter']
    ))

    # Build
    doc.build(story)
    print(f"PDF generated: {output_path}")


if __name__ == "__main__":
    base_dir = r"G:\我的雲端硬碟\004 教學資料 at Hsinchu 院內\Teaching materials CV education web at github\saq-questionnaire-main"
    md_path = os.path.join(base_dir, "HOCM_教學講義 by B97.md")
    output_path = os.path.join(base_dir, "HOCM_教學講義.pdf")
    build_pdf(md_path, output_path)
