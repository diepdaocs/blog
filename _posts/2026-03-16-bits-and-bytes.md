---
layout: single
title: "Bits & Bytes: How Computers Encode, Transmit, and Decode Everything"
date: 2026-03-16 10:00:00 +0800
categories:
  - computer-science
tags:
  - bits
  - bytes
  - encoding
  - networking
  - tcp-ip
  - compression
  - ascii
  - unicode
  - audio
  - image
  - video
---

This is the second deep-dive in the [Computer Science Series](/computer-science/2026/02/27/welcome-to-computer-science/). The [first post](/computer-science/2026/03/16/introduction-to-computer-science/) mapped the entire CS landscape — from hardware to generative AI. Now we zoom in on the very first layer: **bits and bytes**.

Every YouTube video you stream, every emoji you send, every song you play — it all comes down to the same thing: billions of **ones and zeros** flying through cables and the air at the speed of light.

This post traces the full journey. Starting from what a bit physically is, all the way to how pixels light up on your screen. By the end you'll have a clear mental model of how computers encode numbers, text, sound, images, and video — and how all of it travels across the internet to reach you.

---

## The End-to-End Flow

Before diving in, here's the complete picture. Every piece of data follows this path:

<div class="post-diagram">
  <img src="/assets/images/bits-bytes-end-to-end-flow.png" alt="Bits & Bytes End-to-End Data Flow">
</div>

Keep this diagram in mind as we walk through each layer.

---

## 1. The Bit — The Atom of Computing

A **bit** (binary digit) is the smallest unit of information a computer can store. It has exactly two possible values: **0** or **1**.

Physically, a bit can be:
- A high or low voltage on a wire
- A magnetic region pointing north or south on a hard drive
- A pit or land on an optical disc
- A charged or uncharged cell in flash memory

Eight bits grouped together form a **byte**. This grouping is fundamental to how computers are designed — CPUs process data in multiples of bytes (8, 16, 32, 64 bits at a time).

```
1 bit      = 0 or 1
1 byte     = 8 bits       → 256 possible values (0–255)
1 KB       = 1,024 bytes
1 MB       = 1,024 KB     → ~1 million bytes
1 GB       = 1,024 MB     → ~1 billion bytes
1 TB       = 1,024 GB
```

The reason we use base-2 (binary) instead of base-10 (decimal) is simple: electronic circuits naturally have two stable states (on/off). Building a reliable 10-state circuit is much harder than building a reliable 2-state circuit.

---

## 2. Encoding Numbers

### Integers

Whole numbers are stored using **binary positional notation** — exactly like decimal, but each position represents a power of 2 instead of 10.

```
Decimal 42 in binary:

Position:  32  16   8   4   2   1
Bit:        1   0   1   0   1   0

32 + 8 + 2 = 42 ✓
Binary: 00101010
```

**Negative numbers** use **two's complement**. To negate a number: flip all bits, then add 1.

```
42  in 8-bit:  00101010
-42 in 8-bit:  11010110  (flip) → 11010111 (add 1)
```

Two's complement is elegant because addition and subtraction use the same hardware circuit, with no special casing for negative numbers.

**Integer sizes** determine the range:

| Type    | Bits | Range (signed)                    |
|---------|------|-----------------------------------|
| int8    | 8    | −128 to 127                       |
| int16   | 16   | −32,768 to 32,767                 |
| int32   | 32   | −2.1B to 2.1B                     |
| int64   | 64   | −9.2 quintillion to 9.2 quintillion |
| uint64  | 64   | 0 to 18.4 quintillion             |

### Floating-Point Numbers

Real numbers use **IEEE 754** — a standard that every modern CPU implements. A 32-bit float has three parts:

```
[sign: 1 bit] [exponent: 8 bits] [mantissa: 23 bits]

 0 10000100 01001000000000000000000
 ↑     ↑              ↑
 +    132           mantissa
       ↓
exponent = 132 - 127 (bias) = 5
value = 1.01001 × 2^5 = 41.0
```

This is why floating-point arithmetic has rounding errors: `0.1 + 0.2 ≠ 0.3` in most languages. You can't represent `0.1` exactly in binary — just like you can't represent `1/3` exactly in decimal.

### Endianness

When a multi-byte number is stored in memory, the byte order matters. A 32-bit integer `0x01020304` can be stored two ways:

```
Big-endian (network byte order):  01 02 03 04  ← most significant byte first
Little-endian (x86, ARM default): 04 03 02 01  ← least significant byte first
```

Network protocols use big-endian by convention. Intel CPUs use little-endian. When data moves between systems, byte order must be swapped — this is why you'll see `htonl()` (host-to-network-long) calls in network code.

---

## 3. Encoding Text

### ASCII

In 1963, the American Standard Code for Information Interchange (**ASCII**) defined a mapping of 7 bits to 128 characters: uppercase, lowercase, digits, punctuation, and 33 control characters (newline, tab, etc.).

```
'A' = 65  = 01000001
'a' = 97  = 01100001
'0' = 48  = 00110000
' ' = 32  = 00100000
```

ASCII works for English but falls apart for anything else. It can't represent `é`, `中`, `ا`, or `😀`.

### Unicode

Unicode is the solution: a standard that assigns a **code point** to every character in every human writing system — over 150,000 characters in Unicode 15.

```
'A'  → U+0041
'é'  → U+00E9
'中' → U+4E2D
'😀' → U+1F600
```

Unicode is just a numbering scheme. The **encoding** determines how those numbers are stored as bytes.

### UTF-8

**UTF-8** is the dominant encoding on the web (used by ~98% of websites). It uses 1 to 4 bytes per character, with a clever design: ASCII characters (U+0000 to U+007F) are encoded identically to 7-bit ASCII, so all existing ASCII files are valid UTF-8.

```
U+0041  ('A')  →  1 byte:  41
U+00E9  ('é')  →  2 bytes: C3 A9
U+4E2D  ('中') →  3 bytes: E4 B8 AD
U+1F600 ('😀') →  4 bytes: F0 9F 98 80
```

The encoding uses the high bits of the first byte to signal how many bytes follow:

```
0xxxxxxx          → 1 byte  (U+0000–U+007F)
110xxxxx 10xxxxxx → 2 bytes (U+0080–U+07FF)
1110xxxx 10xxxxxx 10xxxxxx → 3 bytes (U+0800–U+FFFF)
11110xxx 10xxxxxx 10xxxxxx 10xxxxxx → 4 bytes (U+10000–U+10FFFF)
```

This self-synchronising design means you can start reading a UTF-8 stream at any byte boundary and immediately know if you're at the start of a character.

---

## 4. Encoding Audio

Sound is a continuous pressure wave in air. To store it digitally, we must sample it at discrete points in time and quantize each sample to a discrete level.

### Pulse-Code Modulation (PCM)

**Sampling rate**: how many snapshots per second. CD quality is **44,100 Hz** (44.1 kHz). The Nyquist theorem says you need to sample at twice the highest frequency you want to capture. Human hearing tops out at ~20 kHz, so 44.1 kHz captures everything we can hear.

**Bit depth**: how many levels each sample can take. At **16-bit**, each sample is one of 65,536 values. At 24-bit, one of 16.7 million values.

```
PCM audio data rate:
CD (44.1 kHz, 16-bit, stereo) = 44,100 × 16 × 2 = 1,411,200 bits/sec ≈ 10 MB/min
```

### Lossy Compression: MP3, AAC, Opus

Raw PCM is large. Audio codecs exploit **psychoacoustics** — the science of what humans actually hear — to discard data we can't perceive:

- **Masking**: a loud sound at one frequency masks quieter sounds nearby (temporal and frequency masking)
- **Stereo redundancy**: left and right channels share a lot of information
- **Irrelevancy reduction**: discard frequencies we can't distinguish from noise

**MP3** (MPEG-1 Audio Layer III) uses a Modified Discrete Cosine Transform (MDCT) to transform samples into the frequency domain, then quantises and Huffman-codes them. A 10× compression at 128 kbps is typical with good quality.

**AAC** (Advanced Audio Codec) is successor to MP3 — same principles, better psychoacoustic model, better at low bitrates. Used by Apple, YouTube, streaming services.

**Opus** (open standard) is the state of the art for low-latency communication (WebRTC, Discord).

---

## 5. Encoding Images

### Pixels and Colour

A digital image is a rectangular grid of **pixels** (picture elements). Each pixel stores a colour, typically as three channels:

```
Red:   0–255 (8 bits)
Green: 0–255 (8 bits)
Blue:  0–255 (8 bits)
───────────────────────
Total: 24 bits = 3 bytes per pixel
```

A 1920×1080 image has 2,073,600 pixels × 3 bytes = **~6 MB uncompressed**.

Colour spaces matter:
- **sRGB** — standard for screens (web, JPEG, PNG)
- **Adobe RGB / P3** — wider gamut for print and HDR displays
- **YCbCr** — used in video: separate luma (brightness) from chroma (colour), exploiting that humans are more sensitive to brightness than colour

### PNG — Lossless Compression

PNG uses **deflate** compression (the same algorithm as gzip). It first applies a **filter** to each row — predicting each pixel from its neighbours and storing the *difference* instead of the raw value. Differences are small, and small values compress well.

```
Original row: [100, 102, 103, 105, ...]
Filtered (sub filter): [100, 2, 1, 2, ...]   ← much more compressible
```

PNG is lossless: you get back exactly the original pixels. It's ideal for screenshots, icons, and anything with text.

### JPEG — Lossy Compression

JPEG uses a sequence of steps that achieve 10–20× compression at the cost of small, mostly imperceptible quality loss:

1. **Colour space conversion**: RGB → YCbCr. Then **chroma subsampling** — store Cb and Cr at half resolution. Humans barely notice colour blur.
2. **8×8 block division**: the image is split into 8×8 pixel blocks.
3. **DCT (Discrete Cosine Transform)**: transforms each block from spatial domain (pixel values) to frequency domain (coefficients for different spatial frequencies).
4. **Quantisation**: divide DCT coefficients by a quantisation table and round to integers. High-frequency coefficients (fine detail) are divided by large numbers → many round to zero. **This is the lossy step.**
5. **Entropy coding**: Huffman or arithmetic coding on the quantised coefficients.

```
High quality JPEG: ~1 MB for a 1920×1080 photo
Low quality JPEG:  ~150 KB for the same photo (but visible artefacts)
PNG (same photo):  ~6+ MB (lossless)
```

### WebP and AVIF

Modern formats like **WebP** (Google) and **AVIF** (AV1-based) achieve better compression than JPEG using newer transforms and intra-frame prediction, similar to video codecs.

---

## 6. Encoding Video

Video is a sequence of images (frames) played back fast enough to create the illusion of motion (16–60+ fps), with synchronised audio. Naively storing 30 1080p frames per second:

```
30 fps × 6 MB/frame = 180 MB/s = 10.8 GB/min
```

That's impossible to stream. The key insight that makes video compression work: **consecutive frames are very similar**. Only small parts of the scene change.

### Frame Types

**I-frames (Intra-coded)** are complete images, compressed independently like JPEGs. They're the "anchor" frames. A video typically has an I-frame every 1–5 seconds.

**P-frames (Predictive)** only store the *difference* from the previous frame, plus motion vectors describing where objects moved. A P-frame might be 10× smaller than an I-frame.

**B-frames (Bi-directional)** can reference both a past *and* a future frame for prediction, achieving even better compression. The codec reorders frames internally for encoding.

```
I → P → P → B → P → B → P → I → ...
     ↑         ↑
  References  References past AND future
  previous
```

### Codecs

| Codec   | Used by         | Key tech                       | Compression vs H.264 |
|---------|-----------------|--------------------------------|----------------------|
| H.264   | Universal       | CABAC, 4×4/8×8 transforms      | baseline             |
| H.265   | Netflix, 4K     | Larger CTUs, better motion est.| ~40% better          |
| VP9     | YouTube         | Open source by Google          | ~30% better          |
| AV1     | Netflix, YouTube| Open source by Alliance        | ~50% better          |

H.265 can compress a 4K movie to around 15–20 Mbps — that's a 600× reduction from the raw 10 GB/s.

### Container Formats

A **container** (`.mp4`, `.mkv`, `.webm`) wraps the encoded video stream, audio stream(s), subtitles, and metadata. The container defines how streams are interleaved and provides timing information so the player keeps audio and video in sync.

---

## 7. Sending It Over the Internet

Now that data is encoded, it needs to travel. The internet is built on a layered model (OSI / TCP/IP), where each layer adds a header with its own information.

### Application Layer: HTTP, TLS, DNS

Before any bytes leave your machine, several things happen:

**DNS resolution**: your browser looks up `google.com` → `142.250.64.142`. This is done via UDP to port 53. The response is cached so it doesn't happen on every request.

**TLS handshake** (for HTTPS):
1. Client sends `ClientHello` with supported cipher suites
2. Server sends its certificate (containing its public key)
3. Both parties derive a shared secret using **ECDH** (Elliptic Curve Diffie-Hellman)
4. All subsequent data is encrypted with **AES-256-GCM** using that shared secret

**HTTP/2** multiplexes many requests over a single TCP connection using streams, and compresses headers with **HPACK**, dramatically reducing overhead vs HTTP/1.1.

### Transport Layer: TCP and UDP

**TCP (Transmission Control Protocol)** provides reliable, ordered delivery:
- Three-way handshake: `SYN → SYN-ACK → ACK`
- Every segment is acknowledged; lost segments are retransmitted
- Flow control (receiver window) and congestion control (CUBIC, BBR) prevent flooding

**UDP (User Datagram Protocol)** is fire-and-forget:
- No handshake, no acknowledgements, no ordering guarantees
- Much lower overhead and latency
- Used where speed matters more than reliability: live video, gaming, VoIP, DNS

**QUIC** (HTTP/3) runs over UDP but re-implements reliability and multiplexing at the application layer, avoiding TCP's head-of-line blocking.

### Network Layer: IP Routing

The **IP header** carries the source and destination IP address, TTL (decremented at each hop — prevents packets from looping forever), and a checksum.

**Routing** is how packets find their way across the globe:
- Within a network, **OSPF** or **IS-IS** compute shortest paths
- Between networks, **BGP (Border Gateway Protocol)** advertises reachability. Your packet might traverse 15–20 routers from your laptop to a server in another continent

### Data Link and Physical Layers

At the **Data Link layer**, IP packets are wrapped in **Ethernet frames** (on a wired network) or **Wi-Fi frames** (802.11). Each frame includes the MAC address of the next hop (not the final destination — that's what IP does).

**ARP (Address Resolution Protocol)** maps IP addresses to MAC addresses on a local network.

At the **Physical layer**, bits become:
- **Voltage pulses** on copper (Ethernet, your home cable)
- **Light pulses** in optical fibre (backbone links, submarine cables) — a single fibre strand carries 100+ Gbps
- **Radio waves** (Wi-Fi, 4G/5G) using modulation schemes like **OFDM + QAM-256**

### What a Packet Actually Looks Like

As your data travels, each layer wraps it in its own header:

```
[Ethernet header | IP header | TCP header | TLS record | HTTP/2 frame | your data]
     14 bytes       20 bytes    20 bytes     5 bytes        9 bytes
```

This is **encapsulation**. At the destination, each layer strips its header and passes the payload up.

---

## 8. How CDNs and Infrastructure Help

A request to watch a Netflix video doesn't go to a server in Silicon Valley. It goes to a nearby **CDN (Content Delivery Network)** edge node — there might be one in the same city.

**CDN flow:**
1. Your DNS query for `netflix.com` resolves to an edge node close to you
2. Edge node checks if the content is cached locally
3. If yes: serves it directly (milliseconds away)
4. If no: fetches from origin, caches it, serves you

**Load balancers** distribute traffic across server fleets:
- **L4 (Layer 4)** load balancers route by IP + port, purely at the TCP level — very fast
- **L7 (Layer 7)** load balancers understand HTTP — can route by URL path, host header, or cookies

**NAT (Network Address Translation)** allows many devices in your home to share a single public IP. Your router maintains a mapping table:

```
192.168.1.5:52341 → 203.0.113.1:52341 (your public IP)
192.168.1.7:33212 → 203.0.113.1:33212
```

When a response arrives, the router reverses the translation and delivers it to the right device.

---

## 9. Receiving and Decoding

When the bytes arrive at the destination, the process unwinds in reverse:

**1. Reassemble**: TCP collects segments, re-orders them by sequence number, and presents a contiguous byte stream to the application.

**2. Decrypt**: the TLS layer decrypts the AES-256-GCM ciphertext using the session key established during the handshake.

**3. Decompress**: HTTP responses are typically compressed with **gzip** or **brotli**. A 100 KB HTML file might compress to 15 KB.

**4. Decode**: if the content is JPEG, the decoder reverses the entropy coding, dequantises the DCT coefficients, applies the inverse DCT, and converts YCbCr back to RGB. For MP3, a filterbank reconstructs audio samples from coded frequency coefficients.

**5. Parse**: the application layer parses the data — HTML into a DOM tree, JSON into objects, protobuf binary into structs.

**6. Render**: the browser (or media player) draws pixels to the screen. For HTML, this involves layout (CSS box model), painting (rasterisation), and compositing (GPU). For video, each decoded frame is uploaded to the GPU as a texture and displayed at the right time.

---

## 10. Processing: The CPU and Memory

All of this encoding, decoding, and routing happens in **processor cycles**.

Modern CPUs process data in **64-bit chunks**. The processor fetches bytes from memory, runs arithmetic and logic instructions, and writes results back — potentially billions of operations per second.

**Cache hierarchy** is why data locality matters so much:

| Level    | Size     | Latency   |
|----------|----------|-----------|
| Register | < 1 KB   | < 1 ns    |
| L1 cache | 32–64 KB | ~1 ns     |
| L2 cache | 256 KB–1 MB | ~4 ns  |
| L3 cache | 8–64 MB  | ~10–40 ns |
| RAM      | 8–128 GB | ~60–100 ns|
| SSD      | TB       | ~100 µs   |

When a video decoder processes pixels in raster order (left-to-right, top-to-bottom), it hits L1/L2 cache most of the time. If it jumped randomly through the frame, every access would hit RAM — 60× slower.

**SIMD (Single Instruction Multiple Data)** instructions let a CPU process 4, 8, or 16 pixels simultaneously. Video codecs and image processing code are heavily hand-optimised to use AVX2/AVX-512 on x86 or NEON on ARM.

**GPUs** take this further: a modern GPU has 10,000+ cores optimised for parallel floating-point operations — perfect for decoding and rendering video frames, training neural networks, and rendering 3D graphics.

---

## Bringing It All Together

Everything in computing and networking is built on the humble bit. Here's the layered view:

```
Raw data (sound wave, pixel values, keystrokes)
        ↓  [Encode]
Bits and bytes (PCM, RGB, UTF-8, IEEE 754)
        ↓  [Compress]
Fewer bits (MP3, JPEG, H.265, deflate)
        ↓  [Encrypt]
Ciphertext (AES-256, TLS record)
        ↓  [Packetize]
TCP segments, IP packets, Ethernet frames
        ↓  [Transmit]
Physical signals (light pulses, voltage, radio waves)
        ↓  [Route]
Hops through routers, CDN edges, load balancers
        ↓  [Receive]
Frames, packets, segments — reverse order
        ↓  [Decrypt & Decompress]
Original bits and bytes
        ↓  [Decode & Render]
Pixels on screen, sound from speakers
```

Each layer has one job, and the power comes from composing them. You can swap JPEG for AVIF at the encoding layer without changing TCP. You can switch from HTTP/1.1 to HTTP/3 without changing your AES keys. The separation of concerns is what lets the internet evolve incrementally.

The next time you stream a video or send a message, you'll know exactly what's happening at every step of that journey — from the photons entering a camera lens all the way to the photons leaving your screen.

In the next post in this series, we'll go deeper into **how CPUs actually execute instructions** — the fetch-decode-execute cycle, branch prediction, out-of-order execution, and why modern CPUs are so fast.

Back to the series: [Welcome to the Computer Science Series](/computer-science/2026/02/27/welcome-to-computer-science/)
