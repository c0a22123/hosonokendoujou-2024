// static/js/bingo.js

let qrCodeReader = null;

// Start camera to scan QR code
function startCamera() {
    if (qrCodeReader) {
        qrCodeReader.stop().then(() => {
            document.getElementById('qr-reader').innerHTML = '';
            initializeQrReader();
        }).catch(err => console.error("QRコードリーダーの停止エラー:", err));
    } else {
        initializeQrReader();
    }
}

// Initialize QR code reader and start camera
function initializeQrReader() {
    qrCodeReader = new Html5Qrcode("qr-reader");
    qrCodeReader.start(
        { facingMode: "environment" },
        { fps: 10, qrbox: 250 },
        handleQrCodeSuccess,
        handleQrCodeError
    ).catch(err => console.error("QRコードリーダーの起動エラー:", err));
}

// Handle successful QR code scan
function handleQrCodeSuccess(qrCodeMessage) {
    console.log(`QRコードが読み取られました: ${qrCodeMessage}`);
    
    qrCodeReader.stop().then(() => {
        document.getElementById('qr-reader').style.display = 'none';
        document.getElementById('qr-reader').innerHTML = '';
        fetch(`/stamp/${qrCodeMessage}`)
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    const cellId = data.cell_id - 1;
                    updateCell(cellId);
                    showOverlay(data.spot_name, data.spot_trivia);
                } else {
                    alert('無効なQRコードです');
                }
            })
            .catch(error => console.error('エラー:', error));
    }).catch(err => console.error("カメラ停止エラー:", err));
}

// Handle QR code reading error
function handleQrCodeError(errorMessage) {
    console.warn(`QRコード読み取りエラー: ${errorMessage}`);
}

// Update bingo cell with stamp
function updateCell(cellId) {
    const cell = document.getElementById(`cell-${cellId}`);
    cell.innerHTML = `<img src="/static/images/stamp/tamabingo_stamp.png" alt="スタンプ ${cellId + 1}">`;
    cell.classList.add("checked");
}

// Show overlay with stamp animation, confetti, and trivia
function showOverlay(spotName, trivia) {
    document.getElementById('spot-name').textContent = `${spotName} のスタンプが押されました！`;
    document.getElementById('spot-trivia').textContent = trivia;

    const stampImage = document.createElement('img');
    stampImage.src = '/static/images/stamp/tamabingo_stamp.png';
    stampImage.alt = 'スタンプ';
    stampImage.classList.add('stamp-animation');

    const overlayContent = document.querySelector('.overlay-content');
    overlayContent.insertBefore(stampImage, document.getElementById('spot-trivia'));

    document.getElementById('overlay').style.display = 'flex';

    // Trigger the confetti effect
    createConfetti();

    // Add autumn leaves effect
    createFallingLeaves();
}

// Close overlay and remove animations
function closeOverlay() {
    document.getElementById('overlay').style.display = 'none';
    closeCamera();

    const stampImage = document.querySelector('.overlay-content .stamp-animation');
    if (stampImage) {
        stampImage.remove();
    }

    // Remove all confetti and leaf elements
    document.querySelectorAll('.confetti, .leaf').forEach(element => element.remove());
}

// Stop the camera manually
function closeCamera() {
    if (qrCodeReader) {
        qrCodeReader.stop().then(() => {
            document.getElementById('qr-reader').style.display = 'none';
            document.getElementById('qr-reader').innerHTML = '';
            qrCodeReader = null;
        }).catch(err => console.error("カメラ停止エラー:", err));
    }
}

// Setup prize exchange button and popup
function setupPrizeExchange() {
    document.getElementById('exchange-prize').addEventListener('click', () => {
        document.getElementById('exchange-popup').style.display = 'flex';
    });

    document.getElementById('confirm-exchange').addEventListener('click', () => {
        fetch('/exchange_prize', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                document.getElementById('exchange-message').textContent = data.message;
                document.getElementById('exchange-prize').textContent = '景品は交換済みです';
                document.getElementById('exchange-prize').disabled = true;
            } else {
                alert(data.message);
            }
            setTimeout(() => {
                document.getElementById('exchange-popup').style.display = 'none';
            }, 1000);
        })

        .catch(error => console.error('交換エラー:', error));
    });

    document.getElementById('cancel-exchange').addEventListener('click', () => {
        document.getElementById('exchange-popup').style.display = 'none';
    });
}

// Create confetti animation
function createConfetti() {
    for (let i = 0; i < 20; i++) {
        const confetti = document.createElement('div');
        confetti.classList.add('confetti');
        confetti.style.left = `${Math.random() * 100}%`;
        confetti.style.animationDelay = `${Math.random() * 2}s`;
        confetti.style.backgroundColor = `hsl(${Math.random() * 360}, 70%, 60%)`;
        
        document.body.appendChild(confetti);

        // Remove confetti after animation completes
        confetti.addEventListener('animationend', () => {
            confetti.remove();
        });
    }
}

// Create falling leaves animation
function createFallingLeaves() {
    for (let i = 0; i < 10; i++) {
        const leaf = document.createElement('div');
        leaf.classList.add('leaf');
        leaf.style.left = `${Math.random() * 100}%`;
        leaf.style.animationDelay = `${Math.random() * 2 + 1}s`;
        leaf.style.backgroundImage = 'url("/static/images/leaf.png")';
        
        document.body.appendChild(leaf);

        // Remove leaf after animation completes
        leaf.addEventListener('animationend', () => {
            leaf.remove();
        });
    }
}

// Initialize event listeners
document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('start-camera').addEventListener('click', startCamera);
    setupPrizeExchange();
});
