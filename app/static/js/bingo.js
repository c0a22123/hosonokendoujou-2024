// QRコードの読み取りとビンゴ状態更新
let qrCodeReader;

function startCamera() {
    qrCodeReader = new Html5Qrcode("qr-reader");
    qrCodeReader.start({ facingMode: "environment" }, { fps: 10, qrbox: 250 },
        handleQRCodeScan,
        handleQRCodeError
    );
}

function handleQRCodeScan(qrCodeMessage) {
    console.log(`QRコードが読み取られました: ${qrCodeMessage}`);
    qrCodeReader.stop().then(() => {
        document.getElementById('qr-reader').style.display = 'none';
        updateBingoSheet(qrCodeMessage);
    }).catch(error => console.error("カメラ停止エラー:", error));
}

function handleQRCodeError(errorMessage) {
    console.warn(`QRコード読み取りエラー: ${errorMessage}`);
}

function updateBingoSheet(qrCodeMessage) {
    fetch(`/stamp/${qrCodeMessage}`)
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                updateBingoCell(data.cell_id, data.spot_name, data.spot_trivia);
            } else {
                alert('無効なQRコードです');
            }
        })
        .catch(error => console.error('エラー:', error));
}

function updateBingoCell(cellId, spotName, trivia) {
    const cellElement = document.getElementById(`cell-${cellId}`);
    cellElement.textContent = 'チェック済み';
    cellElement.classList.add('checked');
    showOverlay(spotName, trivia);
}

// オーバーレイの表示と閉じる機能
function showOverlay(spotName, trivia) {
    document.getElementById('spot-name').textContent = `${spotName} のスタンプが押されました！`;
    document.getElementById('spot-trivia').textContent = trivia;
    document.getElementById('overlay').style.display = 'flex';
}

function closeOverlay() {
    document.getElementById('overlay').style.display = 'none';
    document.getElementById('qr-reader').style.display = 'block';
}

// 景品交換のポップアップ処理
function setupExchangePopup() {
    document.getElementById('exchange-prize').addEventListener('click', () => {
        document.getElementById('exchange-popup').style.display = 'flex';
    });

    document.getElementById('confirm-exchange').addEventListener('click', () => {
        document.getElementById('exchange-message').textContent = '景品を交換しました！';
        document.getElementById('exchange-prize').textContent = '景品は交換済みです';
        document.getElementById('exchange-prize').disabled = true;
        setTimeout(() => document.getElementById('exchange-popup').style.display = 'none', 1000);
    });

    document.getElementById('cancel-exchange').addEventListener('click', () => {
        document.getElementById('exchange-popup').style.display = 'none';
    });
}

// ページロード時にビンゴ状態を保持
function maintainBingoState(bingoSheet) {
    bingoSheet.forEach((state, index) => {
        const cell = document.getElementById(`cell-${index}`);
        if (state === "True") {
            cell.classList.add("checked");
            cell.textContent = "チェック済み";
        } else {
            cell.classList.remove("checked");
            cell.textContent = "未チェック";
        }
    });
}

// 初期化処理
document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('start-camera').addEventListener('click', startCamera);
    setupExchangePopup();
});