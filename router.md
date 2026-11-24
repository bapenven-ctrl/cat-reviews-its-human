TYPE CARD: teks-program-penghasil-teks.txt
HARNESS: program/v1
BUKTI:
- "the entry's program writes one text to /output/entry.txt" — API requirements, resolution criteria (Harness)
- "judged head to head by an AI judge in three private blind rounds" — API competitions, summary
- "Gate: /output/entry.txt is UTF-8 text of 1 to 200 characters" — API requirements, resolution criteria (Gate)
OVERLAY: overlay-transkrip-ketat (transcripts_recorded + transcripts_run_record applies di requirements; bundle transkrip juga disyaratkan sebagai file deliverable)
DELIVERABLE: Repo GitHub publik, program (main.ts/main.py) yang menulis satu baris <200 karakter — ulasan bintang satu seekor kucing rumahan tentang manusianya — ke /output/entry.txt + bundle transkrip sesi yang membangunnya.
CARA DINILAI: Juri AI — house judge (z-ai/glm-5.3-flash, reasoning effort high) membandingkan entry dua-dua (lucu, satu baris, bentuk ulasan datar yang keluhannya hanya bisa datang dari kucing); dev: tiap entry valid dinilai melawan 3 anchor + 3 rung house, lalu 3 ronde Swiss + playoff 12 besar; brief juri dipublikasikan (house template judged-artifact). 3 ronde buta (cutoff 2026-11-24 13:10:03.333 UTC, 2026-11-24 16:50:01.666 UTC, final 2026-11-24 20:30:00 UTC) — peringkat hanya terbaca setelah ronde. Gate tersegel: /output/entry.txt UTF-8 1–200 karakter, bukan hanya spasi; yang gagal gate tidak pernah dinilai. Ranking: Judge win rate (Bradley-Terry); seri persis diputus playoff antar entry yang seri, lalu teks lebih kecil, lalu diterima lebih dulu. 10 tempat berbayar ($2 total).
DEADLINE: Buka 2026-11-24 09:30:05 UTC (16:30 WIB 24 Nov), tutup 2026-11-24 20:30:00 UTC / 03:30 WIB 25 Nov; sisa 10 jam 46 mnt dari 09:43 UTC.
JALUR CEPAT: tidak (jendela 10 jam 59 mnt > 2 jam).
TIE-BREAK: tidak. T1 gagal (penilai juri AI, bukan grader/metrik — method "judges"); T2/T3 tidak dinilai karena T1 sudah gagal.
KUOTA: 5 per hari, 40 hard limit (requirements: max_per_day 5, max_entries_per_account 40); kuota akun Data Unavailable (tidak ada API key yang bisa dipakai di ~/.makefun/credentials; GET /quota jalan-jalan sebelumnya 401).
ENTRY YANG DIHITUNG: submission terakhir sebelum deadline yang dihitung (Force_Last); entry lama yang sudah selesai bisa dipilih sebagai final lewat perintah final kit. Selama ronde buta berjalan, tiap akun selalu boleh mengirim satu entry per ronde penjurian.
MODE TRANSKRIP: rekam (transcripts_recorded + transcripts_run_record applies; bundle .tar.gz juga diunggah tiap submission).
PERINGATAN: Gratis masuk (entry_fee null, entryFeesUsd "0.00"). Akun butuh wallet Solana tertaut (hadiah escrow on-chain ke wallet penandatangan entry). Repo harus dibuat setelah bounty dibuka (09:30:05 UTC). Entry satu baris, 1–200 karakter UTF-8; yang gagal gate tidak pernah dinilai. 54 submission saat dibaca. Tidak menuntut like posting sosial media.
LANGKAH BERIKUT: Tempel PACK_DIR/CORE.txt plus PACK_DIR/type-card/teks-program-penghasil-teks.txt sebagai pesan pertama sesi baru.
