#!/usr/bin/env python3
import qrcode
import sys
from pathlib import Path

def generate_qr(record_id, content_hash, archive_ref, output_dir="qr"):
    """Record bilgisinden QR kod oluştur"""
    Path(output_dir).mkdir(exist_ok=True)
    
    qr_data = f"{record_id}|{content_hash}|{archive_ref}"
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(qr_data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    output_path = Path(output_dir) / f"{record_id}.png"
    img.save(output_path)
    print(f"✅ QR oluşturuldu: {output_path}")
    return str(output_path)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Kullanım: python src/qr.py <record_id> <content_hash> <archive_ref>")
        sys.exit(1)
    
    record_id = sys.argv[1]
    content_hash = sys.argv[2]
    archive_ref = sys.argv[3]
    
    generate_qr(record_id, content_hash, archive_ref)
