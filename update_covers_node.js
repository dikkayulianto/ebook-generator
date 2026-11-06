const fs = require('fs');
const path = require('path');
const { createCanvas, loadImage } = require('@napi-rs/canvas');

async function processCover(grade, semester) {
  const srcPath = path.join(__dirname, `assets/cover_penjualan_buku_kelas${grade}.jpg`);
  const img = await loadImage(srcPath);

  const canvas = createCanvas(img.width, img.height);
  const ctx = canvas.getContext('2d');

  // Draw background image
  ctx.drawImage(img, 0, 0);

  // Helper for rounded pill
  function drawPill(x, y, w, h, r, fillStyle, strokeStyle, strokeWidth) {
    ctx.save();
    ctx.beginPath();
    ctx.roundRect(x, y, w, h, r);
    ctx.fillStyle = fillStyle;
    ctx.fill();
    if (strokeStyle) {
      ctx.lineWidth = strokeWidth || 4;
      ctx.strokeStyle = strokeStyle;
      ctx.stroke();
    }
    ctx.restore();
  }

  // Helper for text with optional shadow
  function drawPillText(text, x, y, font, color, shadow = false) {
    ctx.save();
    ctx.font = font;
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    if (shadow) {
      ctx.shadowColor = 'rgba(0, 0, 0, 0.45)';
      ctx.shadowOffsetY = 2;
      ctx.shadowBlur = 3;
    }
    ctx.fillStyle = color;
    ctx.fillText(text, x, y);
    ctx.restore();
  }

  const semText = `SEMESTER ${semester}`;

  if (grade === 1) {
    const x = 185, y = 395, w = 526, h = 62, r = 31;
    const grad = ctx.createLinearGradient(0, y, 0, y + h);
    grad.addColorStop(0, '#fee2e2');
    grad.addColorStop(1, '#fecdd3');
    drawPill(x, y, w, h, r, grad, '#ebc378', 4);
    drawPillText(`KELAS 1 SD • ${semText}`, x + w / 2, y + h / 2, 'bold 24px Arial', '#064e3b');
  } else if (grade === 2) {
    const x = 206, y = 435, w = 484, h = 58, r = 29;
    const grad = ctx.createLinearGradient(x, 0, x + w, 0);
    grad.addColorStop(0, '#009bb4');
    grad.addColorStop(1, '#d72d69');
    drawPill(x, y, w, h, r, grad, '#ebc378', 4);
    drawPillText(`KELAS 2 SD • ${semText}`, x + w / 2, y + h / 2, 'bold 23px Arial', '#ffffff', true);
  } else if (grade === 3) {
    const x = 190, y = 390, w = 516, h = 56, r = 28;
    const grad = ctx.createLinearGradient(0, y, 0, y + h);
    grad.addColorStop(0, '#784ba5');
    grad.addColorStop(1, '#411e69');
    drawPill(x, y, w, h, r, grad, '#ebc378', 4);
    drawPillText(`KELAS 3 SD • ${semText}`, x + w / 2, y + h / 2, 'bold 23px Arial', '#ffffff', true);
  } else if (grade === 4) {
    // Circle badge on left: center (136, 475), radius 84
    ctx.save();
    ctx.beginPath();
    ctx.arc(136, 475, 84, 0, Math.PI * 2);
    ctx.clip();

    const grad = ctx.createLinearGradient(0, 502, 0, 542);
    grad.addColorStop(0, '#d76014');
    grad.addColorStop(1, '#aa4108');
    ctx.fillStyle = grad;
    ctx.fillRect(45, 502, 185, 40);

    drawPillText(`• ${semText}`, 136, 520, 'bold 15px Arial', '#ffffff', true);
    ctx.restore();
  } else if (grade === 5) {
    const x = 195, y = 360, w = 506, h = 60, r = 30;
    const grad = ctx.createLinearGradient(0, y, 0, y + h);
    grad.addColorStop(0, '#0d9488');
    grad.addColorStop(1, '#064e4b');
    drawPill(x, y, w, h, r, grad, '#ebc378', 4);
    drawPillText(`KELAS 5 SD • ${semText}`, x + w / 2, y + h / 2, 'bold 23px Arial', '#fef3c7', true);
  } else if (grade === 6) {
    const x = 206, y = 376, w = 484, h = 52, r = 26;
    const grad = ctx.createLinearGradient(0, y, 0, y + h);
    grad.addColorStop(0, '#fef08a');
    grad.addColorStop(1, '#eab308');
    drawPill(x, y, w, h, r, grad, '#ffeb96', 4);
    drawPillText(`KELAS 6 SD • ${semText}`, x + w / 2, y + h / 2, 'bold 23px Arial', '#2b0b02');
  }

  // Save to buffer
  const buf = canvas.toBuffer('image/jpeg', 95);

  if (semester === 1) {
    fs.writeFileSync(path.join(__dirname, `assets/cover_penjualan_buku_kelas${grade}.jpg`), buf);
    fs.writeFileSync(path.join(__dirname, `assets/cover_penjualan_buku_kelas${grade}_sem1.jpg`), buf);
  } else {
    fs.writeFileSync(path.join(__dirname, `assets/cover_penjualan_buku_kelas${grade}_sem2.jpg`), buf);
  }
  console.log(`Successfully generated Grade ${grade} Semester ${semester}`);
}

async function run() {
  for (let g = 1; g <= 6; g++) {
    await processCover(g, 1);
    await processCover(g, 2);
  }
  console.log('All 6 grades processed for both Semester 1 and Semester 2!');
}

run().catch(console.error);
