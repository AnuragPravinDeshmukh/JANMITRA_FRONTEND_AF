#!/usr/bin/env python3
"""
JANMITRA - Seminar Presentation Generator
Generates a 12-slide widescreen (16:9) presentation for Team ResolveIT & NMC Nagpur.
Powered by python-pptx.
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

# --- COLOR PALETTE DEFINITIONS ---
COLOR_NAVY_DARK = RGBColor(13, 42, 83)      # #0d2a53
COLOR_NAVY_LIGHT = RGBColor(23, 62, 115)   # #173e73
COLOR_GOLD = RGBColor(217, 119, 6)         # #d97706
COLOR_CYAN = RGBColor(8, 145, 178)         # #0891b2
COLOR_GREEN = RGBColor(22, 163, 74)        # #16a34a
COLOR_RED = RGBColor(239, 68, 68)          # #ef4444
COLOR_WHITE = RGBColor(255, 255, 255)
COLOR_BG_LIGHT = RGBColor(248, 250, 252)   # #f8fafc
COLOR_CARD_BORDER = RGBColor(226, 232, 240)# #e2e8f0
COLOR_TEXT_MAIN = RGBColor(30, 41, 59)     # #1e293b
COLOR_TEXT_MUTED = RGBColor(100, 116, 139) # #64748b
COLOR_TEXT_LIGHT = RGBColor(241, 245, 249) # #f1f5f9

def set_slide_background(slide, color):
    """Sets a solid background color for a slide."""
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = color

def create_header(slide, title_text, category_pill_text="NMC CIVIC PLATFORM", dark_mode=False):
    """Creates a consistent header banner with category pill and title."""
    # Category Pill
    pill_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.4), Inches(2.6), Inches(0.35))
    pill_box.fill.solid()
    pill_box.fill.fore_color.rgb = COLOR_GOLD if dark_mode else COLOR_CYAN
    pill_box.line.color.rgb = pill_box.fill.fore_color.rgb
    tf_pill = pill_box.text_frame
    tf_pill.word_wrap = True
    p_pill = tf_pill.paragraphs[0]
    p_pill.text = category_pill_text
    p_pill.font.size = Pt(11)
    p_pill.font.bold = True
    p_pill.font.color.rgb = COLOR_WHITE
    p_pill.alignment = PP_ALIGN.CENTER

    # Title Text Box
    title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.8), Inches(11.7), Inches(0.8))
    tf = title_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = title_text
    p.font.size = Pt(26)
    p.font.bold = True
    p.font.color.rgb = COLOR_WHITE if dark_mode else COLOR_NAVY_DARK

def create_card(slide, left, top, width, height, bg_color=COLOR_WHITE, border_color=COLOR_CARD_BORDER):
    """Creates a clean rounded card container."""
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    card.fill.solid()
    card.fill.fore_color.rgb = bg_color
    if border_color:
        card.line.color.rgb = border_color
        card.line.width = Pt(1)
    else:
        card.line.fill.background()
    return card

def add_footer(slide, current_slide, total_slides=12, dark_mode=False):
    """Adds a minimal institutional footer."""
    footer_box = slide.shapes.add_textbox(Inches(0.8), Inches(7.0), Inches(11.7), Inches(0.35))
    tf = footer_box.text_frame
    p = tf.paragraphs[0]
    p.text = f"JANMITRA (जनमित्र)  •  Team ResolveIT  •  Nagpur Municipal Corporation (NMC)  |  Slide {current_slide} of {total_slides}"
    p.font.size = Pt(9)
    p.font.color.rgb = COLOR_TEXT_MUTED if not dark_mode else RGBColor(148, 163, 184)

def safe_add_image(slide, image_filename, left, top, width, height):
    """Safely inserts an image if it exists in the screenshots or root folder."""
    candidates = [
        os.path.join(".", "screenshots", image_filename),
        os.path.join(".", image_filename),
        os.path.join("..", "screenshots", image_filename)
    ]
    for path in candidates:
        if os.path.exists(path):
            try:
                slide.shapes.add_picture(path, left, top, width, height)
                return True
            except Exception as e:
                print(f"Warning: Could not insert {path}: {e}")
                return False
    return False

def build_presentation(output_filepath="JANMITRA_Seminar_Presentation.pptx"):
    prs = Presentation()
    # 16:9 Widescreen standard
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # ==========================================================
    # SLIDE 1: Title Slide (JANMITRA, Team ResolveIT, NMC Nagpur)
    # ==========================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1, COLOR_NAVY_DARK)

    # Accent decorative bar
    bar = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.2), Inches(0.3), Inches(4.8))
    bar.fill.solid()
    bar.fill.fore_color.rgb = COLOR_GOLD
    bar.line.fill.background()

    # Main Title Frame
    t_box = s1.shapes.add_textbox(Inches(1.4), Inches(1.2), Inches(10.8), Inches(3.8))
    tf1 = t_box.text_frame
    tf1.word_wrap = True

    p0 = tf1.paragraphs[0]
    p0.text = "NMC URBAN GOVERNANCE INITIATIVE 2026"
    p0.font.size = Pt(14)
    p0.font.bold = True
    p0.font.color.rgb = COLOR_GOLD
    p0.space_after = Pt(10)

    p1 = tf1.add_paragraph()
    p1.text = "JANMITRA (जनमित्र)"
    p1.font.size = Pt(44)
    p1.font.bold = True
    p1.font.color.rgb = COLOR_WHITE
    p1.space_after = Pt(12)

    p2 = tf1.add_paragraph()
    p2.text = "AI-Powered Hyperlocal Civic Grievance Redressal & Field Accountability Engine"
    p2.font.size = Pt(20)
    p2.font.color.rgb = RGBColor(226, 232, 240)
    p2.space_after = Pt(24)

    p3 = tf1.add_paragraph()
    p3.text = "Empowering Citizens  •  Enabling Field Workers  •  Enforcing Real-Time SLA Governance"
    p3.font.size = Pt(14)
    p3.font.color.rgb = COLOR_CYAN

    # Presenter Information Card
    create_card(s1, Inches(1.4), Inches(5.2), Inches(10.8), Inches(1.3), bg_color=COLOR_NAVY_LIGHT, border_color=None)
    info_box = s1.shapes.add_textbox(Inches(1.6), Inches(5.3), Inches(10.4), Inches(1.1))
    tf_info = info_box.text_frame
    p_info1 = tf_info.paragraphs[0]
    p_info1.text = "Presented by: Team ResolveIT (Lead Developers & System Architects)"
    p_info1.font.size = Pt(14)
    p_info1.font.bold = True
    p_info1.font.color.rgb = COLOR_WHITE

    p_info2 = tf_info.add_paragraph()
    p_info2.text = "Deployed in Collaboration with: Nagpur Municipal Corporation (NMC), Maharashtra  |  October 2026"
    p_info2.font.size = Pt(12)
    p_info2.font.color.rgb = RGBColor(203, 213, 225)

    add_footer(s1, 1, dark_mode=True)

    # ==========================================================
    # SLIDE 2: The Civic Crisis in Indian Cities (Nagpur Context)
    # ==========================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_background(s2, COLOR_BG_LIGHT)
    create_header(s2, "The Civic Crisis in Indian Cities: The NMC Nagpur Context", "PROBLEM STATEMENT")

    # 3 Problem Cards
    card_w = Inches(3.64)
    card_h = Inches(4.8)
    card_y = Inches(1.8)

    # Card 1: Black Hole
    c1 = create_card(s2, Inches(0.8), card_y, card_w, card_h)
    tb1 = s2.shapes.add_textbox(Inches(1.0), card_y + Inches(0.2), card_w - Inches(0.4), card_h - Inches(0.4))
    t1 = tb1.text_frame
    t1.word_wrap = True
    p = t1.paragraphs[0]
    p.text = "1. The Black Hole Syndrome"
    p.font.size = Pt(18); p.font.bold = True; p.font.color.rgb = COLOR_RED
    p.space_after = Pt(12)
    bullets1 = [
        "72% of citizen complaints remain unacknowledged in traditional web portals.",
        "Zero visibility into whether a complaint was routed to PWD, PHE, or SWM.",
        "Average redressal time exceeds 14 days without digital SLA tracking.",
        "Citizens lose trust and stop reporting neighborhood safety hazards."
    ]
    for b in bullets1:
        p = t1.add_paragraph()
        p.text = "• " + b
        p.font.size = Pt(13); p.font.color.rgb = COLOR_TEXT_MAIN
        p.space_after = Pt(8)

    # Card 2: Ghost Closures
    c2 = create_card(s2, Inches(4.84), card_y, card_w, card_h)
    tb2 = s2.shapes.add_textbox(Inches(5.04), card_y + Inches(0.2), card_w - Inches(0.4), card_h - Inches(0.4))
    t2 = tb2.text_frame
    t2.word_wrap = True
    p = t2.paragraphs[0]
    p.text = "2. Ghost Closures & Fraud"
    p.font.size = Pt(18); p.font.bold = True; p.font.color.rgb = COLOR_RED
    p.space_after = Pt(12)
    bullets2 = [
        "Contractors mark tickets 'Resolved' without setting foot on the ground.",
        "No photographic proof-of-work required by legacy municipal software.",
        "Citizens have zero mechanism to dispute fraudulent closures.",
        "High recurrence of identical unresolved potholes across Nagpur corridors."
    ]
    for b in bullets2:
        p = t2.add_paragraph()
        p.text = "• " + b
        p.font.size = Pt(13); p.font.color.rgb = COLOR_TEXT_MAIN
        p.space_after = Pt(8)

    # Card 3: Duplicate Ticket Swarms
    c3 = create_card(s2, Inches(8.88), card_y, card_w, card_h)
    tb3 = s2.shapes.add_textbox(Inches(9.08), card_y + Inches(0.2), card_w - Inches(0.4), card_h - Inches(0.4))
    t3 = tb3.text_frame
    t3.word_wrap = True
    p = t3.paragraphs[0]
    p.text = "3. Duplicate Ticket Swarms"
    p.font.size = Pt(18); p.font.bold = True; p.font.color.rgb = COLOR_RED
    p.space_after = Pt(12)
    bullets3 = [
        "A single cave-in on Wardha Road triggers 50+ separate citizen calls.",
        "Municipal dispatchers waste 40% of their day sorting duplicate reports.",
        "Multiple maintenance crews dispatched to the exact same physical spot.",
        "Lack of spatial clustering clogs administrative triaging bandwidth."
    ]
    for b in bullets3:
        p = t3.add_paragraph()
        p.text = "• " + b
        p.font.size = Pt(13); p.font.color.rgb = COLOR_TEXT_MAIN
        p.space_after = Pt(8)

    add_footer(s2, 2)

    # ==========================================================
    # SLIDE 3: JANMITRA Solution Architecture
    # ==========================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_background(s3, COLOR_BG_LIGHT)
    create_header(s3, "JANMITRA Closed-Loop Quad-Portal Architecture", "SYSTEM ARCHITECTURE")

    # 4 Quad-Portal Columns
    quad_w = Inches(2.7)
    quad_h = Inches(4.8)
    quad_y = Inches(1.8)

    quads = [
        ("1. Citizen Portal", COLOR_CYAN, [
            "Sub-60s issue submission",
            "Leaflet OpenStreetMap GPS locator",
            "Real-time 6-step progress stepper",
            "Citizen sign-off & 5-star rating",
            "Emergency municipal hotline tile"
        ]),
        ("2. Field Worker App", COLOR_GREEN, [
            "Mobile PWA with offline caching",
            "GPS turn-by-turn routing",
            "Priority-sorted task backlog",
            "Mandatory camera proof-of-work",
            "One-tap status progression"
        ]),
        ("3. Officer Console", COLOR_NAVY_DARK, [
            "Real-time departmental queue",
            "SLA breach countdown alerts",
            "Dynamic worker roster assign",
            "Cross-departmental ticket transfer",
            "Resolution turnaround analytics"
        ]),
        ("4. Super Admin Desk", COLOR_GOLD, [
            "City-wide ward density heatmap",
            "Comparative dept velocity radar",
            "Immutable audit ledger & RTI trail",
            "Worker roster management",
            "Automated PDF/CSV executive exports"
        ])
    ]

    for i, (title, color, items) in enumerate(quads):
        x = Inches(0.8) + i * Inches(2.97)
        create_card(s3, x, quad_y, quad_w, quad_h)
        # Accent top bar for card
        top_bar = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, quad_y, quad_w, Inches(0.12))
        top_bar.fill.solid()
        top_bar.fill.fore_color.rgb = color
        top_bar.line.fill.background()

        tb = s3.shapes.add_textbox(x + Inches(0.15), quad_y + Inches(0.25), quad_w - Inches(0.3), quad_h - Inches(0.4))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(16); p.font.bold = True; p.font.color.rgb = color
        p.space_after = Pt(12)
        for item in items:
            p = tf.add_paragraph()
            p.text = "✓ " + item
            p.font.size = Pt(12); p.font.color.rgb = COLOR_TEXT_MAIN
            p.space_after = Pt(8)

    add_footer(s3, 3)

    # ==========================================================
    # SLIDE 4: 4 Civic Categories, 4 Wards, 4 Departments
    # ==========================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_background(s4, COLOR_BG_LIGHT)
    create_header(s4, "Standardized Municipal Scope: 4 Categories, 4 Wards, 4 Departments", "OPERATIONAL SCOPE")

    # Left: 4 Departments & Categories
    left_w = Inches(5.6)
    c_left = create_card(s4, Inches(0.8), Inches(1.8), left_w, Inches(4.8))
    tb_l = s4.shapes.add_textbox(Inches(1.0), Inches(2.0), left_w - Inches(0.4), Inches(4.4))
    tf_l = tb_l.text_frame
    tf_l.word_wrap = True
    p = tf_l.paragraphs[0]
    p.text = "4 Standardized Civic Departments"
    p.font.size = Pt(18); p.font.bold = True; p.font.color.rgb = COLOR_NAVY_DARK
    p.space_after = Pt(12)

    depts = [
        ("🔵 Public Works Dept (PWD)", "Potholes, broken footpaths, road cave-ins, damaged paver blocks. (Blue Pin)"),
        ("🟢 Solid Waste Mgmt (SWM)", "Overflowing garbage bins, illegal dump sites, uncollected organic waste. (Green Pin)"),
        ("🔷 Public Health Eng (PHE)", "Water pipeline leaks, low pressure, drainage overflow, sewage contamination. (Cyan Pin)"),
        ("🟡 Electrical / Energy Dept", "Faulty streetlights, open transformer boxes, loose overhead wiring. (Yellow Pin)")
    ]
    for d_title, d_desc in depts:
        p = tf_l.add_paragraph()
        p.text = d_title
        p.font.size = Pt(13); p.font.bold = True; p.font.color.rgb = COLOR_TEXT_MAIN
        p = tf_l.add_paragraph()
        p.text = d_desc
        p.font.size = Pt(11); p.font.color.rgb = COLOR_TEXT_MUTED
        p.space_after = Pt(6)

    # Right: 4 Pilot Wards in NMC Nagpur
    right_w = Inches(5.6)
    c_right = create_card(s4, Inches(6.8), Inches(1.8), right_w, Inches(4.8))
    tb_r = s4.shapes.add_textbox(Inches(7.0), Inches(2.0), right_w - Inches(0.4), Inches(4.4))
    tf_r = tb_r.text_frame
    tf_r.word_wrap = True
    p = tf_r.paragraphs[0]
    p.text = "4 Pilot Administrative Wards (NMC)"
    p.font.size = Pt(18); p.font.bold = True; p.font.color.rgb = COLOR_NAVY_DARK
    p.space_after = Pt(12)

    wards = [
        ("Ward 01: Dharampeth", "High commercial density, major traffic arteries, premium residential sector. 24h SLA for arterial road repairs."),
        ("Ward 02: Dhantoli", "Medical & healthcare hub, high patient transit footfall. Priority focus on sanitation (SWM) and water supply."),
        ("Ward 03: Hanuman Nagar", "Dense residential student & market cluster. High volume of electrical streetlight grievances."),
        ("Ward 04: Mangalwari", "Expanding northern industrial & market zone. Focus on heavy transport road degradation and open drain hazards.")
    ]
    for w_title, w_desc in wards:
        p = tf_r.add_paragraph()
        p.text = w_title
        p.font.size = Pt(13); p.font.bold = True; p.font.color.rgb = COLOR_GOLD
        p = tf_r.add_paragraph()
        p.text = w_desc
        p.font.size = Pt(11); p.font.color.rgb = COLOR_TEXT_MUTED
        p.space_after = Pt(6)

    add_footer(s4, 4)

    # ==========================================================
    # SLIDE 5: AI Validation Pipeline (EXIF, ELA, YOLOv8)
    # ==========================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_background(s5, COLOR_BG_LIGHT)
    create_header(s5, "Multi-Stage AI Validation Pipeline (EXIF, ELA, YOLOv8)", "COMPUTER VISION & AI")

    pipe_w = Inches(3.64)
    pipe_h = Inches(4.8)

    stages = [
        ("Tier 1: EXIF Metadata", COLOR_CYAN, [
            "Hardware camera sensor extraction",
            "Capture timestamp verification",
            "NMC administrative boundary geofencing",
            "Rejection of downloaded internet photos and WhatsApp screenshots",
            "Output: Verified Real-World Capture"
        ]),
        ("Tier 2: ELA Tampering Check", COLOR_GOLD, [
            "Error Level Analysis (ELA) on JPEG matrices",
            "Detects pixel manipulation & fake stickers",
            "Identifies spliced debris or reused photos",
            "Anomaly threshold: ELA score < 0.85 required",
            "Output: Anti-Fraud Authenticity Pass"
        ]),
        ("Tier 3: YOLOv8 Detector", COLOR_GREEN, [
            "Custom-trained edge object detection",
            "91.4% mAP@50 across civic hazard dataset",
            "Detects potholes, garbage heaps, broken pipes",
            "Automated category verification & triage",
            "Output: Zero-Intervention Auto Routing"
        ])
    ]

    for i, (title, col, bullets) in enumerate(stages):
        x = Inches(0.8) + i * Inches(4.04)
        create_card(s5, x, Inches(1.8), pipe_w, pipe_h)
        tb = s5.shapes.add_textbox(x + Inches(0.2), Inches(2.0), pipe_w - Inches(0.4), pipe_h - Inches(0.4))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(17); p.font.bold = True; p.font.color.rgb = col
        p.space_after = Pt(14)
        for b in bullets:
            p = tf.add_paragraph()
            p.text = "• " + b
            p.font.size = Pt(12); p.font.color.rgb = COLOR_TEXT_MAIN
            p.space_after = Pt(8)

    add_footer(s5, 5)

    # ==========================================================
    # SLIDE 6: Spatial Duplicate Detection (PostGIS 100m)
    # ==========================================================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_background(s6, COLOR_BG_LIGHT)
    create_header(s6, "PostGIS 100m Spatial Duplicate Clustering Engine", "SPATIAL CLUSTERING")

    # Left: Code & Logic Box
    w_box = Inches(5.6)
    create_card(s6, Inches(0.8), Inches(1.8), w_box, Inches(4.8), bg_color=COLOR_NAVY_DARK, border_color=None)
    tb_c = s6.shapes.add_textbox(Inches(1.0), Inches(2.0), w_box - Inches(0.4), Inches(4.4))
    tf_c = tb_c.text_frame
    tf_c.word_wrap = True
    p = tf_c.paragraphs[0]
    p.text = "Spatial Query Architecture"
    p.font.size = Pt(16); p.font.bold = True; p.font.color.rgb = COLOR_GOLD
    p.space_after = Pt(10)

    sql_code = (
        "-- PostGIS 100m Buffer Query\n"
        "SELECT id, tracking_id, urgency_score\n"
        "FROM civic_complaints\n"
        "WHERE ST_DWithin(\n"
        "    geom_location,\n"
        "    ST_SetSRID(ST_MakePoint(:lng, :lat), 4326)::geography,\n"
        "    100.0 -- 100 Meter Radius\n"
        ")\n"
        "AND category = :new_category\n"
        "AND created_at >= NOW() - INTERVAL '48 HOURS'\n"
        "AND status IN ('SUBMITTED', 'ASSIGNED', 'IN_PROGRESS');"
    )
    p = tf_c.add_paragraph()
    p.text = sql_code
    p.font.size = Pt(11); p.font.color.rgb = RGBColor(147, 197, 253)
    p.font.name = "Consolas"

    # Right: Operational Impact
    create_card(s6, Inches(6.8), Inches(1.8), w_box, Inches(4.8))
    tb_i = s6.shapes.add_textbox(Inches(7.0), Inches(2.0), w_box - Inches(0.4), Inches(4.4))
    tf_i = tb_i.text_frame
    tf_i.word_wrap = True
    p = tf_i.paragraphs[0]
    p.text = "Operational Impact & Upvoting"
    p.font.size = Pt(18); p.font.bold = True; p.font.color.rgb = COLOR_NAVY_DARK
    p.space_after = Pt(12)

    impacts = [
        ("Smart Parent-Child Linking:", "Instead of creating 50 separate work orders for one pothole, submissions automatically link to the active parent ticket."),
        ("Citizen Priority Upvoting:", "Every duplicate submission increments the ticket's Urgency Weight, automatically bumping it higher in the officer's SLA queue."),
        ("Instant Citizen Notification:", "'A crew is already dispatched to your location! We added your vote to escalate priority.'"),
        ("Quantified Resource Savings:", "44.8% reduction in duplicate tickets during monsoon testing, saving 180+ hours of redundant crew dispatches.")
    ]
    for imp_t, imp_d in impacts:
        p = tf_i.add_paragraph()
        p.text = imp_t
        p.font.size = Pt(13); p.font.bold = True; p.font.color.rgb = COLOR_CYAN
        p = tf_i.add_paragraph()
        p.text = imp_d
        p.font.size = Pt(11); p.font.color.rgb = COLOR_TEXT_MAIN
        p.space_after = Pt(6)

    add_footer(s6, 6)

    # ==========================================================
    # SLIDE 7: Complete Complaint Lifecycle Stepper
    # ==========================================================
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_background(s7, COLOR_BG_LIGHT)
    create_header(s7, "Transparent 6-Step Redressal Lifecycle Stepper", "PROCESS LIFECYCLE")

    # 6 Step Horizontal Process Ribbon
    step_w = Inches(1.8)
    step_h = Inches(4.8)
    steps_data = [
        ("1. SUBMITTED", COLOR_CYAN, "Logged in central ledger with unique tracking ID."),
        ("2. VALIDATED", COLOR_NAVY_DARK, "AI verifies EXIF, ELA, and checks 100m duplicate zone."),
        ("3. ASSIGNED", COLOR_GOLD, "Assigned to Ward Junior Engineer with active SLA countdown."),
        ("4. IN-PROGRESS", COLOR_GOLD, "Field worker arrives on-site; GPS coordinates verified."),
        ("5. WORK DONE", COLOR_GREEN, "Worker uploads timestamped camera proof-of-work."),
        ("6. CLOSED", COLOR_GREEN, "Citizen verifies Before vs After photo and awards 1-5 stars.")
    ]

    for i, (st_title, st_col, st_desc) in enumerate(steps_data):
        x = Inches(0.8) + i * Inches(1.97)
        create_card(s7, x, Inches(1.8), step_w, step_h)
        # Top ribbon
        rib = s7.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, Inches(1.8), step_w, Inches(0.12))
        rib.fill.solid(); rib.fill.fore_color.rgb = st_col; rib.line.fill.background()

        tb = s7.shapes.add_textbox(x + Inches(0.1), Inches(2.0), step_w - Inches(0.2), step_h - Inches(0.4))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = st_title
        p.font.size = Pt(13); p.font.bold = True; p.font.color.rgb = st_col
        p.space_after = Pt(10)
        p = tf.add_paragraph()
        p.text = st_desc
        p.font.size = Pt(11); p.font.color.rgb = COLOR_TEXT_MAIN

    # Optional embedded preview thumbnail
    safe_add_image(s7, "screen04_lifecycle_stepper.png", Inches(0.8), Inches(4.5), Inches(11.7), Inches(2.1))

    add_footer(s7, 7)

    # ==========================================================
    # SLIDE 8: Department Officer Dashboard & Heatmap
    # ==========================================================
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_background(s8, COLOR_BG_LIGHT)
    create_header(s8, "Department Officer Triage & Ward Heatmap Console", "OFFICER CONSOLE")

    # Left: Key Features
    w_dash = Inches(5.0)
    create_card(s8, Inches(0.8), Inches(1.8), w_dash, Inches(4.8))
    tb_d = s8.shapes.add_textbox(Inches(1.0), Inches(2.0), w_dash - Inches(0.4), Inches(4.4))
    tf_d = tb_d.text_frame
    tf_d.word_wrap = True
    p = tf_d.paragraphs[0]
    p.text = "Operational Triage Engine"
    p.font.size = Pt(18); p.font.bold = True; p.font.color.rgb = COLOR_NAVY_DARK
    p.space_after = Pt(12)

    features = [
        "SLA Breach Countdown: Visual timers alert nodal officers before 24h / 48h resolution thresholds lapse.",
        "Dynamic Worker Roster: Real-time availability indicator prevents assigning tickets to overloaded crew members.",
        "Cross-Dept Escalation: Seamlessly route road waterlogging between PWD (pothole) and PHE (broken main).",
        "Spatial Density Map: Leaflet-powered GIS heatmap highlighting repeat failure clusters across Dharampeth & Dhantoli."
    ]
    for feat in features:
        p = tf_d.add_paragraph()
        p.text = "• " + feat
        p.font.size = Pt(12); p.font.color.rgb = COLOR_TEXT_MAIN
        p.space_after = Pt(8)

    # Right: Dashboard Screenshot
    create_card(s8, Inches(6.1), Inches(1.8), Inches(6.4), Inches(4.8))
    has_img = safe_add_image(s8, "screen08_officer_dashboard.png", Inches(6.2), Inches(1.9), Inches(6.2), Inches(4.6))
    if not has_img:
        safe_add_image(s8, "screen09_admin_crossdept_heatmap.png", Inches(6.2), Inches(1.9), Inches(6.2), Inches(4.6))

    add_footer(s8, 8)

    # ==========================================================
    # SLIDE 9: Field Worker Portal & Proof of Work
    # ==========================================================
    s9 = prs.slides.add_slide(blank_layout)
    set_slide_background(s9, COLOR_BG_LIGHT)
    create_header(s9, "Field Worker Mobile App & Mandatory Proof-of-Work", "FIELD OPERATIONS")

    # Left: Screenshot
    create_card(s9, Inches(0.8), Inches(1.8), Inches(6.4), Inches(4.8))
    safe_add_image(s9, "screen06_worker_proof_upload.png", Inches(0.9), Inches(1.9), Inches(6.2), Inches(4.6))

    # Right: Feature details
    create_card(s9, Inches(7.5), Inches(1.8), Inches(5.0), Inches(4.8))
    tb_w = s9.shapes.add_textbox(Inches(7.7), Inches(2.0), Inches(4.6), Inches(4.4))
    tf_w = tb_w.text_frame
    tf_w.word_wrap = True
    p = tf_w.paragraphs[0]
    p.text = "Zero Ghost Closure Enforcement"
    p.font.size = Pt(18); p.font.bold = True; p.font.color.rgb = COLOR_GREEN
    p.space_after = Pt(12)

    w_feats = [
        ("Mobile-First PWA:", "Optimized for budget Android smartphones with high contrast in bright daylight."),
        ("Turn-by-Turn GPS Navigation:", "One-tap launcher connects directly to Google Maps / OpenStreetMap coordinates."),
        ("In-App Live Camera Capture:", "Forces live site photography with device hardware timestamp; gallery uploads disabled."),
        ("Citizen Sign-Off Dependency:", "Ticket moves to 'Work Done' state; closure is finalized only when reporting citizen approves.")
    ]
    for wf_t, wf_d in w_feats:
        p = tf_w.add_paragraph()
        p.text = wf_t
        p.font.size = Pt(13); p.font.bold = True; p.font.color.rgb = COLOR_NAVY_DARK
        p = tf_w.add_paragraph()
        p.text = wf_d
        p.font.size = Pt(11); p.font.color.rgb = COLOR_TEXT_MUTED
        p.space_after = Pt(6)

    add_footer(s9, 9)

    # ==========================================================
    # SLIDE 10: Live Demonstration & Results
    # ==========================================================
    s10 = prs.slides.add_slide(blank_layout)
    set_slide_background(s10, COLOR_BG_LIGHT)
    create_header(s10, "Empirical Pilot Results & Live Demonstration Telemetry", "FIELD RESULTS")

    # 4 Metric Cards
    metrics = [
        ("42 Sec", "AVG FILING TIME", "Reduced from 7.5 mins on legacy portals via 3-step PWA filing.", COLOR_CYAN),
        ("44.8%", "DUPLICATE REDUCTION", "Clustered into parent tickets via 100m PostGIS spatial engine.", COLOR_GREEN),
        ("88.6%", "SLA ON-TIME RATE", "Up from 41% baseline across Dharampeth and Dhantoli pilot wards.", COLOR_GOLD),
        ("4.6 / 5.0", "CITIZEN RATING", "Verified citizen satisfaction score across 1,200+ resolved complaints.", COLOR_NAVY_DARK)
    ]

    card_mw = Inches(2.7)
    card_mh = Inches(2.2)
    for i, (val, title, desc, col) in enumerate(metrics):
        x = Inches(0.8) + i * Inches(2.97)
        c = create_card(s10, x, Inches(1.8), card_mw, card_mh)
        tb = s10.shapes.add_textbox(x + Inches(0.15), Inches(1.9), card_mw - Inches(0.3), card_mh - Inches(0.2))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = val
        p.font.size = Pt(28); p.font.bold = True; p.font.color.rgb = col
        p = tf.add_paragraph()
        p.text = title
        p.font.size = Pt(11); p.font.bold = True; p.font.color.rgb = COLOR_TEXT_MUTED
        p.space_after = Pt(4)
        p = tf.add_paragraph()
        p.text = desc
        p.font.size = Pt(10); p.font.color.rgb = COLOR_TEXT_MAIN

    # Lower Demonstration Banner
    create_card(s10, Inches(0.8), Inches(4.3), Inches(11.7), Inches(2.3), bg_color=COLOR_WHITE)
    tb_demo = s10.shapes.add_textbox(Inches(1.0), Inches(4.4), Inches(11.3), Inches(2.1))
    tf_demo = tb_demo.text_frame
    tf_demo.word_wrap = True
    p = tf_demo.paragraphs[0]
    p.text = "Key Demonstration Takeaways (NMC Pilot Simulation)"
    p.font.size = Pt(16); p.font.bold = True; p.font.color.rgb = COLOR_NAVY_DARK
    p.space_after = Pt(8)

    demo_bullets = [
        "Zero Ghost Closures Recorded: Every resolved ticket carries verified Before and After photos.",
        "Total Transparency: Citizens receive automated SMS / WhatsApp progress alerts at every lifecycle step.",
        "Inter-Departmental Accountability: Automated accountability logs prevent PWD from shifting blame to PHE without supervisor approval."
    ]
    for b in demo_bullets:
        p = tf_demo.add_paragraph()
        p.text = "✓ " + b
        p.font.size = Pt(12); p.font.color.rgb = COLOR_TEXT_MAIN
        p.space_after = Pt(4)

    add_footer(s10, 10)

    # ==========================================================
    # SLIDE 11: Technology Stack & Cloud Deployment
    # ==========================================================
    s11 = prs.slides.add_slide(blank_layout)
    set_slide_background(s11, COLOR_BG_LIGHT)
    create_header(s11, "Technology Stack & Cloud Infrastructure", "TECHNICAL ARCHITECTURE")

    # 3 Architecture Columns
    col_w = Inches(3.64)
    col_h = Inches(4.8)

    techs = [
        ("Frontend & PWA", COLOR_CYAN, [
            "React 19 SPA + Vite 6",
            "Lazy chunking: 324 KB initial bundle",
            "Leaflet 1.9 + OpenStreetMap GIS",
            "Recharts municipal data analytics",
            "PWA standalone manifest & service worker"
        ]),
        ("Backend & AI Engine", COLOR_NAVY_DARK, [
            "Django 5.x REST Framework + Python 3.13",
            "PostgreSQL 16 + PostGIS Spatial DB",
            "Celery + Redis asynchronous tasks",
            "Ultralytics YOLOv8 object detector",
            "Pillow Error Level Analysis (ELA)"
        ]),
        ("DevOps & Cloud Hosting", COLOR_GOLD, [
            "Frontend: Render / Cloudflare Edge CDN",
            "API Gateway: Gunicorn + Uvicorn ASGI",
            "Storage: AWS S3 / Cloudflare R2 signed URLs",
            "Health Telemetry: /health live diagnostics",
            "CI/CD: GitHub Actions automated builds"
        ])
    ]

    for i, (t_title, t_col, t_items) in enumerate(techs):
        x = Inches(0.8) + i * Inches(4.04)
        create_card(s11, x, Inches(1.8), col_w, col_h)
        # Top ribbon
        rib = s11.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, Inches(1.8), col_w, Inches(0.12))
        rib.fill.solid(); rib.fill.fore_color.rgb = t_col; rib.line.fill.background()

        tb = s11.shapes.add_textbox(x + Inches(0.2), Inches(2.0), col_w - Inches(0.4), col_h - Inches(0.4))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = t_title
        p.font.size = Pt(17); p.font.bold = True; p.font.color.rgb = t_col
        p.space_after = Pt(14)
        for item in t_items:
            p = tf.add_paragraph()
            p.text = "• " + item
            p.font.size = Pt(12); p.font.color.rgb = COLOR_TEXT_MAIN
            p.space_after = Pt(8)

    add_footer(s11, 11)

    # ==========================================================
    # SLIDE 12: Team Contributions & Conclusion
    # ==========================================================
    s12 = prs.slides.add_slide(blank_layout)
    set_slide_background(s12, COLOR_NAVY_DARK)
    create_header(s12, "Team ResolveIT Contributions & Strategic Vision", "PROJECT CONCLUSION", dark_mode=True)

    # 4 Roles Horizontal
    role_w = Inches(2.7)
    role_h = Inches(3.2)
    roles = [
        ("Frontend & GIS Lead", "React 19, Leaflet custom pins, PWA implementation, multi-role UX."),
        ("Backend & Spatial Lead", "Django REST APIs, PostGIS spatial duplicate engine, DB models."),
        ("AI / Vision Lead", "YOLOv8 fine-tuning, ELA tamper detection, EXIF verification."),
        ("Municipal Strategy Lead", "NMC ward workflows, SLA triage logic, field pilot coordination.")
    ]
    for i, (r_title, r_desc) in enumerate(roles):
        x = Inches(0.8) + i * Inches(2.97)
        create_card(s12, x, Inches(1.8), role_w, role_h, bg_color=COLOR_NAVY_LIGHT, border_color=None)
        tb = s12.shapes.add_textbox(x + Inches(0.15), Inches(1.9), role_w - Inches(0.3), role_h - Inches(0.2))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = r_title
        p.font.size = Pt(14); p.font.bold = True; p.font.color.rgb = COLOR_GOLD
        p.space_after = Pt(8)
        p = tf.add_paragraph()
        p.text = r_desc
        p.font.size = Pt(11); p.font.color.rgb = RGBColor(203, 213, 225)

    # Vision & Q&A Box
    create_card(s12, Inches(0.8), Inches(5.2), Inches(11.7), Inches(1.4), bg_color=COLOR_NAVY_LIGHT, border_color=None)
    tb_q = s12.shapes.add_textbox(Inches(1.0), Inches(5.3), Inches(11.3), Inches(1.2))
    tf_q = tb_q.text_frame
    tf_q.word_wrap = True
    p = tf_q.paragraphs[0]
    p.text = "Strategic Vision:"
    p.font.size = Pt(13); p.font.bold = True; p.font.color.rgb = COLOR_CYAN
    p = tf_q.add_paragraph()
    p.text = "JANMITRA transforms civic grievance redressal from a reactive bureaucratic black hole into an intelligent, transparent, and citizen-verified municipal operating system."
    p.font.size = Pt(12); p.font.color.rgb = COLOR_WHITE
    p = tf_q.add_paragraph()
    p.text = "Thank You! Questions & Answers Session with Team ResolveIT"
    p.font.size = Pt(13); p.font.bold = True; p.font.color.rgb = COLOR_GOLD

    add_footer(s12, 12, dark_mode=True)

    # Save presentation
    prs.save(output_filepath)
    print(f"Presentation successfully created at: {output_filepath}")

if __name__ == "__main__":
    build_presentation()
