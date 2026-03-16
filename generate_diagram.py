#!/usr/bin/env python3
"""Generate end-to-end bits & bytes flow diagram."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import matplotlib.patheffects as pe
import numpy as np

fig = plt.figure(figsize=(22, 28), facecolor='#0d1117')
ax = fig.add_subplot(111)
ax.set_xlim(0, 22)
ax.set_ylim(0, 28)
ax.axis('off')
ax.set_facecolor('#0d1117')

# ─── Color palette ────────────────────────────────────────────────────────────
C = {
    'bg':       '#0d1117',
    'panel':    '#161b22',
    'border':   '#30363d',
    'blue':     '#58a6ff',
    'green':    '#3fb950',
    'purple':   '#bc8cff',
    'orange':   '#f0883e',
    'pink':     '#f778ba',
    'yellow':   '#d29922',
    'teal':     '#39d353',
    'red':      '#f85149',
    'white':    '#e6edf3',
    'gray':     '#8b949e',
    'darkgray': '#21262d',
}

def draw_box(ax, x, y, w, h, title, subtitle, color, icon='', items=None):
    """Draw a styled section box."""
    # Shadow
    shadow = FancyBboxPatch((x+0.08, y-0.08), w, h,
                             boxstyle="round,pad=0.15",
                             facecolor='black', edgecolor='none', alpha=0.4, zorder=1)
    ax.add_patch(shadow)
    # Main box
    box = FancyBboxPatch((x, y), w, h,
                          boxstyle="round,pad=0.15",
                          facecolor=C['panel'], edgecolor=color,
                          linewidth=2, zorder=2)
    ax.add_patch(box)
    # Title bar
    title_bar = FancyBboxPatch((x+0.05, y+h-0.55), w-0.1, 0.45,
                                boxstyle="round,pad=0.05",
                                facecolor=color+'33', edgecolor='none', zorder=3)
    ax.add_patch(title_bar)
    ax.text(x+w/2, y+h-0.32, f"{icon}  {title}", ha='center', va='center',
            fontsize=10, fontweight='bold', color=color, zorder=4)
    if subtitle:
        ax.text(x+w/2, y+h-0.72, subtitle, ha='center', va='center',
                fontsize=7.5, color=C['gray'], style='italic', zorder=4)
    if items:
        for i, (label, detail) in enumerate(items):
            yy = y + h - 1.05 - i * 0.52
            ax.text(x+0.3, yy, '▸', ha='left', va='center', fontsize=8,
                    color=color, zorder=4)
            ax.text(x+0.55, yy, label, ha='left', va='center', fontsize=8,
                    fontweight='bold', color=C['white'], zorder=4)
            ax.text(x+0.55, yy-0.22, detail, ha='left', va='center', fontsize=7,
                    color=C['gray'], zorder=4)

def arrow(ax, x1, y1, x2, y2, color=C['gray'], label='', lw=1.8):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=color, lw=lw,
                                connectionstyle='arc3,rad=0'))
    if label:
        mx, my = (x1+x2)/2, (y1+y2)/2
        ax.text(mx+0.1, my, label, fontsize=7, color=color, va='center', zorder=5)

# ══════════════════════════════════════════════════════════════════════════════
#  TITLE
# ══════════════════════════════════════════════════════════════════════════════
ax.text(11, 27.4, "Bits & Bytes: End-to-End Data Flow",
        ha='center', va='center', fontsize=18, fontweight='bold',
        color=C['white'], zorder=5)
ax.text(11, 27.0, "From Raw Data → Encoding → Transmission → Decoding → Display",
        ha='center', va='center', fontsize=11, color=C['gray'], zorder=5)

# Horizontal divider
ax.plot([0.5, 21.5], [26.65, 26.65], color=C['border'], lw=1, zorder=3)

# ══════════════════════════════════════════════════════════════════════════════
#  LAYER 1 — THE BIT FOUNDATION  (y ~ 24.8)
# ══════════════════════════════════════════════════════════════════════════════
ax.text(11, 26.45, "① Foundation: The Bit", ha='center', va='center',
        fontsize=11, fontweight='bold', color=C['yellow'], zorder=5)

# Bit box
bit_box = FancyBboxPatch((3.5, 24.0), 15, 2.2,
                          boxstyle="round,pad=0.15",
                          facecolor=C['darkgray'], edgecolor=C['yellow'],
                          linewidth=1.5, zorder=2)
ax.add_patch(bit_box)

# Binary pattern
for i, bit in enumerate('01001000 01100101 01101100 01101100 01101111'):
    xb = 4.0 + i * 0.34
    color = C['blue'] if bit == '1' else C['gray']
    ax.text(xb, 25.55, bit, ha='center', va='center', fontsize=9,
            fontweight='bold', color=color, family='monospace', zorder=4)

ax.text(11, 25.1, '1 bit = 0 or 1  │  8 bits = 1 Byte  │  1 KB = 1,024 Bytes  │  1 MB = 1,024 KB  │  1 GB = 1,024 MB',
        ha='center', va='center', fontsize=8.5, color=C['white'],
        family='monospace', zorder=4)
ax.text(11, 24.65, '"Hello" in ASCII =  72  101  108  108  111  →  binary above',
        ha='center', va='center', fontsize=8, color=C['gray'], style='italic', zorder=4)

arrow(ax, 11, 24.0, 11, 23.2, color=C['yellow'], lw=2)

# ══════════════════════════════════════════════════════════════════════════════
#  LAYER 2 — DATA TYPES  (y ~ 20.5)
# ══════════════════════════════════════════════════════════════════════════════
ax.text(11, 23.1, "② Data Encoding by Type", ha='center', va='center',
        fontsize=11, fontweight='bold', color=C['blue'], zorder=5)

# Numbers box
draw_box(ax, 0.4, 19.3, 4.5, 3.6, "Numbers", "Integer & Float",
         C['blue'], icon='[#]',
         items=[
            ("Integers", "Two's complement, 8/16/32/64-bit"),
            ("Float", "IEEE 754: sign + exponent + mantissa"),
            ("Big/Little", "Endianness: byte order matters"),
            ("Example", "42 -> 00101010 (8-bit)"),
         ])

# Text box
draw_box(ax, 5.5, 19.3, 4.5, 3.6, "Text", "Characters & Strings",
         C['green'], icon='[T]',
         items=[
            ("ASCII", "7-bit, 128 chars (A=65, a=97)"),
            ("Unicode", "1M+ code points, U+0041 = A"),
            ("UTF-8", "Variable 1-4 bytes, backward compat"),
            ("Example", "Smile -> F0 9F 98 80 (4 bytes)"),
         ])

# Audio box
draw_box(ax, 10.6, 19.3, 4.5, 3.6, "Audio", "Sound Encoding",
         C['orange'], icon='[~]',
         items=[
            ("Sampling", "44,100 samples/sec (CD quality)"),
            ("Bit depth", "16-bit = 65,536 amplitude levels"),
            ("PCM", "Raw: ~10 MB/min (stereo 44.1kHz)"),
            ("MP3/AAC", "Perceptual coding, 10x compression"),
         ])

# Image box
draw_box(ax, 15.7, 19.3, 4.5, 3.6, "Images", "Visual Data",
         C['purple'], icon='[*]',
         items=[
            ("Pixels", "Each pixel: R,G,B (0-255 each = 24-bit)"),
            ("PNG", "Lossless, deflate compression"),
            ("JPEG", "DCT + quantize, lossy, 10-20x smaller"),
            ("Example", "1080p = 2,073,600 pixels x 3 bytes"),
         ])

# arrows from layer 1 down to layer 2 boxes
for x_center in [2.65, 7.75, 12.85, 17.95]:
    arrow(ax, 11, 23.1, x_center, 23.1, color=C['border'], lw=1)
    arrow(ax, x_center, 23.1, x_center, 22.95, color=C['blue'], lw=1.5)

# arrows going down from data type boxes
for x_center in [2.65, 7.75, 12.85, 17.95]:
    arrow(ax, x_center, 19.3, x_center, 18.65, color=C['border'], lw=1.5)

# ══════════════════════════════════════════════════════════════════════════════
#  LAYER 3 — VIDEO (special, spans full width) y ~ 17.3
# ══════════════════════════════════════════════════════════════════════════════
arrow(ax, 11, 19.3, 11, 18.65, color=C['border'], lw=1.5)
ax.text(11, 18.55, "③ Video: Images + Audio + Time", ha='center', va='center',
        fontsize=11, fontweight='bold', color=C['pink'], zorder=5)

vid_box = FancyBboxPatch((0.4, 16.0), 21.2, 2.35,
                          boxstyle="round,pad=0.15",
                          facecolor=C['panel'], edgecolor=C['pink'],
                          linewidth=2, zorder=2)
ax.add_patch(vid_box)

vid_items = [
    (1.5,  "Frames",   "24-60 fps still images"),
    (5.2,  "I-frames", "Full keyframe (anchor)"),
    (8.9,  "P-frames", "Predicted from prev frame"),
    (12.6, "B-frames", "Bi-directional prediction"),
    (16.3, "Codec",    "H.264/H.265/AV1 encode"),
    (19.5, "Mux",      "Audio+Video → .mp4 container"),
]
for x, label, detail in vid_items:
    ax.text(x, 17.8, label, ha='left', va='center', fontsize=8.5,
            fontweight='bold', color=C['pink'], zorder=4)
    ax.text(x, 17.45, detail, ha='left', va='center', fontsize=7.5,
            color=C['gray'], zorder=4)
    ax.text(x-0.25, 17.62, '▸', ha='left', va='center', fontsize=8,
            color=C['pink'], zorder=4)

ax.text(11, 16.4, '4K video uncompressed: ~12 GB/s  →  H.265 compressed: ~15-20 Mbps  (600× reduction)',
        ha='center', va='center', fontsize=8, color=C['white'],
        family='monospace', zorder=4)

arrow(ax, 11, 16.0, 11, 15.35, color=C['pink'], lw=2)

# ══════════════════════════════════════════════════════════════════════════════
#  LAYER 4 — PACKETIZATION  y ~ 13.2
# ══════════════════════════════════════════════════════════════════════════════
ax.text(11, 15.25, "④ Packetization (Preparing for Transmission)", ha='center',
        va='center', fontsize=11, fontweight='bold', color=C['teal'], zorder=5)

draw_box(ax, 0.4, 12.0, 9.8, 3.0, "Application Layer", "HTTP / HTTPS / WebSocket / DNS",
         C['teal'], icon='[W]',
         items=[
            ("HTTP/2",    "Multiplexed streams, header compression"),
            ("TLS/SSL",   "Encrypt payload: AES-256, handshake via RSA/ECDH"),
            ("DNS",       "Resolve domain -> IP address"),
         ])

draw_box(ax, 11.1, 12.0, 10.5, 3.0, "Transport Layer", "TCP / UDP",
         C['orange'], icon='[P]',
         items=[
            ("TCP",  "Reliable, ordered, 3-way handshake, ACK"),
            ("UDP",  "Fast, no guarantee (live video/gaming)"),
            ("Port", "Identifies service: 443=HTTPS, 53=DNS"),
         ])

arrow(ax, 11, 12.0, 11, 11.35, color=C['teal'], lw=2)

# ══════════════════════════════════════════════════════════════════════════════
#  LAYER 5 — NETWORK & PHYSICAL  y ~ 9.4
# ══════════════════════════════════════════════════════════════════════════════
ax.text(11, 11.25, "⑤ Network & Physical Transmission", ha='center', va='center',
        fontsize=11, fontweight='bold', color=C['red'], zorder=5)

draw_box(ax, 0.4, 8.5, 6.8, 2.55, "Network Layer", "IP Routing",
         C['red'], icon='[IP]',
         items=[
            ("IPv4/IPv6", "Source & dest IP, TTL, checksum"),
            ("Routing",   "BGP, OSPF find best path globally"),
         ])

draw_box(ax, 7.8, 8.5, 6.6, 2.55, "Data Link Layer", "Ethernet / Wi-Fi / 5G",
         C['yellow'], icon='[L2]',
         items=[
            ("MAC",     "Hardware address, frame encapsulation"),
            ("Wi-Fi",   "OFDM modulation, QAM encoding"),
         ])

draw_box(ax, 15.0, 8.5, 6.6, 2.55, "Physical Layer", "Bits on the Wire",
         C['purple'], icon='[L1]',
         items=[
            ("Fiber",   "Light pulses, 100+ Gbps, low latency"),
            ("Copper",  "Voltage levels, twisted pair (Cat6)"),
         ])

# Fiber-optic illustration
for i in range(8):
    color = C['blue'] if i % 3 != 1 else C['gray']
    ax.text(15.3 + i*0.18, 9.6, '|', ha='center', va='center',
            fontsize=10, color=color, family='monospace', zorder=4)

arrow(ax, 11, 8.5, 11, 7.85, color=C['red'], lw=2)

# ══════════════════════════════════════════════════════════════════════════════
#  LAYER 6 — INTERNET INFRASTRUCTURE  y ~ 5.9
# ══════════════════════════════════════════════════════════════════════════════
ax.text(11, 7.75, "⑥ Internet Infrastructure", ha='center', va='center',
        fontsize=11, fontweight='bold', color=C['blue'], zorder=5)

infra_items = [
    (0.4,  5.7, 4.8, 1.9, "ISP / CDN",      "Backbone & edge caching", C['blue'],
     [("ISP", "Internet Service Provider routes traffic"),
      ("CDN", "Edge nodes cache content near user")]),
    (5.7,  5.7, 4.8, 1.9, "Router / Switch", "Hardware forwarding",     C['green'],
     [("Router", "Forwards packets between networks"),
      ("Switch", "Forwards frames within LAN")]),
    (11.0, 5.7, 4.8, 1.9, "Firewall / NAT",  "Security & address translation", C['red'],
     [("Firewall", "Inspect & filter packets by rules"),
      ("NAT",      "Many devices share one public IP")]),
    (16.3, 5.7, 5.3, 1.9, "Load Balancer",   "Traffic distribution",    C['purple'],
     [("L4 LB",   "TCP/UDP round-robin or hash"),
      ("L7 LB",   "HTTP-aware, route by URL/cookie")]),
]
for x, y, w, h, title, sub, col, items in infra_items:
    draw_box(ax, x, y, w, h, title, sub, col, items=items)

arrow(ax, 11, 5.7, 11, 5.05, color=C['blue'], lw=2)

# ══════════════════════════════════════════════════════════════════════════════
#  LAYER 7 — DECODING & RENDERING  y ~ 2.8
# ══════════════════════════════════════════════════════════════════════════════
ax.text(11, 4.95, "⑦ Receiving, Decoding & Rendering", ha='center', va='center',
        fontsize=11, fontweight='bold', color=C['green'], zorder=5)

dec_box = FancyBboxPatch((0.4, 2.6), 21.2, 2.15,
                          boxstyle="round,pad=0.15",
                          facecolor=C['panel'], edgecolor=C['green'],
                          linewidth=2, zorder=2)
ax.add_patch(dec_box)

decode_steps = [
    (1.0,  "①\nReassemble", "TCP re-orders\nout-of-order packets"),
    (4.5,  "②\nDecrypt",    "TLS decrypt\nAES-256-GCM"),
    (8.0,  "③\nDecompress", "HTTP gzip/brotli\ndecompress body"),
    (11.5, "④\nDecode",     "JPEG/H.265/MP3\ndecompress data"),
    (15.0, "⑤\nParse",      "HTML/JSON/protobuf\nparse structure"),
    (18.5, "⑥\nRender",     "GPU rasterise\nto display pixels"),
]
for x, step, detail in decode_steps:
    step_box = FancyBboxPatch((x-0.1, 3.15), 2.9, 1.3,
                               boxstyle="round,pad=0.1",
                               facecolor=C['darkgray'], edgecolor=C['green']+'88',
                               linewidth=1, zorder=3)
    ax.add_patch(step_box)
    ax.text(x+1.35, 3.92, step, ha='center', va='center', fontsize=8.5,
            fontweight='bold', color=C['green'], zorder=4)
    ax.text(x+1.35, 3.42, detail, ha='center', va='center', fontsize=7,
            color=C['gray'], zorder=4)
    if x < 18.5:
        arrow(ax, x+3.0, 3.8, x+3.3, 3.8, color=C['green'], lw=1.2)

# ══════════════════════════════════════════════════════════════════════════════
#  BOTTOM caption
# ══════════════════════════════════════════════════════════════════════════════
ax.plot([0.5, 21.5], [2.45, 2.45], color=C['border'], lw=1, zorder=3)
ax.text(11, 2.1, "Every YouTube video, WhatsApp message, and webpage follows this exact path — billions of times per second.",
        ha='center', va='center', fontsize=9, color=C['gray'], style='italic', zorder=5)
ax.text(11, 1.7, "diepdao.me  •  Computer Science Series  •  Bits & Bytes",
        ha='center', va='center', fontsize=8.5, color=C['blue']+'bb', zorder=5)

# Legend strip
legend_items = [
    (C['yellow'],  "Foundation"),
    (C['blue'],    "Encoding"),
    (C['pink'],    "Video"),
    (C['teal'],    "Transport"),
    (C['red'],     "Network"),
    (C['green'],   "Decoding"),
]
for i, (col, label) in enumerate(legend_items):
    x = 2.5 + i * 3.0
    circ = plt.Circle((x, 1.1), 0.15, color=col, zorder=4)
    ax.add_patch(circ)
    ax.text(x+0.3, 1.1, label, va='center', fontsize=8, color=C['white'], zorder=5)

plt.tight_layout(pad=0.3)
plt.savefig('/home/user/blog/assets/images/bits-bytes-end-to-end-flow.png',
            dpi=150, bbox_inches='tight', facecolor=C['bg'])
print("Diagram saved.")
